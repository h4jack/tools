import sys

def takeInt(prompt):
    try:
        return int(input("Enter the number: "))
    except:
        print("Wrong Enter a valid Number/0 to exit.")
        return takeInt(prompt)

def main(string="", shift=None):
    if not string:
        string = input("Enter the string: ")
    if not shift:
        shift = takeInt("Enter the shift No: ")
    else:
        try:
            shift = int(shift)
        except:
            print("Invalid No shifted to 32.")
            shift = 32
    print(shiftString(string, shift))

def shiftString(string, shift):
    result = ""
    for char in string:
        result += shiftChar(char, shift)
    return result

def shiftChar(char, shift):
    if char.isupper():
        return upperShift(char, shift)
    if char.islower():
        return lowerShift(char, shift)
    return char

def upperShift(char, shift):
    c = ord(char)
    c = (c - shift - 65) % 26 + 65
    return chr(c)

def lowerShift(char, shift):
    c = ord(char)
    c = (c - shift - 97) % 26 + 97
    return chr(c)

if __name__ == '__main__':
    l = len(sys.argv)
    if l > 3:
        print("Usage: python rot32_decrypt.py <string> <shift>")
    elif l == 3:
        main(sys.argv[1], sys.argv[2])
    elif l == 2:
        main(sys.argv[1])
    elif l == 1:
        main()