# 📌 Calculadora de Dois Usuários com Colorama

Esta é uma calculadora interativa para dois usuários, feita em Python, utilizando a biblioteca Colorama para exibir os resultados coloridos no terminal.

📌 Requisitos

Antes de executar o código, certifique-se de ter o Python 3 instalado no seu sistema.

Você também precisa instalar a biblioteca Colorama, que permite a exibição de cores no terminal. Para instalá-la, execute:

pip install colorama

📌 Como Executar a Calculadora

Opção 1: Executando diretamente o arquivo Python

Abra o terminal ou prompt de comando e navegue até a pasta do projeto.

Execute o seguinte comando:

python calculadora.py

Opção 2: Executando via script shell (.sh) [Linux/macOS]

Se você deseja rodar o script utilizando um arquivo .sh, faça o seguinte:

Crie um arquivo chamado rodar.sh no mesmo diretório do calculadora.py e adicione o seguinte conteúdo:

#!/bin/bash
python3 calculadora.py

Dê permissão de execução ao arquivo:

chmod +x rodar.sh

Execute o script:

./rodar.sh

📌 Funcionalidades da Calculadora

O programa solicita os nomes de dois usuários.

Cada usuário informa dois números.

Possibilidade de escolher entre as seguintes operações matemáticas:

Soma

Subtração

Multiplicação

Divisão

Potência

Resto da divisão

Todas as operações de uma vez

Os resultados são exibidos com cores no terminal.

Os resultados também são salvos automaticamente em um arquivo resultado.txt.

📌 Estrutura do Projeto

📂 Calculadora
│── calculadora.py    # Script principal
│── resultado.txt     # Arquivo gerado com os resultados
│── rodar.sh          # Script para execução no Linux/macOS
│── README.md         # Documentação do projeto


📌 Autor

Desenvolvido por [thiago alvarenga] 🚀


