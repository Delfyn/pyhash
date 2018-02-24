#!c:/Python36/python.exe
import bcrypt
import hash as tmp
import os


def bcrypt_string(string):
    return bcrypt.hashpw(string.encode("utf-8"), bcrypt.gensalt())

def password_check():
    print("Type password :", end=" ")
    password = input()
    print("Type password HASH:", end=" ")
    hash = input()
    print("")
    try:
        if bcrypt.checkpw(password.encode("utf-8"), hash.encode("utf-8")):
            print("{} YES !!".format(password))
        else:
            print("NOPE")
    except ValueError:
        print("Invalid hash")
    except:
        print("Error")

def get_folder_hashes():
    files = tmp.get_folder_files()
    hash_dic = {}
    for i in range(len(files)):
        if os.path.isdir(files[i]) or files[i] == tmp.filename:
            # print("{} is folder .. ".format(files[i]))
            continue
        try:
            hash_dic[files[i]] = tmp.sha256_checksum(files[i])
        except:
            print("{} error".format(files[i]))
    return hash_dic

def get_file_hashes(filename=tmp.filename):
    file_hash_dic = {}
    with open(filename, "r") as f:
        words = f.readlines()
        for l in words:
            first_word = l.split()
            if len(first_word[0]) == 64:
                file_hash_dic[first_word[2]] = first_word[0]
    return file_hash_dic

def main():
    print("Not changed files : HASH | NAME_IN_CRC_FILE | NAME_IN_FOLDER")
    print()
    for x in get_folder_hashes().values():
        for y in get_file_hashes().values():
            if x == y:
                if list(get_file_hashes().keys())[list(get_file_hashes().values()).index(x)] == list(get_folder_hashes().keys())[list(get_folder_hashes().values()).index(x)]:
                    print("{} == {}".format(x, list(get_file_hashes().keys())[list(get_file_hashes().values()).index(x)]))
                else:
                    print("{} == {} -> {}".format(x, list(get_file_hashes().keys())[list(get_file_hashes().values()).index(x)], list(get_folder_hashes().keys())[list(get_folder_hashes().values()).index(x)]))

    print()
    password_check()

if __name__ == '__main__':
    main()