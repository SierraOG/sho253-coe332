from flask import Flask, request
import json
import generate_animals
import redis
from datetime import datetime
app = Flask(__name__)
rd = redis.StrictRedis(host='127.0.0.1', port=6379, db=0)

@app.route('/animals', methods=['GET'])
def get_animals():   
   return json.dumps(get_data())

@app.route('/animals/reset', methods=['GET'])
def reset_animals():   
   generate_animals.main()
   return "Reset"

# With post request
# @app.route('/animals/id/<key>', methods=['GET', 'POST'])
# def get_animal_by_id(key):
#    if request.method == 'POST':
#       rd.hmset(key, request.form)
#       return f"Successfully updated {key}"
#    else:
#       banimal = rd.hgetall(key)
#       animal = { y.decode('utf-8'): banimal.get(y).decode('utf-8') for y in banimal.keys() }
#       return json.dump(animal)

# Without post request
@app.route('/animals/id/<key>', methods=['GET'])
def get_animal_by_id(key):
   banimal = rd.hgetall(key)
   animal = { y.decode('utf-8'): banimal.get(y).decode('utf-8') for y in banimal.keys() }
   return json.dump(animal)

@app.route('/animals/update/id/<key>/<stats>', methods=['GET'])
def update_animal_by_id(key):
   rd.hmset(key, json.loads(stats))
   return "Successfully updated"

@app.route('/animals/head/<head>', methods=['GET'])
def get_animals_by_head(head):
   return json.dumps([animal for animal in get_data() if animal['head'] == head])

@app.route('/animals/body/<body>', methods=['GET'])
def get_animals_by_body(body):
   return json.dumps([animal for animal in get_data() if body in animal['body']])

@app.route('/animals/date/<date1>/<date2>', methods=['GET'])
def get_animals_by_date(date1, date2):
   a = datetime.strptime(date1, "%d/%m/%Y-%H:%M:%S")
   b = datetime.strptime(date2, "%d/%m/%Y-%H:%M:%S")
   return json.dumps([animal for animal in get_data() if a <= datetime.strptime(animal['created_on'], "%d/%m/%Y %H:%M:%S") <= b])

@app.route('/animals/delete/date/<date1>/<date2>', methods=['GET'])
def delete_animals_by_date(date1, date2):
   a = datetime.strptime(date1, "%d/%m/%Y-%H:%M:%S")
   b = datetime.strptime(date2, "%d/%m/%Y-%H:%M:%S")
   for key in rd.keys():
      banimal = rd.hgetall(key)
      animal = { y.decode('utf-8'): banimal.get(y).decode('utf-8') for y in banimal.keys() }
      if a <= datetime.strptime(animal['created_on'], "%d/%m/%Y %H:%M:%S") <= b:
         rd.delete(key) 
   return f"Successfully deleted animals between {date1} and {date2}"

@app.route('/animals/average/<body_part>', methods=['GET'])
def get_average(body_part):
   assert body_part == 'legs' or body_part == 'tails' or body_part == 'arms'
   animals = get_data()
   return sum([num for animal[body_part] in animals])/len(animals)

@app.route('/animals/total', methods=['GET'])
def get_total():
   return len(get_data())

def get_data():
   keys = [key.decode("utf-8") for key in rd.keys()]
   banimals = [rd.hgetall(key) for key in keys]
   animals = [{ y.decode('utf-8'): banimal.get(y).decode('utf-8') for y in banimal.keys() } for banimal in banimals] 
   return animals

if __name__ == '__main__':
   app.run(debug=True, host='0.0.0.0')

