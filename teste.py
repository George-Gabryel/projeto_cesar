import sys

# Imprime a primeira parte, vai para a linha de baixo, depois volta para sobrescrever
print("Eu tenho ", end="")
sys.stdout.flush()  # Garante que o texto apareça antes do input
entrada = input()
print(f"Eu tenho {entrada} ideias.")   