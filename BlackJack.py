import random

def calculate_total(list_of_cards):
    user_list = list_of_cards[::]
    if ace not in user_list:
        return sum(user_list)
    
    ace_count = -1
    for i in user_list:
        ace_count += 1
        if i == ace:
            break
    
    if sum(user_list) > 21:
        user_list[ace_count] = 1
        return sum(user_list) 
    return sum(user_list)

ace = 11
cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, ace]

def play_blackjack():
    user = [random.choice(cards), random.choice(cards)]
    computer = [random.choice(cards), random.choice(cards)]
    user_total = calculate_total(user)
    computer_total = calculate_total(computer)

    print(f"user: {user}")
    print(f"user total: {user_total}")
    print(f"computer: {computer}")
    print(f"computer total: {computer_total}")

    if user_total == 21:
        if computer_total != 21:
            print("You Win!")
            return 
        elif computer_total == 21:
           print("Tie")
           return
    elif computer_total == 21:
        print("Computer Wins!")
        return

    else:
        while True:
            hit_or_stand = input("hit or stand \n")
            if hit_or_stand == "hit":
                user.append(random.choice(cards))

                user_total = calculate_total(user)


                print(f"user: {user}")
                print(f"user total: {user_total}")
                if user_total > 21:
                    print("Over 21")
                    print("Computer Wins!")
                    return 
                elif user_total == 21:
                    print("User Wins!")
                    return
            elif hit_or_stand == "stand":
                break
    
    computer_total = calculate_total(computer)
    while computer_total <= 17:
        computer.append(random.choice(cards))
        computer_total = calculate_total(computer)   
        if computer_total > 21:
            print("Computer Over 21")
            return
            

    print(f"User: {user}")
    print(f"Computer: {computer}")
    if user_total > computer_total:
        print("User Wins")
        return 
    elif user_total < computer_total:
        print("Computer Wins")
        return 
    else: 
        print("Tie")
        return 

