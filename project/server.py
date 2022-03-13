import statistics
import string
import random
from modules.mongo import *

from flask import Flask, render_template, request, redirect
from os import system

app = Flask(__name__)

@app.route('/')
def index():
  return render_template("index.html")

@app.route('/generate', methods=["POST"])
def generate(): 
  if request.method == 'POST':
    url = request.json["url"]
    
    #generate unique token
    token = generate_token()

    #store it
    tokens_collections.insert_one({
      "url": url,
      "token": token,
      "hits": 0,
    })

    return  {
      "status": "ok",
      "token": token,
    }, 200

@app.route('/get-from-token', methods=["POST"])
def get_from_token():
  if request.method == "POST":
    token = request.json["token"]

    #search it up on mongodb
    tokens_cursor = tokens_collections.find({
      "token": token
    })
    
    entries = list(tokens_cursor)

    #invalid token
    if not len(entries):
      return {
      "status": "error",
      "msg": "token not found"
    }, 404
    else:
      data = entries[0]
      
      return {
        "status": "ok",
        "url": data["url"],
        "token": token,
        "hits": data["hits"]
      }, 200

'''
@app.route('/get-from-url', methods=["POST"])
def get_from_url():
  if request.method == "POST":
    url = request.json["url"]

    pointer = tokens_collections.find({
      "url": url
    })

    data = list(pointer)[0]

    return {
      "status": "ok",
      "url": url,
      "token": data["token"],
      "hits": data["hits"]
    }, 200
'''

@app.route('/search', methods=["POST"])
def search():
  if request.method == "POST":
    query = request.json["query"]

    #check if that query was already searched
    statistics_cursor = statistics_collections.find({
      "query": query
    })

    statistics_entries = list(statistics_cursor)

    #check if query was already searched
    if len(statistics_entries):     
      data = statistics_entries[0]
      n_hits = data["hits"]

      statistics_collections.update_one(
        {"_id": data["_id"]},
        {"$set":
          {
            "hits": n_hits + 1,
          }
        }
      )
    
    else:
      statistics_collections.insert_one({
        "query": query,
        "hits": 0
      })

    #get every thing
    tokens_cursor = tokens_collections.find()

    found_entries = []
    for entry in tokens_cursor:
      if query in entry["url"]:
        found_entries.append({
          "url": entry["url"],
          "token": entry["token"],
          "hits": entry["hits"]
        })
  
    return {
      "status": "ok",
      "data": found_entries
    }, 200


#Main endpoint
@app.route('/r/<token>')
def redirect_page(token):
  tokens_cursor = tokens_collections.find({
    "token": token
  })

  tokens_entries = list(tokens_cursor)

  data = tokens_entries[0]
  url = data["url"]
  n_hits = data["hits"]

  #register hit
  tokens_collections.update_one(
    {"_id": data["_id"]},
    {"$set":
        {
          "hits": n_hits + 1,
        }
    }
  )

  return redirect(url, code=301)


def generate_token():
  token = ''.join(random.choices(string.ascii_uppercase + string.digits + string.ascii_lowercase, k = 8))

  #create a unique token that isn't in the db yet
  tokens_cursor = tokens_collections.find({
    "token": token
  })

  tokens_entries = list(tokens_cursor)

  #while the token generated already exists in the db
  while len(tokens_entries):

    #generate a new token
    token = ''.join(random.choices(string.ascii_uppercase + string.digits + string.ascii_lowercase, k = 8))

    tokens_cursor = tokens_collections.find({
      "token": token
    })

    tokens_entries = list(tokens_cursor)

  return token


if __name__ == '__main__':
  #connect to database
  db = connect()

  #collections
  tokens_collections = db.tokens

  #statistics
  statistics_collections = db.statistics

  system('title ServerLogs')
  app.run(host='0.0.0.0', debug=True)
