import hashlib
import itertools
import datetime
import sys

# The given SHA1 hash to crack
hash1 = "67ae1a64661ac8b4494666f58c4822408dd0a3e4"

# Character sets based on provided patterns
str2 = [['Q', 'q'], ['W', 'w'], ['%', '5'], ['8', '('], ['=', '0'], ['I', 'i'], ['*', '+'], ['n', 'N']]

# Function to compute SHA1 hash
def sha_encrypt(string):
    sha = hashlib.sha1(string.encode())  # Convert string to bytes before hashing
    return sha.hexdigest()

starttime = datetime.datetime.now()
str3 = ["0"] * 8

# Iterate through each combination of character sets
for a in range(2):
    str3[0] = str2[0][a]
    for b in range(2):
        str3[1] = str2[1][b]
        for c in range(2):
            str3[2] = str2[2][c]
            for d in range(2):
                str3[3] = str2[3][d]
                for e in range(2):
                    str3[4] = str2[4][e]
                    for f in range(2):
                        str3[5] = str2[5][f]
                        for g in range(2):
                            str3[6] = str2[6][g]
                            for h in range(2):
                                str3[7] = str2[7][h]
                                newS = "".join(str3)
                                # Generate all permutations of the new string
                                for perm in itertools.permutations(newS, 8):
                                    candidate = "".join(perm)
                                    str4 = sha_encrypt(candidate)
                                    if str4 == hash1:
                                        print("Cracked password:", candidate)
                                        endtime = datetime.datetime.now()
                                        print("Time taken:", (endtime - starttime).seconds, "seconds")
                                        sys.exit(0)

print("Password not found.")


