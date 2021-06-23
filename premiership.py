from tabulate import tabulate
import random

headers=["Club", "MP", "W", "D", "L", "GF", "GA", "GD", "Pts"]
arsenal=["Arsenal", 0, 0, 0, 0, 0, 0, 0, 0]
aston_villa=["Aston Villa", 0, 0, 0, 0, 0, 0, 0, 0]
brentford=["Brentford", 0, 0, 0, 0, 0, 0, 0, 0]
brighton=["Brighton", 0, 0, 0, 0, 0, 0, 0, 0]
burnley=["Burnley", 0, 0, 0, 0, 0, 0, 0, 0]
chelsea=["Chelsea", 0, 0, 0, 0, 0, 0, 0, 0]
crystal_palace=["Crystal Palace", 0, 0, 0, 0, 0, 0, 0, 0]
everton=["Everton", 0, 0, 0, 0, 0, 0, 0, 0]
leeds_united=["Leeds United", 0, 0, 0, 0, 0, 0, 0, 0]
leicester_city=["Leicester City", 0, 0, 0, 0, 0, 0, 0, 0]
liverpool=["Liverpool", 0, 0, 0, 0, 0, 0, 0, 0]
manchester_city=["Manchester City", 0, 0, 0, 0, 0, 0, 0, 0]
manchester_united=["Manchester United", 0, 0, 0, 0, 0, 0, 0, 0]
newcastle_united=["Newcastle United", 0, 0, 0, 0, 0, 0, 0, 0]
norwich_city=["Norwich City", 0, 0, 0, 0, 0, 0, 0, 0]
southampton=["Southampton", 0, 0, 0, 0, 0, 0, 0, 0]
tottenham=["Tottenham", 0, 0, 0, 0, 0, 0, 0, 0]
watford=["Watford", 0, 0, 0, 0, 0, 0, 0, 0]
west_ham=["West Ham", 0, 0, 0, 0, 0, 0, 0, 0]
wolves=["Wolves", 0, 0, 0, 0, 0, 0, 0, 0]

teams=[arsenal, aston_villa, brentford, brighton, burnley, chelsea, crystal_palace, everton, leeds_united, leicester_city, liverpool, manchester_city, manchester_united, newcastle_united, norwich_city, southampton, tottenham, watford, west_ham, wolves]

score=[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 7]



#print(random_teams)
#for i in teams:
 #   print (i[0])


#print((random.choice(score)),":",(random.choice(score)))

round=0

season_p1=2021
season_p2=2022
season=str(season_p1)+"/"+str(season_p2)


