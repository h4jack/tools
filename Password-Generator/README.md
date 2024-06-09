
# Random Password Generator
This Python script generates random passwords based on user-defined criteria.

## Introduction
This script utilizes Python's argparse module to allow users to generate random passwords with specified characteristics. The generated passwords can include special characters, uppercase letters, lowercase letters, and/or numeric characters.
## Usage
    usage: main.py [-h] [-s] [-u] [-l] [-n] [-v] length
### Arguments
    length: Length of the password (required)
    -s, --special: Include special characters
    -u, --uppercase: Include uppercase letters
    -l, --lowercase: Include lowercase letters
    -n, --numeric: Include numeric characters
    -v, --verbose: Show verbose output


## Example
#### First Example:
```bash
python main.py 12 -suln
```
This command generates a password of length 12 with special characters, uppercase letters, lowercase letters, and numeric characters.
- OUTPUT: 
```bash
Generated password: 0|vHC3F5lGp7
```
#### Second Example
```bash
python password_generator.py 8 -s -v
```
This command generates a password of length 8 with special characters and displays verbose output during generation.
- OUTPUT:
```bash
Generating password...
=!=%<(}+

Shuffling...
Generated password: ==+}!(%<
```
## Tech Stack

**Language:** Python 3.x+\
```
    argparse
    sys
    time
    randint and shuffle from random  
```
## Authors

- [@h4jack](https://www.github.com/h4jack)