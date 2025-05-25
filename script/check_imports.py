""" Script para verificar imports duplicados. """
import ast
import sys
from collections import defaultdict
from pathlib import Path
from typing import Dict, List, Set, Tuple

def get_imports(file_path: Path) -> Tuple[Set[str], Set[str]]:
    """ Extrai todos os imports e from imports de um arquivo Python. """
    with open(file_path, "r", encoding="utf-8") as f:
        try:
            tree = ast.parse(f.read())
        except SyntaxError:
            print(f"🚨 Erro de sintaxe em {file_path}")
            return set(), set()

    direct_imports = set()
    from_imports = set()

    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            for name in node.names:
                direct_imports.add(name.name)
        elif isinstance(node, ast.ImportFrom):
            module = node.module or ""
            for name in node.names:
                from_imports.add(f"{module}.{name.name}")

    return direct_imports, from_imports

def check_duplicate_imports(directory: Path) -> Dict[str, List[Path]]:
    """ Verifica imports duplicados em todos os arquivos Python. """
    direct_import_map = defaultdict(list)
    from_import_map = defaultdict(list)
    
    for file_path in directory.rglob("*.py"):
        if "test" not in str(file_path) and "venv" not in str(file_path):
            direct_imports, from_imports = get_imports(file_path)
            
            for imp in direct_imports:
                direct_import_map[imp].append(file_path)
            for imp in from_imports:
                from_import_map[imp].append(file_path)

    duplicates = {}
    
    # Verificar imports diretos duplicados
    for imp, files in direct_import_map.items():
        if len(files) > 1:
            duplicates[f"import {imp}"] = files
    
    # Verificar from imports duplicados
    for imp, files in from_import_map.items():
        if len(files) > 1:
            module_parts = imp.split(".")
            duplicates[f"from {'.'.join(module_parts[:-1])} import {module_parts[-1]}"] = files

    return duplicates

def main() -> int:
    """ Função principal. """
    src_dir = Path("src")
    if not src_dir.exists():
        print("🚨 Diretório 'src' não encontrado!")
        return 1

    duplicates = check_duplicate_imports(src_dir)
    
    if duplicates:
        print("\n🚨 Imports duplicados encontrados:\n")
        for imp, files in duplicates.items():
            print(f"\n{imp} importado em:")
            for file in files:
                print(f"  - {file}")
        return 1
    
    print("✅ Nenhum import duplicado encontrado!")
    return 0

if __name__ == "__main__":
    sys.exit(main())
