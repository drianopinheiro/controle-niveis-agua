
from colorama import Fore, Style, init

# Inicializa a biblioteca Colorama
init(autoreset=False)

# Lista com os níveis e suas situações
niveis_agua = [
    ("Nível 1", "Muito baixo (crítico)"),
    ("Nível 2", "Baixo"),
    ("Nível 3", "Médio"),
    ("Nível 4", "Alto"),
    ("Nível 5", "Muito alto (alerta)")
]


def definir_cor(nivel):
    """Define a cor da mensagem conforme o nível da água."""
    cores = {
        1: Fore.RED,
        2: Fore.YELLOW,
        3: Fore.GREEN,
        4: Fore.CYAN,
        5: Fore.BLUE
    }

    return cores.get(nivel, Fore.WHITE)


def exibir_alerta(nivel):
    """Exibe a situação do reservatório com a cor correspondente."""
    if 1 <= nivel <= len(niveis_agua):
        nome, situacao = niveis_agua[nivel - 1]
        cor = definir_cor(nivel)

        print(f"{cor}{nome}: {situacao}{Style.RESET_ALL}")
    else:
        print(f"Nível inválido!{Style.RESET_ALL}")


# Simulação do monitoramento do reservatório
print("=== MONITORAMENTO DO RESERVATÓRIO ===\n")

for nivel in range(1, 6):
    exibir_alerta(nivel)

