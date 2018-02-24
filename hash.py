#!c:/Python36/python.exe
import os
import sys
import hashlib
import datetime
import bcrypt

filename = "CRC.txt"

def get_folder_files():
    return os.listdir()

def sha256_checksum(filename, block_size=65536):
    sha256 = hashlib.sha256()
    with open(filename, 'rb') as f:
        for block in iter(lambda: f.read(block_size), b''):
            sha256.update(block)
    return sha256.hexdigest()

def bcrypt_string(string):
    return bcrypt.hashpw(string.encode("utf-8"), bcrypt.gensalt())

def main():
    f = open(filename, "w", encoding="utf-8")
    now = datetime.datetime.now()
    print("SHA-256 hash, at {}, files : ".format(now.strftime("%Y-%m-%d %H:%M")))
    f.write("SHA-256 hash, at {}, files : ".format(now.strftime("%Y-%m-%d %H:%M")))
    files = get_folder_files()
    print(files)
    print()
    f.write(' '.join(files))
    f.write("\n")
    for i in range(len(files)):
        if os.path.isdir(files[i]) or files[i] == filename:
            # print("{} is folder .. ".format(files[i]))
            continue
        try:
            checksum = sha256_checksum(files[i])
            print("{} => {}".format(checksum, files[i]))
            f.write("{} => {} \n".format(checksum, files[i]))
        except:
            print("{} error".format(files[i]))
            f.write("{} error \n".format(files[i]))
    f.write("\n")
    print("Type password :", end=" " )
    password_hash = bcrypt_string(input())
    f.write(str(password_hash))
    print("\n{}".format(password_hash))

if __name__ == '__main__':
    main()