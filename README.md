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