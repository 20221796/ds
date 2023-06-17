from circularDoublyLinkedList import CircularDoublyLinkedList

def do_sim(cache_slots):

    cache_hit = 0
    tot_cnt = 0

    cache = CircularDoublyLinkedList() #양방향 연결리스트 이용

    data_file = open("linkbench_short.trc") #절대주소를 이용해 파일을 불러옴

    for line in data_file.readlines():
        lpn = line.split()[0]
        
        if cache.count(lpn) == 0: #<miss> - 새로 넣으려는 값이 없는 기존에 경우
            if (cache.size() == cache_slots): #cash slots이 가득찬 경우
                cache.pop(0) #가장 예전에 호출된 값을 삭제
    
        else: #<hit> - 값이 있는 경우
            cache.remove(lpn) #기존에 있는 값을 삭제함
            cache_hit += 1
        
        cache.append(lpn) #받은 값을 넣어줌

        tot_cnt += 1
                
 

    print("cache_slot = ", cache_slots, "cache_hit = ", cache_hit, "hit ratio = ", cache_hit / tot_cnt)

if __name__ == "__main__":

    for cache_slots in range(100, 1000, 100):
        do_sim(cache_slots)
