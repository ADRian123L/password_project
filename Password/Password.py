# Adrian Lozada and Jiahui Dang

import os
import time 
from math import fabs as abs

# Run variable:
run = True

# Create and open a text file for input:
try:
    with open("Password.txt", "w"):
        pass
except:
    print("Couldn't create file")

# Start timer:
start = time.time()
amount = 12
correct = False

# Opens the text file:
os.popen("open Password.txt")

# Read the files:
while run:

    # Countdown:
    begun = time.time()
    run = False if (abs(begun - start) >= amount) else True

    # Reads the file:
    password = open("Password.txt", "r")
    content = password.read()
    if (content == "A"):
        run = False
        correct = True
    password.close()

if (correct == True):
    print("Password was correct")
else:
    print("Time is over.")
# Removes the file:
os.remove("Password.txt")
