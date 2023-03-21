#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#data structure - STACK
#data structure definition-- 1)structured data(name,etc..) 2)un-stuctured data(images,audio,video,etc..)
# 2 types of data structure: 1)linear 2)non linear
#structured data in linear ds,unsrtucted data in non linear ds
#stack principle: Last in First out (LIFO)


# In[11]:


#tradtional implementation of stack
class Stack:
    arr=[]
    size=5
    def stack_push(self,element):
        if len(self.arr)<self.size:
            self.arr.append(element)
        else:
            print("STACK IS FULL")
    def stack_pop(self):
        if len(self.arr)>0:
            self.arr.pop()
        else:
            print("STACK IS EMPTY")
    def stack_peek(self):
        if len(self.arr)==0:
            return "stack is empty"
        return self.arr[-1]
    def isEmpty(self):
        if len(self.arr)==0:
            return True
        else:
            return False
s=Stack()
s.stack_push(10)
s.stack_push(20)
s.stack_push(30)
s.stack_push(40)
print(s.arr)
s.stack_peek()
s.stack_push(50)
print(s.arr)
s.stack_push(60)
print(s.arr)
s.stack_pop()
s.stack_pop()
s.stack_pop()
s.stack_pop()
print(s.arr)
s.stack_pop()
print(s.arr)
s.stack_pop()
print(s.arr)


# In[ ]:


#frequency,contains addtitional functions
#reversing the stack


# In[19]:


class stack:
       arr=[1,2,3,4,5]
       arr1=[]
       def stack_push(self,element):
           self.arr.append(element)
  
       def stack_pop(self):
   
           self.arr.pop()
 
       def stack_peek(self):
           if len(self.arr)==0:
               return "stack is empty"
           return self.arr[-1]
       def isEmpty(self):
           if len(self.arr)==0:
               return True
           else:
               return False

"""            
s=stack()
print(s.arr)
for i in range(len(s.arr)):
   print(s.arr[0],end=" ")
   s.arr.pop(0)
"""
#to reverse the stack we need 2 stacks


# In[40]:


class stack:
        arr=[]
        def stack_push(self,element):
            self.arr.append(element)
   
        def stack_pop(self):
    
            self.arr.pop()
  
        def stack_peek(self):
            if len(self.arr)==0:
                return "stack is empty"
            return self.arr[-1]
        def isEmpty(self):
            if len(self.arr)==0:
                return True
            else:
                return False
        def printstack(self):
            print(self.arr)
s1=stack()
s2=stack()
s1.stack_push(10)
s1.stack_push(20)
s1.stack_push(30)
s1.stack_push(40)
s2.stack_push(s1.stack_pop()) 
s2.printstack()


# In[44]:


#queue is double ended data structure
class Queue:
    arr=[]
    size=5
    def enqueue(self,element):
        if len(self.arr)<self.size:
            self.arr.append(element)
        else:
            print("STACK IS FULL")
    def dequeue(self):
        if len(self.arr)>0:
            self.arr.pop(0)
        else:
            print("STACK IS EMPTY")
    def printqueue(self):
        print(self.arr)
    def isEmpty(self):
        if len(self.arr)==0:
            return True
        else:
            return False    
q=Queue()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.printqueue()
q.dequeue()
q.printqueue()
q.isEmpty()


        


# In[ ]:


#implement functionalities of stack using queues
class Stack:
    arr=[]
    size=5
    def stack_push(self,element):
        if len(self.arr)<self.size:
            self.arr.insert(0,element)
        else:
            print("STACK IS FULL")
    def stack_pop(self):
        if len(self.arr)>0:
            self.arr.pop(0)
        else:
            print("STACK IS EMPTY")
    def stack_peek(self):
        if len(self.arr)==0:
            return "stack is empty"
        return self.arr[-1]
    def isEmpty(self):
        if len(self.arr)==0:
            return True
        else:
            return False


# In[ ]:


#reversing queue
#searching for an element in the given array--->linear search and time complexities
#master theorem for time complexity


