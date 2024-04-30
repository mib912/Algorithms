import sys

input = sys.stdin.readline

n = int(input())

types = set()  # 입력 받은 용량 집합
typesArr = []
answer = 0

for _ in range(n):
    b = int(input())
    types.add(b)
    typesArr.append(b)

if len(types) == 1:
    print(len(typesArr))
else:
    for i in types:
        tmpArr = typesArr[:]  # 단순히 typesArr로 초기화 하면 처음 상태로 초기화 할 수 없음
        result = 1
        while i in tmpArr:
            tmpArr.remove(i)  # remove는 앞에 하나 만난 것만 지워주기 때문에 while문 사용

        for j in range(1, len(tmpArr)):
            if tmpArr[j-1] == tmpArr[j]:
                result += 1
            else:
                answer = max(answer, result)
                result = 1
        answer = max(answer, result)
print(answer)
