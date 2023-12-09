import random
import string
import time

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def generating_animation():
    animation = ["Generating Your Password", "Generating Your Password.", "Generating Your Password..", "Generating Your Password...", "Generating Your Password....", "Generating Your Password.....", "Generating Your Password.....", "Generating Your Password.... ", "Generating Your Password...  ", "Generating Your Password..   ", "Generating Your Password.    ", "Generating Your Password     ", "Generating Your Password", "Generating Your Password.", "Generating Your Password..", "Generating Your Password...", "Generating Your Password....", "Generating Your Password.....", "Generating Your Password.....", "Generating Your Password.... ", "Generating Your Password...  ", "Generating Your Password..   ", "Generating Your Password.    ", "Generating Your Password     ", "Generating Your Password", "Generating Your Password.", "Generating Your Password..", "Generating Your Password...", "Generating Your Password....", "Generating Your Password.....", "Generating Your Password.....", "Generating Your Password.... ", "Generating Your Password...  ", "Generating Your Password..   ", "Generating Your Password.    ", "Generating Your Password     "]
    for frame in animation:
        print(frame, end="\r")
        time.sleep(0.11)

print("\n***Unique Password Generator***")

try:
    length = int(input("\nEnter the desired length of the password: "))
    if length <= 0:
        print("Please enter a valid positive length.")

    password = generate_password(length)
    generating_animation()
    print("                                     ")
    print(f"Generated Password: {password}")

except ValueError:
    print("Invalid input. Please enter a valid positive integer for the password length.")