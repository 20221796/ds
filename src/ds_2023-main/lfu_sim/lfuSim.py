from Heap import *

def lfu_sim(cache_slots):
  cache_hit = 0
  tot_cnt = 0

  data_file = open("src\ds_2023-main\lfu_sim\linkbench.trc")
  memory = {}
  cache = Heap()

  for line in data_file.readlines():
    lpn = line.split()[0]

    # Program here 
    if lpn in memory: memory[lpn] += 1
    else: memory[lpn] = 1
    
    frequency = memory[lpn]
    
    if cache.insert(lpn, frequency): cache_hit += 1 #cache.insert()는 ishitted를 리턴
    elif cache.size() > cache_slots: cache.deleteMin() #캐쉬가 가득차면 freqency가 최소인 노드를 삭제
    
    tot_cnt +=1
    
  print("cache_slot = ", cache_slots, "cache_hit = ", cache_hit, "hit ratio = ", cache_hit / tot_cnt)

if __name__ == "__main__":
  for cache_slots in range(100, 1000, 100):
    lfu_sim(cache_slots)