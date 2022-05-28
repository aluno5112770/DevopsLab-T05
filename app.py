from flask import Flask
from flask_wtf.csrf import CSRFProtect

app = Flask(__name__)

csrf = CSRFProtect(app)

@app.route("/")
def pagina_inicial():
    return "Agora temos uma mensagem Personalizada, Colocamos os Testes - Hi Ever Bode"

@app.route('/bug')                                                                                                                                
def bad():                                                                                                                                        
    try:                                                                                                                                          
        raise TypeError()                                                                                                                         
    except TypeError as e:                                                                                                                        
        print(e)                                                                                                                                  
    

if __name__ == '__main__':
    port = os.getenv('PORT')
    app.run('0.0.0.0', port=port)
