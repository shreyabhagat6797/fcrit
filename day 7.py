#selection sort
def swap(num_list,first_index,second_index):
    temp=num_list[first_index]
    num_list[first_index]=num_list[second_index]
    num_list[second_index]=temp

def find_next_min(num_list,start_index):
    minimum=min(num_list[start_index::])
    return num_list.index(minimum)

def selection_sort(num_list):
    for i in range(len(num_list)):
        index=find_next_min(num_list,i)
        swap(num_list,i,index)

num_list=[64,25,12,22,11]
print("before sorting",num_list)
selection_sort(num_list)
print("after sorting",num_list)

#bubble sort

def swap(num_list,first_index,second_index):
    temp=num_list[first_index]
    num_list[first_index]=num_list[second_index]
    num_list[second_index]=temp

def bubble_sort(num_list):
    total_passes=0
    end_index=len(num_list)
    for index1 in range(0,end_index-1):
        swapped=False
        total_passes+=1
        for index2 in range(0,end_index-index1-1):
            if num_list[index2]>num_list[index2+1]:
                swap(num_list,index2,index2+1)
                swapped=True
        if swapped==False:
            break
    return total_passes

num_list=[-2,45,0,11,-9]
print("no of passes: ",bubble_sort(num_list))
print(num_list)

#merge sort

def merge_sort(num_list):
    low=0
    high=len(num_list)-1
    if low==high:
        return num_list
    else:
        left_list=num_list[:len(num_list)//2]
        right_list=num_list[len(num_list)//2:]
        list1=merge_sort(left_list)
        list2=merge_sort(right_list)
        sorted_list=merge(list1,list2)
        return sorted_list

def merge(left_list,right_list):
    i,j=0,0
    sorted_list=[]
    while(i<len(left_list) and j<len(right_list)):
        if left_list[i]<=right_list[j]:
            sorted_list.append(left_list[i])
            i+=1
        else:
            sorted_list.append(right_list[j])
            j+=1
    if i<len(left_list):
        sorted_list.extend(left_list[i::])
    if j<len(right_list):
        sorted_list.extend(right_list[j::])
    return sorted_list

num_list=[6,5,12,10,9,1]
sorted_list=merge_sort(num_list)
print(sorted_list)
