def solution(book_time):
    for i in range(len(book_time)):
        start, end = book_time[i]
        book_time[i][0] = int(start.split(":")[0])*60+int(start.split(":")[1])
        book_time[i][1] = int(end.split(":")[0])*60+int(end.split(":")[1])
    
    book_time.sort(key = lambda x : (x[0], x[1]))
    hotel = []
    for i in range(len(book_time)):
        start, end = book_time[i]
        flag = 0
        if hotel:
            for k in range(len(hotel)):
                if hotel[k][1]+10 <= start:
                    hotel[k][0], hotel[k][1] = start, end
                    flag = 1
                    break
        if flag == 0:  
            hotel.append([start, end])
            
        hotel.sort(key = lambda x : (x[1]))
        
    answer = len(hotel)
    return answer

# 필요한 최소 객실 수 