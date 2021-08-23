import os
from flask import Flask 
app = Flask(__name__)

@app.route("/")
def main():
  return "welcome"

@app.route('/How are you')
def hello():
  return 'I am fine, what about you'

if __name__ == "__main__":
  app.run()
  pass debug=True
