students = {
    "male": ["Tom", "Charlie", "Bob", "Frank"],
    "female": ["Sarah", "Mary", "Samantha", "Dot"],
    }

for key in students.keys():
    for name in students[key]:
        if "a" in name:
            print(name)
