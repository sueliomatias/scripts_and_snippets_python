from flask import Flask, request, jsonify
from functools import wraps

app = Flask(__name__)

# Função para verificar se o token de autenticação é válido
def verificar_token(f):
    @wraps(f)
    def decorator(*args, **kwargs):
        token = request.headers.get('Authorization')

        # Verificar se o token é válido
        if token == 'meu_token_de_autenticacao':
            return f(*args, **kwargs)
        else:
            return jsonify({'mensagem': 'Token inválido'}), 401

    return decorator

# Rota protegida que requer autenticação
@app.route('/rota_protegida', methods=['GET'])
@verificar_token
def rota_protegida():
    return jsonify({'mensagem': 'Rota protegida'})

# Rota pública
@app.route('/rota_publica', methods=['GET'])
def rota_publica():
    return jsonify({'mensagem': 'Rota pública'})

if __name__ == '__main__':
    app.run()