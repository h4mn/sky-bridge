"""Command Line Interface para o Sky Bridge."""
import os
import subprocess
from pathlib import Path
from typing import Optional

import typer
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.text import Text

from src import __version__
from src.utils.logging import setup_logging

# Inicialização do CLI
app = typer.Typer(
    name="sky-bridge",
    help="CLI do Sky Bridge para gerenciamento de scripts e configurações",
    add_completion=True,
)
console = Console()

# Grupos de comandos
check_app = typer.Typer(help="Comandos de verificação")
config_app = typer.Typer(help="Comandos de configuração")

app.add_typer(check_app, name="check")
app.add_typer(config_app, name="config")

def version_callback(value: bool) -> None:
    """Mostra a versão do Sky Bridge."""
    if value:
        console.print(f"[bold blue]Sky Bridge[/bold blue] versão: [green]{__version__}[/green]")
        raise typer.Exit()

@app.callback()
def main(
    version: Optional[bool] = typer.Option(
        None,
        "--version",
        "-v",
        help="Mostra a versão do Sky Bridge.",
        callback=version_callback,
        is_eager=True,
    ),
    debug: bool = typer.Option(
        False,
        "--debug",
        help="Ativa modo debug com logs detalhados.",
    ),
) -> None:
    """Sky Bridge - Framework Python para Projetos."""
    if debug:
        setup_logging(level="DEBUG")
    else:
        setup_logging(level="INFO")

@check_app.command("imports")
def check_imports(
    path: Path = typer.Option(
        "src",
        "--path",
        "-p",
        help="Caminho para verificar imports.",
        exists=True,
        dir_okay=True,
        file_okay=False,
    ),
) -> None:
    """Verifica imports duplicados no código."""
    script_path = Path("script") / "check_imports.py"
    if not script_path.exists():
        console.print("[red]Erro: Script check_imports.py não encontrado![/red]")
        raise typer.Exit(1)
    
    result = subprocess.run(["python", str(script_path)], capture_output=True, text=True)
    if result.returncode == 0:
        console.print("[green]✓[/green] Nenhum import duplicado encontrado!")
    else:
        console.print(result.stdout)
        raise typer.Exit(1)

@check_app.command("pre-commit")
def run_pre_commit(
    all_files: bool = typer.Option(
        False,
        "--all",
        "-a",
        help="Executa em todos os arquivos.",
    ),
) -> None:
    """Executa verificações do pre-commit."""
    # Garantindo que estamos na raiz do projeto
    project_root = Path(__file__).parent.parent
    os.chdir(project_root)
    
    cmd = ["pre-commit", "run"]
    if all_files:
        cmd.extend(["--all-files"])
    
    console.print("[yellow]Executando pre-commit hooks...[/yellow]")
    result = subprocess.run(cmd, capture_output=True, text=True)
    
    if result.returncode == 0:
        console.print("[green]✓ Todos os hooks passaram![/green]")
    else:
        console.print("[red]✗ Alguns hooks falharam:[/red]")
        # Exibe stdout mesmo se houver erro, pois pode conter informações úteis
        if result.stdout:
            console.print(result.stdout)
        if result.stderr:
            console.print("[red]Erros:[/red]")
            console.print(result.stderr)
        raise typer.Exit(1)

@check_app.command("tests")
def run_tests(
    verbose: bool = typer.Option(
        False,
        "--verbose",
        "-v",
        help="Mostra output detalhado dos testes.",
    ),
    coverage: bool = typer.Option(
        False,
        "--coverage",
        "-c",
        help="Gera relatório de cobertura.",
    ),
) -> None:
    """Executa suite de testes."""
    cmd = ["pytest"]
    if verbose:
        cmd.append("-v")
    if coverage:
        cmd.extend(["--cov=src", "--cov-report=term-missing"])
    
    console.print("[yellow]Executando testes...[/yellow]")
    result = subprocess.run(cmd, capture_output=True, text=True)
    
    if result.returncode == 0:
        console.print("[green]✓[/green] Todos os testes passaram!")
    else:
        console.print(result.stdout)
        console.print(result.stderr)
        raise typer.Exit(1)

@config_app.command("info")
def show_config() -> None:
    """Mostra informações de configuração do projeto."""
    table = Table(title="Configuração do Sky Bridge")
    
    table.add_column("Configuração", style="cyan")
    table.add_column("Valor", style="green")
    
    # Informações básicas
    table.add_row("Versão", __version__)
    table.add_row("Python", "3.11")
    table.add_row("Ambiente", "Desenvolvimento")
    
    # Diretórios principais
    dirs = ["src", "test", "doc", "script"]
    for dir_name in dirs:
        path = Path(dir_name)
        status = "✓" if path.exists() else "✗"
        table.add_row(f"Diretório {dir_name}", f"{status} {path.absolute()}")
    
    console.print(table)

@app.command()
def setup(
    force: bool = typer.Option(
        False,
        "--force",
        "-f",
        help="Força reconfiguração mesmo se já configurado.",
    ),
) -> None:
    """Configura o ambiente de desenvolvimento."""
    steps = [
        ("Criando ambiente virtual", "python -m venv .venv"),
        ("Instalando dependências", "pip install -r requirements.txt"),
        ("Configurando pre-commit", "pre-commit install"),
    ]
    
    with console.status("[bold green]Configurando ambiente...") as status:
        for step_name, cmd in steps:
            console.print(f"\n▶ {step_name}")
            try:
                subprocess.run(cmd, check=True, shell=True)
                console.print(f"[green]✓[/green] {step_name} completado!")
            except subprocess.CalledProcessError as e:
                console.print(f"[red]✗[/red] Erro em {step_name}: {e}")
                if not force:
                    raise typer.Exit(1)

if __name__ == "__main__":
    app()
