@echo off

:: Configura encode do output para UTF-8
chcp 65001 >nul

:: Habilita processamento de sequências ANSI
for /f "tokens=2 delims==" %%G in ('wmic os get buildnumber /value ^| find "="') do set "BUILD=%%G"
if %BUILD% geq 10586 (
    reg add HKCU\Console /v VirtualTerminalLevel /t REG_DWORD /d 1 /f >nul 2>&1
)

:: Define o caractere de escape ANSI (ESC = \033)
for /f %%a in ('echo prompt $E ^| cmd') do set "ESC=%%a"

:: Cores para output usando sequências ANSI
set "GREEN=%ESC%[32m"
set "CYAN=%ESC%[36m"
set "RESET=%ESC%[0m"

@cls
echo.
echo  %CYAN%Sky Bridge CLI%RESET% v0.1.0
echo  %GREEN%Framework Python para Projetos Modernos%RESET%
echo  -----------------------------------------------------
echo.
:: ═══════════════════════════════════════════════════════════════
:: Uso: sb [comando] [opções]
:: Exemplos:
::   sb --help      # Mostra ajuda
::   sb check       # Executa verificações
::   sb config      # Configurações
:: ═══════════════════════════════════════════════════════════════

:: Se não houver argumentos, mostra o help
if "%~1"=="" (
    echo Uso: sb [comando] [opções]
    echo.
    echo Comandos principais:
    echo   sb --help      :: Mostra ajuda
    echo   sb --version   :: Mostra versão
    echo   sb check      :: Comandos de verificação
    echo   sb config     :: Comandos de configuração
    exit /b
)

:: Repassa todos os argumentos para o CLI
py -m src.cli %*