#setting fixtures
def fixtures():
    global group_a
    global group_b
    global rnd1
    global rnd2
    global rnd3
    global rnd4
    global rnd5
    global rnd6
    global rnd7
    global rnd8
    global rnd9
    global rnd10
    global rnd11
    global rnd12
    global rnd13
    global rnd14
    global rnd15
    global rnd16
    global rnd17
    global rnd18
    global rnd19

    random.shuffle(teams)
    group_a=teams[:10]
    group_b=teams[10:]

    rnd1=[[group_a[0], group_b[-1]], [group_b[-2], group_a[1]], [group_a[2], group_b[-3]],
          [group_b[-4], group_a[3]], [group_a[4], group_b[-5]], [group_b[-6], group_a[5]],
          [group_a[6], group_b[-7]], [group_b[-8], group_a[7]], [group_a[8], group_b[-9]],
          [group_b[-10], group_a[9]]]
    print("----------\nRound 1\n----------")
    for i in rnd1:
        print(i[0][0], i[1][0], sep="   vs   ")

    rnd2=[[group_a[0], group_b[-2]], [group_b[-3], group_a[-1]], [group_a[1], group_b[-4]],
          [group_b[-5], group_a[2]], [group_a[3], group_b[-6]], [group_b[-7], group_a[4]],
          [group_a[5], group_b[-8]], [group_b[-9], group_a[6]], [group_a[7], group_b[-10]],
          [group_b[9], group_a[8]]]
    print("----------\nRound 2\n----------")
    for i in rnd2:
        print(i[0][0], i[1][0], sep="   vs   ")

    rnd3=[[group_a[0], group_b[-3]], [group_b[-4], group_a[-2]], [group_a[-1], group_b[-5]],
          [group_b[-6], group_a[1]], [group_a[2], group_b[-7]], [group_b[-8], group_a[3]],
          [group_a[4], group_b[-9]], [group_b[-10], group_a[5]], [group_a[6], group_b[9]],
          [group_b[8], group_a[7]]]
    print("----------\nRound 3\n----------")
    for i in rnd3:
        print(i[0][0], i[1][0], sep="   vs   ")

    rnd4=[[group_a[0], group_b[-4]], [group_b[-5], group_a[-3]], [group_a[-2], group_b[-6]],
          [group_b[-7], group_a[-1]], [group_a[1], group_b[-8]], [group_b[-9], group_a[2]],
          [group_a[3], group_b[-10]], [group_b[9], group_a[4]], [group_a[5], group_b[8]],
          [group_b[7], group_a[6]]]
    print("----------\nRound 4\n----------")
    for i in rnd4:
        print(i[0][0], i[1][0], sep="   vs   ")

    rnd5=[[group_a[0], group_b[-5]], [group_b[-6], group_a[-4]], [group_a[-3], group_b[-7]],
          [group_b[-8], group_a[-2]], [group_a[-1], group_b[-9]], [group_b[-10], group_a[1]],
          [group_a[2], group_b[9]], [group_b[8], group_a[3]], [group_a[4], group_b[7]],
          [group_b[6], group_a[5]]]
    print("----------\nRound 5\n----------")
    for i in rnd5:
        print(i[0][0], i[1][0], sep="   vs   ")

    rnd6=[[group_a[0], group_b[-6]], [group_b[-7], group_a[-5]], [group_a[-4], group_b[-8]],
          [group_b[-9], group_a[-3]], [group_a[-2], group_b[-10]], [group_b[9], group_a[-1]],
          [group_a[1], group_b[8]], [group_b[7], group_a[2]], [group_a[3], group_b[6]],
          [group_b[5], group_a[4]]]
    print("----------\nRound 6\n----------")
    for i in rnd6:
        print(i[0][0], i[1][0], sep="   vs   ")

    rnd7=[[group_a[0], group_b[-7]], [group_b[-8], group_a[-6]], [group_a[-5], group_b[-9]],
          [group_b[-10], group_a[-4]], [group_a[-3], group_b[9]], [group_b[8], group_a[-2]],
          [group_a[-1], group_b[7]], [group_b[6], group_a[1]], [group_a[2], group_b[5]],
          [group_b[4], group_a[3]]]
    print("----------\nRound 7\n----------")
    for i in rnd7:
        print(i[0][0], i[1][0], sep="   vs   ")

    rnd8 = [[group_a[0], group_b[-8]], [group_b[-9], group_a[-7]], [group_a[-6], group_b[-10]],
            [group_b[9], group_a[-5]], [group_a[-4], group_b[8]], [group_b[7], group_a[-3]],
            [group_a[-2], group_b[6]], [group_b[5], group_a[-1]], [group_a[1], group_b[4]],
            [group_b[3], group_a[2]]]
    print("----------\nRound 8\n----------")
    for i in rnd8:
        print(i[0][0], i[1][0], sep="   vs   ")

    rnd9 = [[group_a[0], group_b[-9]], [group_b[-10], group_a[-8]], [group_a[-7], group_b[9]],
            [group_b[8], group_a[-6]], [group_a[-5], group_b[7]], [group_b[6], group_a[-4]],
            [group_a[-3], group_b[5]], [group_b[4], group_a[-2]], [group_a[-1], group_b[3]],
            [group_b[2], group_a[1]]]
    print("----------\nRound 9\n----------")
    for i in rnd9:
        print(i[0][0], i[1][0], sep="   vs   ")

    rnd10 = [[group_a[0], group_b[-10]], [group_b[9], group_a[-9]], [group_a[-8], group_b[8]],
            [group_b[7], group_a[-7]], [group_a[-6], group_b[6]], [group_b[5], group_a[-5]],
            [group_a[-4], group_b[4]], [group_b[3], group_a[-3]], [group_a[-2], group_b[2]],
            [group_b[1], group_a[-1]]]
    print("----------\nRound 10\n----------")
    for i in rnd10:
        print(i[0][0], i[1][0], sep="   vs   ")

    rnd11 = [[group_a[0], group_b[8]], [group_b[-10], group_a[9]], [group_a[-9], group_b[7]],
             [group_b[6], group_a[-8]], [group_a[-7], group_b[5]], [group_b[4], group_a[-6]],
             [group_a[-5], group_b[3]], [group_b[2], group_a[-4]], [group_a[-3], group_b[1]],
             [group_b[-1], group_a[-2]]]
    print("----------\nRound 11\n----------")
    for i in rnd11:
        print(i[0][0], i[1][0], sep="   vs   ")

    rnd12 = [[group_a[0], group_b[8]], [group_b[-10], group_a[9]], [group_a[-9], group_b[7]],
             [group_b[6], group_a[-8]], [group_a[-7], group_b[5]], [group_b[4], group_a[-6]],
             [group_a[-5], group_b[3]], [group_b[2], group_a[-4]], [group_a[-3], group_b[1]],
             [group_b[-1], group_a[-2]]]
    print("----------\nRound 12\n----------")
    for i in rnd12:
        print(i[0][0], i[1][0], sep="   vs   ")

    rnd13 = [[group_a[0], group_b[7]], [group_b[6], group_a[8]], [group_a[9], group_b[5]],
             [group_b[4], group_a[-10]], [group_a[-9], group_b[3]], [group_b[2], group_a[-8]],
             [group_a[-7], group_b[1]], [group_b[-1], group_a[-6]], [group_a[-5], group_b[-2]],
             [group_b[-3], group_a[-4]]]
    print("----------\nRound 13\n----------")
    for i in rnd13:
        print(i[0][0], i[1][0], sep="   vs   ")

    rnd14 = [[group_a[0], group_b[6]], [group_b[5], group_a[7]], [group_a[8], group_b[4]],
             [group_b[3], group_a[9]], [group_a[-10], group_b[2]], [group_b[1], group_a[-9]],
             [group_a[-8], group_b[-1]], [group_b[-2], group_a[-7]], [group_a[-6], group_b[-3]],
             [group_b[-4], group_a[-5]]]
    print("----------\nRound 14\n----------")
    for i in rnd14:
        print(i[0][0], i[1][0], sep="   vs   ")

    rnd15 = [[group_a[0], group_b[5]], [group_b[4], group_a[6]], [group_a[7], group_b[3]],
             [group_b[2], group_a[8]], [group_a[9], group_b[1]], [group_b[-1], group_a[-10]],
             [group_a[-9], group_b[-2]], [group_b[-3], group_a[-8]], [group_a[-7], group_b[-4]],
             [group_b[-5], group_a[-6]]]
    print("----------\nRound 15\n----------")
    for i in rnd15:
        print(i[0][0], i[1][0], sep="   vs   ")

    rnd16 = [[group_a[0], group_b[4]], [group_b[3], group_a[5]], [group_a[6], group_b[2]],
             [group_b[1], group_a[7]], [group_a[8], group_b[-1]], [group_b[-2], group_a[9]],
             [group_a[-10], group_b[-3]], [group_b[-4], group_a[-9]], [group_a[-8], group_b[-5]],
             [group_b[-6], group_a[-7]]]
    print("----------\nRound 16\n----------")
    for i in rnd16:
        print(i[0][0], i[1][0], sep="   vs   ")

    rnd17 = [[group_a[0], group_b[3]], [group_b[2], group_a[4]], [group_a[5], group_b[1]],
             [group_b[-1], group_a[6]], [group_a[7], group_b[-2]], [group_b[-3], group_a[8]],
             [group_a[9], group_b[-4]], [group_b[-5], group_a[-10]], [group_a[-9], group_b[-6]],
             [group_b[-7], group_a[-8]]]
    print("----------\nRound 17\n----------")
    for i in rnd17:
        print(i[0][0], i[1][0], sep="   vs   ")

    rnd18 = [[group_a[0], group_b[2]], [group_b[1], group_a[3]], [group_a[4], group_b[-1]],
             [group_b[-2], group_a[5]], [group_a[6], group_b[-3]], [group_b[-4], group_a[7]],
             [group_a[8], group_b[-5]], [group_b[-6], group_a[9]], [group_a[-10], group_b[-7]],
             [group_b[-8], group_a[-9]]]
    print("----------\nRound 18\n----------")
    for i in rnd18:
        print(i[0][0], i[1][0], sep="   vs   ")

    rnd19 = [[group_a[0], group_b[1]], [group_b[-1], group_a[2]], [group_a[3], group_b[-2]],
             [group_b[-3], group_a[4]], [group_a[5], group_b[-4]], [group_b[-5], group_a[6]],
             [group_a[7], group_b[-6]], [group_b[-7], group_a[8]], [group_a[9], group_b[-8]],
             [group_b[-9], group_a[-10]]]
    print("----------\nRound 19\n----------")
    for i in rnd19:
        print(i[0][0], i[1][0], sep="   vs   ")





