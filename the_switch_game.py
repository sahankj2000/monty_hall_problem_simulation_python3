import random
from tqdm import tqdm

def play_random_game(switch):
    prize = random.randint(1,3)
    players_pick = random.randint(1,3)
    available_doors = []
    for i in range(1,4):
        if prize != i and players_pick != i:
            available_doors.append(i)
    revealed_door = random.choice(available_doors)
    if switch:
        # player switches
        for i in range(1,4):
            if i != revealed_door and i != players_pick:
                players_pick = i
                break
    # doesnt switch
    return players_pick == prize

    

def main():
    # number of games to play
    number_of_games = 1000000
    switch_and_win = 0
    switch_and_loose = 0
    stay_and_win = 0
    stay_and_loose = 0
    for i in tqdm(range(number_of_games)):
        switch = random.choice([True, False])
        outcome = play_random_game(switch)
        if switch:
            if outcome:
                switch_and_win += 1
            else:
                switch_and_loose += 1
        else:
            if outcome:
                stay_and_win += 1
            else:
                stay_and_loose += 1
    print('Number of games played :',number_of_games)
    switched_games = switch_and_loose + switch_and_win
    print('Total games switched :',switched_games,'( '+str((100*switched_games)/number_of_games)+'% )')
    print('Switched and won :',switch_and_win,'( '+str((100*switch_and_win)/switched_games)+'% )')
    print('Switched and lost :',switch_and_loose,'( '+str((100*switch_and_loose)/switched_games)+'% )')
    stayed_games = stay_and_loose + stay_and_win
    print('Total gamed stayed :',stayed_games,'( '+str((100*stayed_games)/number_of_games)+'% )')
    print('Stayed and won :',stay_and_win,'( '+str((100*stay_and_win)/stayed_games)+'% )')
    print('Stayed and lost :',stay_and_loose,'( '+str((100*stay_and_loose)/stayed_games)+'% )')

    

if __name__ == '__main__':
    main()