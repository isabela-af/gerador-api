# Importa as bibliotecas necessárias
from http.server import BaseHTTPRequestHandler
import json
import random

# A Vercel espera uma classe chamada 'handler' que herda de BaseHTTPRequestHandler
class handler(BaseHTTPRequestHandler):

    def do_GET(self):
        # 1. Define o cabeçalho da resposta
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        # IMPORTANTE: A linha abaixo resolve o problema de CORS!
        # Ela permite que seu site no GitHub Pages acesse esta API.
        self.send_header('Access-Control-Allow-Origin', '*') 
        self.end_headers()

        # 2. Sua lógica para gerar o número
        # Troque esta linha pela sua lógica proprietária se desejar
        numero_gerado = random.randint(1, 1000)

        # 3. Prepara o dicionário de resposta
        response = {'numero': numero_gerado}

        # 4. Envia a resposta no formato JSON
        self.wfile.write(json.dumps(response).encode('utf-8'))
        return
