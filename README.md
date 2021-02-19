# PyPortScanner

[![Generic badge](https://img.shields.io/badge/build-passing-green.svg)](https://shields.io/)
[![Generic badge](https://img.shields.io/badge/python-2.6|3.x-yellow.svg)](https://shields.io/)
[![Generic badge](https://img.shields.io/badge/license-MIT-red.svg)](https://shields.io/)

Um PortScanner desenvolvido em Python

## Instalação

Você pode baixar o repositório diretamente com o git clone

```bash
git clone https://github.com/tiago-dias-laureano/PyPortScanner.git
```


## Como usar

Para obter ajuda de como utilizar a ferramenta:
```python
python pyps.py -h
```
Para executar o scanner em um site:
```python
python pyps.py --url https://site.com.br/ 
```

![alt text](https://i.ibb.co/BZ6cXRW/img1.png)


Para executar o scanner em um ip:
```python
python pyps.py --ip 192.168.0.1
```

![alt text](https://i.ibb.co/Svj7QdX/im2.png)

Para executar o scanner em um ip ou site no modo verbose:
```python
python pyps.py --url https://site.com.br/ --verbose True
```
![alt text](https://i.ibb.co/PFN0RSF/im3.png)

## Relatórios
Todos os scanners realizados com o PyPS tem geração automática de um arquivo CSV contendo informações necessárias para fazer a ánalise geral dos serviços sendo utilizados. Criações de relatórios visuais será possivel em versões posteriores.

## Contribuição
Correções de bugs, implementação de features são bem-vindas. Para mudanças importantes, abra um problema primeiro para discutir o que você gostaria de mudar ou adicionar.

## Licensa
[MIT](https://choosealicense.com/licenses/mit/)
