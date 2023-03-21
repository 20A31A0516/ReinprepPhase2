#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#applications of stack and queues


# In[6]:


#balancing paranthesis --->write a program to check whether a given string balanced or  not of one type of paranthesis
s=input("enter string:")
stack=[]
for i in s:
    if i=='(':
        stack.append(i)
    elif i==")" and len(stack)!=0:
        stack.pop()
    else:
        print("Invalid String")
        break
if len(stack)==0:
    print("valid string")   #issue
else:
    print("invalid string")


# In[8]:


#linked list
class Node:
    def __init__(self,value):
        self.data=value
        self.next=None
class LinkedList:
    def add_ele_at_start(self,head,value):
        new_node=Node(value)
        new_node.next=head
        head=new_node
        return head
    def add_element_at_end(self,head,value):
        new_node=Node(value)
        temp=head
        while temp.next != None:
            temp=temp.next
        temp.next=new_node
    def remove_element_at_end(self,value):
        temp=head
        while temp.next.next!=None:
            temp=temp.next
        temp.next=None 
    def remove_ele_at_given_position(self,position):pass
    def remove_ele_at_start(self):
        head.next=head
        
    def add_ele_at_given_position(self,head,position,value):
        new_node=Node(value)
        curr=head
        prev=None
        while position!=0:
            prev=curr
            curr=curr.next
            position=position-1
        prev.next=new_node
        new_node.next=curr
        
            
    def print_list(self,head):
        temp=head
        while temp != None:
            print(temp.data,end="->")
            temp=temp.next
    def search_element(self,value):pass
obj=LinkedList()
head=Node(10)   #never change the head value until problem said so
obj.add_element_at_end(head,20)
obj.add_element_at_end(head,30)
obj.add_element_at_end(head,40)
obj.add_element_at_end(head,50)
head=obj.add_ele_at_start(head,value=60)
obj.add_ele_at_given_position(head,3,100)
obj.print_list(head)


# In[10]:


#add 5 elements into linked list and print those  5 elements

head=Node(int(input("enter head")))
class Node:
    def __init__(self,value):
        self.data=value
        self.next=None
class LinkedList:
    
    def add_elements(self,head,value):
        new_node=Node(value)
        temp=head
        while temp.next != None:
            temp=temp.next
        temp.next=new_node
    def print_list(self,head):
        temp=head
        while temp != None:
            print(temp.data,end="->")
            temp=temp.next
obj=LinkedList()
for i in range(4):
    value=int(input("enter value"))
    obj.add_elements(head,value)
obj.print_list(head)    
    
        


# In[22]:


#write a program to reverse the linked list
class Node:
    def __init__(self,value):
        self.data=value
        self.next=None
class LinkedList:
    def add_ele_at_start(self,head,value):
        new_node=Node(value)
        new_node.next=head
        head=new_node
        return head
    def add_element_at_end(self,head,value):
        new_node=Node(value)
        temp=head
        while temp.next != None:
            temp=temp.next
        temp.next=new_node
    def remove_element_at_end(self):
        temp=head
        while temp.next.next!=None:
            temp=temp.next
        temp.next=None 
    def remove_ele_at_given_position(self,head,position):
        temp=head
        while position!=1:
            temp=temp.next
            position=position-1
        temp.next=temp.next.next    
    def remove_ele_at_start(self,head):pass
        
        
    def add_ele_at_given_position(self,head,position,value):
        new_node=Node(value)
        curr=head
        prev=None
        while position!=0:
            prev=curr
            curr=curr.next
            position=position-1
        prev.next=new_node
        new_node.next=curr
        
            
    def print_list(self,head):
        temp=head
        while temp != None:
            print(temp.data,end="->")
            temp=temp.next
        print()    
    def search_element(self,value):pass
    def reverse_linked_list(self,head):
        cur=head
        prev=None
        while cur!=None:
            temp=cur.next
            cur.next=prev
            prev=cur
            cur=temp    
        return prev
obj=LinkedList()
head=Node(10)   #never change the head value until problem said so
obj.add_element_at_end(head,20)
obj.add_element_at_end(head,30)
obj.add_element_at_end(head,40)
obj.add_element_at_end(head,50)
head=obj.add_ele_at_start(head,value=60)
obj.add_ele_at_given_position(head,3,100)
obj.print_list(head)
obj.remove_ele_at_given_position(head,1)
obj.print_list(head)
obj.remove_element_at_end()
obj.print_list(head)
obj.remove_ele_at_start(head)
obj.print_list(head)
head=obj.reverse_linked_list(head)
obj.print_list(head)


# In[ ]:




