print(r"""


  ______                           __                   ______             __           
 /      \                         |  \                 /      \           |  \          
|  $$$$$$\  ______   ______ ____   \$$  _______       |  $$$$$$\ __    __  \$$ ________ 
| $$   \$$ /      \ |      \    \ |  \ /       \      | $$  | $$|  \  |  \|  \|        \
| $$      |  $$$$$$\| $$$$$$\$$$$\| $$|  $$$$$$$      | $$  | $$| $$  | $$| $$ \$$$$$$$$
| $$   __ | $$  | $$| $$ | $$ | $$| $$| $$            | $$ _| $$| $$  | $$| $$  /    $$ 
| $$__/  \| $$__/ $$| $$ | $$ | $$| $$| $$_____       | $$/ \ $$| $$__/ $$| $$ /  $$$$_ 
 \$$    $$ \$$    $$| $$ | $$ | $$| $$ \$$     \       \$$ $$ $$ \$$    $$| $$|  $$    \
  \$$$$$$   \$$$$$$  \$$  \$$  \$$ \$$  \$$$$$$$        \$$$$$$\  \$$$$$$  \$$ \$$$$$$$$
                                                            \$$$                                                                                                                                                                                                                                                          
""")

# Intro
print("Welcome to the Comic Character Quiz! How well do you know Earth's greatest heroes? Let's find out... Here are some basic questions to test your knowledge.")
print()
print()


questions =  ("Q1. Superman's vast power set includes density shifting, allowing him to phase his body through solid objects.", "Q2. THe name of the man who turns into the INCREDIBLE HULK is Bruce Banner.", "Q3.The members of the original X-men team are Cyclops, Marvel Girl, Iceman, Beast, and Hawkman.", "Q4. The mentor of Wally West, The Flash, is Barry Allen, also The Flash.")
answers = ("F", "T", "F", "T")
numberQuestions = len(questions)
numberCorrect = 0


# Loop for each question- Get user answers
for index in range(numberQuestions):
  print(questions[index])
  print()
  guess = input("   Please ONLY enter T for True or F for False: ")
  print()
  while guess != "T" and guess != "F":
    guess = input("   Please ONLY enter T for True or F for False: ")
    print()
  if guess == answers[index]:
    numberCorrect += 1

print(f"*** Looks like you got {numberCorrect} out of {numberQuestions} correct! ***")

