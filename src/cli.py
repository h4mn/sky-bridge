# -*- coding: utf-8 -*-

"""Command Line Interface para o Sky Bridge."""
import os
import subprocess

import typer
from rich.console import Console
from rich.panel import Panel
from rich.table import Table

from src import __version__, setup_logging
from src.types import Callable, Optional, Path, cast

# Inicialização do CLI
app: typer.Typer = typer.Typer(
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
        console.print(
            f"[bold blue]Sky Bridge[/bold blue] versão: [green]{__version__}[/green]"
        )
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
    if version:
        console.print(
            f"[bold blue]Sky Bridge[/bold blue] versão: [green]{__version__}[/green]"
        )
        raise typer.Exit()
    if debug:
        setup_logging(level="DEBUG")
    else:
        setup_logging(level="INFO")


main = cast(Callable[[], None], app.command()(main))


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
    script_path = Path(path) / "check_imports.py"  # Usando o argumento path
    if not script_path.exists():
        console.print("[red]Erro: Script check_imports.py não encontrado![/red]")
        raise typer.Exit(1) from FileNotFoundError(
            f"Script não encontrado: {script_path}"
        )

    result = subprocess.run(
        ["python", str(script_path)], capture_output=True, text=True, check=False
    )
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

    # Usando o Python do ambiente virtual
    venv_path = project_root / ".venv"
    if os.name == "nt":  # Windows
        python_exe = venv_path / "Scripts" / "python.exe"
    else:  # Linux/Mac
        python_exe = venv_path / "bin" / "python"

    if not python_exe.exists():
        console.print(
            "[red]Erro: Ambiente virtual não encontrado. Execute 'sb setup' primeiro.[/red]"
        )
        raise typer.Exit(1)

    # Instalando pre-commit se necessário
    try:
        subprocess.run(
            [str(python_exe), "-m", "pip", "install", "pre-commit"],
            capture_output=True,
            check=True,
        )
    except subprocess.CalledProcessError as exc:
        console.print("[red]Erro: Não foi possível instalar o pre-commit.[/red]")
        raise typer.Exit(1) from exc

    # Executando pre-commit
    cmd = [str(python_exe), "-m", "pre_commit", "run"]
    if all_files:
        cmd.extend(["--all-files"])

    console.print("[yellow]Executando pre-commit hooks...[/yellow]")
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, check=False)

        if result.returncode == 0:
            console.print("[green]✓ Todos os hooks passaram![/green]")
        else:
            console.print("[red]✗ Alguns hooks falharam:[/red]")
            if result.stdout:
                console.print(result.stdout)
            if result.stderr:
                console.print("[red]Erros:[/red]")
                console.print(result.stderr)
            raise typer.Exit(1)
    except FileNotFoundError as exc:
        console.print("[red]Erro: Não foi possível executar o pre-commit.[/red]")
        raise typer.Exit(1) from exc


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
    result = subprocess.run(cmd, capture_output=True, text=True, check=False)

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
    dev: bool = typer.Option(
        True,
        "--dev/--no-dev",
        help="Instala dependências de desenvolvimento.",
    ),
) -> None:
    """Configura o ambiente de desenvolvimento."""
    steps = [
        ("sb ambiente virtual", "python -m venv .venv"),
    ]

    # Determina o caminho do pip do ambiente virtual
    if os.name == "nt":  # Windows
        pip_exe = ".venv\\Scripts\\pip"
    else:  # Linux/Mac
        pip_exe = ".venv/bin/pip"

    # Adiciona os comandos de instalação usando o pip do venv
    steps.append(
        (
            "Instalando dependências",
            f"{pip_exe} install -r requirements.txt --no-warn-script-location",
        ),
    )

    if dev:
        steps.append(
            (
                "Instalando dependências de desenvolvimento",
                f"{pip_exe} install -r requirements-dev.txt --no-warn-script-location",
            )
        )
        # Para o pre-commit, também usamos o Python do venv
        steps.append(
            (
                "Configurando pre-commit",
                ".venv\\Scripts\\pre-commit install"
                if os.name == "nt"
                else ".venv/bin/pre-commit install",
            )
        )

    with console.status("[bold green]Configurando ambiente..."):
        for step_name, cmd in steps:
            console.print(f"\n▶ {step_name}")
            try:
                subprocess.run(cmd, check=True, shell=True)
                console.print(f"[green]✓[/green] {step_name} completado!")
            except subprocess.CalledProcessError as e:
                console.print(f"[red]✗[/red] Erro em {step_name}: {e}")
                if not force:
                    raise typer.Exit(1)


@check_app.command("git")
def check_git_status() -> None:
    """Verifica status do repositório git."""
    project_root = Path(__file__).parent.parent
    os.chdir(project_root)

    # Capturando informações do git
    git_status = subprocess.run(
        ["git", "status"], capture_output=True, text=True, check=False
    )
    branch = subprocess.run(
        ["git", "branch", "--show-current"], capture_output=True, text=True, check=False
    )
    remote = subprocess.run(
        ["git", "remote", "-v"], capture_output=True, text=True, check=False
    )

    # Criando painel informativo
    panel = Panel(
        "\n".join(
            [
                f"[bold cyan]Branch Atual:[/bold cyan] {branch.stdout.strip()}",
                "",
                "[bold cyan]Remotes:[/bold cyan]",
                remote.stdout.strip() or "Nenhum remote configurado",
                "",
                "[bold cyan]Status:[/bold cyan]",
                git_status.stdout.strip() or "Workspace limpo",
            ]
        ),
        title="[bold]Status do Git[/bold]",
        border_style="blue",
    )
    console.print(panel)


@check_app.callback(invoke_without_command=True)
def check_callback(ctx: typer.Context) -> None:
    """Mostra opções de verificação disponíveis."""
    if ctx.invoked_subcommand is None:
        table = Table(title="[bold]Comandos de Verificação Disponíveis[/bold]")
        table.add_column("Comando", style="cyan")
        table.add_column("Descrição", style="green")

        # Lista de comandos disponíveis
        commands = [
            ("git", "Verifica status do repositório git"),
            ("imports", "Verifica imports duplicados no código"),
            ("pre-commit", "Executa verificações do pre-commit"),
            ("tests", "Executa suite de testes"),
        ]

        for cmd, desc in commands:
            table.add_row(f"sb check {cmd}", desc)

        console.print(table)
        raise typer.Exit()


if __name__ == "__main__":
    app()
