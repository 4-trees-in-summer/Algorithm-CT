from itertools import permutations

cnt = int(input())
numbers = list(map(int, input().split()))
oper_num = list(map(int, input().split()))
oper_ = ['+', '-', '*', '/']

oper = []
for idx, num in enumerate(oper_num) :
    for _ in range(num) : 
        oper.append(oper_[idx])

permu_oper = list(set(permutations(oper, len(oper))))

# print(permu_oper)
answer_list = []
for oper in permu_oper :
    answer = ''
    oper = list(oper)

    for idx, num in enumerate(numbers) :
        if idx == 0 :
            answer = str(num)
            continue

        answer = str(answer)
        answer += oper[idx-1]
        answer += str(num)
        answer = int(eval(answer))

    answer_list.append(answer)

print(max(answer_list))
print(min(answer_list))