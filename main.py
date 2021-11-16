from flask import Flask
from flask import request
from smsTwilio import *
from emailSMTP import *

from dotenv import load_dotenv
project_folder = os.path.expanduser('~/PYTHON-SMTPMAIL')  # adjust as appropriate
load_dotenv(os.path.join(project_folder, '.env'))



app = Flask(__name__)

@app.route("/")
def main():
    test = "Prueba de variables de entorno"
    return test

@app.route("/sms")
def sms():
    contenido = request.args.get("mensaje")
    destino =  request.args.get("telefono")    
    return enviarSMS(contenido, destino)

@app.route("/mailSMTP")
def email():
    para = request.args.get("email")
    asunto = request.args.get("asunto")
    mensaje = request.args.get("mensaje")
    return sendEmail(para, asunto, mensaje)


if __name__ == "__main__":
    app.run()