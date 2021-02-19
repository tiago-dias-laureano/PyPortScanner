import argparse
from src import scanner_ip
from src import scanner_url

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

if args.url:
    scanner_url.scanner_url(args)
elif args.ip:
    scanner_ip.scanner_ip(args)
else:
    print('Você precisa setar um argumento correto!')