#!/usr/bin/env python3

import random
import petname
import uuid
import redis
from datetime import datetime

def main(rd):
    heads = ['snake', 'bull', 'lion', 'raven', 'bunny']
    animals = []
    for i in range(20):
        animal = {}
        uid = str(uuid.uuid4())
        animal['head'] = heads[random.randint(0,4)]
        animal['body'] = petname.name() + '-' + petname.name()
        animal['arms'] = random.randint(2, 10)
        animal['legs'] = random.randint(3, 12)
        animal['tails'] = animal['arms'] + animal['legs']
        animal['created_on'] = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        rd.hmset(uid, animal)

if __name__ == '__main__':
    main()
