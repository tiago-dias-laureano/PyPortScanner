import argparse
import socket
import datetime
from src import code_info
from src import main_ports

parser = argparse.ArgumentParser(description='PyPortScanner v1.0')

parser.add_argument('--url', 
                    required=False, 
                    help='Set a url que deseja fazer o scanner.')
parser.add_argument('--ip', 
                    required=False, 
                    help="Set o ip que deseja fazer o scanner." )
parser.add_argument('--verbose',
                    required=False, 
                    help="Com essa opção o scanner retorna todos os detalhes. Set o valor True para obter todos os detalhes",
                    )
args = parser.parse_args()

def scanner_ip(args):
    verbose = "false"
    ip = args.ip
    verbose = bool(args.verbose)
    print(f'[*] {datetime.datetime.now().strftime("%H:%M:%S")} [*] #> Scanner Iniciado No IP: {ip}')
    for porta in main_ports.return_port():
        conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        conn.settimeout(0.5)
        resposta = conn.connect_ex((ip, porta))

        if resposta == 0:
            print(f'[*] {datetime.datetime.now().strftime("%H:%M:%S")} [*] #> A porta {porta} ({code_info.dict_de_code[str(porta)]}) está ABERTA!')
        elif resposta == 111 or resposta == 13:    
            print(f'[!] {datetime.datetime.now().strftime("%H:%M:%S")} [!] #> A conexão com a porta {porta} ({code_info.dict_de_code[str(porta)]}) foi RECUSADA / NEGADA!')
        else:
            if verbose.upper() == "TRUE":
                print(f'[*] {datetime.datetime.now().strftime("%H:%M:%S")} [*] #> A porta {porta} ({code_info.dict_de_code[str(porta)]}) está FECHADA!')
            else:
                pass

def scanner_url(args):
    url = args.url
    verbose = bool(args.verbose)

    if 'http://' in args.url:
        url_parser = args.url.split('http://')
        url_parser = url_parser[1]
    elif 'https://' in args.url:
        url_parser = args.url.split('https://')
        url_parser = url_parser[1]

    ip = socket.gethostbyname(url_parser)

    for porta in main_ports.return_port():
        conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        conn.settimeout(0.5)
        resposta = conn.connect_ex((ip, porta))

        if resposta == 0:
            print(f'[*] {datetime.datetime.now().strftime("%H:%M:%S")} [*] #> A porta {porta} ({code_info.dict_de_code[str(porta)]}) está ABERTA!')
        elif resposta == 111 or resposta == 13:    
            print(f'[!] {datetime.datetime.now().strftime("%H:%M:%S")} [!] #> A conexão com a porta {porta} ({code_info.dict_de_code[str(porta)]}) foi RECUSADA / NEGADA!')
        else:
            if verbose:
                print(f'[*] {datetime.datetime.now().strftime("%H:%M:%S")} [*] #> A porta {porta} ({code_info.dict_de_code[str(porta)]}) está FECHADA!')
            else:
                pass

if args.url:
    scanner_url(args)
elif args.ip:
    scanner_ip(args)
else:
    print('Você precisa setar um argumento correto!')