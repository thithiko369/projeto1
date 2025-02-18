import colorama
from colorama import Fore, Style

colorama.init(autoreset=True)

print(Fore.CYAN + "=" * 40)
print(Fore.YELLOW + "            CALCULADORA              ")
print(Fore.CYAN + "=" * 40 + "\n")


usuario01 = input(Fore.GREEN + 'Digite o seu  nome de usuário 1: ')
usuario02 = input(Fore.GREEN + 'Digite o seu  nome de usuário 2: ')

def realizar_todas_operacoes(nome, num1, num2):
    """Executa todas as operações matemáticas e exibe os resultados."""
    operacoes = {
        "Soma": f"{num1} + {num2} = {num1 + num2}",
        "Subtração": f"{num1} - {num2} = {num1 - num2}",
        "Multiplicação": f"{num1} * {num2} = {num1 * num2}",
        "Divisão": f"{num1} / {num2} = {num1 / num2}" if num2 != 0 else "Erro: Divisão por zero",
        "Resto da divisão": f"{num1} % {num2} = {num1 % num2}" if num2 != 0 else "Erro: Divisão por zero"
    }


    try:
        operacoes["Potência"] = f"{num1} ** {num2} = {num1 ** num2}"
    except OverflowError:
        operacoes["Potência"] = f"{num1} ** {num2} = Erro: Número muito grande"

    print(Fore.CYAN + "=" * 40)
    print(Fore.YELLOW + f"📌   Seus Resultados {nome}:")

    for operacao, resultado in operacoes.items():
        print(Fore.GREEN + f"{operacao}: {resultado}")

    print(Fore.CYAN + "=" * 40)

    salvar_resultado(nome, num1, num2, operacoes)


def realizar_operacao_especifica(nome, num1, num2, opcao):
    """Executa apenas a operação escolhida pelo usuário."""
    operacoes = {
        "1": ("Soma", f"{num1} + {num2} = {num1 + num2}"),
        "2": ("Subtração", f"{num1} - {num2} = {num1 - num2}"),
        "3": ("Multiplicação", f"{num1} * {num2} = {num1 * num2}"),
        "4": ("Divisão", f"{num1} / {num2} = {num1 / num2}" if num2 != 0 else "Erro: Divisão por zero"),
        "5": ("Potência", f"{num1} ** {num2} = {num1 ** num2}" if num1 ** num2 < 1e100 else "Erro: Número muito grande"),
        "6": ("Resto da divisão", f"{num1} % {num2} = {num1 % num2}" if num2 != 0 else "Erro: Divisão por zero"),
    }


    nome_operacao, resultado = operacoes.get(opcao, ("Opção inválida", "Erro"))

    print(Fore.CYAN + "=" * 40)
    print(Fore.YELLOW + f"📌  Seu Resultado {nome}:")
    print(Fore.GREEN + f"{nome_operacao}: {resultado}")
    print(Fore.CYAN + "=" * 40)


    if opcao in operacoes:
        salvar_resultado(nome, num1, num2, {nome_operacao: resultado})

def solicitar_numeros(nome_usuario):
    """Solicita dois números ao usuário e retorna como float."""
    while True:
        try:
            num1 = float(input(Fore.MAGENTA + f"\n{nome_usuario}, digite o primeiro número: "))
            num2 = float(input(Fore.MAGENTA + f"{nome_usuario}, digite o segundo número: "))
            return num1, num2
        except ValueError:
            print(Fore.RED + "Por favor, insira apenas números válidos.")

def exibir_menu():
    """Exibe o menu de operações."""
    print(Fore.BLUE + "\nEscolha a operação:")
    print("1 - Soma")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")
    print("5 - Potência")
    print("6 - Resto da divisão")
    print("7 - Todas as operações")

def salvar_resultado(nome, num1, num2, operacoes):
    """Salva os resultados das operações em um arquivo de texto."""
    with open("resultado.txt", "a") as arquivo:
        arquivo.write(f"\n{nome}: {num1} e {num2}\n")
        for operacao, resultado in operacoes.items():
            arquivo.write(f"{operacao}: {resultado}\n")
        arquivo.write("=" * 40 + "\n")


continuar = 's'
while continuar.lower() == 's':
    for usuario in [usuario01, usuario02]:
        print(Fore.CYAN + f"\nUsuário: {usuario}")
        num1, num2 = solicitar_numeros(usuario)

        exibir_menu()
        opcao = input(Fore.YELLOW + "Digite o número da operação desejada: ")

        if opcao == "7":
            realizar_todas_operacoes(usuario, num1, num2)
        elif opcao in ["1", "2", "3", "4", "5", "6"]:
            realizar_operacao_especifica(usuario, num1, num2, opcao)
        else:
            print(Fore.RED + "Opção inválida. Tente novamente.")

    continuar = input(Fore.YELLOW + "\nDeseja realizar outra operação? (s/n): ").strip()
    if continuar.lower() != 's':
        print(Fore.CYAN + "\nObrigado por usar a calculadora! Até mais.")
        break











































