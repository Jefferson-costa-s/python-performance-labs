Middleware de Auditoria de Segurança (Meta-programação)
Assignee: Jefferson
Priority: P1 (Crítico / Compliance)
🔬 Under the Hood: First-Class Functions (Ponteiros de Função)

Para entender Decorators, você precisa esquecer a ideia de que uma "função" é apenas um bloco mágico de código que roda. No interpretador CPython, uma função é um objeto, alocado na memória Heap, exatamente como uma lista, um dicionário ou uma string.

Quando você digita def processar_pagamento():, o Python compila o seu código para bytecode, aloca esse bloco de instruções na memória e cria uma variável chamada processar_pagamento (na Stack) que funciona como um ponteiro para aquele endereço no Heap.

Em C (a linguagem do CS50), chamamos isso de Function Pointers. Como funções são apenas ponteiros para endereços de memória, você pode pegar a função A, passar o endereço dela como argumento para a função B, e pedir para a função B executá-la. Esse é o padrão de projeto conhecido como Wrapper (Embrulho). O Decorator do Python (o @) é apenas um syntax sugar (um atalho visual) para esse padrão de injeção de dependência.