from Higher_Or_Lower.art import logo
from Higher_Or_Lower.art import vs
from Higher_Or_Lower.game_data import data
from os import system
import random

def get_random():
    return random.choice(data)

def formated(dic):
    return f"{dic["name"]}, a {dic["description"]}, from {dic["country"]}."

def compare_A_and_B(person1, person2):
    if person1["follower_count"] > person2["follower_count"]:
        return 1
    elif person1["follower_count"] < person2["follower_count"]:
        return 2





while True:
    person1 = get_random()
    person2 = get_random()
    if person1 != person2:
        break


counter = 0
print(logo)
print(f"Compare A: {formated(person1)}")
print(logo)
print(f"Against B: {formated(person2)}")
guess = input("Who has more followers? Type 'A' or 'B': ")


if guess == 'a' or guess == 'A':
    if compare_A_and_B(person1, person2) == 1:
        while True:
            person1 = person2
            person2 = get_random()
            counter += 1
            system("cls||clear")
            print(logo)
            print(f"You're right! Score: {counter}.")
            print(f"Compare A: {formated(person1)}")
            print(f"Against B: {formated(person2)}")
            compare = input("Who has more followers? Type 'A' or 'B': ")
            if compare == 'a' or compare == 'A':
                if compare_A_and_B(person1, person2) == 1:
                    continue
                elif compare_A_and_B(person1, person2) == 2:
                    print(f"Wrong {counter}")
                    break
            elif compare == 'b' or compare == 'B':
                if compare_A_and_B(person1, person2) == 2:
                    continue
                elif compare_A_and_B(person1, person2) == 1:
                    print(f"Wrong {counter}")
                    break

    elif compare_A_and_B(person1, person2) == 2:
        print("Wrong")


elif guess == 'b' or guess == 'B':
    if compare_A_and_B(person1, person2) == 2:
        while True:
            person1 = person2
            person2 = get_random()
            counter += 1
            system("cls||clear")
            print(logo)
            print(f"You're right! Score: {counter}.")
            print(f"Compare A: {formated(person1)}")
            print(f"Against B: {formated(person2)}")
            compare = input("Who has more followers? Type 'A' or 'B': ")
            if compare == 'a' or compare == 'A':
                if compare_A_and_B(person1, person2) == 1:
                    continue
                elif compare_A_and_B(person1, person2) == 2:
                    print(f"Wrong {counter}")
                    break
            elif compare == 'b' or compare == 'B':
                if compare_A_and_B(person1, person2) == 2:
                    continue
                elif compare_A_and_B(person1, person2) == 1:
                    print(f"Wrong {counter}")
                    break
                    
    elif compare_A_and_B(person1, person2) == 1:
        print("Wrong")
        

