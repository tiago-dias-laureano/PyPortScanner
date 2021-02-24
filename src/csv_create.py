import csv

def create_csv(csv_name):
    global arquivo
    nome_arquivo = csv_name.replace('.','_')
    arquivo = open(f'relatorios/{nome_arquivo}.csv', 'w')
    esc = csv.writer(arquivo)
    esc.writerow(('IP', 'PORTA', 'STATUS', 'SERVIÇO', 'VERSÃO'))

def make_csv(ip, porta, status, servico, versao="N/D"):
    esc = csv.writer(arquivo)
    esc.writerow((ip, porta, status, servico, versao))

def close_csv():
    arquivo.close()