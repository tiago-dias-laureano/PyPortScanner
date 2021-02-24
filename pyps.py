# -*- coding: utf-8 -*-

import argparse

from src import scanner


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='PyPortScanner v1.0')

    parser.add_argument('--url', 
                        required=False, 
                        help='Set a url que deseja fazer o scanner.')

    parser.add_argument('--ip', 
                        required=False, 
                        help="Set o ip que deseja fazer o scanner." )
                        
    parser.add_argument('-v', '--verbose',
                        required=False,
                        default=False,
                        help="Com essa opção o scanner retorna todos os detalhes. Set o valor True para obter todos os detalhes",
                        )

    args = parser.parse_args()

    if args.url:
        scanner.url(args.url, args.verbose)

    elif args.ip:
        scanner.ip(args.ip, args.verbose)
        
    else:
        print('Você precisa setar um argumento correto!')
