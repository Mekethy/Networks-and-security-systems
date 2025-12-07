import hashlib
import bcrypt

def hash_md5(password):
    return hashlib.md5(password.encode()).hexdigest()

def hash_sha256(password):
    return hashlib.sha256(password.encode()).hexdigest()

def hash_bcrypt(password):
    hashed = bcrypt.hashpw(password.encode(), bcrypt.gensalt(12))
    return hashed

def verify_bcrypt(password, hashed):
    return bcrypt.checkpw(password.encode(), hashed)


