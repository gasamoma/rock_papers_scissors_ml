import random
choices = {'r':'rock', 'p': 'paper', 's':'scissors'}
rules = {'r': ['s'], 's': ['p'], 'p': ['r']}


def play():
    print "choices ", choices
    print "rules ", rules
    print "type exit to finish game"
    pc_wins = 0
    user_wins = 0
    ties = 0
    while True:
        user_play = raw_input("Play: ")
        pc_play = random.choice(choices.keys())
        if user_play in choices:
            if pc_play == user_play:
                ties +=1
                print "Tie"
            elif pc_play in rules[user_play]:
                user_wins +=1
                print "User Wins"
            elif user_play in rules[pc_play]:
                pc_wins +=1
                print "Pc Wins"
            else:
                print "wierd"
        elif user_play == "exit":
            break
        else:
            print "Not a Valid Option"
    total = user_wins+pc_wins+ties
    pc_w_r = (pc_wins * 100 / total)
    us_w_r = (user_wins * 100 / total)
    ties_w_r = (ties * 100 / total)
    print "Stats"
    print "Total games:", total
    print "Pc Win rate: ", pc_w_r, "%"
    print "User Win rate: ", us_w_r , "%"
    print "Ties Rate: ", ties_w_r, "%"
play()