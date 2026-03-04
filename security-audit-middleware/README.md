# PoC: Security Audit Middleware (Meta-programming)

## Problema de Negócio
O time de Segurança da Informação exigiu a implementação de logs de auditoria para todas as funções críticas do sistema (ex: processamento de pagamentos, deleção de usuários). 

Alterar dezenas de rotas manualmente violaria o princípio **DRY** (*Don't Repeat Yourself*) e aumentaria o risco de inserção de *bugs* na lógica financeira (regra de negócio).

## A Solução de Engenharia (Meta-programação)
A arquitetura escolhida foi a injeção de dependência via **Decorators** (`@`). No CPython, funções são cidadãos de primeira classe (*First-Class Objects*) alocadas no *Heap*. Isso nos permite passar ponteiros de função como argumentos para outras funções.

Foi construído um **Wrapper** (Higher-Order Function) que:
1. Intercepta a chamada da função original.
2. Extrai os argumentos dinamicamente utilizando `*args` e `**kwargs` (garantindo compatibilidade com qualquer assinatura de função).
3. Utiliza a biblioteca nativa `logging` para registrar a telemetria (I/O assíncrono e thread-safe).
4. Restaura os metadados da função original para as ferramentas de *debug* utilizando `functools.wraps`.
5. Libera o ponteiro para execução da lógica de negócio intocada.

## 🛠️ Stack e Padrões Aplicados
- **Linguagem:** Python 3
- **Conceitos:** Decorators, Closures, Padrão de Projeto *Wrapper*, *Separation of Concerns* (SoC).
- **Módulos:** `logging`, `functools`.