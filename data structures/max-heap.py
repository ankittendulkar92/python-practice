class max_heap:
	def__init__(self):
		self.heaplist[0]=0
		self.currentsize=1

	def percup(self,i):
		while i//2>0:
			if self.heaplist[i]>self.heaplist[i//2]:
				temp=self.heaplist[i//2]
				self.heaplist[i//2]=self.heaplist[i]
				self.heaplist[i]=temp
			i=i//2

	def insert(self,val):
		self.heaplist.append(val)
		self.currentsize+=1
		percup(self.currentsize)

	def max_child(self,i):
		if i*2+1>self.currentsize:
			return i*2
		if self.heaplist[i*2]>self.heaplist[i*2+1]:
			return i*2
		else:
			return i*2+1

	def percdn(self,i):
		while i*2+1<=self.currentsize:
			mc=max_child(i)
			if self.heaplist[i]<self.heaplist[mc]:
				temp=self.heaplist[i]
				self.heaplist[i]=self.heaplist[mc]
				self.heaplist[mc]=temp
			i=mc

	def del_max(self):
		retval=self.heaplist[1]
		self.heaplist[1]=self.heaplist[self.currentsize]
		self.currentsize-=1
		self.heaplist.pop()
		self.percdn(1)
		return retval
	def build_heap(self,a):
		self.heaplist=[0]+a
		self.currentsize=len(a)
		i=currentsize//2
		while i>0:
			percdn(i)
			i=i-1

