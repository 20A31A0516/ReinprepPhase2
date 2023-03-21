#!/usr/bin/env python
# coding: utf-8

# In[1]:


class Node:
    def __init__(self,value):
        self.data=value
        self.left=None
        self.right=None

class BSTree:
    def add_ele(self,root,value):

        new_node=Node(value) #create a new node to add an ele
        if new_node.data < root.data:
            if root.left!=None:
                self.add_ele(root.left,value)
            else:
                root.left=new_node
        else:
            if root.right!=None:
                self.add_ele(root.right,value)
            else:
                root.right=new_node
    def search(self,root,value):
        if root==None or root.data==value:
            return root
        elif root.data<value:
            return self.search(root.right,value)
        else:
            return self.search(root.left,value)
    def sum(self,root):
        sum=root.data
        if root.left!=None:
            sum+=self.sum(root.left)
        if root.right!=None:
            sum+=self.sum(root.right)
        return sum
    def height(self,root):
        if root==None:
            return -1
        left_height=self.height(root.left)
        right_height=self.height(root.right)

        return 1+max(left_height,right_height)



ob=BSTree()
root=Node(10)
ob.add_ele(root,7)
ob.add_ele(root,40)
ob.add_ele(root,5)
ob.add_ele(root,9)
ob.add_ele(root,15)
ob.add_ele(root,60)
x=ob.search(root,60)
if(x):
    print("yes")
else:
    print("No")
a=ob.sum(root.left)
print("left sum=",a)
b=ob.sum(root.right)
print("right sum=",b)
d=ob.height(root)
print("10 : ",d)
e=ob.height(root.right)
print("40 : ",e)
c=ob.height(root.right.right)
print("60 : " ,c)


# In[2]:


#selection sort
l=list(map(int,input().split()))
for i in range(len(l)-1):
    m=min(l[i+1::])
    if l[i]>m:
        j=l.index(m)
        l[i],l[j]=l[j],l[i]
print("sorted list after applying selection sort is",l)


# In[ ]:




