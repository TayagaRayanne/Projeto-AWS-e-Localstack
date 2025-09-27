# Registro de Progresso - LocalStack

Este arquivo documenta o progresso do projeto Lambda, registrando prints do LocalStack, testes da Lambda, S3, DynamoDB e API Gateway.

---

## 1. AWS Configure
Descrição: Configurando os acessos AWS no powershell
![AWS configure](prints/awsconfigure.png)

---

## 2. Criação do Lambda
Descrição: Print mostrando a função Lambda `ProcessarNotasFiscais` criada atravez do powershell e também no localstack.
![Lambda Criada](prints/lambdacriada.png)
![Lambda Localstack](prints/lambdanolocalstack.png)

---

## 3. Criação do Bucket S3
Descrição: Print do console mostrando a criação do bucket `notas-fiscais-upload` no powershell e no localstack.
![S3 Bucket](prints/s3criado.png)
![Bucket Localstack](prints/bucket.png)

---

## 4. Criação da Tabela DynamoDB
Descrição: Print mostrando a tabela `NotasFiscais` criada no DynamoDB no powershell.
![DynamoDB Tabela](prints/dynamodbcriada.png)
![DynamoDB LLocalstack](prints/dynamodb.png)

---

## 5. Status Localstack
Descrição: Print mostrando quando foi criada o localstack.
![Status Localstack](prints/statuslocalstack.png) 
![Localstack Rodando](prints/localstackrodando.png)

---

## 6. API Gateway Configurada
Descrição: Print mostrando o recurso `/notas` e integração com a Lambda no localstack.
![API Gateway](prints/apicriada.png)
![API Localstack](prints/imagemapilocalstack.png)

---
