import datetime
import socket
from src import code_info
from src import csv_create
from src import service_version

def scanner_ip(ip, verbose):
    ip = ip
    verbose = bool(verbose)
    csv_create.create_csv(ip)
    print(f'[*] {datetime.datetime.now().strftime("%H:%M:%S")} [*] #> Scanner Iniciado No IP: {ip}')
    for porta in code_info.dict_de_code.keys():
        conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        conn.settimeout(0.5)
        resposta = conn.connect_ex((ip, int(porta)))

        if resposta == 0:
            info = service_version.get_version(ip, porta)

            print(f'[*] {datetime.datetime.now().strftime("%H:%M:%S")} [*] #> A porta {porta} ({code_info.dict_de_code[porta]}) está ABERTA! {info}')
            csv_create.make_csv(ip, porta, 'ABERTA', code_info.dict_de_code[porta], info)
        elif resposta == 111 or resposta == 13:   
            if verbose:
                print(f'[!] {datetime.datetime.now().strftime("%H:%M:%S")} [!] #> A conexão com a porta {porta} ({code_info.dict_de_code[porta]} foi RECUSADA / NEGADA!')
            csv_create.make_csv(ip, porta, 'RECUSADA / NEGADA', code_info.dict_de_code[porta])
        else:
            csv_create.make_csv(ip, porta, 'FECHADA', code_info.dict_de_code[porta])
            if verbose:
                print(f'[*] {datetime.datetime.now().strftime("%H:%M:%S")} [*] #> A porta {porta} ({code_info.dict_de_code[porta]}) está FECHADA!')
            else:
                pass

def scanner_url(url, verbose):
    url = url
    verbose = bool(verbose)
    
    if 'http://' in url:
        url_parser = url.split('http://')
        url_parser = url_parser[1]
    elif 'https://' in url:
        url_parser = url.split('https://')
        url_parser = url_parser[1]
    else:
        url_parser = url

    csv_create.create_csv(url_parser)

    ip = socket.gethostbyname(url_parser)
    print(f'[*] {datetime.datetime.now().strftime("%H:%M:%S")} [*] #> Scanner Iniciado No IP: {ip} | {url}')
    for porta in code_info.dict_de_code.keys():
        conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        conn.settimeout(0.5)
        resposta = conn.connect_ex((ip, porta))

        if resposta == 0:
            info = service_version.get_version(ip, porta)
            print(f'[*] {datetime.datetime.now().strftime("%H:%M:%S")} [*] #> A porta {porta} ({code_info.dict_de_code[porta]}) está ABERTA! {info}')
            csv_create.make_csv(url, porta, 'ABERTA', code_info.dict_de_code[porta], info)
        elif resposta == 111 or resposta == 13:    
            csv_create.make_csv(url, porta, 'RECUSADA / NEGADA', code_info.dict_de_code[porta])
            if verbose:
                print(f'[!] {datetime.datetime.now().strftime("%H:%M:%S")} [!] #> A conexão com a porta {porta} ({code_info.dict_de_code[porta]}) foi RECUSADA / NEGADA!')
        else:
            csv_create.make_csv(url, porta, 'FECHADA', code_info.dict_de_code[porta])
            if verbose:
                print(f'[*] {datetime.datetime.now().strftime("%H:%M:%S")} [*] #> A porta {porta} ({code_info.dict_de_code[porta]}) está FECHADA!')
            else:
                pass