import string
import math

def calculate_entropy(password):
    pool_size = 0
    
    #Checking which character sets are used in the password
    if any(c.islower() for c in password):
        pool_size += 26
    if any(c.isupper() for c in password):
        pool_size += 26
    if any(c.isdigit() for c in password):
        pool_size += 10
    if any(c in string.punctuation for c in password):
        pool_size += len(string.punctuation)

    if pool_size == 0:
        return 0
    
    return len(password) * math.log2(pool_size)

COMMON_BAD_PASSWORDS = ["password", "123456", "qwerty", "letmein", "pass123"]

def analyse_password(password):
    score = 0
    feedback = []

    #Length checks
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Shorter than 8 characters.")

    if len(password) >= 12:
        score += 1

    #Character checks
    if any(c.islower() for c in password):
        score += 1
    if any(c.isupper() for c in password):
        score += 1
    if any(c.isdigit() for c in password):
        score += 1
    if any(c in string.punctuation for c in password):
        score += 1

    #Bad password check
    if password.lower() in COMMON_BAD_PASSWORDS:
        score -= 2
        feedback.append("Very common password!")

    entropy = calculate_entropy(password)

    return score, entropy, feedback

if __name__ == "__main__":
    tests = ["Pass123", "MyP@ssw0rd"]
    for pwd in tests:
        score, ent, fb = analyse_password(pwd)
        print(f"\nPassword: {pwd}")
        print("Score:", score)
        print("Entropy:", ent)
        print("Feedback:", fb)

#Pass123 shorter than 8 and very common MyP@ssw0rd good length and variety 
