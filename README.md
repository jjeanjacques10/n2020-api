# API - N2020 - Goodbot

A API desenvolvida para o aplicativo [Goodbot](https://github.com/jjeanjacques10/n2020-mobile). Desafio FIAP

## Configuração

Configurar banco de dados: [`repository/database_helper.py`](./repository/database_helper.py)

``` py
mydb = mysql.connector.connect(
    host="",
    user="",
    passwd="",
    database="",
    auth_plugin='mysql_native_password'
)
```

## Tecnologias 

- Python
- Flask

## Endpoints

- Conversas
- Usuários
- Sugestões

---
Developed by [Jean Jacques Barros](https://github.com/jjeanjacques10)
