
#  ROT32 Decryptor
A simple Python program to decrypt strings encoded using ROT32.

##  Installation
1. Clone the ROT32 repository to your local machine:
```
git clone https://github.com/h4jack/rot32.git
```
2. Change the path to the `rot32` repository folder:
```
cd rot32
```
3. Copy the binary to an environment path (optional):
```
cp rot32.py /usr/local/bin/
```

##  Usage
Run the program with command-line arguments:
```
python rot32.py "your_encrypted_string" 10
```
Replace `"your_encrypted_string"` with the actual string you want to decrypt and `10` with the desired shift value.

##  Features
- Decodes ROT32-encoded strings.
- Supports both uppercase and lowercase characters.
- Provides a command-line interface for easy usage.

##  Examples
Decrypt a string with a shift of 10:
```
python rot32.py "uryyb jbeyq" 10
# Output: "hello world"
```

##  Options
- To search for a specific word or string, use the `-s` flag:
```
python rot32.py -s "hello" "uryyb jbeyq"
# Output: "Found: hello"
```
- To exclude specific characters, use the `-x` flag:
```
python rot32.py -x "aeiou" "uryyb jbeyq"
# Output: "hll wrld"
```
- For additional options, use the `-h` flag:
```
python rot32.py -h
```

##  Authors

* [h4jack](https://github.com/h4jack)

## License
This repository is licensed under [MIT LICENSE](https://github.com/h4jack/tools/tree/main/LICENSE).