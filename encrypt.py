from cryptography.fernet import Fernet
import rsa


def symmKey():
    message = str(input("message to encrypt: "))

    key = Fernet.generate_key()

    fernet = Fernet(key)

    encMessage = fernet.encrypt(message.encode())

    print("original string: ", message)
    print("encrypted string: ", encMessage)

    decMessage = fernet.decrypt(encMessage).decode()

    print("decrypted string: ", decMessage)


def asymmKey():
    # Two keys, since its asymmetric encryption
    publicKey, privateKey = rsa.newkeys(512)

    message = str(input("message to encrypt: "))

    encMessage = rsa.encrypt(message.encode(), publicKey)

    print("original string: ", message)
    print("encrypted string: ", encMessage)

    decMessage = rsa.decrypt(encMessage, privateKey).decode()
    print("decrypted string: ", decMessage)


def tester():
    choose = input("symm or asymm ")
    try:
        if choose == "symm":
            symmKey()
        else:
            asymmKey()
    except:
        "no"

if __name__ == "__main__":
    tester()