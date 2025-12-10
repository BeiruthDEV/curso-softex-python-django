# 🚀 Jornada Backend: Python & Django | BFD Softex

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white)
![MySQL](https://img.shields.io/badge/MySQL-00000F?style=for-the-badge&logo=mysql&logoColor=white)

Este repositório documenta minha trajetória e evolução no curso de **Backend com Python e Django**, oferecido pela **BFD Softex**. Aqui estão reunidos meus exercícios, anotações de estudo e os projetos práticos desenvolvidos ao longo das aulas.

---

## 💡 Sobre o Repositório

O foco deste repositório é demonstrar a aplicação prática dos conceitos de Engenharia de Software voltados para o desenvolvimento web backend. O curso abrange desde a lógica de programação até a construção de aplicações monolíticas robustas e APIs.

### 🎯 Objetivos de Aprendizado Alcançados

- [x] **Domínio do Python:** Sintaxe, estruturas de dados e POO.
- [x] **Desenvolvimento Web:** Compreensão do ciclo de requisição/resposta HTTP.
- [x] **Framework Django:** Implementação do padrão MTV, Autenticação e Forms.
- [x] **Banco de Dados:** Modelagem SQL e integração com Python.
- [x] **APIs REST:** Criação de endpoints com Django Rest Framework.

---

## 📂 Estrutura do Projeto

O repositório mantém a organização original cronológica dos módulos do curso:

```bash
📁 curso-softex-python-django
│
├── 📂 modulo_1
├── 📂 modulo_2 
├── 📂 modulo_3  
├── 📂 modulo_4                    
├── 📂 modulo_05                   
│
├── 📂 exercicio_django           
├── 📂 exercicio_django_apostila2  
├── 📂 exercicio_sql               
└── 📂 exercicio_poo              
```

## 🛠️ Tecnologias e Ferramentas
As principais ferramentas utilizadas durante o desenvolvimento dos projetos:

Linguagem: Python 3.10+

Framework: Django 4.x / 5.x & Django Rest Framework

Database: MySQL / SQLite

Frontend: HTML5, CSS3 (Templates Django)

Outros: Git, Virtualenv

## 🚀 Como executar os projetos Django
Para rodar qualquer um dos projetos (ex: exercicio_django ou modulo_05) localmente:

Clone o repositório:
```bash
git clone [https://github.com/BeiruthDEV/curso-softex-python-django.git](https://github.com/BeiruthDEV/curso-softex-python-django.git)
```

Crie e ative um ambiente virtual:
```bash
python -m venv venv
# Windows:
venv\Scripts\activate
# Linux/Mac:
source venv/bin/activate
```

Instale as dependências:
```bash
pip install -r requirements.txt
```

Entre na pasta do projeto desejado e rode o servidor:
```bash
cd exercicio_django  # ou a pasta do projeto que deseja testar
python manage.py migrate
python manage.py runserver

```

## 📖 Licença
Este projeto está licenciado sob a licença MIT. Consulte o arquivo LICENSE para mais informações.