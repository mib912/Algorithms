def solution(people, limit):
    answer = 0
    people.sort()
    start = 0
    end = len(people)-1
    
    while start <= end:
        weight = people[start] + people[end]
        if weight <= limit:
            start += 1
            end -= 1
            answer += 1
        else:
            end -= 1
            answer += 1
    return answer