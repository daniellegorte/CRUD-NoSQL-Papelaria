# Sistema de Cadastro e Controle de Produtos — Papelaria

## Objetivo

O projeto tem como objetivo desenvolver um sistema de cadastro e controle de produtos para uma papelaria, utilizando a linguagem Python integrada ao banco de dados MongoDB.

A aplicação permite realizar operações de consulta, cadastro, atualização e exclusão de produtos, armazenando suas informações em uma estrutura NoSQL.

## Tecnologias utilizadas
<p align="center">
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/visualstudio/visualstudio-original.svg" width="65" alt="Visual Studio"/>
  &nbsp;&nbsp;&nbsp;
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/mongodb/mongodb-original.svg" width="65" alt="MongoDB"/>
  &nbsp;&nbsp;&nbsp;
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/python/python-original.svg" width="65" alt="Python"/>
</p>

## Funcionalidades

O sistema possui um menu interativo com as seguintes funcionalidades:

| Funcionalidade | Descrição |
|---|---|
| 🔎 Consultar produto | Pesquisa um produto utilizando seu código de identificação. |
| ➕ Cadastrar produto | Permite inserir novos produtos no banco de dados, verificando a existência de códigos duplicados. |
| ✏️ Atualizar produto | Localiza um produto pelo código e permite atualizar suas informações. |
| 🗑️ Excluir produto | Localiza o produto, solicita confirmação e realiza sua exclusão. |
| 🚪 Encerrar sistema | Finaliza a execução da aplicação. |

## Como reproduzir o sistema

### 1. Requisitos

Antes de executar o projeto, é necessário instalar:

- [Python](https://www.python.org/downloads/);
- [Visual Studio](https://visualstudio.microsoft.com/);
- [MongoDB Community Server](https://www.mongodb.com/try/download/community);
- [MongoDB Compass](https://www.mongodb.com/try/download/compass).

**Importante:** durante a instalação do Visual Studio, certifique-se de selecionar a carga de trabalho **Desenvolvimento em Python**.

O MongoDB Community Server deve estar instalado e em execução como serviço do Windows.

### 2. Instalação do PyMongo

O PyMongo é a biblioteca que permite conectar a aplicação Python ao banco de dados MongoDB.

Para instalar, siga as etapas:

1. Abra o terminal do Visual Studio ou o Prompt de Comando (CMD).
2. Execute o seguinte comando:

```bash
pip install pymongo
```

3. Aguarde a conclusão da instalação.

Para verificar se a biblioteca foi instalada corretamente, execute:

```bash
pip show pymongo
```

Caso esteja utilizando o comando `python` para executar seus arquivos, também é possível instalar utilizando:

```bash
python -m pip install pymongo
```

### 3. Conexão com o servidor MongoDB

1. Certifique-se de que o serviço MongoDB esteja em execução.
2. Abra o MongoDB Compass.
3. Na tela de conexão, utilize a URI padrão do servidor local:

```text
mongodb://localhost:27017/
```

4. Clique em **Connect** para estabelecer a conexão.

### 4. Criação do banco de dados e da Collection

Após estabelecer a conexão:

1. Clique em **Create Database**.
2. Preencha os campos conforme indicado:

| Campo | Valor |
|---|---|
| Database Name | `papelaria_db` |
| Collection Name | `produtos` |

3. Clique em **Create Database** para concluir a criação.

### 5. Importação dos dados

O projeto disponibiliza o arquivo `papelaria_db.produtos.json`, contendo os dados iniciais dos produtos.

Para importar:

1. Selecione o banco de dados `papelaria_db`.
2. Abra a Collection `produtos`.
3. Clique em **Add Data**.
4. Selecione **Import JSON or CSV file**.
5. Localize e selecione o arquivo `papelaria_db.produtos.json`.
6. Selecione o formato JSON, caso solicitado.
7. Conclua a importação.

Após esse procedimento, os documentos estarão disponíveis na Collection `produtos`.

### 6. Execução do sistema

1. Abra a solução do projeto no Visual Studio.
2. Localize o arquivo Python principal:

```text
Sistema_de_Cadastro_e_Controle_Papelaria.py
```

3. Certifique-se de que o MongoDB esteja em execução.
4. Execute o arquivo pelo Visual Studio.

**Alternativamente**, abra o terminal na pasta onde está localizado o arquivo Python e execute:

```bash
python Sistema_de_Cadastro_e_Controle_Papelaria.py
```

O menu principal será apresentado no terminal, permitindo selecionar as operações disponíveis.
