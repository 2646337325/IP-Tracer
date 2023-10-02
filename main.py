import requests
from colorama import init, Fore, Back, Style
init()

arte_ascii = """\n
  /$$$$$$            /$$                         /$$$$$$$$                  /$$   /$$ /$$      
 /$$__  $$          |__/                        | $$_____/                 | $$  | $$| $$      
| $$  \ $$ /$$$$$$$  /$$ /$$$$$$/$$$$   /$$$$$$ | $$     /$$$$$$   /$$$$$$ | $$  | $$| $$   /$$
| $$$$$$$$| $$__  $$| $$| $$_  $$_  $$ /$$__  $$| $$$$$ /$$__  $$ /$$__  $$| $$$$$$$$| $$  /$$/
| $$__  $$| $$  \ $$| $$| $$ \ $$ \ $$| $$$$$$$$| $$__/| $$  \__/| $$$$$$$$|_____  $$| $$$$$$/ 
| $$  | $$| $$  | $$| $$| $$ | $$ | $$| $$_____/| $$   | $$      | $$_____/      | $$| $$_  $$ 
| $$  | $$| $$  | $$| $$| $$ | $$ | $$|  $$$$$$$| $$   | $$      |  $$$$$$$      | $$| $$ \  $$
|__/  |__/|__/  |__/|__/|__/ |__/ |__/ \_______/|__/   |__/       \_______/      |__/|__/  \__/
                                                                                               
                                                                                               
                                                                                               """

print(Fore.RED + arte_ascii + Fore.RESET)

def obter_informacoes_ip(ip):
    url = f'https://ipinfo.io/{ip}/json'
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        return data
    else:
        return None

if __name__ == '__main__':
    while True:
        endereco_ip = input(Fore.RESET + 'Digite o endereço IP para obter informações (ou digite "s" para sair): ')

        if endereco_ip.lower() == 's':
            break

        resultado = obter_informacoes_ip(endereco_ip)

        if resultado:
            print(Fore.BLUE + '\nInformações sobre o endereço IP:')
            print(Fore.GREEN + 'IP:', resultado['ip'])
            print(Fore.GREEN + 'Hostname:', resultado['hostname'])
            print(Fore.GREEN + 'Cidade:', resultado['city'])
            print(Fore.GREEN + 'Região:', resultado['region'])
            print(Fore.GREEN + 'País:', resultado['country'])
            print(Fore.GREEN + 'Provedor de serviços de Internet (ISP):', resultado['org'])
            print()
        else:
            print(Fore.RED + 'Erro ao obter informações do endereço IP.')
            print(Style.RESET_ALL)



