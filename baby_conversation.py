from random import choice

questions = ["Why is the sky blue? ", "Why do I sleep? ",
             "Why are clouds fluffy? "]

question = choice(questions)
answer = input(question).strip().lower()

while answer != ("just because"):
        answer = input("why?: ").strip().lower()

print("Oh...Okay.")
