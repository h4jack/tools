
# Hash Cracker
This Python script is designed to crack MD5 hashes by comparing them with hashes generated from a wordlist.

## Introduction
This script takes a hash as input and compares it with hashes generated from a provided wordlist (e.g., rockyou.txt). If a match is found, it prints the corresponding password.

## Usage
To crack a MD5 hash, run the script with the path to the wordlist file and the target hash as parameters from the command line.

    python crackmd5.py [wordlist_file] [target_hash]

### Arguments
    wordlist_file: Path to the wordlist file (required).
    target_hash: Hash to be cracked (required).

## Example
#### Crack a hash using a wordlist:
```bash
python crackmd5.py rockyou.txt 2cb42f...
```

## Tech Stack
**Language:** Python 3.x+\
```modules
hashlib
sys
```

## Authors
- [@h4jack](https://www.github.com/h4jack)