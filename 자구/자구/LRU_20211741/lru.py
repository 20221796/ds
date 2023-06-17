from circularDoublyLinkedList import *

def do_sim(cache_slots):

    cache_hit = 0
    tot_cnt = 0

    data_file = open("linkbench_short.trc")
    list1 = CircularDoublyLinkedList()

    for line in data_file.readlines():
        lpn = line.split()[0]

        if lpn in list1:
            list1.pop(lpn)
            cache_hit += 1
            list1.insert(0, lpn)

            if list1.size() > cache_slots:
                list1.pop()
            
        tot_cnt += 1

    print("cache_slot = ", cache_slots, "cache_hit = ", cache_hit, "hit ratio = ", cache_hit / tot_cnt)

if __name__ == "__main__":

    for cache_slots in range(100, 1000, 100):
        do_sim(cache_slots)