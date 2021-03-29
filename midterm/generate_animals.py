#!/usr/bin/env python3

import random
import petname
import uuid
import json
# import redis
import time
from datetime import datetime

def main():
    # rd = redis.StrictRedis(host='127.0.0.1', port=6379, db=0)
    heads = ['snake', 'bull', 'lion', 'raven', 'bunny']
    animals = []
    for i in range(20):
        animal = {}
        animal['uid'] = str(uuid.uuid4())
        animal['head'] = heads[random.randint(0,4)]
        animal['body'] = petname.name() + '-' + petname.name()
        animal['arms'] = random.randint(2, 10)
        animal['legs'] = random.randint(3, 12)
        animal['tails'] = animal['arms'] + animal['legs']
        animal['created_on'] = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        animals.append(animal)
        time.sleep(1)
        # rd.hmset(uid, animal)
    with open('./data/data_file.json', 'w', encoding='utf-8') as f:
        json.dump({'animals': animals}, f, ensure_ascii=False, indent=4)

if __name__ == '__main__':
    main()
