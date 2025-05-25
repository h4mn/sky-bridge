@echo off
:: Script para adicionar o diretório script ao PATH do Windows
setlocal enabledelayedexpansion

:: Configura encode do output para UTF-8
chcp 65001 >nul

:: Cores para output
set "GREEN=[92m"
set "RED=[91m"
set "CYAN=[96m"
set "RESET=[0m"

:: Obtém o diretório atual
set "SCRIPT_DIR=%~dp0"
set "SCRIPT_DIR=%SCRIPT_DIR:~0,-1%"

echo %CYAN%Sky Bridge - Configuração de PATH%RESET%
echo.

:: Verifica se já está no PATH
echo %PATH% | findstr /i /c:"%SCRIPT_DIR%" >nul
if %errorlevel% equ 0 (
    echo %RED%O diretório já está no PATH!%RESET%
    echo %CYAN%PATH atual:%RESET% %SCRIPT_DIR%
    goto :end
)

:: Adiciona ao PATH do usuário usando PowerShell
powershell -Command "[Environment]::SetEnvironmentVariable('PATH', [Environment]::GetEnvironmentVariable('PATH', 'User') + ';%SCRIPT_DIR%', 'User')"

if %errorlevel% equ 0 (
    echo %GREEN%✓ Diretório adicionado ao PATH com sucesso!%RESET%
    echo.
    echo Agora você pode usar os comandos:
    echo   sb           :: Sky Bridge CLI
    echo.
    echo %CYAN%Nota: Você precisa reiniciar o terminal para as mudanças terem efeito.%RESET%
) else (
    echo %RED%✗ Erro ao adicionar ao PATH. Tente executar como administrador.%RESET%
)

:end
:: Pausa para o usuário ler a mensagem
pause
