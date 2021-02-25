import datetime
import socket
from src import code_info
from src import main_ports
from src import csv_create
from src import get_version

def scanner_ip(args):
    verbose = "false"
    ip = args.ip
    verbose = bool(args.verbose)
    csv_create.create_csv(ip)
    print(f'[*] {datetime.datetime.now().strftime("%H:%M:%S")} [*] #> Scanner Iniciado No IP: {ip}')
    for porta in code_info.dict_de_code.keys():
        conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        conn.settimeout(0.5)
        resposta = conn.connect_ex((ip, int(porta)))

        if resposta == 0:
            info = get_version.get_version(ip, porta)

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
