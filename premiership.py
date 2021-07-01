from tabulate import tabulate
import random
from random import sample

#premiership teams
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


#championship teams
barnsley=["Barnsley", 0, 0, 0, 0, 0, 0, 0, 0]
birmingham_city=["Birmingham City", 0, 0, 0, 0, 0, 0, 0, 0]
blackburn_rovers=["Blackburn Rovers", 0, 0, 0, 0, 0, 0, 0, 0]
blackpool=["Blackpool", 0, 0, 0, 0, 0, 0, 0, 0]
bournemouth=["Bournemouth", 0, 0, 0, 0, 0, 0, 0, 0]
bristol_city=["Bristol City", 0, 0, 0, 0, 0, 0, 0, 0]
cardiff_city=["Cardiff City", 0, 0, 0, 0, 0, 0, 0, 0]
coventry_city=["Coventry City", 0, 0, 0, 0, 0, 0, 0, 0]
derby_county=["Derby County", 0, 0, 0, 0, 0, 0, 0, 0]
fulham=["Fulham", 0, 0, 0, 0, 0, 0, 0, 0]
huddersfield_town=["Huddersfield Town", 0, 0, 0, 0, 0, 0, 0, 0]
hull_city=["Hull City", 0, 0, 0, 0, 0, 0, 0, 0]
luton_town=["Luton Town", 0, 0, 0, 0, 0, 0, 0, 0]
middlesbrough=["Middlesbrough", 0, 0, 0, 0, 0, 0, 0, 0]
millwall=["Millwall", 0, 0, 0, 0, 0, 0, 0, 0]
nottingham_forest=["Nottingham Forest", 0, 0, 0, 0, 0, 0, 0, 0]
peterborough_united=["Peterborough United", 0, 0, 0, 0, 0, 0, 0, 0]
preston_north_end=["Preston North End", 0, 0, 0, 0, 0, 0, 0, 0]
queens_park_rangers=["Queens Park Rangers", 0, 0, 0, 0, 0, 0, 0, 0]
reading=["Reading", 0, 0, 0, 0, 0, 0, 0, 0]
sheffield_united=["Sheffield United", 0, 0, 0, 0, 0, 0, 0, 0]
stoke_city=["Birmingham", 0, 0, 0, 0, 0, 0, 0, 0]
swansea_city=["Swansea City", 0, 0, 0, 0, 0, 0, 0, 0]
west_bromwich_albion=["West Bromwich Albion", 0, 0, 0, 0, 0, 0, 0, 0]

championship = [barnsley, birmingham_city, blackburn_rovers, blackpool, bournemouth, bristol_city, cardiff_city, coventry_city, derby_county, fulham, huddersfield_town, hull_city, luton_town, middlesbrough, millwall, nottingham_forest, peterborough_united, preston_north_end, queens_park_rangers, reading, sheffield_united, stoke_city, swansea_city, west_bromwich_albion]



score=[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 7]



