#!/usr/bin/env python

import random
import json
import argparse
import os

def main(index = None, file_path = './animals.json'):
    assert os.path.exists(file_path)
    with open(file_path, 'r', encoding='utf-8') as f:
        animals_json = json.load(f)
        animals = animals_json['animals']
        if index is not None:
            assert type(index) == int
            assert 0 <= index <= 19
            print(animals[index])
            return(animals[index])
        else:
            print(animals[random.randint(0,19)])

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--index', '-i', type=int,
                        help='Index of animal to return')

    parser.add_argument('file_path', nargs='?', help='Path to animals json file', default='./animals.json')

    args = parser.parse_args()

    main(args.index, args.file_path)