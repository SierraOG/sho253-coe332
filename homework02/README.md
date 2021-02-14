# Generate and Read Random Animals


## Usage Instructions
Use generate_animals.py to general a json file with 20 randomly generated animals. Example usage:

```generate_animals.py rand_animals.json ```

If a file path is not provided, it will default to using animals.json in the current working directory.

Use read_animals.py to read an animal from the generated json file. You can provide an index to read from using the --index or -i flag or if not provide it will randomly select an animal. 

Example usage:

```read_animals.py -i 7 rand_animals.json```

If a file path is not provided, it will again default to using animals.json in the current working directory.

## Testing
A test suite is provide for the read_animals.py function which can be ran using:

```python test_read_animals.py```

## Building Docker Image
To build the image using the provided Dockerfile, use:

```docker build -t sierrao/hw2:1.0 . ```

## Running Inside Container
Start a shell inside the container, using:

```docker run --rm -it sierrao/hw2:1.0 /bin/bash ```

Run scripts as described in Usage Instructions.

Example:
```generate_animals.py```
```read_animals.py```