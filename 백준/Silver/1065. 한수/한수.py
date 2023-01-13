"""
어떤 양의 정수 X의 각 자리가 등차수열을 이룬다면, 그 수를 한수라고 한다. 
등차수열은 연속된 두 개의 수의 차이가 일정한 수열을 말한다. 
N이 주어졌을 때, 1보다 크거나 같고, N보다 작거나 같은 한수의 개수를 출력하는 프로그램을 작성하시오. 
"""

def hansu(n):
    if n < 100:
        return True
    
    num = str(n)
    
    differ = int(num[0])-int(num[1])
    j = int(num[0])
    
    for i in num[1:] :
        realDiffer = int(j)-int(i)
        
        if realDiffer == differ :
            j = i
        else:
            return False
    
    return True


N = int(input())
count = 0

for i in range(N):
    if hansu(i+1) :
        count += 1
    
print(count)
        
