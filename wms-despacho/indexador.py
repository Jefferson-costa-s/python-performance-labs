import random
import string
import time


def gerar_placa():
    letras = string.ascii_uppercase
    numeros = string.digits

    return f"{random.choice(letras)}{random.choice(letras)}{random.choice(letras)}{random.choice(numeros)}{random.choice(letras)}{random.choice(numeros)}{random.choice(numeros)}"


def main():
    frota_lista = []
    frota_dict = {}
    status = ("Em trânsito", "Descarregando", "Manutenção")

    for _ in range(100000):
        placa = gerar_placa()
        frota_dict[placa] = f"{random.choice(status)}"
        frota_lista.append(placa)

    placa_alvo = frota_lista[-1]

    resultado_lista = "Placa não encontrada"  # Aqui padrão é erro, caso a placa não seja encontrada, não atualiza.
    inicio = time.time()

    if placa_alvo in frota_lista:
        resultado_lista = placa_alvo

    fim = time.time()
    print(f"Resultado (lista): {resultado_lista} | Tempo: {fim - inicio} segundos")

    inicio_dict = time.time()
    resultado_dict = frota_dict.get(placa_alvo, "Placa não encontrada")
    fim_dict = time.time()
    print(
        f"Resultado da busca:{placa_alvo} Status: {resultado_dict} | Tempo: {fim_dict - inicio_dict}"
    )


if __name__ == "__main__":
    main()
