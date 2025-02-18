#!/bin/bash

# Verifica se o Python está instalado
if ! command -v python3 &> /dev/null
then
    echo "Python3 não encontrado. Instale o Python para continuar."
    exit 1
fi

# Executa a calculadora
python3 calculadora.py
