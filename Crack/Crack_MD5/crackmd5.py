import hashlib
import sys

# Target hash
if len(sys.argv) < 3:
    print("at least two argument required. e.g: {script.name} {rockyou.txt} {md5_hash(2cb42f...)}") 
    sys.exit()
target_hash = sys.argv[2]

# Open the rockyou.txt file
with open(sys.argv[1], "r") as f:
    for line in f:
        # Generate the MD5 hash of the line
        line_hash = hashlib.md5(line.strip().encode()).hexdigest()
        # Compare the hash with the target hash
        if line_hash == target_hash:
            # Print the corresponding password and exit
            print("Hash Matched");
            print(f"Match found: {line.strip()}")
            exit()
        print("Checking Password: `{0}` \n Comparing Hash...\n".format(line.strip(),line_hash,target_hash))
    print("Hash Didn't matched at all.")
