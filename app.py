from flask import Flask
from flask_wtf.csrf import CSRFProtect

app = Flask(__name__)

csrf = CSRFProtect(app)

@app.route("/")
def pagina_inicial():
    return "Agora temos uma mensagem Personalizada, Colocamos os Testes - Hi Ever Bode"
if __name__ == '__main__':
    app.run()