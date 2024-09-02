def solution(s):
    answer = ""
    s = s.lower()

    for word in s:
        if answer == "": # 완전 첫단어 
            if word.isalpha():
                answer += word.upper()
            else:
                answer += word.upper()
            continue
        if word == " " and answer[-1] != " ": # 공백 추가 
            answer += " "
            continue
        if answer[-1] == " ": #첫단어 
            if word.isalpha():
                answer += word.upper()
                continue
        answer += word
        
    return answer