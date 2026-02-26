# LOGICA DE NEGOCIO (Ferramentas)


def auditar_logs(log_a, log_b):
    """
    Compara dyuas estruturas de inventario avaliando os endereços de memoria  (ponteiros)
    Retorna o nivel de risco de mutabilidade compartilhada"""
    if log_a is log_b:
        return "CRÍTICO: Risco de Contaminação (Mesmo Objeto)"

    elif log_a == log_b:
        return "SEGURO: Cópia Rasa Otimizada"
    else:
        return "DIVERGENTE: Os logs contêm dados diferentes"


# 2 AMBIENTE DE SIMULAÇÃO (Testes locais)


def main():
    print("INICIANDO SETUP DE MEMÓRIA")
    inventory_log = []

    product_1 = ("SKUBRAHMA600", "DOCA-01")
    product_2 = ("SKUBRAHMA600", "DOCA-01")

    inventory_log.append(product_1)
    inventory_log.append(product_2)

    # Execução da Cópia Rasa (Shallow Copy)
    simulation_log = list(inventory_log)

    # Inserção divergente apenas na simulação
    product_3 = ("SKU-FANTASMA", "DOCA-99")
    simulation_log.append(product_3)

    # Relatório de Diagnóstico de Memória
    print("DIAGNÓSTICO DE ALOCAÇÃO")
    print(f"Log Original: {inventory_log}")
    print(f"Log Simulado: {simulation_log}")
    print(f"ID Original : {id(inventory_log)}")
    print(f"ID Simulado : {id(simulation_log)}")

    print("Os itens internos compartilham a mesma memória (Tuplas imutáveis)?")
    print(id(inventory_log[0]) == id(simulation_log[0]))

    # Testando o Motor de Auditoria
    print("RESULTADOS DA AUDITORIA")
    print("Cenário 1 (Passando a mesma lista):")
    print(auditar_logs(inventory_log, inventory_log))

    print("Cenário 2 (Passando uma Cópia Rasa - Shallow Copy):")
    print(auditar_logs(inventory_log, list(inventory_log)))

    print("Cenário 3 (Passando a Simulação com divergência):")
    print(auditar_logs(inventory_log, simulation_log))


if __name__ == "__main__":
    main()
