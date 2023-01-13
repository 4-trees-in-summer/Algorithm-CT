"""
시험 점수를 입력받아
90 ~ 100점은 A, 
80 ~ 89점은 B, 
70 ~ 79점은 C, 
60 ~ 69점은 D, 
나머지 점수는 F를 출력하는 프로그램을 작성하시오.
"""

exam = int(input())

if 90 <= exam <= 100:
    print("A")
elif 80 <= exam <= 89:
    print("B")
elif 70 <= exam <= 79:
    print("C")
elif 60 <= exam <= 69:
    print("D")
else :
    print("F")