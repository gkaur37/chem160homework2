from random import choices
ntrials = 10000
player1wins = 0
for i in range(ntrials):
    num_dice1 = 2
    num_dice2 = 3
    dice1 = choices(range(1, 7), k= num_dice1)
    if dice1[0] == dice1[1]:
        player1wins += 1
        continue

    dice2 = choices(range(1, 7), k= num_dice2)
    dice2.sort(reverse=True)

    if dice2.count(2) == 2:
        player1wins += 1
        continue

    sum1 = dice1[0]+dice1[1]
    sum2 = dice2[0]+dice2[1]
    if sum1 >= sum2:
        player1wins +=1
    avg_rolls = (1 - player1wins/ ntrials)
print(avg_rolls)