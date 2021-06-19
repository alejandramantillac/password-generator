import random

def generate_password():
    capital = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    lowercase = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    symbols = ["!", "#", "$", "/", "(", ")"]
    numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    
    characters = capital + lowercase + symbols + numbers

    password = []

    for i in range (15):
        random_character = random.choice(characters)
        password.append(random_character)

    password = ''.join(password)
    return password

def run():
    password = generate_password()
    print("Tu nueva contraseña es: ", password)

if __name__ == '__main__':
    run()