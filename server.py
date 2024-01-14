
from twilio.rest import Client

account_sid = 'AC6543e2959280693ae2ec878390b6b2c6'
auth_token = 'd500b3d4ed09e33f4a3622c799c22508'
client = Client(account_sid, auth_token)

message = client.messages.create(
  from_='whatsapp:+14155238886',
  body='hello world',
  to='whatsapp:+972537203731'
)

print(message.sid)