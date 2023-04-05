class Stack:
    def __init__(self,max_size):
        self.__max_size=max_size
        self.__top=-1
        self.__elements=[None]*max_size

    def get_max_size(self):
        return self.__max_size

    def full(self):
        if self.__top==self.__max_size-1:
            return True
        else:
            return False

    def push(self,data):
        if self.full():
            print("Stack Overflow ")
        else:
            self.__top+=1
            self.__elements[self.__top]=data

    def empty(self):
        if self.__top==-1:
            return True
        else:
            return False

    def pop(self):
        if self.empty():
            print("Stack underflow")
        else:
            data=self.__elements[self.__top]
            self.__top-=1
            return data

    def display(self):
        if self.empty():
            print("stack is empty")
        else:
            index=self.__top
            while(index>=0):
                print(self.__elements[index])
                index-=1
                
s=Stack(5)
s.push(9)
s.push(8)
s.push('a')
s.display()
print("-----")
s.pop()
s.display()


'''
Given a stack of integers, 
write a python program that updates the input stack such that all occurrences of the smallest values are at the bottom of the stack, 
while the order of the other elements remains the same.

For example:
Input stack (top-bottom) :   5 66  5  8  7
Output:  66  8  7  5  5
 
'''

class Stack:
    def __init__(self,max_size):
        self.__max_size=max_size
        self.__top=-1
        self.__elements=[None]*max_size

    def get_max_size(self):
        return self.__max_size

    def full(self):
        if self.__top==self.__max_size-1:
            return True
        else:
            return False

    def push(self,data):
        if self.full():
            print("Stack Overflow ")
        else:
            self.__top+=1
            self.__elements[self.__top]=data

    def empty(self):
        if self.__top==-1:
            return True
        else:
            return False

    def pop(self):
        if self.empty():
            print("Stack underflow")
        else:
            data=self.__elements[self.__top]
            self.__top-=1
            return data

    def display(self):
        if self.empty():
            print("stack is empty")
        else:
            index=self.__top
            while(index>=0):
                print(self.__elements[index])
                index-=1

def change_smallest_value(number_stack):
    l=[]
    while(not number_stack.empty()):
        l.append(number_stack.pop())
    minimum=min(l)
    counter=l.count(min(l))
    for i in range(counter):
        number_stack.push(minimum)
    for element in l[::-1]:
        if element!=minimum:
            number_stack.push(element)
    return number_stack

number_stack=Stack(5)
number_stack.push(7)
number_stack.push(8)
number_stack.push(5)
number_stack.push(66)
number_stack.push(5)

print("initial stack")
number_stack.display()

change_smallest_value(number_stack)
print("after updation")
number_stack.display()



practice qts
'''
Set of clothes:
A procurement of new clothing has arrived a store. The procurement contains 'm'
Caps, 'n' Shirts, 'o' Pants and 'p' Shoes.
The store sells two types of clothing set:First set consist of one cap and one
shoes.Second set consist of one shirt, one pants and one shoe. The First set costs 'a'
coins and Second set costs 'b' coins.What could be the maximum possible cost of a
set that can be assembled from the arrived clothings?Note : One item cannot be used
in more than one set however some items may be left unused.

Input Format
m(1≤m≤100000) — the number of caps.
n(1≤n≤100000) — the number of shirts.
o(1≤o≤100000) — the number of pants.
p(1≤p≤100000) — the number of shoes.
a(1≤a≤1000) — Cost of first set
b(1≤b≤1000) — Cost of second set

Constraints
m(1≤m≤100000) n(1≤n≤100000) o(1≤o≤100000) p(1≤p≤100000) a(1≤a≤1000)
b(1≤b≤1000)

Output Format
The maximum total cost of the set.
4
5
6
3
1
2

6
'''


m,n,o,p,a,b=[int(input())for _ in[0]*6]
x,y=min(m,p),min(n,o,p)
print(max(x*a+min(n,o,p-x)*b,y*b+min(m,p-y)*a))

'''
Given the participants' score sheet for your University Sports Day, 
you are required to find the runner-up score. You are given scores. 
Store them in a list and find the score of the runner-up.

Sample Input 
5
2 3 6 6 5

Sample Output 
5

'''

n=int(input())
scores=map(int,input().split())
print(sorted(list(set(scores)))[-2])

'''
A Police Job
There was a robbery last night!
All the mobile phones which were in the shop were numbered in ascending order
from the integer number x
For example, if x = 5 and there were 4 mobile phones in the shop,then the phone
has indices 5,6,7 and 8 and if x = 9 and there were 6 devices the phones had indices
9,10,11,12,13 and 14.
After the heist only n mobile phones remain and the indices, they have m1, m2,
m3....mn.
Find the minimum possible number of mobile phones that have been stolen. The
employees working in the shop neither remember x nor the number of mobile
phones in the store before the heist.

Input Format
The first line contains number of mobile phones after the robbery
The second line contain indices of the mobile phone after the robbery

Constraints
n (1≤n≤1000) (1≤mi≤10^9)

Output Format
Print the minimum number of mobile phones stolen from the shop, if the employees
in the shop neither remember x nor the number of mobile phones in the store before
the heist.
4
10 13 12 8
2

'''

input();indices=[*map(int,input().split())]
print(max(indices)-min(indices)-len(indices)+1)

