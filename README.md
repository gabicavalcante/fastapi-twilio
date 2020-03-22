# fastapi-twilio

### python code formartter

- [`black`](https://github.com/psf/black)
- [`flake8`](http://flake8.pycqa.org/en/latest/)

### libs

- config: [`dynaconf`](https://dynaconf.readthedocs.io/en/latest/)

## setup

### create and configure .secrets.toml

```
$ cp .secrets.toml.sample .secrets.toml
```

## flask run

#### virtualenv

```
# virtualenv
$ virtualenv -p python3 venv
$ source venv/bin/activate
```

#### install requirements

```
$ cd fastapi-twilio
$ pip install -r requirements.txt
```

#### run

```
$  uvicorn app:app --reload
```

#### rasa

```
$ rasa init
$ rasa run --enable-api -m rasa/models/<model-name>.tar.gz
```

### to run

```
$ uvicorn app:app --reload
$ curl -X POST -F 'From=+5454545454' -F 'Body=i want pizza' -H "X-Twilio-Signature: ..."  http://127.0.0.1:8000/bot
```

### test actions

```
$ rasa run actions
$ curl -X POST --data '{ "sender": "Rasa1", "message": "sad" }' -H "Content-Type: application/json"  http://127.0.0.1:5005/webhooks/rest/webhook
[{"recipient_id":"Rasa1","text":"Here is something to cheer you up:"},{"recipient_id":"Rasa1","image":"https:\/\/i.imgur.com\/nGF1K8f.jpg"},{"recipient_id":"Rasa1","text":"Did that help you?"}]%
```

#### references

- form data:
  - https://fastapi.tiangolo.com/tutorial/request-forms/
- requests:
  - https://www.starlette.io/requests/
  - https://fastapi.tiangolo.com/advanced/using-request-directly/
