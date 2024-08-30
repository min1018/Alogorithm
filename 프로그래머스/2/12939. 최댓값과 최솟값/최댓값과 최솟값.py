def solution(s):
    min_num = float("inf")
    max_num = float("-inf")
    for num in s.split(" "):
        if min_num > int(num):
            min_num = int(num)
        if max_num < int(num):
            max_num = int(num)
    answer = str(min_num) + " " + str(max_num)
    return answer