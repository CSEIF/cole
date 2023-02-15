print("Welcome to the Sopranos Season 1 Quiz")

playing = input ("Do you want to play or what? ")

if playing != "yes":
    quit()
print("Okay! Lets play!")
score = 0

answer = input("""What is Tony’s daughter's soccer coach’s name?
A: Don Hauser
B: Eric Taylor
C: Mickey Goldmill
D: Ken Carter """)

if answer == "A": 
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("""What is the name of Uncle Junior's long-term girlfriend?
A: Carla Espinosa
B: April Ludgate
C: Roberta Bobbi Sanfillipo
D: Jane Villanueva """)

if answer == "C":
     print("Correct!")
     score += 1
else:
    print("Incorrect!")

answer = input("""Who is NOT one of the five captains?
A: Ray Curto
B: Larry Barese
C: Jimmy Altieri
D: Dwight Manfredi """)

if answer == "D":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")
          
answer = input("""What is the name of the rapper in Season 1?
A: Prodigy
B: Massive Genius
C: Camron
D: B-Rad """)

if answer == "B":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("""What is the name of the detective Tony hires to spy on Dr. Melfi?
A: Vin Makazian
B: Clancy Wiggum
C: James McNulty
D: Rustin Cohle """)

if answer == "A":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

print("You got " + str(score) + " questions correct")
