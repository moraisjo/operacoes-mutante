# Laboratório: Teste de Mutação com a "Calculadora Mutante"

Bem-vindo ao trabalho prático de Teste de Mutação. O objetivo deste projeto é usar a ferramenta StrykerJS para avaliar e fortalecer uma suíte de testes que, à primeira vista, parece boa.

## Contexto

Este repositório contém uma biblioteca de cálculos simples. A suíte de testes inicial em `__tests__/` foi projetada para ter uma alta **cobertura de código**, mas esconde fraquezas que só o **teste de mutação** pode revelar.

Sua missão é atuar como um engenheiro de qualidade para encontrar essas fraquezas e escrever testes mais robustos para corrigi-las.

## Tarefas

1.  **Prepare o ambiente:** Clone o repositório e rode `npm install`.
2.  **Análise Inicial:**
    - Rode `npm test` para ver os testes passando.
    - Rode `npm run coverage` e anote o percentual de cobertura.
3.  **Análise de Mutação:**
    - Configure o StrykerJS (`npx stryker init`).
    - Execute a análise com `npx stryker run` (ou `npm run mutate` após configurar o script).
    - Abra o relatório HTML e analise os **mutantes que sobreviveram**.
4.  **Aprimore os Testes:**
    - Para cada mutante sobrevivente, entenda por que ele não foi "morto".
    - Adicione novos testes em `__tests__/operacoes.test.js` focados em asserções mais específicas para matar esses mutantes.
5.  **Validação Final:**
    - Rode o Stryker novamente e verifique se sua pontuação de mutação aumentou, idealmente para mais de 95%.

Siga as instruções do documento do trabalho para a entrega final. Boa sorte!

## Sessão de ferramentas e versões utilizadas

Para a elaboração deste trabalho, foi utilizado o seguinte conjunto de ferramentas e versões no ambiente local:

- Node.js: 22.13.0
- npm: 11.11.0
- Python: 3.12.3
- Matplotlib: 3.11.2
- Jest: 29.7.0
- Babel Jest: 29.7.0
- @babel/preset-env: 7.23.2
- StrykerJS Core: 10.0.0
- @stryker-mutator/jest-runner: 10.0.0

Essas versões foram empregadas para executar a suíte de testes, gerar relatórios de cobertura, aplicar mutações com StrykerJS e produzir os gráficos de apoio ao relatório final.

## Árvore de diretórios do projeto

```text
operacoes-mutante/
├── .git/
├── .gitignore
├── .stryker-tmp/
├── .venv/
├── README.md
├── assets/
│   ├── cobertura-inicial.svg
│   ├── mutacao-comparativa.svg
│   └── status-mutantes.svg
├── coverage/
│   ├── clover.xml
│   ├── coverage-final.json
│   ├── lcov.info
│   └── lcov-report/
├── docs/
│   └── RELATORIO.md
├── node_modules/
├── package-lock.json
├── package.json
├── reports/
│   └── mutation/
│       └── mutation.html
├── requirements.txt
├── scripts/
│   └── gerar_graficos.py
├── src/
│   └── operacoes.js
├── stryker.config.json
├── test/
│   └── operacoes.test.js
└── .
```

> Observação: o diretório `node_modules/` e os arquivos gerados em `coverage/`, `assets/` e `reports/` foram produzidos durante a execução do ambiente, sendo parte do processo de validação e documentação do laboratório.
