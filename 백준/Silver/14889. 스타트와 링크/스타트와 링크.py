from itertools import combinations, permutations

N = int(input())

s = []
for _ in range(N) :
    s.append(list(map(int, input().split())))

team = list(range(N))
power_list = []
for team1 in list(combinations(team, N//2)) :

    power_1, power_2 = 0, 0
    team2 = tuple(set(team)-set(team1))

    for team1_, team2_ in zip(permutations(team1, 2), permutations(team2, 2)) :
        power_1 += s[team1_[0]][team1_[1]]
        power_2 += s[team2_[0]][team2_[1]]

    power = abs(power_1 - power_2)
    power_list.append(power)
        
print(min(power_list))