# EVENTEX

Sistema de Eventos encomendado pela Morena.

## Como desenvolver?

1. Clone o repositório.
2. Crie uma virtualenv com python 3.11
3. Ative a virtualenv
4. Instale as dependências
5. Configure a instância com o .env
6. Execute os testes

```console
git clone git@github.com:mrcadu7/WTTD.git
cd wttd
python -m venv .wttd
source .wttd/bin/activate
pip install -r requirements-dev.txt
cp contrib/env-sample .env
python manage.py test
```

## Como fazer o deploy? 

*Infelizmente o Heroku não é mais gratuito*

1. Crie uma instância no Heroku (R.I.P)
2. Envie as configurações para o Heroku
3. Defina uma SECRET_KEY segura para instância
4. Defina DEBUG=False
5. Configure o serviço de email
6. Envie o código para o Heroku

```console
heroku create minhainstancia
heroku config:push
heroku config:set SECRET_KEY`python contrib/secret_gen.py`
heroku config:set DEBUG=False
configuro o email
git push heroku master --force

```
