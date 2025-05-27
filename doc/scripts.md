# Scripts Utilitários

Este documento contém a documentação detalhada de todos os scripts utilitários do projeto Sky Bridge.

## Índice

1. [Check Imports](#check-imports) - Verificação de imports duplicados
2. [Sky Bridge CLI](#sky-bridge-cli) - Scripts de execução do CLI
3. [Windows PATH Setup](#windows-path-setup) - Adiciona o diretório `script` ao PATH do Windows

---

## Check Imports (`script/check_imports.py`)

Script para detectar e reportar imports duplicados no código fonte do projeto.

### Funcionalidades

- Detecta imports diretos duplicados (`import xyz`)
- Detecta from-imports duplicados (`from abc import xyz`)
- Ignora arquivos de teste e ambiente virtual
- Suporta verificação de sintaxe Python
- Integrado com pre-commit e CI

### Uso

1. **Verificação Manual**:
```cmd
python script\check_imports.py
```

2. **Via Pre-commit** (automático em cada commit):
```cmd
pre-commit run check-duplicate-imports
```

3. **Via CI** (automático em GitHub Actions):
- Executa em cada push/PR
- Parte do pipeline de qualidade de código

### Saída

O script produz uma das seguintes saídas:

1. Quando não encontra duplicatas:
```
✅ Nenhum import duplicado encontrado!
```

2. Quando encontra duplicatas:
```
🚨 Imports duplicados encontrados:

import xyz importado em:
  - src/module1.py
  - src/module2.py

from abc import xyz importado em:
  - src/core/file1.py
  - src/utils/file2.py
```

### Configuração

#### Pre-commit Hook (`.pre-commit-config.yaml`)
```yaml
-   repo: local
    hooks:
    -   id: check-duplicate-imports
        name: Check for duplicate imports
        entry: python script/check_imports.py
        language: python
        types: [python]
        pass_filenames: false
```

#### GitHub Actions (`ci.yml`)
```yaml
    - name: Check code quality
      run: |
        pre-commit run --all-files
        python script/check_imports.py
```

### Detalhes Técnicos

- Usa `ast` para análise segura do código Python
- Mantém sets separados para diferentes tipos de imports
- Retorna código 1 se encontrar duplicatas (falha o CI)
- Suporta módulos aninhados (`from a.b.c import d`)

### Casos de Uso

1. **Desenvolvimento Local**:
   - Verificar antes de commits
   - Refatorar imports duplicados
   - Manter código organizado

2. **Integração Contínua**:
   - Garantir qualidade do código
   - Prevenir duplicação de imports
   - Manter consistência do projeto

3. **Code Review**:
   - Identificar problemas de organização
   - Sugerir melhorias de estrutura
   - Manter padrões do projeto

---

## Sky Bridge CLI

Scripts para execução do CLI do Sky Bridge em diferentes sistemas operacionais.

### Windows (`script/sb.cmd`)

Script para execução do CLI no Windows.

### Unix/Linux (`script/sb.sh`)

Script para execução do CLI em sistemas Unix/Linux.

### Funcionalidades

- Executa o CLI do Sky Bridge
- Repassa argumentos corretamente
- Fornece ajuda quando executado sem argumentos
- Suporte a cores no terminal

### Uso no Windows

```cmd
# Adicione script\ ao PATH ou execute da raiz do projeto
script\sb.cmd --help
script\sb.cmd check imports
script\sb.cmd config info
```

### Uso no Unix/Linux

```bash
# Primeiro, dê permissão de execução
chmod +x script/sb.sh

# Depois execute
./script/sb.sh --help
./script/sb.sh check imports
./script/sb.sh config info
```

### Configuração Recomendada

1. **Windows**:
   - Adicione o diretório `script\` ao PATH do sistema
   - Ou crie um atalho no diretório de trabalho

2. **Unix/Linux**:
   - Crie um link simbólico: `ln -s script/sb.sh /usr/local/bin/sb`
   - Ou adicione um alias no seu `.bashrc` ou `.zshrc`:
     ```bash
     alias sb='/caminho/para/script/sb.sh'
     ```

### Exemplos de Uso

```bash
# Verificar versão
sb --version

# Rodar testes com cobertura
sb check tests --coverage

# Ver informações do projeto
sb config info

# Configurar ambiente
sb setup
```

---

## Windows PATH Setup (`script/add_to_path.cmd`)

Script para adicionar o diretório `script` ao PATH do Windows, permitindo executar o CLI de qualquer lugar.

### Funcionalidades

- Adiciona o diretório `script` ao PATH do usuário
- Verifica se o diretório já está no PATH
- Feedback visual com cores
- Requer apenas uma execução

### Uso

1. Execute como administrador:
```cmd
script\add_to_path.cmd
```

2. Reinicie seu terminal

3. Use o comando `sb` de qualquer diretório:
```cmd
sb --help
sb check imports
```

### Notas Importantes

- Requer privilégios de administrador
- Modifica apenas o PATH do usuário atual
- É necessário reiniciar o terminal após a execução
- A alteração é permanente