#instert matches played to table
def mp():
    i[0][1] = i[0][1]+1
    i[1][1] = i[1][1]+1

#insert win, lose, draw and points to table
def wld_pts():
    if score1==score2:
        i[0][3] = i[0][3]+1
        i[1][3] = i[1][3]+1
        i[0][8] = i[0][8]+1
        i[1][8] = i[1][8]+1
    elif score1>score2:
        i[0][2] = i[0][2]+1
        i[1][4] = i[1][4]+1
        i[0][8] = i[0][8]+3
        i[1][8] = i[1][8]+0
    elif score1<score2:
        i[0][4] = i[0][4] + 1
        i[1][2] = i[1][2] + 1
        i[0][8] = i[0][8] + 0
        i[1][8] = i[1][8] + 3

#insert gf ga and gd into table
def gf_ga_gd():
    i[0][5] = i[0][5] + score1
    i[1][5] = i[1][5] + score2

    i[0][6] = i[0][6] + score2
    i[1][6] = i[1][6] + score1

    i[0][7] = i[0][5] - i[0][6]
    i[1][7] = i[1][5] - i[1][6]





game=True
while game:
    round=0
    print ("\nWelcome to",(season), "season\n")
    print ("Fixtures for this season are: ")
    fixtures()
        #print(tabulate(teams, headers=["Club", "MP", "W ", "D ", "L ", "GF", "GA", "GD", "Pts"], tablefmt="fancy_grid", numalign="center"))
    print("--------------------")
    input("Hit enter to start the season")

    #round 1
    round = round + 1
    print("\nRound", round, "of 38")
    print("Results of round", round, "are: ")
    for i in rnd1:
        score1=(random.choice(score))
        score2=(random.choice(score))
        mp()
        wld_pts()
        gf_ga_gd()
        print(i[0][0], i[1][0], sep="   vs   ")
        print(score1,":",score2)
    print("\nTable after round", round)
    teams.sort(key=lambda team: (team[8], team[7]), reverse=True)
    print(tabulate(teams, headers=["Club", "MP", "W ", "D ", "L ", "GF", "GA", "GD", "Pts"],))
    input("Hit enter to start next round")
    print("--------------------")

    #round 2
    round = round + 1
    print("\nRound", round, "of 38")
    print("Results of round", round, "are: ")
    for i in rnd2:
        score1 = (random.choice(score))
        score2 = (random.choice(score))
        mp()
        wld_pts()
        gf_ga_gd()
        print(i[0][0], i[1][0], sep="   vs   ")
        print(score1, ":", score2)
    print("\nTable after round", round)
    teams.sort(key=lambda team: (team[8], team[7]), reverse=True)
    print(tabulate(teams, headers=["Club", "MP", "W ", "D ", "L ", "GF", "GA", "GD", "Pts"]))
    input("Hit enter to start next round")
    print("--------------------")

    # round 3
    round = round + 1
    print("\nRound", round, "of 38")
    print("Results of round", round, "are: ")
    for i in rnd3:
        score1 = (random.choice(score))
        score2 = (random.choice(score))
        mp()
        wld_pts()
        gf_ga_gd()
        print(i[0][0], i[1][0], sep="   vs   ")
        print(score1, ":", score2)
    print("\nTable after round", round)
    teams.sort(key=lambda team: (team[8], team[7]), reverse=True)
    print(tabulate(teams, headers=["Club", "MP", "W ", "D ", "L ", "GF", "GA", "GD", "Pts"]))
    input("Hit enter to start next round")
    print("--------------------")

    # round 4
    round = round + 1
    print("\nRound", round, "of 38")
    print("Results of round", round, "are: ")
    for i in rnd4:
        score1 = (random.choice(score))
        score2 = (random.choice(score))
        mp()
        wld_pts()
        gf_ga_gd()
        print(i[0][0], i[1][0], sep="   vs   ")
        print(score1, ":", score2)
    print("\nTable after round", round)
    teams.sort(key=lambda team: (team[8], team[7]), reverse=True)
    print(tabulate(teams, headers=["Club", "MP", "W ", "D ", "L ", "GF", "GA", "GD", "Pts"]))
    input("Hit enter to start next round")
    print("--------------------")

    # round 5
    round = round + 1
    print("\nRound", round, "of 38")
    print("Results of round", round, "are: ")
    for i in rnd5:
        score1 = (random.choice(score))
        score2 = (random.choice(score))
        mp()
        wld_pts()
        gf_ga_gd()
        print(i[0][0], i[1][0], sep="   vs   ")
        print(score1, ":", score2)
    print("\nTable after round", round)
    teams.sort(key=lambda team: (team[8], team[7]), reverse=True)
    print(tabulate(teams, headers=["Club", "MP", "W ", "D ", "L ", "GF", "GA", "GD", "Pts"]))
    input("Hit enter to start next round")
    print("--------------------")

    # round 6
    round = round + 1
    print("\nRound", round, "of 38")
    print("Results of round", round, "are: ")
    for i in rnd6:
        score1 = (random.choice(score))
        score2 = (random.choice(score))
        mp()
        wld_pts()
        gf_ga_gd()
        print(i[0][0], i[1][0], sep="   vs   ")
        print(score1, ":", score2)
    print("\nTable after round", round)
    teams.sort(key=lambda team: (team[8], team[7]), reverse=True)
    print(tabulate(teams, headers=["Club", "MP", "W ", "D ", "L ", "GF", "GA", "GD", "Pts"]))
    input("Hit enter to start next round")
    print("--------------------")

    # round 7
    round = round + 1
    print("\nRound", round, "of 38")
    print("Results of round", round, "are: ")
    for i in rnd7:
        score1 = (random.choice(score))
        score2 = (random.choice(score))
        mp()
        wld_pts()
        gf_ga_gd()
        print(i[0][0], i[1][0], sep="   vs   ")
        print(score1, ":", score2)
    print("\nTable after round", round)
    teams.sort(key=lambda team: (team[8], team[7]), reverse=True)
    print(tabulate(teams, headers=["Club", "MP", "W ", "D ", "L ", "GF", "GA", "GD", "Pts"]))
    input("Hit enter to start next round")
    print("--------------------")

    # round 8
    round = round + 1
    print("\nRound", round, "of 38")
    print("Results of round", round, "are: ")
    for i in rnd8:
        score1 = (random.choice(score))
        score2 = (random.choice(score))
        mp()
        wld_pts()
        gf_ga_gd()
        print(i[0][0], i[1][0], sep="   vs   ")
        print(score1, ":", score2)
    print("\nTable after round", round)
    teams.sort(key=lambda team: (team[8], team[7]), reverse=True)
    print(tabulate(teams, headers=["Club", "MP", "W ", "D ", "L ", "GF", "GA", "GD", "Pts"]))
    input("Hit enter to start next round")
    print("--------------------")

    # round 9
    round = round + 1
    print("\nRound", round, "of 38")
    print("Results of round", round, "are: ")
    for i in rnd9:
        score1 = (random.choice(score))
        score2 = (random.choice(score))
        mp()
        wld_pts()
        gf_ga_gd()
        print(i[0][0], i[1][0], sep="   vs   ")
        print(score1, ":", score2)
    print("\nTable after round", round)
    teams.sort(key=lambda team: (team[8], team[7]), reverse=True)
    print(tabulate(teams, headers=["Club", "MP", "W ", "D ", "L ", "GF", "GA", "GD", "Pts"]))
    input("Hit enter to start next round")
    print("--------------------")

    # round 10
    round = round + 1
    print("\nRound", round, "of 38")
    print("Results of round", round, "are: ")
    for i in rnd10:
        score1 = (random.choice(score))
        score2 = (random.choice(score))
        mp()
        wld_pts()
        gf_ga_gd()
        print(i[0][0], i[1][0], sep="   vs   ")
        print(score1, ":", score2)
    print("\nTable after round", round)
    teams.sort(key=lambda team: (team[8], team[7]), reverse=True)
    print(tabulate(teams, headers=["Club", "MP", "W ", "D ", "L ", "GF", "GA", "GD", "Pts"]))
    input("Hit enter to start next round")
    print("--------------------")

    # round 11
    round = round + 1
    print("\nRound", round, "of 38")
    print("Results of round", round, "are: ")
    for i in rnd11:
        score1 = (random.choice(score))
        score2 = (random.choice(score))
        mp()
        wld_pts()
        gf_ga_gd()
        print(i[0][0], i[1][0], sep="   vs   ")
        print(score1, ":", score2)
    print("\nTable after round", round)
    teams.sort(key=lambda team: (team[8], team[7]), reverse=True)
    print(tabulate(teams, headers=["Club", "MP", "W ", "D ", "L ", "GF", "GA", "GD", "Pts"]))
    input("Hit enter to start next round")
    print("--------------------")

    # round 12
    round = round + 1
    print("\nRound", round, "of 38")
    print("Results of round", round, "are: ")
    for i in rnd12:
        score1 = (random.choice(score))
        score2 = (random.choice(score))
        mp()
        wld_pts()
        gf_ga_gd()
        print(i[0][0], i[1][0], sep="   vs   ")
        print(score1, ":", score2)
    print("\nTable after round", round)
    teams.sort(key=lambda team: (team[8], team[7]), reverse=True)
    print(tabulate(teams, headers=["Club", "MP", "W ", "D ", "L ", "GF", "GA", "GD", "Pts"]))
    input("Hit enter to start next round")
    print("--------------------")

    # round 13
    round = round + 1
    print("\nRound", round, "of 38")
    print("Results of round", round, "are: ")
    for i in rnd13:
        score1 = (random.choice(score))
        score2 = (random.choice(score))
        mp()
        wld_pts()
        gf_ga_gd()
        print(i[0][0], i[1][0], sep="   vs   ")
        print(score1, ":", score2)
    print("\nTable after round", round)
    teams.sort(key=lambda team: (team[8], team[7]), reverse=True)
    print(tabulate(teams, headers=["Club", "MP", "W ", "D ", "L ", "GF", "GA", "GD", "Pts"]))
    input("Hit enter to start next round")
    print("--------------------")

    # round 14
    round = round + 1
    print("\nRound", round, "of 38")
    print("Results of round", round, "are: ")
    for i in rnd14:
        score1 = (random.choice(score))
        score2 = (random.choice(score))
        mp()
        wld_pts()
        gf_ga_gd()
        print(i[0][0], i[1][0], sep="   vs   ")
        print(score1, ":", score2)
    print("\nTable after round", round)
    teams.sort(key=lambda team: (team[8], team[7]), reverse=True)
    print(tabulate(teams, headers=["Club", "MP", "W ", "D ", "L ", "GF", "GA", "GD", "Pts"]))
    input("Hit enter to start next round")
    print("--------------------")

    # round 15
    round = round + 1
    print("\nRound", round, "of 38")
    print("Results of round", round, "are: ")
    for i in rnd15:
        score1 = (random.choice(score))
        score2 = (random.choice(score))
        mp()
        wld_pts()
        gf_ga_gd()
        print(i[0][0], i[1][0], sep="   vs   ")
        print(score1, ":", score2)
    print("\nTable after round", round)
    teams.sort(key=lambda team: (team[8], team[7]), reverse=True)
    print(tabulate(teams, headers=["Club", "MP", "W ", "D ", "L ", "GF", "GA", "GD", "Pts"]))
    input("Hit enter to start next round")
    print("--------------------")

    # round 16
    round = round + 1
    print("\nRound", round, "of 38")
    print("Results of round", round, "are: ")
    for i in rnd16:
        score1 = (random.choice(score))
        score2 = (random.choice(score))
        mp()
        wld_pts()
        gf_ga_gd()
        print(i[0][0], i[1][0], sep="   vs   ")
        print(score1, ":", score2)
    print("\nTable after round", round)
    teams.sort(key=lambda team: (team[8], team[7]), reverse=True)
    print(tabulate(teams, headers=["Club", "MP", "W ", "D ", "L ", "GF", "GA", "GD", "Pts"]))
    input("Hit enter to start next round")
    print("--------------------")

    # round 17
    round = round + 1
    print("\nRound", round, "of 38")
    print("Results of round", round, "are: ")
    for i in rnd17:
        score1 = (random.choice(score))
        score2 = (random.choice(score))
        mp()
        wld_pts()
        gf_ga_gd()
        print(i[0][0], i[1][0], sep="   vs   ")
        print(score1, ":", score2)
    print("\nTable after round", round)
    teams.sort(key=lambda team: (team[8], team[7]), reverse=True)
    print(tabulate(teams, headers=["Club", "MP", "W ", "D ", "L ", "GF", "GA", "GD", "Pts"]))
    input("Hit enter to start next round")
    print("--------------------")

    # round 18
    round = round + 1
    print("\nRound", round, "of 38")
    print("Results of round", round, "are: ")
    for i in rnd18:
        score1 = (random.choice(score))
        score2 = (random.choice(score))
        mp()
        wld_pts()
        gf_ga_gd()
        print(i[0][0], i[1][0], sep="   vs   ")
        print(score1, ":", score2)
    print("\nTable after round", round)
    teams.sort(key=lambda team: (team[8], team[7]), reverse=True)
    print(tabulate(teams, headers=["Club", "MP", "W ", "D ", "L ", "GF", "GA", "GD", "Pts"]))
    input("Hit enter to start next round")
    print("--------------------")

    # round 19
    round = round + 1
    print("\nRound", round, "of 38")
    print("Results of round", round, "are: ")
    for i in rnd19:
        score1 = (random.choice(score))
        score2 = (random.choice(score))
        mp()
        wld_pts()
        gf_ga_gd()
        print(i[0][0], i[1][0], sep="   vs   ")
        print(score1, ":", score2)
    print("\nTable after round", round)
    teams.sort(key=lambda team: (team[8], team[7]), reverse=True)
    print(tabulate(teams, headers=["Club", "MP", "W ", "D ", "L ", "GF", "GA", "GD", "Pts"]))
    input("Hit enter to start next round")
    print("--------------------")

    #winner on end of the season
    print ("Winner of the season is: ",(teams[0][0]))
    game=False




