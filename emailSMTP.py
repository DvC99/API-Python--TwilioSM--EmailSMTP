import os
# Importamos los módulos necesarios
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from email.mime.text import MIMEText
from email.encoders import encode_base64

FROM = os.getenv("FROM")
PASSWORD = os.getenv("PASSWORD")

def sendEmail(para, asunto, mensaje):

    # Creamos objeto Multipart, quien será el recipiente que enviaremos
    msg = MIMEMultipart()
    msg['From'] = os.environ.get('FROM')
    msg['To'] = para
    msg['Subject'] = asunto

    # add in the message body
    msg.attach(MIMEText(mensaje, 'plain'))  
    
    try:        
        # Autenticamos
        mailServer = smtplib.SMTP_SSL('smtp.gmail.com', 465) 
        mailServer.ehlo()      
        mailServer.login(os.environ.get('FROM'), os.environ.get('PASSWORD'))
        

        # Enviamos
        mailServer.sendmail(os.environ.get('FROM'), para, msg.as_string())

        # Cerramos conexión
        mailServer.quit()
        return "El correo se mando correctamente"
    except Exception as e:
        return str(e)