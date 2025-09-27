# Projeto AWS e Localstack
Criado por: Tayaga Rayanne

Este projeto faz parte de uma atividade do Bootcamp AWS Code Girls da Dio.

Este projeto é um hands-on de AWS Lambda, DynamoDB, S3 e API Gateway usando **LocalStack** como ambiente local de simulação da AWS.  
O objetivo é criar um fluxo completo: enviar arquivos para um bucket S3, acionar uma Lambda, inserir dados no DynamoDB e disponibilizar via API Gateway.

---
## Minha experiência durante o desenvolvimento:

Desafios:
Docker não estava conectando corretamente; tive que rinstalar o docker pois a minha versão não estava mais funcionando e isso me trouxe muitos problemas de conexão.
Conectar o LocalStack foi difícil, exigiu várias tentativas e ajustes. Muito pelo problema que tive com o docker e com uma incompatibilidade que encontrei no gitbash.

Partes mais fáceis:
Criar a Lambda, o DynamoDB e a API Gateway funcionou sem grandes problemas.
O projeto foi muito enriquecedor para entender o fluxo completo de AWS Lambda + S3 + DynamoDB + API Gateway, mesmo simulando localmente.

Registro de Progresso:
Criei uma pasta prints/ para armazenar imagens do LocalStack, prints do console e do progresso do projeto.

---

## Estrutura do Projeto

- `grava_db.py` - Código responsável por gravar os dados no DynamoDB.
- `teste_lambda.py` - Código para testar a Lambda localmente.
- `requirements.txt` - Dependências do projeto.
- `.gitignore` - Arquivos e pastas ignorados pelo Git.
- `README.md` - Documentação do projeto.
- `prints/` - Pasta para armazenar imagens do LocalStack e registros do progresso.
- `prints.mb` - Arquivo com os prints do progresso.

---

## Pré-requisitos

- **LocalStack**  
  Baixar e instalar: [Instalação LocalStack](https://docs.localstack.cloud/getting-started/installation/)  
  Opção Desktop: [LocalStack Desktop](https://docs.localstack.cloud/user-guide/tools/localstack-desktop/)

- **Docker** (opcional, se usar LocalStack em container)  
```bash
docker run -d --name localstack -p 4566:4566 -p 4571:4571 \
-e SERVICES=ALL -e DEBUG=1 \
-v /var/run/docker.sock:/var/run/docker.sock \
localstack/localstack
AWS CLI Local

powershell
Copiar código
aws configure
# Defina credenciais fictícias:
$env:AWS_ACCESS_KEY_ID="?"
$env:AWS_SECRET_ACCESS_KEY="?"
$env:AWS_DEFAULT_REGION="us-east-1"
$env:AWS_DEFAULT_OUTPUT=json
Passo a Passo
1. Iniciar LocalStack
bash
Copiar código
localstack start
Acesse: http://localhost:4566
Verifique o status:

powershell
Copiar código
Invoke-RestMethod -Uri "http://localhost:4566/_localstack/health"
2. Criar recursos AWS local
Bucket S3: notas-fiscais-upload

bash
Copiar código
awslocal s3api create-bucket --bucket notas-fiscais-upload
Tabela DynamoDB: NotasFiscais (chave primária: id)

bash
Copiar código
aws dynamodb create-table --endpoint-url=http://localhost:4566 \
--table-name NotasFiscais \
--attribute-definitions AttributeName=id,AttributeType=S \
--key-schema AttributeName=id,KeyType=HASH \
--provisioned-throughput ReadCapacityUnits=5,WriteCapacityUnits=5
Lambda Function: ProcessarNotasFiscais

bash
Copiar código
aws lambda create-function --function-name ProcessarNotasFiscais \
--runtime python3.9 \
--role arn:aws:iam::000000000000:role/lambda-role \
--handler grava_db.lambda_handler \
--zip-file fileb://lambda_function.zip \
--endpoint-url=http://localhost:4566
Trigger do S3 para Lambda

bash
Copiar código
aws lambda add-permission --function-name ProcessarNotasFiscais \
--statement-id s3-trigger-permission \
--action "lambda:InvokeFunction" \
--principal s3.amazonaws.com \
--source-arn "arn:aws:s3:::notas-fiscais-upload" \
--endpoint-url=http://localhost:4566

aws s3api put-bucket-notification-configuration \
--bucket notas-fiscais-upload \
--notification-configuration file://notification_roles.json \
--endpoint-url=http://localhost:4566
API Gateway

bash
Copiar código
aws apigateway create-rest-api --name "NotasFiscaisAPI" --endpoint-url=http://localhost:4566
Configure recursos /notas, métodos POST/GET e integração com Lambda.
Conceda permissão à API para invocar a Lambda e faça o deployment no stage dev.

Testando o fluxo
Enviar arquivo JSON para S3

bash
Copiar código
aws s3 cp notas_fiscais_2025.json s3://notas-fiscais-upload --endpoint-url=http://localhost:4566
Testar API via Python

python
Copiar código
import requests
url = "http://localhost:4566/restapis/<api_id>/dev/_user_request_/notas"
data = {"id": "NF-999", "cliente": "João Silva", "valor": 1000.0, "data_emissao": "2025-01-31"}
response = requests.post(url, json=data)
print(response.json())
Verifique os logs da Lambda e os dados inseridos no DynamoDB.

---

Como rodar
Instale as dependências:

bash
Copiar código
pip install -r requirements.txt
Configure LocalStack e AWS CLI conforme descrito acima.

Teste a Lambda:

bash
Copiar código
python teste_lambda.py
Observações
Projeto pronto para subir no GitHub.

Adapte grava_db.py e teste_lambda.py conforme suas necessidades.
