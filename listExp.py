games = ["Football","Cricket","baseball","Hockey"]
name ="jack"

mixedList=[1,10.5,"hi",True,[1,2,'Hello',[50,100]]]

# print(games)
# print(type(games))

# print(games[0])

# print(name[0])

# print(games[0:4])
# print(games[-2])


# print(mixedList)
# print(type(mixedList))
# print(type(mixedList[-1]))

# print(mixedList[-1][-1][1])

# games.append("Tenis")
# games.insert(0,"Tenis")
# games.extend(mixedList)

# games[1]="Socer"


# del games[0]

# games.pop(0)
# games.remove("Socer")
# del games
print(len(games))

for game in games:
    print(game.upper())

list_one = [15, 61, 23, 6, 87, 5, 93]  

sum=0

for i in list_one:
    sum+=i


print(sum)