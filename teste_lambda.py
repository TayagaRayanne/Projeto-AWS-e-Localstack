from grava_db import lambda_handler
import json

# Teste POST
evento_post = {
    "body": json.dumps({"idNota": "1", "descricao": "Nota teste"})
}
resposta_post = lambda_handler(evento_post, None)
print("Resposta POST:", resposta_post)

# Teste GET
evento_get = {}
resposta_get = lambda_handler(evento_get, None)
print("Resposta GET:", resposta_get)

