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

    csv_create.create_csv(ip_address)

    _print_log(f'Scanner Iniciado No IP: {ip_address}')

    for port in code_info.dict_de_code.keys():
        conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        conn.settimeout(0.5)
        response = conn.connect_ex((ip_address, int(port)))

        if response == 0:
            info = get_version.get_version(ip_address, port)

            _print_log(f'A porta {port} ({code_info.dict_de_code[port]}) está ABERTA! {info}')

            csv_create.make_csv(ip_address, port, 'ABERTA', code_info.dict_de_code[port], info)

        elif response == 111 or response == 13: 
            if verbose:

                _print_log(f'A conexão com a porta {port} ({code_info.dict_de_code[port]} foi RECUSADA / NEGADA!')

            csv_create.make_csv(ip_address, port, 'RECUSADA / NEGADA', code_info.dict_de_code[port])

        else:

            csv_create.make_csv(ip_address, port, 'FECHADA', code_info.dict_de_code[port])

            if verbose:

                _print_log(f'A porta {port} ({code_info.dict_de_code[port]}) está FECHADA!')


def url(url_address, verbose=False):

    if 'http://' in url_address:
        url_parser = url_address.split('http://')
        url_parser = url_parser[1]

    elif 'https://' in url_address:
        url_parser = url_address.split('https://')
        url_parser = url_parser[1]

    else:
        url_parser = url_address

    ip(ip_address=socket.gethostbyname(url_parser))
