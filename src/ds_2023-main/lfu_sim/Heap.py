class Heap:
	def __init__(self, *args):
		if len(args) != 0:
			self.__A = args[0]
		else:
			self.__A = []
		
	def insert(self, lpn, frequency):		
		lpn_list = [node[0] for node in self.__A] #lpn 값만 리스트로 받아오기
		is_hitted = False

		if lpn not in lpn_list:
			self.__A.append([lpn,frequency])
			is_hitted = False
		else:
			lpn_index = lpn_list.index(lpn)
			self.__A[lpn_index][1] += 1
			frequency = self.__A[lpn_index][1]
			is_hitted = True

		self.__percolateUp(len(self.__A)-1)
		
		return is_hitted

	def __percolateUp(self, i:int):
		parent = (i - 1) // 2
		if i > 0 and self.__A[i][1] < self.__A[parent][1]: #frequency를 기준으로 동작하도록 변경
			self.__A[i], self.__A[parent] = self.__A[parent], self.__A[i]
			self.__percolateUp(parent)

	def deleteMin(self):
		# heap is in self.__A[0...len(self.__A)-1]
		if (not self.isEmpty()):
			min = self.__A[0]
			self.__A[0] = self.__A.pop()
			self.__percolateDown(0)
			return min
		else:
			return None

	def __percolateDown(self, i:int):
		# Percolate down w/ self.__A[i] as the root
		child = 2 * i + 1
		right = 2 * i + 2  # right child
		if (child <= len(self.__A)-1):
			if (right <= len(self.__A)-1 and self.__A[child][1] >= self.__A[right][1]):
				child = right  # index of smaller child
			if self.__A[i][1] >= self.__A[child][1]:
				self.__A[i], self.__A[child] = self.__A[child], self.__A[i]
				self.__percolateDown(child)

	def isHitted(self):
		return self.is_hitted

	def min(self):
		return self.__A[0]
	
	def isEmpty(self) -> bool:
		return len(self.__A) == 0

	def clear(self):
		self.__A = []

	def size(self) -> int:
		return len(self.__A)
	
	def heapPrint(self):
		if self.isEmpty(): return

		print("=" *20)
		row = 0
		cnt = 0
		for i in self.__A:
			print(i, end = ' ')
			cnt+=1
			
			if (cnt >= 2**row):
				row += 1
				cnt = 0
				print()
		print()