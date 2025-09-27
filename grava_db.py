# grava_db.py

import json
import boto3
import os

# Criar cliente DynamoDB apontando para o LocalStack
dynamodb = boto3.resource(
    'dynamodb',
    endpoint_url="http://localhost:4566",  # LocalStack
    region_name="us-east-1"
)

# Referência da tabela
table = dynamodb.Table('NotasFiscais')

def lambda_handler(event, context):
    print("Evento recebido:", event)
    
    # Tentar obter dados do POST ou GET
    body = event.get('body')
    if body:
        data = json.loads(body)
        # Gravar no DynamoDB
        table.put_item(Item=data)
        return {
            "statusCode": 200,
            "body": json.dumps({"message": "Nota gravada com sucesso!", "nota": data})
        }
    else:
        # Se não tiver body, retornamos todos os itens da tabela
        response = table.scan()
        return {
            "statusCode": 200,
            "body": json.dumps(response.get('Items', []))
        }
