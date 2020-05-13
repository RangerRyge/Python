import math

#opgave 1

names = list(["Preben", "Brian", "Dennis", "Christian", "Therese"])
new_list = [  item for item in names if item[0]=="H" ]
new_list

#opgave 2

[ item**3 for item in range(1,101) ]

#opgave 3

names = list(["Preben", "Brian", "Dennis", "Christian", "Therese"])
[ (len(item), item) for item in names ]

#opgave 4

str = "djfhk3sdjksh2"
for x in str:
    if x.isdigit():
        print(x)

#opgave 5

set([dice1+dice2 for dice1 in range(1,7) for dice2 in range(1,7)])

#opgave 6

names = list(["Preben", "Brian", "Dennis", "Christian", "Therese"])
dict_list = {el:len(el) for el in names}
print(dict_list)

#opgave 7

number_list = list([9, 16, 25])
dict_list = {el:el**0.5 for el in number_list}
print(dict_list)

#opgave 8

dice1 = list(range(1,7))
dice2 = list(range(1,7))

diceDict = {x:0 for x in range(2,13)} # Making dictionary 

for x in dice1: ## Adding throws that can have sum
    for y in dice2:
        diceDict[x+y] += 1
print(diceDict)

for x in diceDict: ## Calculates the probability
     diceDict[x] = (round(diceDict.get(x)/36*100,2)) + "%"

print(diceDict)