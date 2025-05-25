@echo off
:: Sky Bridge CLI - Script de configuração de atalhos
echo [92mConfigurando atalhos do Sky Bridge...[0m

:: Define o atalho sb para o CLI
doskey sb=python -m src.cli $*

:: Mensagem de confirmação
echo [92m✓[0m Atalho 'sb' configurado com sucesso!
echo [96mUso:[0m
echo   sb --help      :: Mostra ajuda
echo   sb --version   :: Mostra versão
echo   sb check       :: Comandos de verificação
echo   sb config      :: Comandos de configuração
echo   sb setup       :: Configura ambiente

:: Mantém as configurações visíveis
cmd /k
