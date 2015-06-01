def the_flying_circus():
    print "Welcome to the flying circus!"
    print "Do you want to get popcorn?"
    answer = raw_input("Type \"yes\" or \"no\" and then hit \"Enter\".").lower() #type response
    if answer == "yes":
        print "Do you have money?"
        answer = raw_input("Type \"yes\" or \"no\" and then hit \"Enter\".").lower() #type response
        if answer == "yes":
            print "How much do you have?"
            try:
                answer = float(raw_input("Answer me! Type a number and let's see if we can get popcorn!")) #type response
                if answer >= 5:
                    print "Hey, you've got enough to buy both of us popcorn! Good, because that's exactly what you're going to do."
                    return "GOOD ENDING" #good ending
                elif answer >= 2.50 and answer < 5:
                    print "You've only got enough for 1 helping of popcorn. Aww thanks, you want to buy it just for me? You shouldn't have! Thanks!"
                    return "GOOD ENDING" #good ending
                elif answer < 2.50 and answer > 0:
                    print "You don't have enough! I can't believe you!"
                    return "GAME OVER" #bad ending
                elif answer == 0:
                    print "That's the same as not having any money at all! You're so stupid!"
                    return "GAME OVER" #bad ending
                elif answer < 0:
                    print "You can't have negative money! Ugh, you're so stupid!"
                    return "GAME OVER" #bad ending
            except ValueError:
                print "I asked for a number, not mumbled garbage from a stupid idiot! I've had it with your shenanigans - GET OUT OF MY SIGHT!"
                return "WORST ENDING" #end block, bad ending
        elif answer == "no":
            print "I can't believe you came here without money! I should just leave you here, you useless dimwit!"
            return "GAME OVER" #bad ending
        else:
            print "You can't even answer a simple yes/no question?! I can't believe you!"
            return "GAME OVER" #end block, bad ending
    elif answer == "no":
        print "What? Do you not like popcorn or something?"
        answer = raw_input("Type \"yes\" or \"no\" and then hit \"Enter\".").lower() #type response
        if answer == "yes":
            print "Wow. You don't like popcorn. I'm not sure if we can be friends anymore."
            return "GAME OVER" #bad ending
        elif answer == "no":
            print "Oh. I guess you're just not in the mood for popcorn then. I guess that's alright."
            return "NEUTRAL ENDING" #okay ending
        else:
            print "You idiot! Give me a straight answer! That means 'yes' or 'no'! Can't you understand even the simplest things?!"
            return "GAME OVER" #block end
    else:
        print "WRONG ANSWER! Start the game over, you idiot!" #block end, retry
        the_flying_circus()
print the_flying_circus()
