# -*- coding: utf-8 -*-

import csv
import os

def _sanitaze_filename(filename):
    return filename.replace('.','_')


def _write_csv_file(filename, content):
    filename = _sanitaze_filename(filename)
    
    reports_path = os.path.join('relatorios', f'{filename}.csv')

    with open(reports_path, 'w', encoding='utf-8', newline='') as file:

        esc = csv.writer(file)

        for c in content:
            esc.writerow(c)


def create_csv(filename):
    _write_csv_file(filename, content=('IP', 'PORTA', 'STATUS', 'SERVIÇO', 'VERSÃO'))


def make_csv(filename, content):
    _write_csv_file(filename, content)
