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

random_teams=random.shuffle(teams)

#print(random_teams)
for i in teams:
    print (i[0])


print((random.choice(score)),":",(random.choice(score)))

round=0

season_p1=2021
season_p2=2022
season=str(season_p1)+"/"+str(season_p2)



game=True
while game:
    round=round+1
    print ("Welcome to",(season), "season")
    for i in range(37):
        round = round + 1

        print ("Round",round,"of 38")
        print(tabulate(teams, headers=["Club", "MP", "W ", "D ", "L ", "GF", "GA", "GD", "Pts"], tablefmt="fancy_grid", numalign="center"))
        print("Results of round",round,"are: ")
        print("--------------------")
    game=False
