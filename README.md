# Stark Bank challenge

![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)

## Pré-requisitos

Antes de começar, certifique-se de que você tenha o seguinte software instalado em seu ambiente:

- Python 3.x
- FastApi
- Ngrok

## Instalação

1. **Clonando o repositório**

   Clone este repositório para o seu ambiente local:

   ```
   git clone https://github.com/gabrielgimenez98/starkbank_challenge.git
   cd starkbank_challenge

2. **Criando Ambiente Virtual**

   Clone este repositório para o seu ambiente local:

   ```
    python3 -m venv venv
    source venv/bin/activate  # No Windows, use "venv\Scripts\activate"

3. **Instalando dependências**

   Instale as dependências usando

   ```
    pip install -r requirements.txt
    
4. **Antes de rodar localmente**
    Tenha uma conta de desenvolvimento no starkbank e coloque o arquivo ```privateKey.pem``` na raiz do projeto.
    Faça uma rota de redirecionamento com o Ngrok para o seu localhost e coloque essa URL como um webhook de invoices.
   

5. **Rodando o projeto localmente**

   ```
    uvicorn views:app --reload
    ```

    Após isso é possível encontrar o swagger na rota ```\docs```

6. **Rodando os testes unitários**

   ```
    pytest -s tests/
    ```


