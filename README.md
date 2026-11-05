# Gitflow Demo — Gerenciador de Tarefas

## Objetivo

Projeto demonstrativo desenvolvido em Python para praticar o Gitflow, utilizando branches, commits padronizados e Pull Requests para simular um fluxo de desenvolvimento colaborativo.

A aplicação consiste em um gerenciador de tarefas simples, com funcionalidades implementadas progressivamente para demonstrar o controle de versões.

## Funcionalidades

- Listagem de tarefas no terminal.
- Adição de novas tarefas a uma lista.
- Exibição da lista atualizada após a inclusão de uma tarefa.

## Estrutura do projeto

- `README.md`: documentação do projeto e do fluxo Gitflow.
- `tarefas.py`: implementação das funções de gerenciamento de tarefas.

## Organização das branches

- **main:** mantém a versão estável do projeto, representando o ambiente de produção.
- **develop:** branch de integração das funcionalidades em desenvolvimento.
- **feature/adicionar-tarefa:** desenvolvimento isolado da funcionalidade de adicionar tarefas.

## Fluxo de desenvolvimento

1. Criar uma branch `feature/*` a partir da `develop`.
2. Implementar a funcionalidade sem modificar diretamente a `main`.
3. Registrar as alterações utilizando commits padronizados.
4. Publicar a branch no repositório remoto.
5. Abrir um Pull Request direcionado à `develop`.
6. Solicitar revisão de código antes da integração.
7. Após aprovação, realizar o merge na `develop`. Posteriormente, uma versão validada poderá ser integrada à `main`.

## Evolução do projeto

### Versão inicial — main

Implementação da função `listar_tarefas()`, responsável por exibir tarefas predefinidas no terminal.

### Nova funcionalidade — feature/adicionar-tarefa

Implementação da função `adicionar_tarefa()`, utilizando o método `append()` para adicionar novos itens à lista.

A função `listar_tarefas()` também foi adaptada para percorrer os elementos da lista utilizando um laço `for`.

As alterações são propostas à branch `develop` por meio de um Pull Request, permitindo a revisão antes da integração.

## Padrão de commits

O projeto utiliza mensagens baseadas em Conventional Commits:

- `feat:` implementação de novas funcionalidades.
- `fix:` correção de erros.
- `docs:` alterações na documentação.
- `chore:` manutenção e configuração do projeto.

## Execução

Para executar o projeto, utilize:

`python3 tarefas.py`

Não são necessárias dependências externas.

## Tecnologias

- Python
- Git
- GitHub