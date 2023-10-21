def make_end_time(t) :
    t = t+10
    
    if t%100 >= 60 :
        t += 100
        t -= 60
    
    return t

def solution(book_time):
    answer = 0

    start_time = []
    end_time = []
    
    book_time = [[int(''.join(t1.split(':'))), int(''.join(t2.split(':')))] for t1,t2 in book_time]
    book_time.sort(key = lambda x:(x[0], x[1]))

    room_list = []

    for start, end in book_time :
        end = make_end_time(end)
        
        room_list.append(end)

        for room in room_list :
            if room <= start :
                room_list.remove(room)

        answer = max(answer, len(room_list))
        
    if answer == 0 :
        return 1
    else :
        return answer