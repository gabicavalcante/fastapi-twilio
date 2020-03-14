from fastapi import FastAPI, Form, Request
from twilio.twiml.messaging_response import MessagingResponse
from twilio.request_validator import RequestValidator
from dynaconf import settings

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


@app.post('/sms/security/reset')
async def reset(request: Request):
    validator = RequestValidator(settings.TWILIO_AUTH_TOKEN)
    
    form_ = await request.form() 
    if not validator.validate(str(request.url), dict(form_.items()), request.headers['X-Twilio-Signature']):
        return {"message": "error"}

    sender = form_.get('From')
    user = User.get_user_from_phone_number(sender)
    temporary_password = user.reset_password()
    resp = MessagingResponse()
    msg = resp.message()
    msg.body(f'Your reset link is https://example.com/reset/{temporary_password}')
    return str(resp)
