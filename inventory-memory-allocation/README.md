# PoC: Otimização de Alocação de Memória e Referências no CPython

## 📌 O Problema de Negócio (Contexto)
O sistema de WMS (Warehouse Management System) estava sofrendo com picos severos de consumo de memória RAM. Durante a madrugada, o algoritmo de simulação de reabastecimento entrava em execução e frequentemente acionava o *OOM Killer* (Out Of Memory) dos containers Linux, derrubando o serviço.

Além disso, falhas lógicas no algoritmo de simulação estavam "contaminando" o inventário real de produção com "SKUs fantasmas".

## 🔬 A Hipótese Técnica
A auditoria de código revelou dois problemas de arquitetura de dados:
1. **Mutabilidade Desnecessária:** A entidade `Produto` (SKU + Doca) estava modelada como um *Dynamic Array* (Lista). Como listas são mutáveis, o CPython realiza *over-allocation* (superalocação de memória no *Heap*) para prever futuros `appends`, desperdiçando RAM.
2. **Referência de Ponteiros (Memory Leak Lógico):** O algoritmo de simulação estava apenas copiando o ponteiro da lista original (`simulacao = inventario`). Qualquer alteração na simulação afetava o bloco de memória original.

A hipótese era refatorar a base para estruturas imutáveis (`tuple`) e isolar a simulação com Cópias Rasas (*Shallow Copies*).



## 🛠️ Metodologia do Laboratório
A prova de conceito foi estruturada para rastrear a forma como o interpretador do Python gerencia endereços de memória na Stack e no Heap:
* **Inspeção de Ponteiros:** Utilização da função `id()` nativa do C para provar fisicamente se duas variáveis apontavam para o mesmo bloco de silício na memória RAM.
* **Operadores de Identidade:** Teste de estresse comparando as abordagens de validação de valores (`==`, complexidade O(N)) versus validação de identidade (`is`, complexidade O(1)).
* **Shallow Copy:** Implementação do construtor `list()` para forçar a alocação de um novo *Array* no Heap, mantendo os ponteiros internos apontando para as mesmas tuplas imutáveis originais (economizando CPU e Memória).

## 📊 Resultados e Resolução
1. **Otimização de Tuplas:** Foi provado empiricamente que o CPython otimiza tuplas idênticas apontando-as para o mesmo endereço de memória. A refatoração das listas para tuplas eliminou o *over-allocation* e mitigou os riscos de *OOM*.
2. **Prevenção de Contaminação:** A criação da *Shallow Copy* garantiu que o motor de simulação operasse em uma lista segregada, isolando a mutabilidade da lista original, mas compartilhando a imutabilidade das tuplas.

## 🛡️ Motor de Auditoria
Como entrega final, foi desenvolvida a função `auditar_logs(log_a, log_b)`, uma ferramenta de *Code Review* automatizada que utiliza operadores O(1) (`is`) como primeira linha de defesa para alertar desenvolvedores sobre riscos de mutabilidade compartilhada (mesmo objeto no *Heap*) antes de varrer os dados (O(N)).

---
*Este laboratório faz parte do meu portfólio de estudos avançados em Engenharia de Software e arquitetura de backend.*