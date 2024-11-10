import sys
number = int(sys.argv[1])

# 1부터 number까지 나누어떨어지는 수를 찾음
for i in range(1, number + 1):  # 1부터 number까지 반복
    if number % i == 0:  # 나누어떨어지는 수일 때
        print(i, end=" ")
print()  # 출력 끝내기
