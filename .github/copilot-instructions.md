<!-- Use this file to provide workspace-specific custom instructions to Copilot. For more details, visit https://code.visualstudio.com/docs/copilot/copilot-customization#_use-a-githubcopilotinstructionsmd-file -->

# Sky Bridge - Instruções para o Copilot

Este é um projeto Python que segue as seguintes convenções e práticas:

1. Estilo de código:
   - Seguimos a PEP 8
   - Usamos Black para formatação
   - Imports são organizados com isort
   - Docstrings seguem o formato Google Style Python Docstrings

2. Testes:
   - Usamos pytest para testes
   - Todos os testes devem estar no diretório `test/`
   - Arquivos de teste devem começar com `test_`
   - Funções de teste devem começar com `test_`

3. Convenções de commit:
   - Usamos Conventional Commits
   - Commitizen é usado para gerenciar as versões

4. Estrutura do projeto:
   - Código fonte principal está em `src/`
   - Documentação está em `doc/`
   - Scripts utilitários estão em `script/`
   - Testes estão em `test/`

5. Dependências:
   - Todas as dependências devem ser listadas em `requirements.txt`
   - Versões específicas devem ser fixadas para produção
