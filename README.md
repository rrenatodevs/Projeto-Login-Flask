# Projeto Login - Flask

Sistema de autenticação (login/cadastro) construído para estudo, conectando um frontend em HTML/CSS/JavaScript a um backend em Python com Flask e banco de dados SQLite.

## 🎯 Sobre o projeto

Este projeto tem como objetivo praticar a integração completa entre frontend e backend:

- Interface de login responsiva (HTML + CSS)
- API REST em Flask para autenticação
- Banco de dados estruturado com SQLAlchemy
- Senhas armazenadas com hash seguro (nunca em texto puro)
- Comunicação frontend ↔ backend via JavaScript (fetch)

## 🛠️ Tecnologias utilizadas

- **Python 3.14**
- **Flask** — servidor e rotas da API
- **Flask-SQLAlchemy** — ORM para o banco de dados
- **Werkzeug** — hash de senhas
- **SQLite** — banco de dados
- **HTML5 / CSS3 / JavaScript** — frontend

## 📁 Estrutura do projeto
Projeto Login/
├── static/
│   └── style.css          # Estilos da aplicação
├── templates/
│   └── index.html         # Página de login
├── app.py                 # Servidor Flask e rotas da API
├── models.py               # Modelo do banco de dados (Usuario)
└── requirements.txt        # Dependências do projeto

## 🚀 Como rodar o projeto

### 1. Clone o repositório

```bash
git clone https://github.com/rrenatodevs/Projeto-Login-Flask.git
cd Projeto-Login-Flask
```

### 2. Crie e ative um ambiente virtual

```bash
python -m venv venv
venv\Scripts\activate      # Windows
```

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

### 4. Rode o servidor

```bash
python app.py
```

### 5. Acesse no navegador
http://127.0.0.1:5000

## 📌 Rotas da API

| Método | Rota            | Descrição                          |
|--------|-----------------|-------------------------------------|
| GET    | `/`              | Retorna a página de login          |
| POST   | `/api/cadastro`  | Cria um novo usuário                |
| POST   | `/api/login`     | Autentica um usuário existente     |

## 🔜 Próximos passos

- [ ] Criar tela de cadastro de usuário
- [ ] Implementar sessão de login (Flask session)
- [ ] Criar página protegida após login (dashboard)
- [ ] Deploy em produção

## 👤 Autor

Renato — estudante de Análise e Desenvolvimento de Sistemas (UNICID)
