#!/bin/env python3

from flask import Flask

app = Flask(__name__)


@app.route("/")
def index_root():
  with open('index.html', 'r') as file:
    return file.read()


if __name__ == "__main__":
  app.run()

