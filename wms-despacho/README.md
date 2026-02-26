# PoC: Otimização de Motor de Busca em Memória (Big O Notation)

## 📌 O Problema de Negócio (Contexto)
Em um cenário de logística de alta escala (WMS/Despacho de Frota), o sistema precisava monitorar o status de 100.000 veículos em tempo real. A implementação inicial utilizava uma estrutura de busca linear para validar a entrada de caminhões nas docas. 

Durante os horários de pico, a busca da placa no final da fila causava *overhead* e travava a CPU do servidor, resultando em lentidão e *timeouts* na API.

## 🔬 A Hipótese Técnica
A estrutura de dados original era um *Dynamic Array* (Lista em Python), que possui complexidade de tempo **O(n)**. A hipótese de engenharia era substituir essa alocação por uma *Hash Table* (Dicionário), reduzindo a complexidade de busca para **O(1)** (Tempo Constante) e poupando ciclos do processador.

## 🛠️ Metodologia do Laboratório
Para provar a hipótese sem usar dados sensíveis de produção, foi criado um script de *benchmark* isolado:
1. **Mock Data Realista:** Geração de 100.000 placas simuladas no padrão Mercosul (LLLNLNN) utilizando as bibliotecas nativas `string` e `random`.
2. **Ambiente Controlado:** Inserção simultânea dos mesmos dados na `list` e no `dict` para garantir integridade.
3. **Pior Cenário (Worst-case):** A busca foi realizada mirando o último item alocado na memória para forçar a lista a varrer todo o *Heap*.
4. **Isolamento de I/O:** O cronômetro (`time.time()`) isolou estritamente o tempo de processamento da CPU, deixando operações lentas de *Input/Output* (como `print`) de fora da medição.

## 📊 Telemetria e Resultados

Os testes rodaram em ambiente Linux, medindo as frações de segundo para encontrar a mesma placa nas duas estruturas:

| Estrutura de Dados | Complexidade | Tempo de Execução |
| :--- | :--- | :--- |
| **Lista (Dynamic Array)** | O(n) | ~ 0.00195 segundos |
| **Dicionário (Hash Map)** | O(1) | ~ 0.000009 segundos |

**Conclusão:** O Hash Map foi cerca de **216 vezes mais rápido**. Enquanto a lista exigiu 100.000 comparações de ponteiros, o dicionário utilizou uma função *hash* para converter a string em um endereço de memória exato, custando apenas 1 operação da CPU.

## 🛡️ Resiliência e Observabilidade
Além da performance, o código foi refatorado para garantir a estabilidade da aplicação:
* **Graceful Degradation:** Implementação do método `.get()` no dicionário para evitar exceções fatais (`KeyError`) caso uma doca bipe uma placa inexistente.
* **Default State:** Gerenciamento manual de estado na lista para garantir que os logs de observabilidade imprimam resultados precisos, eliminando "falsos positivos" de rastreamento.

---
*Este laboratório faz parte do meu portfólio de estudos avançados em Engenharia de Software e arquitetura de backend.*