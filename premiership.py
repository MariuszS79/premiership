from tabulate import tabulate

headers=["Club", "MP", "W", "D", "L", "GF", "GA", "GD", "Pts"]
arsenal=["Arsenal", 0, 0, 0, 0, 0, 0, 0, 0]
aston_villa=["Aston Villa", 0, 0, 0, 0, 0, 0, 0, 0]
brentford=["Brentford", 0, 0, 0, 0, 0, 0, 0, 0]
brighton=["Brighton", 0, 0, 0, 0, 0, 0, 0, 0]
burnley=["Burnley", 0, 0, 0, 0, 0, 0, 0, 0]

print(tabulate([arsenal, aston_villa, brentford, brighton, burnley], headers=["Club", "MP", "W", "D", "L", "GF", "GA", "GD", "Pts"], tablefmt='orgtbl'))