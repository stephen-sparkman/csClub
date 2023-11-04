import re


def run_quiz():
    class Question:
        def __init__(self, prompt, answer):
            self.prompt = prompt
            self.answer = answer

    question_prompts = [
        "\nWhat is the correct way to create a variable 'a' that stores the number 5??\n(a)a == 5\n(b)int a = 5\n(c)a = 5\n(d)5 -> a\n\n",
        "\nHow do you start a comment in Python?\n(a)// this is a comment\n(b)<!-- this is a comment -->\n(c)# this is a comment\n(d)* This is a comment *\n\n",
        "\nWhich of the following is the output of this code snippet?\n\nprint(2 * 3 + 3)\n\n(a)12\n(b)9\n(c)8\n(d)5\n\n",
        "\nHow do you create a list in Python?\n(a)list = (1, 2, 3)\n(b)list = [1, 2, 3]\n(c)list = {1, 2, 3}\n(d)list = <>\n\n",
        "\nWhat will be the output of the following code?\n\nif not True:\n     print('1')\nelse:\n     print('2')\n\n(a)1\n(b)2\n(c)True\n(d)False\n\n",
        "\nWhat is the correct way to define a function in Python?\n(a)function myFunc():\n(b)def myFunc():\n(c)create myFunc():\n(d)func myFunc():\n\n",
        "\nWhich data type would you use to store a sequence of characters?\n(a)Integer\n(b)String\n(c)List\n(d)Character\n\n",
        "\nWhat will this code print?\n\na = 'Hello World!'\nprint(a[1])\n\n(a)Hello, World!\n(b)e\n(c)H\n(d)ello, World!\n\n",
        "\nWhich of the following lines of code will cause an error?\n(a)print('Hello World')\n(b)x = 10\n(c)y = 2.5\n(d)1st_number = 3\n\n",
        "\nWhat is the result of this code snippet?\n\nprint(4 == 4.0)\n\n(a)True\n(b)False\n(c)Error\n(d)None\n\n"
    ]
          
    questions = [
        Question(question_prompts[0], "c"),
    Question(question_prompts[1], "c"),
    Question(question_prompts[2], "b"),
    Question(question_prompts[3], "b"),
    Question(question_prompts[4], "b"),
    Question(question_prompts[5], "b"),
    Question(question_prompts[6], "b"),
    Question(question_prompts[7], "a"),
    Question(question_prompts[8], "d"),
    Question(question_prompts[9], "a"),
    ]

    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print('\nYou answered', score, 'out of', len(questions), 'correct!\n')
    if score >= 8:
        discord_link = "placeholder"
        print("Congratulations on solving the challenge! Join our Discord here: {discord_link}\nWe meet every Thursday in person at 25 Park Pl, Room 755, from 3-4pm\nWe meet every Friday online, via discord, from 3-4pm.\n")
    else:
        print("You can do better, try again!\n p.s feel free to look at the source code!")
        while True:
            repeat = input("\nTry again?\n Y - Yes!\n N - Exit\n").lower()
            if repeat == "y":
                run_quiz()
                break
            elif repeat == "n":
                print("\nExiting the quiz...")
                break
            else:
                print("Invalid Input, please enter, 'Y' for Yes or 'N' for No.\n")

print("""
      
    Welcome to the Computer Science Club Coding Challege!
    Answer 8/10 of the questions correctly and the time
    and place of our next meeting will be revelaed!
      
    """)
run_quiz()