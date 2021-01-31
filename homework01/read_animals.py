import random
import json

def main():
    with open('animals.json', 'r', encoding='utf-8') as f:
        animals_json = json.load(f)
        animals = animals_json['animals']
        print(animals[random.randint(0,19)])

if __name__ == '__main__':
    main()