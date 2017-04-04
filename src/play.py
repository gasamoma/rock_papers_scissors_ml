import random
import math
choices = {'r': 'rock', 'p': 'paper', 's': 'scissors'}
reap_choices = dict(choices)
rules = {'r': ['s'], 's': ['p'], 'p': ['r']}
deviation1 = 2
deviation2 = 6
inverse_rules = dict()


def think(historical):
    n = len(historical)
    if n > deviation1:
        subset = historical[-deviation1:n-1]
        max_l, max_n = most_played(subset)
        if max_l != '':
            return inverse_rules[max_l][0]
    if n > deviation2:
        subset = historical[-deviation2:n-1]
        max_l, max_n = most_played(subset)
        if max_l != '':
            return inverse_rules[max_l][0]
    return random.choice(choices.keys())


def most_played(set):
    maxl = ''
    maxn = 0
    for key, value in reap_choices.iteritems():
        reap_choices[key] = 0
    for x in set:
        reap_choices[x] += 1
        if reap_choices[x] > maxn:
            maxn = reap_choices[x]
            maxl = x
    if maxn >= math.ceil(len(set)*0.7):
        return maxl, maxn
    else:
        return '', 0


def initialize():
    global inverse_rules
    for key, value in rules.iteritems():
        for x in value:
            if x in inverse_rules:
                inverse_rules[x].append(key)
            else:
                inverse_rules[x] = [key]


def play():
    print "choices ", choices
    print "rules ", rules
    print "type exit to finish game"
    initialize()
    pc_wins = 0
    user_wins = 0
    ties = 0
    historical = []
    while True:
        user_play = raw_input("Play: ")
        pc_play = think(historical)
        print "Pc Play ", pc_play
        if user_play in choices:
            historical.append(user_play)
            if pc_play == user_play:
                ties += 1
                print "Tie"
            elif pc_play in rules[user_play]:
                user_wins += 1
                print "User Wins"
            elif user_play in rules[pc_play]:
                pc_wins += 1
                print "Pc Wins"
            else:
                print "wierd"
        elif user_play == "exit":
            break
        else:
            print "Not a Valid Option"
        print "\n"
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