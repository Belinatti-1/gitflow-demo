# Gitflow Demo — Gerenciador de Tarefas

## Objetivo

Projeto demonstrativo em Python para praticar o Gitflow, utilizando branches, commits padronizados e Pull Requests para simular o desenvolvimento colaborativo.

## Funcionalidades

- Listar tarefas no terminal.
- Adicionar novas tarefas (funcionalidade planejada).

## Organização das branches

- `main`: versão estável, representando produção.
- `develop`: integração das funcionalidades em desenvolvimento.
- `feature/*`: desenvolvimento isolado de novas funcionalidades.

## Fluxo de desenvolvimento

1. Criar uma branch de feature a partir da `develop`.
2. Implementar a funcionalidade.
3. Registrar alterações com commits padronizados.
4. Abrir um Pull Request para a `develop`.
5. Solicitar revisão antes de integrar as alterações.
6. Após aprovação, realizar o merge na `develop`. Posteriormente, uma versão validada poderá ser integrada à `main`.

## Padrão de commits

- `feat:` nova funcionalidade.
- `fix:` correção de erros.
- `docs:` alterações na documentação.
- `chore:` manutenção e configuração.

## Execução

Execute no terminal:

`python3 tarefas.py`

## Tecnologias

- Python
- Git
- GitHub
