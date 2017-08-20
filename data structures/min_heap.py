lass min_heap:
	def__init__(self):
		self.heaplist[0]=[0]
		self.currentsize=0

	def percup(self,i):
		while i//2>0:
			if self.heaplist[i]<self.heaplist[i//2]:
				temp=self.heaplist[i//2]
				self.heaplist[i//2]=self.heaplist[i]
				self.heaplist[i]=temp
				
			i=i//2


	def insert(self,val):
		self.heaplist.append(val)
		self.currentsize+=1
		percup(self.currentsize)

	def min_child(self,i):
		if self.heaplist[i*2]>self.heaplist[i*2+1]:
			minchild=i*2
		else:
			minchild=i*2+1
		return minchild

	def perdn(sefl,i):
		while i*2+1<=self.currentsize:
			mc=self.minchild(i)
			if self.heaplist[i]>self.heaplist[mc]:
				temp=self.heaplist[i]
				self.heaplist[i]=self.heaplist[mc]
				self.heaplist[mc]=temp
			i=mc

	def min_delete(self,i):
		retval=self.heaplist[1]
		self.heaplist[1]=self.heaplist[self.currentsize]
		self.currentsize-=1
		self.heaplist.pop()
		percdn(1)
		return retval

	def build_heap(self,a):
		self.heaplist=[0]+a
		self.currentsize=len(a)
		i=currentsize//2
		while i>0:
			percdn(i)
			i=i-1

