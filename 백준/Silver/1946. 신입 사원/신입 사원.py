import sys

cnt = int(sys.stdin.readline())

for _ in range(cnt) :
    num = int(sys.stdin.readline())
    people = []
    for i in range(num) :
        people.append(list(map(int, sys.stdin.readline().split())))

    people.sort(key = lambda x:x[0])
    # max_a = people[0][0]
    min_b = people[0][1]
    people_pass = 1
    for person in people[1:] :
        if min_b > person[1] :
            min_b = person[1]
            people_pass += 1

    print(people_pass)