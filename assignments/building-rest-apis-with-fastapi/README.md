# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Construa uma API REST para gerenciar tarefas usando FastAPI. Você praticará a criação de rotas HTTP, validação de dados com modelos e o uso de códigos de status e respostas de erro apropriados.

## 📝 Tasks

### 🛠️ Create the FastAPI Application and Read Routes

#### Descrição
Crie uma aplicação FastAPI para gerenciar uma lista de tarefas. Cada tarefa deve ter um identificador, um título e um indicador de conclusão. Comece expondo a lista e permitindo consultar uma tarefa pelo identificador.

#### Requisitos
O programa concluído deve:

- Criar uma aplicação FastAPI executável com Uvicorn
- Implementar `GET /tasks` para retornar todas as tarefas
- Implementar `GET /tasks/{task_id}` para retornar uma tarefa pelo identificador
- Retornar uma lista vazia quando ainda não houver tarefas
- Confirmar as rotas pela documentação interativa em `/docs`


### 🛠️ Add Task Creation and Data Validation

#### Descrição
Defina um modelo Pydantic para os dados de uma tarefa e implemente a criação de tarefas. A API deve validar os dados recebidos e gerar um identificador para cada nova tarefa.

#### Requisitos
O programa concluído deve:

- Definir um modelo de entrada que exija um título não vazio e aceite um indicador de conclusão opcional, com valor padrão `false`
- Implementar `POST /tasks` para criar e retornar uma tarefa
- Atribuir um identificador único a cada tarefa criada
- Retornar o código de status `201 Created` quando uma tarefa for criada
- Retornar erros de validação para dados de entrada inválidos


### 🛠️ Complete CRUD and Handle Missing Tasks

#### Descrição
Complete a API com operações para atualizar e remover tarefas. Trate identificadores inexistentes de maneira consistente e verifique os diferentes fluxos da API.

#### Requisitos
O programa concluído deve:

- Implementar `PUT /tasks/{task_id}` para atualizar uma tarefa existente
- Implementar `DELETE /tasks/{task_id}` para remover uma tarefa existente
- Retornar `404 Not Found` ao consultar, atualizar ou remover uma tarefa inexistente
- Retornar uma resposta apropriada após uma exclusão bem-sucedida
- Verificar os fluxos de sucesso, validação e recurso inexistente usando `/docs` ou testes automatizados
