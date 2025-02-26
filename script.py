import random
import string

def genera_password(lunghezza=12):
    caratteri = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(caratteri) for i in range(lunghezza))
    return password

if __name__ == "__main__":
    print("Generatore di Password Sicure ")
    lunghezza = int(input("Inserisci la lunghezza della password: "))
    print(f" La tua password generata è: {genera_password(lunghezza)}")