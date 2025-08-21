# Importa as bibliotecas necessárias
from http.server import BaseHTTPRequestHandler
import json
import random

# A Vercel espera uma classe chamada 'handler' que herda de BaseHTTPRequestHandler
class handler(BaseHTTPRequestHandler):

    def do_GET(self):
        from urllib.parse import urlparse, parse_qs
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()

        # Pega os parâmetros da URL
        query = urlparse(self.path).query
        params = parse_qs(query)
        tipo = params.get('tipo', ['aleatorio'])[0]

        if tipo == 'intervalo':
            min_str = params.get('min', [''])[0]
            max_str = params.get('max', [''])[0]
            if min_str.isdigit() and max_str.isdigit():
                min_val = int(min_str)
                max_val = int(max_str)
                if min_val > max_val:
                    numero_gerado = 'Erro: mínimo maior que máximo'
                else:
                    numero_gerado = random.randint(min_val, max_val)
            else:
                numero_gerado = 'Erro: valores inválidos'
        else:
            numero_gerado = random.randint(1, 1000)

        response = {'numero': numero_gerado}
        self.wfile.write(json.dumps(response).encode('utf-8'))
        return
