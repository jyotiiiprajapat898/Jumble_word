import random
Word=["Mango","Apple", "Elephant","Computer","School","Tiger","Python","Laptop","Cricket","Rainbow"]
hint=["Fruit","Fruit","Animal","Electronic Device","Place to Study","Wild Animal","Programming Language","Electronic Device","Sport","Natural Phenomenon"]
count=0
for i in range(len(Word)):
    letters=list(Word[i])
    random.shuffle(letters)
    scrambled=" ".join(letters)
    print(scrambled)
    print(hint[i])
    for j in range(3):
        guess_word=input("Enter your word-->").title()
        if Word[i]==guess_word:
            print("Good!")
            count+=1
            break
        else:
            print("Wrong guess!")
if (count>=10):
    print("Good")
elif (count>=15):
    print("Amazing")
else:
    print("Good try!")
    
print("Would you like to play NEXT level?")
choice = input("YES or NO: ").upper()

if choice == "YES":
    print("Wait for LEVEL 2")
else:
    print("Thank you!")


