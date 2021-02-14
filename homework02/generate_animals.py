#!/usr/bin/env python3

import random
import petname
import json
import argparse

def main(file_path='./animals.json'):
    heads = ['snake', 'bull', 'lion', 'raven', 'bunny']
    animals = []
    for i in range(20):
        animal = {}
        animal['head'] = heads[random.randint(0,4)]
        animal['body'] = petname.name() + '-' + petname.name()
        animal['arms'] = random.randint(2, 10)
        animal['legs'] = random.randint(3, 12)
        animal['tails'] = animal['arms'] + animal['legs']
        animals.append(animal)
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump({'animals': animals}, f, ensure_ascii=False, indent=4)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    parser.add_argument('file_path', nargs='?', help='Path to animals json file', default='./animals.json')

    args = parser.parse_args()

    main(args.file_path)
