from flask import Flask

app = Flask(__name__)

@app.route("/")
def pagina_inicial():
    return "Colocamos os Testes - Hi Ever Bode"

if __name__ == '__main__':
    app.run()