# FastAPI + Mangum + AWS Lambda

Este projeto demonstra como rodar uma API FastAPI em um ambiente serverless usando AWS Lambda e API Gateway, com o auxílio do [Mangum](https://github.com/jordaneremieff/mangum).

## Pré-requisitos

- Python 3.8+
- [pip](https://pip.pypa.io/en/stable/)
- AWS CLI configurado
- [Docker](https://www.docker.com/) (opcional, mas recomendado para empacotamento)

## Instalação local

```sh
pip install -r requirements.txt
```

Para rodar localmente:

```sh
uvicorn main:app --reload
```

Acesse [http://localhost:8000](http://localhost:8000).

## Deploy na AWS Lambda

### 1. Empacote as dependências

Crie uma pasta chamada `package` e instale as dependências nela:

```sh
mkdir package
pip install --target ./package -r requirements.txt
```

Copie o `main.py` para dentro da pasta `package`:

```sh
cp main.py package/
```

Dentro da pasta `package`, compacte tudo em um arquivo ZIP:

```sh
cd package
zip -r ../deployment-package.zip .
cd ..
```

### 2. Crie a função Lambda

- No console AWS Lambda, crie uma nova função (Python 3.8 ou superior).
- Informe que a funcão terá uma URL
- Faça upload do arquivo `deployment-package.zip` como código da função.

### 3. Configure o handler

No campo **Handler**, coloque:

```
main.handler
```

### 4. Integre com o API Gateway

- Crie um novo API Gateway REST ou HTTP.
- Configure como proxy para a função Lambda criada.

### 5. Teste

Acesse a URL do API Gateway para testar os endpoints:

- `/` → Mensagem de boas-vindas
- `/hello/{name}` → Saudação personalizada

## Observações

- O arquivo principal deve se chamar `main.py` e conter a variável `handler = Mangum(app)`.
- Para ambientes de produção, utilize camadas (Layers) para dependências maiores.

---

Qualquer dúvida, consulte a [documentação do Mangum](https://mangum.io/) ou [FastAPI](https://fastapi.tiangolo.com/)