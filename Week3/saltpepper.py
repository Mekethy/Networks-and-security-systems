import hashlib
import os

def sha256_no_salt(password):
    return hashlib.sha256(password.encode()).hexdigest()

def sha256_with_salt(password, salt):
    return hashlib.sha256(password.encode() + salt).hexdigest()

PEPPER = "SECRET_PEPPER_123"

def sha256_salt_pepper(password, salt):
    return hashlib.sha256(password.encode() + salt + PEPPER.encode()).hexdigest()

if __name__ == "__main__":
    pwd = "user123password"

    print("Not salted")
    print(sha256_no_salt(pwd))
    print(sha256_no_salt(pwd))

    print("Salted")
    salt1 = os.urandom(16)
    salt2 = os.urandom(16)

    print(sha256_with_salt(pwd, salt1))
    print(sha256_with_salt(pwd, salt2))

    print("Salt + Pepper")
    print(sha256_salt_pepper(pwd, salt1))
