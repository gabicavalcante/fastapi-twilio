import json
import random
from fastapi import FastAPI, Form, Request
from twilio.twiml.messaging_response import MessagingResponse
from twilio.request_validator import RequestValidator
from dynaconf import settings
import requests


app = FastAPI()

intent_ranking = {
    "greet": ["hi!", "hey, how are you?", "how can i help?"],
    "goodbye": ["Bye!", "adios!", "take care"],
    "deny": ["Non!", "nop", "now way"],
    "mood_great": ["So happy!"],
    "affirm": ["Yes!", "OK", "great"],
    "bot_challenge": ["Yes, I'm!"],
    "mood_unhappy": [":("],
    "ask_pizza": ["what type of pizza you want?"]
}


def bot_replay(text: str) -> str:
    url = "http://localhost:5005/model/parse"  
    payload = {'text': text}
    r = requests.post(url=url, data=json.dumps(payload))
     
    intent = r.json()["intent"]["name"]
    intent_response = random.choice(intent_ranking.get(intent, ["I don't undestand"]))
    return intent_response


@app.post("/bot")
async def bot(From: str = Form(...), Body: str = Form(...)):
    resp = MessagingResponse()
    msg = resp.message()

    incoming_msg = Body.strip().lower()

    response = bot_replay(incoming_msg)
    msg.body(response)
    return str(msg)


@app.post("/user/new/reset")
async def security_bot(request: Request):
    validator = RequestValidator(settings.TWILIO_AUTH_TOKEN)

    form_ = await request.form()
    if not validator.validate(
        str(request.url), dict(form_.items()), request.headers["X-Twilio-Signature"]
    ):
        return {"message": "error"}

    sender = form_.get("From")
    
    resp = MessagingResponse()
    msg = resp.message()
    msg.body(f"Your reset link is https://example.com/reset/{temporary_password}")
    return str(resp)