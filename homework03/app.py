from flask import Flask, request
import json
app = Flask(__name__)

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
   with open("./animals.json", "r") as json_file:
      animal_data = json.load(json_file)
      return animal_data['animals']

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

