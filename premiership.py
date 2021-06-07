from tabulate import tabulate

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

print(tabulate([arsenal, aston_villa, brentford, brighton, burnley], headers=["Club", "MP", "W", "D", "L", "GF", "GA", "GD", "Pts"], tablefmt='orgtbl'))