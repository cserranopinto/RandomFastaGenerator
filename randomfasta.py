# -*- coding: utf-8 -*-
"""
Created on Mon Apr 15 22:03:10 2024

@author: cserrano
"""

import random
import argparse

def parse_arguments():
    """
    Parsea los argumentos de línea de comandos.

    Returns:
        Namespace: El espacio de nombres con los argumentos parseados.
    """
    parser = argparse.ArgumentParser(
        prog='randomfasta',
        description='Random Fasta Generator'
    )
    parser.add_argument('-t', '--total', required=True, type=int, help='Número de secuencias')
    parser.add_argument('-l', '--large', required=True, type=int, help='Largo de secuencias')
    parser.add_argument('-n', '--nuc', required=False, default='ATGC', type=str, help='Asigna set de letras')
    parser.add_argument('-s', '--seed', type=int, help='Random seed')
    return parser.parse_args()

def fastagenerator(name, large, nuc):
    """
    Genera una secuencia aleatoria en formato FASTA.

    Args:
        name (int): Id de secuencia.
        large (int): Longitud de la secuencia.
        nuc (str): Set de letras para generar la secuencia.

    Returns:
        str: Secuencia en formato FASTA.
    """
    seq = ''.join(random.choices(nuc, k=large))
    return f'>random_{name}\n{seq}'

def main():
    """
    Genera secuencias aleatorias en formato FASTA e imprime en consola.
    """
    args = parse_arguments()
    random.seed(args.seed)
    sequences = [fastagenerator(i, args.large, args.nuc) for i in range(1, args.total + 1)]
    print('\n'.join(sequences))

if __name__ == "__main__":
    main()



    
    
        


 