# In[14]:


#implementing linear search on stack
class Stack:
    arr=[]
    size=5
    def stack_push(self,element):
        if len(self.arr)<self.size:
            self.arr.append(element)
        else:
            print("STACK IS FULL")
    def stack_pop(self):
        if len(self.arr)>0:
            return self.arr.pop()
        else:
            print("STACK IS EMPTY")
            
    def stack_peek(self):
        if len(self.arr)==0:
            return "stack is empty"
        return self.arr[-1]
    def isEmpty(self):
        if len(self.arr)==0:
            return True
        else:
            return False
s=Stack()
s.stack_push(10)
s.stack_push(20)
s.stack_push(30)
s.stack_push(40)
print(s.arr)
key=40
n=len(s.arr)
for i in range(len(s.arr)):
    a=s.stack_pop()
    n=n-1
    if a==key:
        print("key found at ",n)
        break
        


# In[ ]:


#number guessing game
import randint from random
number=randint(1,50)
chance=5
while chance!=0:
    n=int(input("Guess:"))
    if n==number:
        print("won")
        break
    elif n<number:
        print(n,"is samller than the actual number")
    elif n>number:
        print(n,"is gteater than the actual number")
    chance -= 1    


# In[ ]:


#binary search
a=[23,78,56,12,5]
a.sort()
key=78
low=0
high=n
mid=(low+high)//2
flag=0
while flag!=1:
    for i in range(low,high+1):
        if key==a[mid]:
            print("key found at",mid)
            flag=1
            break
        elif key<a[mid]:
            low=0
            high=mid-1
        else:
            low=mid+1
            high=n
if flag==0:
    print("element not found")


# In[ ]:


#binary to solve-->recurssion and while loop
arr=[i for i in range(1,11)]
key=3
low=0
high=len(arr)-1
found=False
while(low<=high):
    mid=(low+high)//2
    if arr[mid]==key:
        print("key is found at ",mid)
        found=True
        break
    elif arr[mid]>key:
        high=mid-1
    else:
        low=mid+1
if found==False:
    print("element not found")


# In[ ]:


def binary_search(arr,low,high,key):
    while(low<=high):
    mid=(low+high)//2
    if arr[mid]==key:
        print("key is found at ",mid)
        found=True
        return 
    elif arr[mid]>key:
        high=mid-1
        return binary_search(arr,low,high,key)
    elif:
        low=mid+1
        return binary_search(arr,low,high,key)
    else:
        print("not found")
    

    
arr=[i for i in range(1,11)]
key=100
low=0
high=len(arr)-1    
binary_search(arr,low,high,key)


# In[ ]:


Reverse the first half of stack
Reverse 2nd half of queue
Peep and pole in queue
PRIORITY QUEUE


# In[10]:


#reversing the first half of stack
class stack():
    arr=[]
    
    def push_stack(self,element):
        self.arr.append(element)
    def pop_stack(self):
         return self.arr.pop()
s1=stack()
s1.push_stack(100)
s1.push_stack(200)
s1.push_stack(300)
s1.push_stack(400)
print(s1.arr)
for i in range(len(s1.arr)//2):
    s1.pop_stack()
print(s.arr) 
s2=stack()
temp_arr=[]
for i in range(len(s1.arr)):
    temp_arr.append(s1.pop_stack())
print(temp_arr)    
    

  


# In[7]:


#reversing the seconf half of queue
class q():
    arr=[]
    temp_arr=[]
    def enq(self,element):
        self.arr.append(element)
    def deq(self):
        return self.arr.pop(0)
a=q()
a.enq(10)
a.enq(20)
a.enq(30)
a.enq(40)
print(a.arr)
for i in range(len(a.arr)//2):
    a.deq()
print(a.arr)    
class stack():
    arr2=[]
    def push_stack(self,element):
        self.arr2.append(element)
    def pop_stack(self):
        return self.arr2.pop()
s=stack()
for i in range(len(a.arr)):
    s.push_stack(a.deq())
print(s.arr2)    

        

