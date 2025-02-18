# 📌 Calculadora de Dois Usuários com Colorama

Uma calculadora interativa para dois usuários, desenvolvida em Python, utilizando a biblioteca Colorama para exibir os resultados coloridos no terminal.

📌 Requisitos
Antes de executar o código, certifique-se de que você tem o Python 3 instalado no seu sistema.

Além disso, é necessário instalar a biblioteca Colorama para exibição de cores no terminal. Para isso, execute:
bash
Copiar
Editar
pip install colorama

📌 Como Executar a Calculadora

🔹 Opção 1: Executando diretamente o arquivo Python
Abra o terminal ou prompt de comando.
Navegue até a pasta onde está o projeto.
Execute o seguinte comando:
bash
Copiar
Editar
python calculadora.py

🔹 Opção 2: Executando via script shell (.sh) [Linux/macOS]
Se estiver utilizando Linux/macOS, pode rodar o script através de um arquivo .sh:

Crie um arquivo chamado rodar.sh no mesmo diretório do calculadora.py.
Adicione o seguinte conteúdo ao arquivo:
bash
Copiar
Editar
#!/bin/bash
python3 calculadora.py
Dê permissão de execução ao script com o comando:
bash
Copiar
Editar
chmod +x rodar.sh
Agora, execute o script:
bash
Copiar
Editar
./rodar.sh
📌 Funcionalidades da Calculadora
✅ Solicita os nomes de dois usuários.
✅ Cada usuário informa dois números.
✅ Permite escolher entre as seguintes operações matemáticas:

Soma
Subtração
Multiplicação
Divisão
Potência
Resto da divisão
Executar todas as operações de uma vez
✅ Exibe os resultados no terminal com cores para melhor visualização.
✅ Salva os resultados automaticamente no arquivo resultado.txt.

📌 Estrutura do Projeto
bash
Copiar
Editar

📂 Calculadora  
│── calculadora.py   # Script principal  
│── resultado.txt    # Arquivo gerado com os resultados  
│── rodar.sh         # Script para execução no Linux/macOS  
│── README.md        # Documentação do projeto  

📌 Autor
Desenvolvido por Thiago Alvarenga 🚀

