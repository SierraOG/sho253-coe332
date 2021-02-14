import unittest
import json
import os
from read_animals import main

class TestReadAnim(unittest.TestCase):
    def test_main(self):
        create_test_animals()
        self.assertEqual({"head": "bull", "body": "bear-cow", "arms": 3,"legs": 9,"tails": 12}, main(0, './test_animals.json'))
        self.assertEqual({"head": "bull","body": "salmon-crow","arms": 4,"legs": 12,"tails": 16}, main(7, './test_animals.json'))
        self.assertEqual({"head": "bunny","body": "jackal-gnat","arms": 7,"legs": 8,"tails": 15}, main(19, './test_animals.json'))
        clean_up_test_animals()
        
        self.assertRaises(AssertionError, main, file_path='./does/not/exist/animals.json')
        self.assertRaises(AssertionError, main, index=20)
        self.assertRaises(AssertionError, main, index="banana")

def create_test_animals():
    test_animals = {
        "animals": [
            {
                "head": "bull",
                "body": "bear-cow",
                "arms": 3,
                "legs": 9,
                "tails": 12
            },
            {
                "head": "bunny",
                "body": "swine-kid",
                "arms": 10,
                "legs": 12,
                "tails": 22
            },
            {
                "head": "bull",
                "body": "flea-husky",
                "arms": 6,
                "legs": 5,
                "tails": 11
            },
            {
                "head": "bunny",
                "body": "badger-yeti",
                "arms": 3,
                "legs": 6,
                "tails": 9
            },
            {
                "head": "lion",
                "body": "weevil-colt",
                "arms": 9,
                "legs": 8,
                "tails": 17
            },
            {
                "head": "snake",
                "body": "oriole-ghost",
                "arms": 9,
                "legs": 7,
                "tails": 16
            },
            {
                "head": "snake",
                "body": "swift-collie",
                "arms": 6,
                "legs": 5,
                "tails": 11
            },
            {
                "head": "bull",
                "body": "salmon-crow",
                "arms": 4,
                "legs": 12,
                "tails": 16
            },
            {
                "head": "snake",
                "body": "jackal-stag",
                "arms": 4,
                "legs": 10,
                "tails": 14
            },
            {
                "head": "bull",
                "body": "bull-gecko",
                "arms": 10,
                "legs": 11,
                "tails": 21
            },
            {
                "head": "raven",
                "body": "kid-crow",
                "arms": 7,
                "legs": 5,
                "tails": 12
            },
            {
                "head": "lion",
                "body": "bird-viper",
                "arms": 6,
                "legs": 12,
                "tails": 18
            },
            {
                "head": "bunny",
                "body": "cub-quagga",
                "arms": 10,
                "legs": 8,
                "tails": 18
            },
            {
                "head": "bunny",
                "body": "ocelot-tuna",
                "arms": 7,
                "legs": 9,
                "tails": 16
            },
            {
                "head": "lion",
                "body": "eagle-orca",
                "arms": 4,
                "legs": 5,
                "tails": 9
            },
            {
                "head": "snake",
                "body": "aphid-jaguar",
                "arms": 6,
                "legs": 4,
                "tails": 10
            },
            {
                "head": "bull",
                "body": "sloth-python",
                "arms": 4,
                "legs": 11,
                "tails": 15
            },
            {
                "head": "bunny",
                "body": "cow-beetle",
                "arms": 7,
                "legs": 3,
                "tails": 10
            },
            {
                "head": "bull",
                "body": "buck-gator",
                "arms": 7,
                "legs": 11,
                "tails": 18
            },
            {
                "head": "bunny",
                "body": "jackal-gnat",
                "arms": 7,
                "legs": 8,
                "tails": 15
            }
        ]
    }
    if os.path.exists("test_animals.json"):
        clean_up_test_animals()
    with open("test_animals.json", "x") as f:
        json.dump(test_animals, f, ensure_ascii=False, indent=4)

def clean_up_test_animals():
    os.remove("test_animals.json")

if __name__ == '__main__':
    unittest.main()