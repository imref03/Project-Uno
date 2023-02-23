def main():
    import random

    card_val = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]
    card_sign = [" of Hearts ", " of Clubs ", " of Spades ", " of Diamonds "]
    points = 0
    uchoice1 = ("")
    playagain = ("")

    random_card_val1 = random.choice(card_val)
    random_card_sign1 = random.choice(card_sign)
    random_card_val2 = random.choice(card_val)
    random_card_sign2 = random.choice(card_sign)

    first_card = (random_card_val1 + random_card_sign1)
    second_card = (random_card_val2 + random_card_sign2)

    random_card_val3 = random.choice(card_val)
    random_card_sign3 = random.choice(card_sign)
    random_card_val4 = random.choice(card_val)
    random_card_sign4 = random.choice(card_sign)
    random_card_val5 = random.choice(card_val)
    random_card_sign5 = random.choice(card_sign)
    random_card_val6 = random.choice(card_val)
    random_card_sign6 = random.choice(card_sign)

    given_card1 = (random_card_val3 + random_card_sign3)
    given_card2 = (random_card_val4 + random_card_sign4)
    given_card3 = (random_card_val5 + random_card_sign5)
    given_card4 = (random_card_val6 + random_card_sign6)

    if first_card == second_card:
        main()
    elif given_card1 == given_card2:
        main()
    elif given_card1 == given_card3:
        main()
    elif given_card1 == given_card4:
        main()
    elif given_card2 == given_card3:
        main()
    elif given_card2 == given_card4:
        main()
    elif given_card3 == given_card4:
        main()
    else:
        print("Introduction:")
        print("You will be dealt 2 cards, later 4 more cards will appear if one of your cards matches with one of the 4 you get one point,")
        print("if both of your cards have matches you get 2 points, if you have no match you get zero points.")
        print("Your first card: " + first_card)
        print("Your second card: " + second_card)
        uchoice1 = input("Would you like to continue or want new cards? Please type c to continue and r to start again: ")

        if uchoice1 == "c":
            print("Given Card 1: " + given_card1)
            print("Given Card 2: " + given_card2)
            print("Given Card 3: " + given_card3)
            print("Given Card 4: " + given_card4)

            if (first_card == given_card1 or first_card == given_card2 or first_card == given_card3 or first_card == given_card4) \
                and (second_card == given_card1 or second_card == given_card2 or second_card == given_card3 or second_card == given_card4):
                points += 2
                print("Congrats, You have " + str(points) + " points, beacause both of your cards have matches!")
                playagain = input("Do you want to play again? Type yes to play again or q to quit: ")
            elif first_card == given_card1 or first_card == given_card2 or first_card == given_card3 or first_card == given_card4:
                points += 1
                print("Congrats, You have " + str(points) + " point, because your first card has a match!")
                playagain = input("Do you want to play again? Type yes to play again or q to quit: ")
            elif second_card == given_card1 or second_card == given_card2 or second_card == given_card3 or second_card == given_card4:
                points += 1
                print("Congrats, You have " + str(points) + " point, because your second card has a match!")
                playagain = input("Do you want to play again? Type yes to play again or q to quit: ")
            else:
                print("You have no matching cards, you lost!")
                playagain = input("Do you want to play again? Type a to play again or q to quit: ")
            
            if playagain == "a":
                main2()
            elif playagain == "q":
                exit()
            else:
                print("error")
                exit()
       
        elif uchoice1 == "r":
            main2()
        else:
            exit()

def main2():
    import random

    card_val = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]
    card_sign = [" of Hearts ", " of Clubs ", " of Spades ", " of Diamonds "]
    points = 0
    uchoice1 = ("")
    playagain = ("")

    random_card_val1 = random.choice(card_val)
    random_card_sign1 = random.choice(card_sign)
    random_card_val2 = random.choice(card_val)
    random_card_sign2 = random.choice(card_sign)

    first_card = (random_card_val1 + random_card_sign1)
    second_card = (random_card_val2 + random_card_sign2)

    random_card_val3 = random.choice(card_val)
    random_card_sign3 = random.choice(card_sign)
    random_card_val4 = random.choice(card_val)
    random_card_sign4 = random.choice(card_sign)
    random_card_val5 = random.choice(card_val)
    random_card_sign5 = random.choice(card_sign)
    random_card_val6 = random.choice(card_val)
    random_card_sign6 = random.choice(card_sign)

    given_card1 = (random_card_val3 + random_card_sign3)
    given_card2 = (random_card_val4 + random_card_sign4)
    given_card3 = (random_card_val5 + random_card_sign5)
    given_card4 = (random_card_val6 + random_card_sign6)

    if first_card == second_card:
        main()
    elif given_card1 == given_card2:
        main()
    elif given_card1 == given_card3:
        main()
    elif given_card1 == given_card4:
        main()
    elif given_card2 == given_card3:
        main()
    elif given_card2 == given_card4:
        main()
    elif given_card3 == given_card4:
        main()
    else:
        print("Your first card: " + first_card)
        print("Your second card: " + second_card)
        uchoice1 = input("Would you like to continue or want new cards? Please type c to continue and r to start again: ")

        if uchoice1 == "c":
            print("Given Card 1: " + given_card1)
            print("Given Card 2: " + given_card2)
            print("Given Card 3: " + given_card3)
            print("Given Card 4: " + given_card4)

            if (first_card == given_card1 or first_card == given_card2 or first_card == given_card3 or first_card == given_card4) \
                and (second_card == given_card1 or second_card == given_card2 or second_card == given_card3 or second_card == given_card4):
                points += 2
                print("Congrats, You have " + str(points) + " points, beacause both of your cards have matches!")
                playagain = input("Do you want to play again? Type yes to play again or q to quit: ")
            elif first_card == given_card1 or first_card == given_card2 or first_card == given_card3 or first_card == given_card4:
                points += 1
                print("Congrats, You have " + str(points) + " point, because your first card has a match!")
                playagain = input("Do you want to play again? Type yes to play again or q to quit: ")
            elif second_card == given_card1 or second_card == given_card2 or second_card == given_card3 or second_card == given_card4:
                points += 1
                print("Congrats, You have " + str(points) + " point, because your second card has a match!")
                playagain = input("Do you want to play again? Type yes to play again or q to quit: ")
            else:
                print("You have no matching cards, you lost!")
                playagain = input("Do you want to play again? Type a to play again or q to quit: ")
            
            if playagain == "a":
                main2()
            elif playagain == "q":
                exit()
            else:
                print("error")
       
        elif uchoice1 == "r":
            main2()
        else:
            exit()

main()