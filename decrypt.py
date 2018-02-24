#!c:/Python36/python.exe
import bcrypt

def bcrypt_string(string):
    return bcrypt.hashpw(string.encode("utf-8"), bcrypt.gensalt())

def main():
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

if __name__ == '__main__':
    main()