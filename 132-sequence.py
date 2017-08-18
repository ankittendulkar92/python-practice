
# coding: utf-8

# In[2]:

def seq_find(a):
    found=False
    small=float('Inf')
    large=-float('Inf')
    medium=0
    for i in a:
        if i<small:
            small=i
        elif i>large:
            large=i
        else:
            found=True
            break
    return found

li=[1,2,3,5,4,6,7]

seq_find(li)
        
    

