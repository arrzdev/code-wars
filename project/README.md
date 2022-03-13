# Shrtner API
> This app aims to create a url shortner allowing big urls to be shortened.

<!-- [![Build Status][travis-image]][gh-actions-url] -->

## Running it
```sh
pip install -r requirements.txt

python server.py
```

## Configuration
You need to setup a mongoDB, you can find the walktrough to this step in [mongo documentation](https://docs.mongodb.com/).


## Fire it up!
To start this app for development purposes:

```sh
python server.py
```

## Endpoints

| Method | Route |
|---|---|
| GET | /r/:token |
| POST | /generate |
| POST | /get-from-token |
| POST | /search |
