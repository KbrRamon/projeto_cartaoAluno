# 🪪 Cartão Aluno - Projeto Django

Este é um projeto web desenvolvido em **Python** e **Django** para o gerenciamento de cartões e informações de alunos. O sistema permite cadastrar alunos com seus respectivos dados de identificação (nome, idade, matrícula), além de gerenciar a persistência dessas informações em um banco de dados relacional por meio do ORM do Django.

---

## 🚀 Tecnologias Utilizadas

* **Python 3.x** - Linguagem de programação principal.
* **Django 5.x** - Framework web para desenvolvimento ágil e seguro.
* **SQLite / PostgreSQL** - Banco de dados relacional.
* **HTML5 / CSS3** - Estrutura e estilização das telas.

---

## 📌 Funcionalidades Principais

* 📝 **Cadastro de Alunos:** Registro com validação de campos obrigatórios (nome, idade, matrícula única).
* 🗃️ **Mapeamento de Banco de Dados:** Modelos integrados via Django ORM (`models.py`).
* ⚙️ **Painel Administrativo:** Interface interna para administração dos registros de alunos.
* 🔄 **Sistema de Migrações:** Gerenciamento estruturado de schemas do banco de dados com `makemigrations` e `migrate`.

---

## 🛠️ Como Executar o Projeto Localmente

### 1. Pré-requisitos
Certifique-se de ter instalado em sua máquina:
* [Python 3.x](https://www.python.org/downloads/)
* [Git](https://git-scm.com/)

---

### 2. Passo a Passo

1. **Clonar o repositório:**
   ```bash
   git clone [https://github.com/KbrRamon/projeto_cartaoAluno.git](https://github.com/KbrRamon/projeto_cartaoAluno.git)
   cd projeto_cartaoAluno