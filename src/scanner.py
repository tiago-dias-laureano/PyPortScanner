# -*- coding: utf-8 -*-

import socket
import datetime

from src import code_info
from src import csv_create
from src import get_version


def _time():
    return datetime.datetime.now().strftime("%H:%M:%S")


def _print_log(msg):
    t = _time()

    print(f'[*] {t} [*] #> {msg}')


def ip(ip_address, verbose=False):

    _print_log(f'Scanner Iniciado No IP: {ip_address}')

    column_names = ('IP', 'PORTA', 'STATUS', 'SERVIÇO', 'VERSÃO')  # Header/Columns of csv file
    
    # A list of tuples of reports used for save in csv file.
    # The first index has the column names.
    reports = [column_names]

    for port in code_info.dict_de_code.keys():
        conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        conn.settimeout(0.5)
        response = conn.connect_ex((ip_address, int(port)))

        if response == 0:
            info = get_version.get_version(ip_address, port)

            _print_log(f'A porta {port} ({code_info.dict_de_code[port]}) está ABERTA! {info}')
            
            reports.append((ip_address, port, 'ABERTA', code_info.dict_de_code[port], info))

        elif response == 111 or response == 13: 
            # Last index is version column with a default value
            reports.append((ip_address, port, 'RECUSADA / NEGADA', code_info.dict_de_code[port], 'N/D'))

            if verbose:
                _print_log(f'A conexão com a porta {port} ({code_info.dict_de_code[port]} foi RECUSADA / NEGADA!')

        else:
            # Last index is version column with a default value
            reports.append((ip_address, port, 'FECHADA', code_info.dict_de_code[port], 'N/D'))

            if verbose:
                _print_log(f'A porta {port} ({code_info.dict_de_code[port]}) está FECHADA!')

    # Save all reports at once
    csv_create.make_csv(filename=ip_address, content=reports)


def url(url_address, verbose=False):

    if 'http://' in url_address:
        url_parser = url_address.split('http://')
        url_parser = url_parser[1]

    elif 'https://' in url_address:
        url_parser = url_address.split('https://')
        url_parser = url_parser[1]

    else:
        url_parser = url_address

    ip(ip_address=socket.gethostbyname(url_parser), verbose=verbose)
