import csv

def create_csv(arg1):
    global arq
    nome_arquivo = arg1.replace('.','_')
    arq = open(f'relatorios/{nome_arquivo}.csv', 'w')
    esc = csv.writer(arq)
    esc.writerow(('IP', 'PORTA', 'STATUS', 'SERVIÇO'))

def make_csv(arg1, arg2, arg3, arg4):
    esc = csv.writer(arq)
    esc.writerow((arg1, arg2, arg3, arg4))

def close_csv():
    arq.close()