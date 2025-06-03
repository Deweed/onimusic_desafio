# 🐍 Desafio Técnico — Vaga de Estágio Backend (Python + Django)

Seja bem-vindo(a) ao nosso desafio técnico! 🎯

O objetivo aqui não é te pressionar, mas sim entender como você aplica lógica de programação, organiza seu raciocínio e estrutura seu código em Python.

---

## 🚀 Desafio

Desenvolva uma pequena API (ou script) para gerenciar um **cadastro simples de filmes**.

Cada filme deve conter as seguintes informações:

- `id` (inteiro)
- `titulo` (string)
- `ano` (inteiro)
- `genero` (string)

---

## 🎯 Funcionalidades obrigatórias:

1. ✅ **Listar todos os filmes cadastrados.**
2. ✅ **Adicionar um novo filme.**
3. ✅ **Buscar um filme pelo ID.**
4. ✅ **Remover um filme pelo ID.**

> A persistência dos dados pode ser feita **em memória** (listas ou dicionários), não é necessário banco de dados.

---

## 💡 Extras (opcional, diferencial):

- 🔎 Filtrar filmes por **gênero** ou **ano**.

---

## 🛠️ Tecnologias

- A solução deve ser desenvolvida em **Python 3**.
- Você pode escolher uma das abordagens:
  - 🖥️ Um script simples no terminal com menu interativo.
  - 🌐 Uma API utilizando **Django** (pode usar Django REST Framework se desejar) ou **Flask**/**FastAPI**, se tiver familiaridade.

---

## ✅ O que vamos avaliar:

- Organização do código.
- Lógica de programação.
- Clareza na estrutura e nomeação de variáveis e funções.
- Uso correto de estruturas como listas, dicionários, funções, classes, etc.
- Boas práticas básicas de desenvolvimento.
- Se fizer API: noções de rotas, métodos HTTP, e estrutura de uma aplicação web.

---

## ⏳ Tempo estimado

- De **1 a 2 horas**.

---

## 📦 Como entregar

1. Suba seu projeto em um repositório no GitHub (ou envie um arquivo .zip, se preferir).
2. Inclua neste repositório:
   - O código-fonte.
   - Este arquivo `README.md` atualizado, com instruções de como executar seu projeto.

---

## 🚀 Como rodar seu projeto

### 📋 Requisitos do Sistema

- Python 3.9+ (versões mais recentes são recomendadas)
- pip (gerenciador de pacotes do Python)
- Git (para clonar o repositório)

---

### 💻 Como Rodar o Projeto
Siga os passos abaixo para configurar e executar a API e a interface.

#### - Clonar o Repositório
Clone o repositório para sua máquina local usando Git:

```
git clone https://github.com/Deweed/onimusic_desafio.git
cd onimusic_desafio
```

#### - Configurar o Ambiente Virtual
É altamente recomendado criar um ambiente virtual para isolar as dependências do projeto.

---

### Criar o ambiente virtual
```
python -m venv venv
```

---

### Ativar o ambiente virtual:
```
1.1 No Windows (PowerShell):

.\venv\Scripts\Activate.ps1

1.2 No Windows (Command Prompt/CMD):

.\venv\Scripts\activate

1.3 No macOS/Linux:

# source venv/bin/activate
```

#### - Instalar Dependências
Com o ambiente virtual ativado, instale todas as bibliotecas Python necessárias:

```
pip install django djangorestframework requests
```

#### - Realizar Migrações do Banco de Dados

Aplique as migrações:
```
python manage.py makemigrations filmes
python manage.py migrate
```

#### - Iniciar o Servidor de Desenvolvimento do Django
Abra seu terminal no VS Code e execute o servidor Django:

```
python manage.py runserver
```
O servidor estará rodando em `http://127.0.0.1:8000/`. Você pode acessar `http://127.0.0.1:8000/api/filmes/` 
no seu navegador para ver a interface de navegação do Django REST Framework.

`Mantenha este terminal aberto e o servidor rodando.`

#### - Rodar a Interface Terminal
Para interagir com a API usando o script que criamos, você precisará de um segundo terminal.

Abra um novo terminal no VS Code: 
Clique no sinal de + ao lado da aba atual do terminal ou vá em Terminal > New Terminal.
Ative o ambiente virtual neste novo terminal também:
```
No Windows (PowerShell):
.\venv\Scripts\Activate.ps1

No Windows (Command Prompt/CMD):
.\venv\Scripts\activate

No macOS/Linux:
source venv/bin/activate
```

Execute o script:

```
python client_cli.py
```

Agora você verá um menu interativo no seu segundo terminal.

---

## 🤝 Contribuição
Sinta-se à vontade para contribuir com este projeto. Crie um fork, faça suas alterações e envie um pull request.
✨
