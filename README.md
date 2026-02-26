# ⚙️ Backend Engineering PoCs & Labs

Este repositório contém uma série de laboratórios e provas de conceito (PoCs) desenvolvidos em Python. O objetivo é explorar conceitos de baixo nível, otimização de CPU/Memória, Big O Notation e estruturas de dados aplicadas a problemas reais de arquitetura de software e engenharia de backend.

---

## 🗂️ Índice de Laboratórios (Provas de Conceito)

Aqui estão os experimentos isolados, documentando o problema de negócio, a hipótese técnica e a prova matemática de performance:

### 1. [Otimização de Alocação de Memória e Referências no CPython](./inventory-memory-allocation)
* **Domínio:** Logística / WMS (Warehouse Management System).
* **Conceitos Explorados:** Stack vs Heap, Ponteiros, Mutabilidade, Prevenção de *OOM Killer*, *Shallow Copy*.
* **O que foi provado:** Como a troca de *Dynamic Arrays* (Listas) por Tuplas imutáveis elimina o *over-allocation* de memória e previne o vazamento lógico de referências.

### 2. [Motor de Busca O(1) e Complexidade de Tempo](./fleet-hashmap-indexer)
* **Domínio:** Despacho de Frota / Telemetria.
* **Conceitos Explorados:** Big O Notation, Hash Tables (Dicionários) vs Arrays (Listas), Resiliência (*Graceful Degradation*).
* **O que foi provado:** A substituição de uma busca linear O(n) por um mapeamento Hash O(1), resultando em uma consulta de CPU mais de 200x mais rápida em uma base de 100.000 registros, evitando *timeouts*.

---

## 🛠️ Stack Analítico
* **Linguagem Base:** Python 3 (Foco no motor CPython)
* **Princípios Aplicados:** Separation of Concerns (SoC), Single Responsibility Principle (SRP), Observabilidade e Gerenciamento de Risco.