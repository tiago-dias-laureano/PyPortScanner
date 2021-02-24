import csv

def create_csv(name):
    global arq
    nome_arquivo = name.replace('.','_')
    arq = open(f'relatorios/{nome_arquivo}.csv', 'w', encoding='utf-8', newline='')
    esc = csv.writer(arq)
    esc.writerow(('IP', 'PORTA', 'STATUS', 'SERVIÇO', 'VERSÃO'))

def make_csv(ip, port, status, service, version=""):
    esc = csv.writer(arq)
    esc.writerow((ip, port, status, service, version))

def close_csv():
    arq.close()