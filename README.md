# BashRio

Plataforma web para divulgar e descobrir eventos. Usuários criam uma conta, exploram os eventos publicados e organizadores cadastram novos eventos com data, local, preço e imagem.

Projeto desenvolvido com **Django 5.2** e **SQLite**.

## Funcionalidades

- Cadastro de usuário com nome, e-mail, telefone, CPF e data de nascimento
- Login e logout com e-mail e senha
- Página inicial com menu (Criadores, Sobre, Contato) e botão **Explorar**
- Área **Minha Conta** com os dados do perfil
- Listagem de eventos, do mais recente para o mais antigo
- Cadastro de eventos com título, cidade, local, preço, data, hora, duração, informações e imagem
- Páginas de alterar senha e esqueci a senha (apenas a interface por enquanto)
- Painel administrativo do Django para gerenciar usuários, perfis, organizadores e eventos

## Tecnologias

| Camada | Tecnologia |
| --- | --- |
| Backend | Python, Django 5.2 |
| Banco de dados | SQLite |
| Upload de imagens | Pillow |
| Frontend | HTML, CSS e templates do Django |

## Pré-requisitos

- Python 3.12 ou superior
- pip
- Git

## Como rodar

1. Clone o repositório e entre na pasta do projeto Django:

```bash
git clone <url-do-repositorio>
cd Bashrio/Projbash-main
```

2. Crie e ative um ambiente virtual:

```bash
python -m venv venv
```

Linux ou macOS:

```bash
source venv/bin/activate
```

Windows (PowerShell):

```powershell
venv\Scripts\Activate.ps1
```

3. Instale as dependências:

```bash
pip install -r requirements.txt
```

4. Aplique as migrações:

```bash
python manage.py migrate
```

5. (Opcional) Crie um superusuário para acessar o `/admin/`:

```bash
python manage.py createsuperuser
```

6. Inicie o servidor:

```bash
python manage.py runserver
```

7. Acesse em http://127.0.0.1:8000/

## Rotas

| Rota | Descrição |
| --- | --- |
| `/` | Tela de login |
| `/cadastro/` | Cadastro de novo usuário |
| `/processar-login/` | Processamento do login |
| `/logout/` | Encerra a sessão |
| `/home/` | Página inicial |
| `/inicio-conta/` | Minha Conta (exige login) |
| `/alterar-senha/` | Alterar senha |
| `/esqueci-senha/` | Recuperação de senha |
| `/add-eventos/` | Lista de eventos |
| `/cadastrar-evento/` | Formulário para publicar um evento |
| `/admin/` | Painel administrativo do Django |

## Modelos

- **Perfil**: ligado ao `User` do Django, com telefone, data de nascimento e CPF
- **Organizador**: nome, e-mail, telefone e CPF
- **Evento**: título, cidade, local, preço, data, hora, duração, informações, imagem, organizador e data de criação
- **Usuario**: nome, e-mail e telefone

## Estrutura do projeto

```
Projbash-main/
├── manage.py
├── requirements.txt
├── project/              configurações do Django (settings, urls, wsgi, asgi)
├── bashrio/              app principal
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── admin.py
│   ├── migrations/
│   ├── static/bashrio/   CSS e imagens
│   └── templates/        páginas HTML
└── media/eventos/        imagens enviadas pelos usuários
```
