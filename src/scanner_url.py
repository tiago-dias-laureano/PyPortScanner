import datetime
import socket
from src import code_info
from src import main_ports
from src import csv_create

def scanner_url(args):

    url = args.url
    verbose = bool(args.verbose)
    
    if 'http://' in args.url:
        url_parser = args.url.split('http://')
        url_parser = url_parser[1]
    elif 'https://' in args.url:
        url_parser = args.url.split('https://')
        url_parser = url_parser[1]

    csv_create.create_csv(url_parser)

    ip = socket.gethostbyname(url_parser)

    for porta in main_ports.return_port():
        conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        conn.settimeout(0.5)
        resposta = conn.connect_ex((ip, porta))

        if resposta == 0:
            csv_create.make_csv(url, porta, 'ABERTA', code_info.dict_de_code[str(porta)])
            print(f'[*] {datetime.datetime.now().strftime("%H:%M:%S")} [*] #> A porta {porta} ({code_info.dict_de_code[str(porta)]}) está ABERTA!')
        elif resposta == 111 or resposta == 13:    
            csv_create.make_csv(url, porta, 'RECUSADA / NEGADA', code_info.dict_de_code[str(porta)])
            if verbose:
                print(f'[!] {datetime.datetime.now().strftime("%H:%M:%S")} [!] #> A conexão com a porta {porta} ({code_info.dict_de_code[str(porta)]}) foi RECUSADA / NEGADA!')
        else:
            csv_create.make_csv(url, porta, 'FECHADA', code_info.dict_de_code[str(porta)])
            if verbose:
                print(f'[*] {datetime.datetime.now().strftime("%H:%M:%S")} [*] #> A porta {porta} ({code_info.dict_de_code[str(porta)]}) está FECHADA!')
            else:
                pass