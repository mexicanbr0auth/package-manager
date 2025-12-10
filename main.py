#!/usr/bin/env python3
"""
GitHub: https://github.com/seu-usuario
Telegram: https://t.me/mexicanbr
X: https://x.com/Mexicanbr_

Script de gerenciamento de pacotes e sistema para Linux
"""

import os
import sys
import time
from colorama import Fore, Style, init

# Inicializa colorama
init(autoreset=True)

# Cores personalizadas
class Colors:
    GREEN = Fore.GREEN
    RED = Fore.RED
    YELLOW = Fore.YELLOW
    BLUE = Fore.BLUE
    CYAN = Fore.CYAN
    MAGENTA = Fore.MAGENTA
    RESET = Style.RESET_ALL

def clear_screen():
    """Limpa a tela do terminal"""
    os.system('clear' if os.name == 'posix' else 'cls')

def print_header():
    """Exibe o cabeçalho do programa"""
    clear_screen()
    print(Colors.GREEN + """
╔══════════════════════════════════════════════════════════════╗
║                                                              ║
║   ██████╗  █████╗  ██████╗██╗  ██╗ █████╗  ██████╗ ███████╗  ║
║   ██╔══██╗██╔══██╗██╔════╝██║ ██╔╝██╔══██╗██╔════╝ ██╔════╝  ║
║   ██████╔╝███████║██║     █████╔╝ ███████║██║  ███╗█████╗    ║
║   ██╔═══╝ ██╔══██║██║     ██╔═██╗ ██╔══██║██║   ██║██╔══╝    ║
║   ██║     ██║  ██║╚██████╗██║  ██╗██║  ██║╚██████╔╝███████╗  ║
║   ╚═╝     ╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝ ╚══════╝  ║
║                                                              ║
║              Sistema de Gerenciamento de Pacotes             ║
║                                                              ║
╚══════════════════════════════════════════════════════════════╝
    """)
    
    print(Colors.CYAN + "═" * 55)
    print(Colors.YELLOW + " GitHub:    https://github.com/mexicanbr0auth")
    print(Colors.YELLOW + " Telegram:  https://t.me/mexicanbr")
    print(Colors.YELLOW + " X:         https://x.com/Mexicanbr_")
    print(Colors.CYAN + "═" * 55 + "\n")

def update_system():
    """Atualiza a lista de pacotes disponíveis"""
    print(Colors.BLUE + "[🔍] Atualizando lista de pacotes...")
    result = os.system('apt update > /dev/null 2>&1')
    if result == 0:
        print(Colors.GREEN + "[✅] Sistema atualizado com sucesso!")
    else:
        print(Colors.RED + "[❌] Falha ao atualizar o sistema.")
    time.sleep(1.5)

def upgrade_system():
    """Atualiza os pacotes instalados"""
    print(Colors.BLUE + "[🔄] Atualizando pacotes do sistema...")
    result = os.system('apt upgrade -y > /dev/null 2>&1')
    if result == 0:
        print(Colors.GREEN + "[✅] Pacotes atualizados com sucesso!")
    else:
        print(Colors.RED + "[❌] Falha ao atualizar pacotes.")
    time.sleep(1.5)

def install_package():
    """Instala um pacote específico"""
    print(Colors.CYAN + "[📦] Instalação de Pacote")
    print(Colors.CYAN + "─" * 30)
    pkg = input(Colors.YELLOW + "[?] Nome do pacote: " + Colors.RESET).strip()
    
    if not pkg:
        print(Colors.RED + "[⚠] Nenhum pacote especificado.")
        return
    
    print(Colors.BLUE + f"[↓] Instalando {pkg}...")
    result = os.system(f'apt install -y {pkg}')
    if result == 0:
        print(Colors.GREEN + f"[✅] {pkg} instalado com sucesso!")
    else:
        print(Colors.RED + f"[❌] Falha ao instalar {pkg}.")
    time.sleep(2)

def alpine_manager():
    """Gerencia a instalação e login do Alpine"""
    print(Colors.MAGENTA + "[🐧] Gerenciador Alpine")
    print(Colors.MAGENTA + "─" * 30)
    
    selc = input(Colors.YELLOW + "[?] Alpine está instalado? (s/n): " + Colors.RESET).lower()
    
    if selc == 's' or selc == 'y':
        print(Colors.BLUE + "[→] Iniciando login no Alpine...")
        os.system('pd login alpine')
    elif selc == 'n':
        print(Colors.BLUE + "[↓] Instalando Alpine...")
        os.system('pd install alpine')
        
        login = input(Colors.YELLOW + "\n[?] Deseja fazer login no Alpine? (s/n): " + Colors.RESET).lower()
        if login in ['s', 'y', 'sim', 'yes']:
            print(Colors.BLUE + "[→] Iniciando login no Alpine...")
            os.system('pd login alpine')
    else:
        print(Colors.RED + "[⚠] Opção inválida.")
    
    time.sleep(1.5)

def pip_manager():
    """Instala bibliotecas Python via pip"""
    print(Colors.CYAN + "[🐍] Gerenciador PIP")
    print(Colors.CYAN + "─" * 30)
    
    pkg = input(Colors.YELLOW + "[?] Nome da biblioteca: " + Colors.RESET).strip()
    
    if not pkg:
        print(Colors.RED + "[⚠] Nenhuma biblioteca especificada.")
        return
    
    print(Colors.BLUE + f"[↓] Instalando {pkg}...")
    result = os.system(f'pip install {pkg}')
    if result == 0:
        print(Colors.GREEN + f"[✅] {pkg} instalado com sucesso!")
    else:
        # Tenta com pip3 se pip falhar
        print(Colors.YELLOW + "[⚠] Tentando com pip3...")
        result = os.system(f'pip3 install {pkg}')
        if result == 0:
            print(Colors.GREEN + f"[✅] {pkg} instalado com sucesso!")
        else:
            print(Colors.RED + f"[❌] Falha ao instalar {pkg}.")
    
    time.sleep(2)

def print_menu():
    """Exibe o menu de opções"""
    print(Colors.GREEN + "\n" + "═" * 55)
    print(Colors.YELLOW + " MENU PRINCIPAL")
    print(Colors.GREEN + "═" * 55)
    
    menu_options = [
        ("1", "🔄 Atualizar lista de pacotes", Colors.BLUE),
        ("2", "⚡ Atualizar sistema", Colors.BLUE),
        ("3", "📦 Instalar pacote", Colors.CYAN),
        ("4", "🐧 Gerenciar Alpine", Colors.MAGENTA),
        ("5", "🐍 Instalar via PIP", Colors.CYAN),
        ("6", "🚪 Sair", Colors.RED)
    ]
    
    for num, text, color in menu_options:
        print(f"{color}[{num}] {text}")
    
    print(Colors.GREEN + "═" * 55)

def main():
    """Função principal do programa"""
    while True:
        print_header()
        print_menu()
        
        select = input(Colors.YELLOW + "\n[?] Selecione uma opção: " + Colors.RESET).strip()
        
        if select == "1":
            update_system()
        elif select == "2":
            upgrade_system()
        elif select == "3":
            install_package()
        elif select == "4":
            alpine_manager()
        elif select == "5":
            pip_manager()
        elif select == "6":
            print(Colors.RED + "\n[👋] Saindo... Até logo!")
            time.sleep(1)
            clear_screen()
            break
        else:
            print(Colors.RED + "\n[❌] Opção inválida!")
            time.sleep(1.5)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(Colors.RED + "\n\n[⚠] Interrompido pelo usuário.")
        time.sleep(1)
        clear_screen()
        sys.exit(0)
