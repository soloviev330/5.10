import os
import random

from bottle import route, run

import sayings

def generate_message():
  first_word = random.choice(sayings.beginnings)
  second_word = random.choice(sayings.subjects)
  third_word = random.choice(sayings.verbs)
  fourth_word = random.choice(sayings.actions)
  fifth_word = random.choice(sayings.ends)
  # return "Сегодня уже не вчера, ещё не завтра!"
  message = first_word + " "+ second_word +" "+third_word+" "+fourth_word+" "+fifth_word
  return message

def generate_big_message(i):
  message = ''
  while i !=0:
    # message = str(i) + str(message) + '\n' + str(generate_message()) 
    message = " %s %s" % (message,generate_message())
    i=i-1
  return message


@route("/api/generate/<some_id:int>")
def index(some_id):
    html = """
<!doctype html>
<html lang="en">
  <head>
    <title>Генератор утверждений</title>
  </head>
  <body>
    <div class="container">
      <h1>Коллеги, добрый день!</h1>
      <p>%s</p>
      <p class="small">Чтобы обновить это заявление, обновите страницу</p>
    </div>
  </body>
</html>
""" % (
        generate_big_message(some_id)
    )
    return html

@route("/api/generate/")
def index():
    html = """
<!doctype html>
<html lang="en">
  <head>
    <title>Генератор утверждений</title>
  </head>
  <body>
    <div class="container">
      <h1>Коллеги, добрый день!</h1>
      <p>{}</p>
      <p class="small">Чтобы обновить это заявление, обновите страницу</p>
    </div>
  </body>
</html>
""".format(
        generate_message()
    )
    return html

@route("/")
def index():
    html = """
<!doctype html>
<html lang="en">
  <head>
    <title>Генератор утверждений</title>
  </head>
  <body>
    <div class="container">
      <h1>Коллеги, добрый день!</h1>
      <p>Стртовая страница работает</p>
    </div>
  </body>
</html>
"""
    return html

@route("/api/roll/<some_id:int>")
def example_api_response(some_id):
    return {"requested_id": some_id, "random_number": random.randrange(some_id)}


if os.environ.get("APP_LOCATION") == "heroku":
    run(
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 5000)),
        server="gunicorn",
        workers=3,
    )
else:
    run(host="localhost", port=8080, debug=True)
