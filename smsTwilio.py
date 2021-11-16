import os
from twilio.rest import Client

TWILIO_ACCOUNT_SID = os.getenv("TWILIO_ACCOUNT_SID")
TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")

def enviarSMS(contenido, destino):
    try:
        account_sid = os.environ.get('TWILIO_ACCOUNT_SID')
        auth_token = os.environ.get('TWILIO_AUTH_TOKEN')
        client = Client(account_sid, auth_token)

        message = client.messages \
                        .create(
                            body= contenido,
                            from_= '+1 9062845744',
                            to = '+57' + destino
                        )

        print(message.sid)
        return "Mensaje enviado"
    except  Exception as e:
        return str(account_sid) + str(auth_token)
    