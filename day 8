#quick sort
def swap(num_list, first_index, second_index):
    temp=num_list[first_index]
    num_list[first_index]=num_list[second_index]
    num_list[second_index]=temp
    

def quick_sort(num_list,low,high):
    if low>=high:
        return 
    split_point=partition(num_list,low,high)
    quick_sort(num_list,low,split_point-1)
    quick_sort(num_list,split_point+1,high)

def partition(num_list,low,high):
    pivot=num_list[low]
    i=low+1
    j=high
    done=False
    while not done:
        while (i<=j and num_list[i]<=pivot):
            i+=1
        while (num_list[j]>=pivot and j>=i):
            j-=1
        if j<i:
            done=True
        else:
            swap(num_list,i,j)
    swap(num_list,low,j)
    return j

num_list=[3,1,0,4,2]
l=len(num_list)
quick_sort(num_list,0,l-1)
print(num_list)


#infytq dsa part2 a5

class Item:
    def __init__(self,item_name,author_name,published_year):
        self.__item_name=item_name
        self.__author_name=author_name
        self.__published_year=published_year

    def get_item_name(self):
        return self.__item_name

    def get_author_name(self):
        return self.__author_name

    def get_published_year(self):
        return self.__published_year

    def __str__(self):
        return "{} by {} published in {}".format(self.__item_name,self.__author_name,self.__published_year)

class Library:
    def  __init__(self,item_list):
        self.__item_list=item_list

    def get_item_list(self):
        return self.__item_list

    def sort_item_list_by_author(self,new_item_list):
        new_item_list.sort(key=lambda x:''.join(e for e in x.get_author_name() if e.isalnum()))
        return new_item_list

    def add_new_items(self,new_item_list):
        self.__item_list.extend(new_item_list)
        self.sort_item_list_by_author(self.__item_list)

    def sort_items_by_published_year(self):
        self.sort_item_list_by_author(self.__item_list)
        self.__item_list.sort(key=lambda x:x.get_published_year())

item1=Item("A Mission In Kashmir","Andrew Whitehead",1995)
item2=Item("A Passage of India","E.M.Forster",2012)
item3=Item("A new deal for Asia","Mahathir Mohammad",1999)
item4=Item("A Voice of Freedom","Nayantara Sehgal",2001)
item5=Item("A pair of blue eyes","Thomas Hardy",1998 )

item_list=[item1,item2,item3,item4,item5]
library=Library(item_list)
print("The current items in the library are:")
for item in library.get_item_list():
    print(item)

item11=Item("Broken Wing","Sarojini Naidu",2012)
item12=Item("Guide","R.K.Narayanan",2001)
item13=Item("Indian Summers","John Mathews",2001)
item14=Item("Innocent in Death","J.D.Robb",2010)
item15=Item("Life of Pi","Yann Martel",2010 )
item16=Item("Sustainability","Johny",2016)
item17=Item("Look Ahead","E.M.Freddy",2012 )

new_item_list=[item11,item12,item13,item14,item15,item16,item17]
print()
print("The new items to be added are:")
for item in new_item_list:
    print(item)

new_item_list_sorted=library.sort_item_list_by_author(new_item_list)
print()
print("The new items after sorting based on the author name are:")
for item in new_item_list_sorted:
    print(item)

library.add_new_items(new_item_list_sorted)
print()
print("The final set of items after adding the new item list are:")
for item in library.get_item_list():
    print(item)

library.sort_items_by_published_year()
print()
print("The items sorted based on the increasing order of their published year:")
for item in library.get_item_list():
    print(item)

'''
Write a python function which accepts two sorted stacks and returns a new stack containing all the elements of input stacks in sorted order.

Note: The output stack should be of the size as that of the sum of the sizes of the input stacks.


Sample Input                                                Expected Output

Stack1 (top - bottom): 7,6,5
Stack2 (top - bottom): 3,2,1                       Stack (top-bottom) : 7,6,5,3,2,1

Stack1 (top - bottom): 15,10,3
Stack2 (top - bottom): 21,9,7                       Stack (top-bottom) : 21,15,10,9,7,3
 
'''

class Stack:
    def __init__(self,max_size):
        self.__max_size=max_size
        self.__elements=[None]*self.__max_size
        self.__top=-1

    def is_full(self):
        if(self.__top==self.__max_size-1):
            return True
        return False

    def is_empty(self):
        if(self.__top==-1):
            return True
        return False

    def push(self,data):
        if(self.is_full()):
            print("The stack is full!!")
        else:
            self.__top+=1
            self.__elements[self.__top]=data

    def pop(self):
        if(self.is_empty()):
            print("The stack is empty!!")
        else:
            data= self.__elements[self.__top]
            self.__top-=1
            return data

    def display(self):
        if(self.is_empty()):
            print("The stack is empty")
        else:
            index=self.__top
            while(index>=0):
                print(self.__elements[index])
                index-=1

    def get_max_size(self):
        return self.__max_size

def merge_stack(stack1,stack2):
    l=[]
    stack3=Stack(stack1.get_max_size()+stack2.get_max_size())
    while(not stack1.is_empty()):
        l.append(stack1.pop())
    while(not stack2.is_empty()):
        l.append(stack2.pop())
    l.sort()
    for element in l:
        stack3.push(element)
    return stack3            

stack1=Stack(3)
stack1.push(7)
stack1.push(10)
stack1.push(21)
stack2=Stack(3)
stack2.push(9)
stack2.push(11)
stack2.push(15)

output=merge_stack(stack1,stack2)
output.display()