#setting fixtures
def fixtures():

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
    global rnd20
    global rnd21
    global rnd22
    global rnd23
    global rnd24
    global rnd25
    global rnd26
    global rnd27
    global rnd28
    global rnd29
    global rnd30
    global rnd31
    global rnd32
    global rnd33
    global rnd34
    global rnd35
    global rnd36
    global rnd37
    global rnd38

    random.shuffle(teams)
    

    rnd1=[[teams[0], teams[19]], [teams[1], teams[18]], [teams[2], teams[17]],
    [teams[3], teams[16]], [teams[4], teams[15]], [teams[5], teams[14]],
    [teams[6], teams[13]], [teams[7], teams[12]], [teams[8], teams[11]],
    [teams[9], teams[10]]]
    print("----------\nRound 1\n----------")
    for i in rnd1:
        print(i[0][0], i[1][0], sep="   vs   ")

    rnd2=[[teams[0], teams[18]], [teams[19], teams[17]], [teams[1], teams[16]],
    [teams[2], teams[15]], [teams[3], teams[14]], [teams[4], teams[13]],
    [teams[5], teams[12]], [teams[6], teams[11]], [teams[7], teams[10]],
    [teams[8], teams[9]]]
    print("----------\nRound 2\n----------")
    for i in rnd2:
        print(i[0][0], i[1][0], sep="   vs   ")

    rnd3=[[teams[0], teams[17]], [teams[18], teams[16]], [teams[19], teams[15]],
    [teams[1], teams[14]], [teams[2], teams[13]], [teams[3], teams[12]],
    [teams[4], teams[11]], [teams[5], teams[10]], [teams[6], teams[9]], [teams[7], teams[8]]]
    print("----------\nRound 3\n----------")
    for i in rnd3:
        print(i[0][0], i[1][0], sep="   vs   ")

    rnd4=[[teams[0], teams[16]], [teams[17], teams[15]], [teams[18], teams[14]],
    [teams[19], teams[13]], [teams[1], teams[12]], [teams[2], teams[11]],
    [teams[3], teams[10]], [teams[4], teams[9]], [teams[5], teams[8]], [teams[6], teams[7]]]
    print("----------\nRound 4\n----------")
    for i in rnd4:
        print(i[0][0], i[1][0], sep="   vs   ")


    rnd5=[[teams[0], teams[15]], [teams[16], teams[14]], [teams[17], teams[13]],
    [teams[18], teams[12]], [teams[19], teams[11]], [teams[1], teams[10]],
    [teams[2], teams[9]], [teams[3], teams[8]], [teams[4], teams[7]], [teams[5], teams[6]]]
    print("----------\nRound 5\n----------")
    for i in rnd5:
        print(i[0][0], i[1][0], sep="   vs   ")

    rnd6=[[teams[0], teams[14]], [teams[15], teams[13]], [teams[16], teams[12]],
    [teams[17], teams[11]], [teams[18], teams[10]], [teams[19], teams[9]],
    [teams[1], teams[8]], [teams[2], teams[7]], [teams[3], teams[6]], [teams[4], teams[5]]]
    print("----------\nRound 6\n----------")
    for i in rnd6:
        print(i[0][0], i[1][0], sep="   vs   ")

    rnd7=[[teams[0], teams[13]], [teams[14], teams[12]], [teams[15], teams[11]],
    [teams[16], teams[10]], [teams[17], teams[9]], [teams[18], teams[8]],
    [teams[19], teams[7]], [teams[1], teams[6]], [teams[2], teams[5]], [teams[3], teams[4]]]
    print("----------\nRound 7\n----------")
    for i in rnd7:
        print(i[0][0], i[1][0], sep="   vs   ")

    rnd8=[[teams[0], teams[12]], [teams[13], teams[11]], [teams[14], teams[10]],
    [teams[15], teams[9]], [teams[16], teams[8]], [teams[17], teams[7]],
    [teams[18], teams[6]], [teams[19], teams[5]], [teams[1], teams[4]], [teams[2], teams[3]]]
    print("----------\nRound 8\n----------")
    for i in rnd8:
        print(i[0][0], i[1][0], sep="   vs   ")

    rnd9=[[teams[0], teams[11]], [teams[12], teams[10]], [teams[13], teams[9]],
    [teams[14], teams[8]], [teams[15], teams[7]], [teams[16], teams[6]],
    [teams[17], teams[5]], [teams[18], teams[4]], [teams[19], teams[3]], [teams[1], teams[2]]]
    print("----------\nRound 9\n----------")
    for i in rnd9:
        print(i[0][0], i[1][0], sep="   vs   ")

    rnd10=[[teams[0], teams[10]], [teams[11], teams[9]], [teams[12], teams[8]],
    [teams[13], teams[7]], [teams[14], teams[6]], [teams[15], teams[5]],
    [teams[16], teams[4]], [teams[17], teams[3]], [teams[18], teams[2]], [teams[19], teams[1]]]
    print("----------\nRound 10\n----------")
    for i in rnd10:
        print(i[0][0], i[1][0], sep="   vs   ")

    rnd11=[[teams[0], teams[9]], [teams[10], teams[8]], [teams[11], teams[7]], [teams[12], teams[6]], [teams[13], teams[5]], [teams[14], teams[4]], [teams[15], teams[3]], [teams[16], teams[2]], [teams[17], teams[1]], [teams[18], teams[19]]]
    print("----------\nRound 11\n----------")
    for i in rnd11:
          print(i[0][0], i[1][0], sep="   vs   ")

    rnd12=[[teams[0], teams[8]], [teams[9], teams[7]], [teams[10], teams[6]],
    [teams[11], teams[5]], [teams[12], teams[4]], [teams[13], teams[3]],
    [teams[14], teams[2]], [teams[15], teams[1]], [teams[16], teams[19]], [teams[17], teams[18]]]
    print("----------\nRound 12\n----------")
    for i in rnd12:
        print(i[0][0], i[1][0], sep="   vs   ")

    rnd13=[[teams[0], teams[7]], [teams[8], teams[6]], [teams[9], teams[5]],
    [teams[10], teams[4]], [teams[11], teams[3]], [teams[12], teams[2]],
    [teams[13], teams[1]], [teams[14], teams[19]], [teams[15], teams[18]], [teams[16], teams[17]]]
    print("----------\nRound 13\n----------")
    for i in rnd13:
        print(i[0][0], i[1][0], sep="   vs   ")

    rnd14=[[teams[0], teams[6]], [teams[7], teams[5]], [teams[8], teams[4]],
    [teams[9], teams[3]], [teams[10], teams[2]], [teams[11], teams[1]],
    [teams[12], teams[19]], [teams[13], teams[18]], [teams[14], teams[17]], [teams[15], teams[16]]]
    print("----------\nRound 14\n----------")
    for i in rnd14:
        print(i[0][0], i[1][0], sep="   vs   ")

    rnd15=[[teams[0], teams[5]], [teams[6], teams[4]], [teams[7], teams[3]],
    [teams[8], teams[2]], [teams[9], teams[1]], [teams[10], teams[19]],
    [teams[11], teams[18]], [teams[12], teams[17]], [teams[13], teams[16]], [teams[14], teams[15]]]
    print("----------\nRound 15\n----------")
    for i in rnd15:
        print(i[0][0], i[1][0], sep="   vs   ")

    rnd16=[[teams[0], teams[4]], [teams[5], teams[3]], [teams[6], teams[2]],
    [teams[7], teams[1]], [teams[8], teams[19]], [teams[9], teams[18]],
    [teams[10], teams[17]], [teams[11], teams[16]], [teams[12], teams[15]], [teams[13], teams[14]]]
    print("----------\nRound 16\n----------")
    for i in rnd16:
        print(i[0][0], i[1][0], sep="   vs   ")

    rnd17=[[teams[0], teams[3]], [teams[4], teams[2]], [teams[5], teams[1]],
    [teams[6], teams[19]], [teams[7], teams[18]], [teams[8], teams[17]],
    [teams[9], teams[16]], [teams[10], teams[15]], [teams[11], teams[14]], [teams[12], teams[13]]]
    print("----------\nRound 17\n----------")
    for i in rnd17:
        print(i[0][0], i[1][0], sep="   vs   ")

    rnd18=[[teams[0], teams[2]], [teams[3], teams[1]], [teams[4], teams[19]],
    [teams[5], teams[18]], [teams[6], teams[17]], [teams[7], teams[16]],
    [teams[8], teams[15]], [teams[9], teams[14]], [teams[10], teams[13]], [teams[11], teams[12]]]
    print("----------\nRound 18\n----------")
    for i in rnd18:
        print(i[0][0], i[1][0], sep="   vs   ")

    rnd19=[[teams[0], teams[1]], [teams[2], teams[19]], [teams[3], teams[18]],
    [teams[4], teams[17]], [teams[5], teams[16]], [teams[6], teams[15]],
    [teams[7], teams[14]], [teams[8], teams[13]], [teams[9], teams[12]], [teams[10], teams[11]]]
    print("----------\nRound 19\n----------")
    for i in rnd19:
        print(i[0][0], i[1][0], sep="   vs   ")

    rnd20=[x[::-1] for x in rnd1]
    print("----------\nRound 20\n----------")
    for i in rnd20:
        print(i[0][0], i[1][0], sep="   vs   ")

    rnd21=[x[::-1] for x in rnd2]
    print("----------\nRound 21\n----------")
    for i in rnd21:
        print(i[0][0], i[1][0], sep="   vs   ")
    
    rnd22=[x[::-1] for x in rnd3]
    print("----------\nRound 22\n----------")
    for i in rnd22:
        print(i[0][0], i[1][0], sep="   vs   ")

    rnd23=[x[::-1] for x in rnd4]
    print("----------\nRound 23\n----------")
    for i in rnd23:
        print(i[0][0], i[1][0], sep="   vs   ")

    rnd24=[x[::-1] for x in rnd5]
    print("----------\nRound 24\n----------")
    for i in rnd24:
        print(i[0][0], i[1][0], sep="   vs   ")

    rnd25=[x[::-1] for x in rnd6]
    print("----------\nRound 25\n----------")
    for i in rnd25:
        print(i[0][0], i[1][0], sep="   vs   ")

    rnd26=[x[::-1] for x in rnd7]
    print("----------\nRound 26\n----------")
    for i in rnd26:
        print(i[0][0], i[1][0], sep="   vs   ")

    rnd27=[x[::-1] for x in rnd8]
    print("----------\nRound 27\n----------")
    for i in rnd27:
        print(i[0][0], i[1][0], sep="   vs   ")

    rnd28=[x[::-1] for x in rnd9]
    print("----------\nRound 28\n----------")
    for i in rnd28:
        print(i[0][0], i[1][0], sep="   vs   ")

    rnd29=[x[::-1] for x in rnd10]
    print("----------\nRound 29\n----------")
    for i in rnd29:
        print(i[0][0], i[1][0], sep="   vs   ")

    rnd30=[x[::-1] for x in rnd11]
    print("----------\nRound 30\n----------")
    for i in rnd30:
        print(i[0][0], i[1][0], sep="   vs   ")

    rnd31=[x[::-1] for x in rnd12]
    print("----------\nRound 31\n----------")
    for i in rnd31:
        print(i[0][0], i[1][0], sep="   vs   ")

    rnd32=[x[::-1] for x in rnd13]
    print("----------\nRound 32\n----------")
    for i in rnd32:
        print(i[0][0], i[1][0], sep="   vs   ")

    rnd33=[x[::-1] for x in rnd14]
    print("----------\nRound 33\n----------")
    for i in rnd33:
        print(i[0][0], i[1][0], sep="   vs   ")

    rnd34=[x[::-1] for x in rnd15]
    print("----------\nRound 34\n----------")
    for i in rnd34:
        print(i[0][0], i[1][0], sep="   vs   ")

    rnd35=[x[::-1] for x in rnd16]
    print("----------\nRound 35\n----------")
    for i in rnd35:
        print(i[0][0], i[1][0], sep="   vs   ")

    rnd36=[x[::-1] for x in rnd17]
    print("----------\nRound 36\n----------")
    for i in rnd36:
        print(i[0][0], i[1][0], sep="   vs   ")

    rnd37=[x[::-1] for x in rnd18]
    print("----------\nRound 37\n----------")
    for i in rnd37:
        print(i[0][0], i[1][0], sep="   vs   ")

    rnd38=[x[::-1] for x in rnd19]
    print("----------\nRound 38\n----------")
    for i in rnd38:
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

