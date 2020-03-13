from fastapi import FastAPI, Form  
from twilio.twiml.messaging_response import MessagingResponse

app = FastAPI()
 
class User():
    @staticmethod
    def get_user_from_phone_number(sender):
        return User()

    def reset_password(self):
        return "12345"

@app.post('/sms/reset')
async def reset(From: str = Form(...)):
    sender = From
    user = User.get_user_from_phone_number(sender)
    temporary_password = user.reset_password()
    resp = MessagingResponse()
    msg = resp.message()
    msg.body(f'Your reset link is https://example.com/reset/{temporary_password}')
    return str(resp)