
def find132pattern(self, nums):
        a=nums
        found=False
        small=float('Inf')
        large=-float('Inf')
        global n
        for i in range(len(a)-1):
            n=i
            if a[i]<small:
                small=a[i]
            elif a[i]>large:
                large=a[i]
            if small<large:
                
                break
        s=[-float('Inf')]
        
        for j in range(n+1,len(a)-1):
            if a[j]<large and a[j]>small:
                found=True
                break
            elif a[j]<s[-1]:
                s.pop
                s.append(a[j])
            else:
                small=s.pop
                large=a[j]
        
        return found