#clearing table after season etc.
def clear_table():
    for i in teams:
        i[1] = 0
        i[2] = 0
        i[3] = 0
        i[4] = 0
        i[5] = 0
        i[6] = 0
        i[7] = 0
        i[8] = 0



season_p1=2020
season_p2=2021
season=str(season_p1)+"/"+str(season_p2)


game=True
while game:
    clear_table()
    season_p1=season_p1+1
    season_p2 = season_p2 + 1
    season = str(season_p1) + "/" + str(season_p2)
    round=0
    print ("\nWelcome to",(season), "season\n")
    print ("Fixtures for this season are: ")
    fixtures()
        #print(tabulate(teams, headers=["Club", "MP", "W ", "D ", "L ", "GF", "GA", "GD", "Pts"], tablefmt="fancy_grid", numalign="center"))
    print("--------------------")

    full_or_results=input('Type "f" if you want to see whole season or "r" if you want to see just the results: ')
    while not (full_or_results == "f" or full_or_results == "r"):
        full_or_results = input('Type "f" if you want to see whole season or "r" if you want to see just the results: ')
    full_or_results=full_or_results



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
    if full_or_results=="f":
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
    if full_or_results == "f":
        print("\nTable after round", round)
        teams.sort(key=lambda team: (team[8], team[7]), reverse=True)
        print(tabulate(teams, headers=["Club", "MP", "W ", "D ", "L ", "GF", "GA", "GD", "Pts"], ))
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
    if full_or_results == "f":
        print("\nTable after round", round)
        teams.sort(key=lambda team: (team[8], team[7]), reverse=True)
        print(tabulate(teams, headers=["Club", "MP", "W ", "D ", "L ", "GF", "GA", "GD", "Pts"], ))
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
    if full_or_results == "f":
        print("\nTable after round", round)
        teams.sort(key=lambda team: (team[8], team[7]), reverse=True)
        print(tabulate(teams, headers=["Club", "MP", "W ", "D ", "L ", "GF", "GA", "GD", "Pts"], ))
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
    if full_or_results == "f":
        print("\nTable after round", round)
        teams.sort(key=lambda team: (team[8], team[7]), reverse=True)
        print(tabulate(teams, headers=["Club", "MP", "W ", "D ", "L ", "GF", "GA", "GD", "Pts"], ))
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
    if full_or_results == "f":
        print("\nTable after round", round)
        teams.sort(key=lambda team: (team[8], team[7]), reverse=True)
        print(tabulate(teams, headers=["Club", "MP", "W ", "D ", "L ", "GF", "GA", "GD", "Pts"], ))
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
    if full_or_results == "f":
        print("\nTable after round", round)
        teams.sort(key=lambda team: (team[8], team[7]), reverse=True)
        print(tabulate(teams, headers=["Club", "MP", "W ", "D ", "L ", "GF", "GA", "GD", "Pts"], ))
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
    if full_or_results == "f":
        print("\nTable after round", round)
        teams.sort(key=lambda team: (team[8], team[7]), reverse=True)
        print(tabulate(teams, headers=["Club", "MP", "W ", "D ", "L ", "GF", "GA", "GD", "Pts"], ))
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
    if full_or_results == "f":
        print("\nTable after round", round)
        teams.sort(key=lambda team: (team[8], team[7]), reverse=True)
        print(tabulate(teams, headers=["Club", "MP", "W ", "D ", "L ", "GF", "GA", "GD", "Pts"], ))
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
    if full_or_results == "f":
        print("\nTable after round", round)
        teams.sort(key=lambda team: (team[8], team[7]), reverse=True)
        print(tabulate(teams, headers=["Club", "MP", "W ", "D ", "L ", "GF", "GA", "GD", "Pts"], ))
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
    if full_or_results == "f":
        print("\nTable after round", round)
        teams.sort(key=lambda team: (team[8], team[7]), reverse=True)
        print(tabulate(teams, headers=["Club", "MP", "W ", "D ", "L ", "GF", "GA", "GD", "Pts"], ))
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
    if full_or_results == "f":
        print("\nTable after round", round)
        teams.sort(key=lambda team: (team[8], team[7]), reverse=True)
        print(tabulate(teams, headers=["Club", "MP", "W ", "D ", "L ", "GF", "GA", "GD", "Pts"], ))
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
    if full_or_results == "f":
        print("\nTable after round", round)
        teams.sort(key=lambda team: (team[8], team[7]), reverse=True)
        print(tabulate(teams, headers=["Club", "MP", "W ", "D ", "L ", "GF", "GA", "GD", "Pts"], ))
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
    if full_or_results == "f":
        print("\nTable after round", round)
        teams.sort(key=lambda team: (team[8], team[7]), reverse=True)
        print(tabulate(teams, headers=["Club", "MP", "W ", "D ", "L ", "GF", "GA", "GD", "Pts"], ))
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
    if full_or_results == "f":
        print("\nTable after round", round)
        teams.sort(key=lambda team: (team[8], team[7]), reverse=True)
        print(tabulate(teams, headers=["Club", "MP", "W ", "D ", "L ", "GF", "GA", "GD", "Pts"], ))
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
    if full_or_results == "f":
        print("\nTable after round", round)
        teams.sort(key=lambda team: (team[8], team[7]), reverse=True)
        print(tabulate(teams, headers=["Club", "MP", "W ", "D ", "L ", "GF", "GA", "GD", "Pts"], ))
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
    if full_or_results == "f":
        print("\nTable after round", round)
        teams.sort(key=lambda team: (team[8], team[7]), reverse=True)
        print(tabulate(teams, headers=["Club", "MP", "W ", "D ", "L ", "GF", "GA", "GD", "Pts"], ))
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
    if full_or_results == "f":
        print("\nTable after round", round)
        teams.sort(key=lambda team: (team[8], team[7]), reverse=True)
        print(tabulate(teams, headers=["Club", "MP", "W ", "D ", "L ", "GF", "GA", "GD", "Pts"], ))
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
    if full_or_results == "f":
        print("\nTable after round", round)
        teams.sort(key=lambda team: (team[8], team[7]), reverse=True)
        print(tabulate(teams, headers=["Club", "MP", "W ", "D ", "L ", "GF", "GA", "GD", "Pts"], ))
        input("Hit enter to start next round")
        print("--------------------")

    # round 20
    round = round + 1
    print("\nRound", round, "of 38")
    print("Results of round", round, "are: ")
    for i in rnd20:
        score1 = (random.choice(score))
        score2 = (random.choice(score))
        mp()
        wld_pts()
        gf_ga_gd()
        print(i[0][0], i[1][0], sep="   vs   ")
        print(score1, ":", score2)
    if full_or_results == "f":
        print("\nTable after round", round)
        teams.sort(key=lambda team: (team[8], team[7]), reverse=True)
        print(tabulate(teams, headers=["Club", "MP", "W ", "D ", "L ", "GF", "GA", "GD", "Pts"], ))
        input("Hit enter to start next round")
        print("--------------------")

    # round 21
    round = round + 1
    print("\nRound", round, "of 38")
    print("Results of round", round, "are: ")
    for i in rnd21:
        score1 = (random.choice(score))
        score2 = (random.choice(score))
        mp()
        wld_pts()
        gf_ga_gd()
        print(i[0][0], i[1][0], sep="   vs   ")
        print(score1, ":", score2)
    if full_or_results == "f":
        print("\nTable after round", round)
        teams.sort(key=lambda team: (team[8], team[7]), reverse=True)
        print(tabulate(teams, headers=["Club", "MP", "W ", "D ", "L ", "GF", "GA", "GD", "Pts"], ))
        input("Hit enter to start next round")
        print("--------------------")

    # round 22
    round = round + 1
    print("\nRound", round, "of 38")
    print("Results of round", round, "are: ")
    for i in rnd22:
        score1 = (random.choice(score))
        score2 = (random.choice(score))
        mp()
        wld_pts()
        gf_ga_gd()
        print(i[0][0], i[1][0], sep="   vs   ")
        print(score1, ":", score2)
    if full_or_results == "f":
        print("\nTable after round", round)
        teams.sort(key=lambda team: (team[8], team[7]), reverse=True)
        print(tabulate(teams, headers=["Club", "MP", "W ", "D ", "L ", "GF", "GA", "GD", "Pts"], ))
        input("Hit enter to start next round")
        print("--------------------")

    # round 23
    round = round + 1
    print("\nRound", round, "of 38")
    print("Results of round", round, "are: ")
    for i in rnd23:
        score1 = (random.choice(score))
        score2 = (random.choice(score))
        mp()
        wld_pts()
        gf_ga_gd()
        print(i[0][0], i[1][0], sep="   vs   ")
        print(score1, ":", score2)
    if full_or_results == "f":
        print("\nTable after round", round)
        teams.sort(key=lambda team: (team[8], team[7]), reverse=True)
        print(tabulate(teams, headers=["Club", "MP", "W ", "D ", "L ", "GF", "GA", "GD", "Pts"], ))
        input("Hit enter to start next round")
        print("--------------------")

    # round 24
    round = round + 1
    print("\nRound", round, "of 38")
    print("Results of round", round, "are: ")
    for i in rnd24:
        score1 = (random.choice(score))
        score2 = (random.choice(score))
        mp()
        wld_pts()
        gf_ga_gd()
        print(i[0][0], i[1][0], sep="   vs   ")
        print(score1, ":", score2)
    if full_or_results == "f":
        print("\nTable after round", round)
        teams.sort(key=lambda team: (team[8], team[7]), reverse=True)
        print(tabulate(teams, headers=["Club", "MP", "W ", "D ", "L ", "GF", "GA", "GD", "Pts"], ))
        input("Hit enter to start next round")
        print("--------------------")

    # round 25
    round = round + 1
    print("\nRound", round, "of 38")
    print("Results of round", round, "are: ")
    for i in rnd25:
        score1 = (random.choice(score))
        score2 = (random.choice(score))
        mp()
        wld_pts()
        gf_ga_gd()
        print(i[0][0], i[1][0], sep="   vs   ")
        print(score1, ":", score2)
    if full_or_results == "f":
        print("\nTable after round", round)
        teams.sort(key=lambda team: (team[8], team[7]), reverse=True)
        print(tabulate(teams, headers=["Club", "MP", "W ", "D ", "L ", "GF", "GA", "GD", "Pts"], ))
        input("Hit enter to start next round")
        print("--------------------")

    # round 26
    round = round + 1
    print("\nRound", round, "of 38")
    print("Results of round", round, "are: ")
    for i in rnd26:
        score1 = (random.choice(score))
        score2 = (random.choice(score))
        mp()
        wld_pts()
        gf_ga_gd()
        print(i[0][0], i[1][0], sep="   vs   ")
        print(score1, ":", score2)
    if full_or_results == "f":
        print("\nTable after round", round)
        teams.sort(key=lambda team: (team[8], team[7]), reverse=True)
        print(tabulate(teams, headers=["Club", "MP", "W ", "D ", "L ", "GF", "GA", "GD", "Pts"], ))
        input("Hit enter to start next round")
        print("--------------------")

    # round 27
    round = round + 1
    print("\nRound", round, "of 38")
    print("Results of round", round, "are: ")
    for i in rnd27:
        score1 = (random.choice(score))
        score2 = (random.choice(score))
        mp()
        wld_pts()
        gf_ga_gd()
        print(i[0][0], i[1][0], sep="   vs   ")
        print(score1, ":", score2)
    if full_or_results == "f":
        print("\nTable after round", round)
        teams.sort(key=lambda team: (team[8], team[7]), reverse=True)
        print(tabulate(teams, headers=["Club", "MP", "W ", "D ", "L ", "GF", "GA", "GD", "Pts"], ))
        input("Hit enter to start next round")
        print("--------------------")

    # round 28
    round = round + 1
    print("\nRound", round, "of 38")
    print("Results of round", round, "are: ")
    for i in rnd28:
        score1 = (random.choice(score))
        score2 = (random.choice(score))
        mp()
        wld_pts()
        gf_ga_gd()
        print(i[0][0], i[1][0], sep="   vs   ")
        print(score1, ":", score2)
    if full_or_results == "f":
        print("\nTable after round", round)
        teams.sort(key=lambda team: (team[8], team[7]), reverse=True)
        print(tabulate(teams, headers=["Club", "MP", "W ", "D ", "L ", "GF", "GA", "GD", "Pts"], ))
        input("Hit enter to start next round")
        print("--------------------")

    # round 29
    round = round + 1
    print("\nRound", round, "of 38")
    print("Results of round", round, "are: ")
    for i in rnd29:
        score1 = (random.choice(score))
        score2 = (random.choice(score))
        mp()
        wld_pts()
        gf_ga_gd()
        print(i[0][0], i[1][0], sep="   vs   ")
        print(score1, ":", score2)
    if full_or_results == "f":
        print("\nTable after round", round)
        teams.sort(key=lambda team: (team[8], team[7]), reverse=True)
        print(tabulate(teams, headers=["Club", "MP", "W ", "D ", "L ", "GF", "GA", "GD", "Pts"], ))
        input("Hit enter to start next round")
        print("--------------------")

    # round 30
    round = round + 1
    print("\nRound", round, "of 38")
    print("Results of round", round, "are: ")
    for i in rnd30:
        score1 = (random.choice(score))
        score2 = (random.choice(score))
        mp()
        wld_pts()
        gf_ga_gd()
        print(i[0][0], i[1][0], sep="   vs   ")
        print(score1, ":", score2)
    if full_or_results == "f":
        print("\nTable after round", round)
        teams.sort(key=lambda team: (team[8], team[7]), reverse=True)
        print(tabulate(teams, headers=["Club", "MP", "W ", "D ", "L ", "GF", "GA", "GD", "Pts"], ))
        input("Hit enter to start next round")
        print("--------------------")

    # round 31
    round = round + 1
    print("\nRound", round, "of 38")
    print("Results of round", round, "are: ")
    for i in rnd31:
        score1 = (random.choice(score))
        score2 = (random.choice(score))
        mp()
        wld_pts()
        gf_ga_gd()
        print(i[0][0], i[1][0], sep="   vs   ")
        print(score1, ":", score2)
    if full_or_results == "f":
        print("\nTable after round", round)
        teams.sort(key=lambda team: (team[8], team[7]), reverse=True)
        print(tabulate(teams, headers=["Club", "MP", "W ", "D ", "L ", "GF", "GA", "GD", "Pts"], ))
        input("Hit enter to start next round")
        print("--------------------")

    # round 32
    round = round + 1
    print("\nRound", round, "of 38")
    print("Results of round", round, "are: ")
    for i in rnd32:
        score1 = (random.choice(score))
        score2 = (random.choice(score))
        mp()
        wld_pts()
        gf_ga_gd()
        print(i[0][0], i[1][0], sep="   vs   ")
        print(score1, ":", score2)
    if full_or_results == "f":
        print("\nTable after round", round)
        teams.sort(key=lambda team: (team[8], team[7]), reverse=True)
        print(tabulate(teams, headers=["Club", "MP", "W ", "D ", "L ", "GF", "GA", "GD", "Pts"], ))
        input("Hit enter to start next round")
        print("--------------------")

    # round 33
    round = round + 1
    print("\nRound", round, "of 38")
    print("Results of round", round, "are: ")
    for i in rnd33:
        score1 = (random.choice(score))
        score2 = (random.choice(score))
        mp()
        wld_pts()
        gf_ga_gd()
        print(i[0][0], i[1][0], sep="   vs   ")
        print(score1, ":", score2)
    if full_or_results == "f":
        print("\nTable after round", round)
        teams.sort(key=lambda team: (team[8], team[7]), reverse=True)
        print(tabulate(teams, headers=["Club", "MP", "W ", "D ", "L ", "GF", "GA", "GD", "Pts"], ))
        input("Hit enter to start next round")
        print("--------------------")

    # round 34
    round = round + 1
    print("\nRound", round, "of 38")
    print("Results of round", round, "are: ")
    for i in rnd34:
        score1 = (random.choice(score))
        score2 = (random.choice(score))
        mp()
        wld_pts()
        gf_ga_gd()
        print(i[0][0], i[1][0], sep="   vs   ")
        print(score1, ":", score2)
    if full_or_results == "f":
        print("\nTable after round", round)
        teams.sort(key=lambda team: (team[8], team[7]), reverse=True)
        print(tabulate(teams, headers=["Club", "MP", "W ", "D ", "L ", "GF", "GA", "GD", "Pts"], ))
        input("Hit enter to start next round")
        print("--------------------")

    # round 35
    round = round + 1
    print("\nRound", round, "of 38")
    print("Results of round", round, "are: ")
    for i in rnd35:
        score1 = (random.choice(score))
        score2 = (random.choice(score))
        mp()
        wld_pts()
        gf_ga_gd()
        print(i[0][0], i[1][0], sep="   vs   ")
        print(score1, ":", score2)
    if full_or_results == "f":
        print("\nTable after round", round)
        teams.sort(key=lambda team: (team[8], team[7]), reverse=True)
        print(tabulate(teams, headers=["Club", "MP", "W ", "D ", "L ", "GF", "GA", "GD", "Pts"], ))
        input("Hit enter to start next round")
        print("--------------------")

    # round 36
    round = round + 1
    print("\nRound", round, "of 38")
    print("Results of round", round, "are: ")
    for i in rnd36:
        score1 = (random.choice(score))
        score2 = (random.choice(score))
        mp()
        wld_pts()
        gf_ga_gd()
        print(i[0][0], i[1][0], sep="   vs   ")
        print(score1, ":", score2)
    if full_or_results == "f":
        print("\nTable after round", round)
        teams.sort(key=lambda team: (team[8], team[7]), reverse=True)
        print(tabulate(teams, headers=["Club", "MP", "W ", "D ", "L ", "GF", "GA", "GD", "Pts"], ))
        input("Hit enter to start next round")
        print("--------------------")

    # round 37
    round = round + 1
    print("\nRound", round, "of 38")
    print("Results of round", round, "are: ")
    for i in rnd37:
        score1 = (random.choice(score))
        score2 = (random.choice(score))
        mp()
        wld_pts()
        gf_ga_gd()
        print(i[0][0], i[1][0], sep="   vs   ")
        print(score1, ":", score2)
    if full_or_results == "f":
        print("\nTable after round", round)
        teams.sort(key=lambda team: (team[8], team[7]), reverse=True)
        print(tabulate(teams, headers=["Club", "MP", "W ", "D ", "L ", "GF", "GA", "GD", "Pts"], ))
        input("Hit enter to start next round")
        print("--------------------")

    # round 38
    round = round + 1
    print("\nRound", round, "of 38")
    print("Results of round", round, "are: ")
    for i in rnd38:
        score1 = (random.choice(score))
        score2 = (random.choice(score))
        mp()
        wld_pts()
        gf_ga_gd()
        print(i[0][0], i[1][0], sep="   vs   ")
        print(score1, ":", score2)
    if full_or_results == "f":
        print("\nTable after round", round)
        teams.sort(key=lambda team: (team[8], team[7]), reverse=True)
        print(tabulate(teams, headers=["Club", "MP", "W ", "D ", "L ", "GF", "GA", "GD", "Pts"], ))
        input("Hit enter to end season")
        
    
    promoted1= random.choice(championship)
    championship.remove(promoted1)
    promoted2= random.choice(championship)
    championship.remove(promoted2)
    promoted3= random.choice(championship)
    championship.remove(promoted3)

    #winner on end of the season
    print("\n--------------------")
    print ("Winner of the season", season," is: ",(teams[0][0]))
    print ("Relegated teams: ", teams[17][0],", ", teams[18][0],", ", teams[19][0])
    print ("Promoted teams: ", promoted1[0], ", ", promoted2[0], ", ", promoted3[0],)
    print("\n--------------------")
    if full_or_results=="r":
        print(tabulate(teams, headers=["Club", "MP", "W ", "D ", "L ", "GF", "GA", "GD", "Pts"], ))

    relegated1=teams.pop(19)
    championship.append(relegated1)
    relegated2=teams.pop(18)
    championship.append(relegated2)
    relegated3=teams.pop(17)
    championship.append(relegated3)
    teams.append(promoted1)
    teams.append(promoted2)
    teams.append(promoted3)

  
    again=input("Would you like to see next season? y/n: ")
    if again=="y" or again=="Y":
        game=True
    else:
        game=False





