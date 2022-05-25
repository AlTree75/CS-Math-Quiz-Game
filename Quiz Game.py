print("CS  &  Math  Quiz")
print("Welcome to the Quiz! ")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()

print("Great! let's play: ")
score = 0

Q1 = input("What does CPU stand for? ")
if Q1.lower() == "central processing unit":
    print('Correct! ')
    score += 1
else:
    print("Incorrect!")

Q2 = input("What does GPU stand for? ")
if Q2.lower() == "graphics processing unit":
    print('Correct! ')
    score += 1
else:
    print("Incorrect!")

Q3 = input("What does RAM stand for? ")
if Q3.lower() == "random-access memory":
    print('Correct! ')
    score += 1
else:
    print("Incorrect!")

Q4 = input("What does PSU stand for? ")
if Q4 == "Power Supply Unit":
    print('Correct! ')
    score += 1
else:
    print("Incorrect!")

Q5 = input("What is binary? ")
if Q5 == "A sequence of 1s and 0s":
    print('Correct! ')
    score += 1
else:
    print("Incorrect!")

Q6 = input("What would the denary number 199 be in binary? ")
if Q6 == "11000111":
    print('Correct! ')
    score += 1
else:
    print("Incorrect!")

Q7 = input("What would the denary number 55 be in binary? ")
if Q7 == "00110111":
    print('Correct! ')
    score += 1
else:
    print("Incorrect!")

Q8 = input("What would the denary number 222 be in binary? ")
if Q8 == "11011110":
    print('Correct! ')
    score += 1
else:
    print("Incorrect!")

Q9 = input("What would 00101110 be as a denary number? ")
if Q9 == "46":
    print('Correct! ')
    score += 1
else:
    print("Incorrect!")

Q10 = input("What would 00100101 + 01000100 be as a binary number? ")
if Q10 == "01101001":
    print('Correct! ')
    score += 1
else:
    print("Incorrect!")

Q11 = input("What is 6.4 ÷ 0.2? ")
"0.32" "3.2" "32"
if Q11 == "32":
    print('Correct! ')
    score += 1
else:
    print("Incorrect!")

Q12 = input("What is 1 ÷ 0.1? ")
"10" "1" "100"
if Q12 == "10":
    print('Correct! ')
    score += 1
else:
    print("Incorrect!")

Q13 = input("What is 0.375 as a fraction in its simplest form? ")
"15/40" "3/8" "3/75"
if Q13 == "3/8":
    print('Correct! ')
    score += 1
else:
    print("Incorrect!")

Q14 = input("What is 117% as a decimal? ")
"1.17" "0.17" "11.7"
if Q14 == "1.17":
    print('Correct! ')
    score += 1
else:
    print("Incorrect!")

Q15 = input("Simplify 6**-2 ")
"-12" "1/36" "36"
if Q15 == "1/36":
    print('Correct! ')
    score += 1
else:
    print("Incorrect!")




print("You got " + str(score) + "/" + "15" + " questions correct")


