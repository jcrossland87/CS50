# scr1.py house2.py Week 1 Conditionals match case example 1

# Uses match with case instead of if/elif/else with or bool to compare multiple strings

print("# scr1.py house2.py Week 1 Conditionals match case example 1 instead of if elif else")

name = input("What's your name? ")

match name:
    case "Harry":
        print("Gryffindor")
    case "Hermione":
        print("Gryffindor")
    case "Ron":
        print("Gryffindor")
    case "Draco":
        print("Syltherin")
    case _:
        print("Who?")

# scr1.py house2.py Week 1 Conditionals match case example 1

# Uses match with case instead of if/elif/else with or bool to compare multiple strings

print("# scr1.py house3.py Week 1 Conditionals match case example 2 using | pipes for or boolean operators")

name = input("What's your name? ")

match name:
    case "Harry" | "Hermione" | "Ron":
        print("Gryffindor")
    case "Draco":
        print("Syltherin")
    case _:
        print("Who?")
