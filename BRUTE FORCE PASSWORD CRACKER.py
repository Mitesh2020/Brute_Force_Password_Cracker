import string
import random
import time

print()
password = input("Enter the password : ")
print()
start_time = time.time()  # Use time.time() for precise time measurement

char = list(string.printable)

while True:
    password_guess = ''.join(random.choices(char, k=len(password)))
    print("Cracking Password >> ", password_guess)

    if password == password_guess:
        print()
        print("Victim Password is : ", password_guess)
        print()
        break

end_time = time.time()
time_taken = end_time - start_time
print("Time taken to crack password :", time_taken, "seconds")
print()
