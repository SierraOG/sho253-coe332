from flask import Flask, request
import json
import generate_animals
import redis
app = Flask(__name__)
rd = redis.StrictRedis(host='127.0.0.1', port=6379, db=7)

@app.route('/animals', methods=['GET'])
def get_animals():
   return json.dumps(get_data())

@app.route('/animals/head/<head>', methods=['GET'])
def get_animals_by_head(head):
   return json.dumps([animal for animal in get_data() if animal['head'] == head])

@app.route('/animals/body/<body>', methods=['GET'])
def get_animals_by_body(body):
   return json.dumps([animal for animal in get_data() if body in animal['body']])

def get_data():
    return [rd.hgetall(key.decode("utf-8")) for key in rd.keys()]

def start_redis():
    generate_animals.main(rd)

if __name__ == '__main__':
    start_redis()
    app.run(debug=True, host='0.0.0.0')
