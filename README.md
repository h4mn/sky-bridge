# Sky Bridge

<div align="center">

[![API](https://img.shields.io/badge/api-SkyBridge-blueviolet?logo=fastapi)]()
[![Python](https://img.shields.io/badge/python-3.11-blue?logo=python)](https://www.python.org/)

![Code Style](https://img.shields.io/badge/code%20style-black-black)
![Tests](https://img.shields.io/badge/tests-pytest-green.svg)
![SemVer](https://img.shields.io/badge/semver-2.0.0-blue.svg)

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Contributions](https://img.shields.io/badge/contributions-welcome-orange)]()

[![Status](https://img.shields.io/badge/status-evolving-brightgreen)]()

</div>

## Descrição
Sky Bridge é um hub que apoia a orquestração de serviços para o consumo de LLMs de desenvolvimento. Sky Bridge é o núcleo que conecta agentics como a Sky — uma assistente virtual em constante evolução — com o mundo real.

## Funcionalidades
- [x] Testes automatizados
- [x] Dockerização
- [x] CI/CD
- [ ] Conexão com LLMs
- [ ] Orquestração de serviços
- [ ] Documentação automatizada

## Requisitos
- Python 3.11
- Docker
- Docker Compose

## Estrutura do Projeto
```
sky-bridge/
├── doc/              # Documentação do projeto
├── src/              # Código fonte
├── test/             # Testes
├── script/           # Scripts utilitários
├── VERSION           # Versão atual do projeto
├── pytest.ini        # Configuração do pytest
├── cz.yaml           # Configuração do commitizen
├── pyproject.toml    # Configuração do projeto Python
├── requirements.txt  # Dependências do projeto
├── Dockerfile        # Configuração do container Docker
├── docker-compose.yml # Configuração do Docker Compose
└── .dockerignore     # Arquivos ignorados pelo Docker
```

## Configuração do Ambiente

### Usando Docker (Recomendado)

1. Clone o repositório:
```bash
git clone [URL_DO_REPOSITORIO]
cd sky-bridge
```

2. Configure as variáveis de ambiente:
```bash
cp .env-example .env
# Edite o arquivo .env com suas configurações
```

3. Execute com Docker Compose:
```bash
# Iniciar a aplicação
docker-compose up -d

# Executar testes
docker-compose run test

# Parar a aplicação
docker-compose down
```

### Configuração Local (Alternativa)

1. Clone o repositório:
```bash
git clone [URL_DO_REPOSITORIO]
cd sky-bridge
```

2. Crie um ambiente virtual:
```bash
python -m venv venv
```

3. Ative o ambiente virtual:
- Windows:
```bash
.\venv\Scripts\activate
```
- Unix ou MacOS:
```bash
source venv/bin/activate
```

4. Instale as dependências:
```bash
pip install -r requirements.txt
```

5. Configure as variáveis de ambiente:
```bash
cp .env-example .env
# Edite o arquivo .env com suas configurações
```

## Uso

[Adicione aqui instruções de como usar seu projeto]

## Desenvolvimento

### Padrões de Código

- PEP 8 para estilo de código
- Docstrings no formato Google Style
- Use `black` para formatação de código
- Use `isort` para ordenar imports
- Use `pylint` para análise estática
- Use `pytest` para testes

### Commits

Usamos Conventional Commits com Commitizen:

```bash
# Fazer commit
cz commit

# Gerar nova versão
cz bump
```

### Testes

```bash
# Rodar todos os testes
pytest

# Com cobertura
pytest --cov=src

# Relatório HTML de cobertura
pytest --cov=src --cov-report=html
```

## Versionamento

Este projeto usa [Semantic Versioning](https://semver.org/) e [Commitizen](https://commitizen-tools.github.io/commitizen/) para gerenciamento de versões.

## Contribuição

Contribuições são bem-vindas! Consulte [CONTRIBUTING.md](CONTRIBUTING.md) para mais detalhes.

### Author 👨‍💻

<div align="center">
  
![Sky Icon](https://em-content.zobj.net/thumbs/120/microsoft/319/bridge-at-night_1f309.png)
<br />
[![Assinado por h4mn](https://img.shields.io/badge/feito%20por-h4mn-black?style=flat-square&logo=github)](https://github.com/h4mn)
<br />
[![☁️ made with Sky](https://img.shields.io/badge/%E2%98%81%EF%B8%8F%20made%20with-Sky-87CEEB?style=flat-square&logo=cloud&logoColor=white)]()
<br /><br />
Desenvolvido em parceria com humanos curiosos.

[![GitHub followers](https://img.shields.io/github/followers/h4mn?style=social)](https://github.com/h4mn)

</div>

## Licença

MIT
