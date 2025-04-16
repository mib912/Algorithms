def solution(s):
    answer = []
    sentence = s.split(' ')
    
    for word in sentence:
        if word:
            answer.append(word[0].upper() + word[1:].lower())
        else:
            answer.append(word)
    return " ".join(answer)