# -*- coding: utf-8 -*-
"""assingment:4

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1l_-hg-G4UdreYOb7j_-pc56KAYLWOUyQ
"""

list_1=[10,20,24,25,26,35,70]

print(list_1[0::1])
print(list_1[-1::-1])

# task_1 
no=5
list_1=[]
for i in range(0,no,1) :
   
  user=int(input())
  list_1.append(user)

  print('number in the list',list_1)

# task_2
first=input('enter a list: ')
first=first[1:-1].split(', ')
if len(first)<4 :
  print('not possible ')
else:
  for i in range(len(first)) :
    first[i] =int(first[i])
  print(first[2:len(first)-2])

# task_3
first=[]
for i in range(5):
    first.append(int(input('Enter a number: ')))
for i in range(4,-1,-1):
    print(first[i])

# task_4
first=[1, 2, 3, 4, 5, 6, 7]
for i in range(len(first)):
    first[i]=(first[i])**2
print(first)

# alternative task_4
user=[1, 2, 3, 4, 5, 6, 7]
lst=[]

 


for i in user:
  i=i**2 
  lst.append(i)

print(lst)

# task_5
lst=["hey", "there", "", "what's", "", "up", "", "?"]
out=[]
for i in lst:
    if i!="":
        out.append(i)
print('Original List:', lst)
print('Modified List:', out)

# task_6 here we cannot use comma like the question 
lst=input('Enter a list: ').split(', ')
for i in range(7):
    lst[i]=int(lst[i])
largest=lst[0]
for i in range(7):
    if lst[i]>largest:
        largest=lst[i]
        large_id=i
print('My list:', lst)
print(f'Largest number in the list is {largest} which was found at index {large_id}.')

lst=input()
lst=lst.split(', ')
for i in range(len(lst)) :
  lst[i]=int(lst[i])
print('my list: ', lst)
max=-99999999
for i in lst :
  if max<i :
    max=i 
    index=lst.index(max)
print('Largest number in the list ',max,'which was founde at index',index)

# here we can use comma like the question 
lst=input()
lst=lst[1:len(lst)-1:1].split(', ')
for i in range(len(lst)):
    lst[i]=int(lst[i])
max=-999999
print(lst)
for i in lst:
  if i>max:
    max=i
    index=lst.index(max)
print(f'the largest number is {max} and the index is {index}')

# task_7
List_one = [1, 4, 7, 5]
List_two = [6, 1, 3, 9]

print(List_one[:len(List_one)-1]+List_two)

# task_8
list_one = [1, 2, 3, 4, 5, 6, 7, 8, 9]
list_two = [10, 11, 12, -13, -14, -15, -16]
out=[]
for i in list_one:
    if i%2==0:
        out.append(i)
for i in list_two:
    if i%2==0:
        out.append(i)
print(out)

# task_9
lst=input('Enter numbers: ')
temp=''
lst_1=[]
out=[]
for i in lst:
    if i!=' ':
        temp+=i
    else:
        lst_1.append(int(temp))
        temp=''
lst_1.append(int(temp))
for i in lst_1:
    if i%2!=0:
        out.append(i)
print('Original list:',lst_1)
print('Modified list:',out)

# task_10
lst=input('Enter a list: ').split(', ')
out=[]
for i in range(len(lst)):
    lst[i]=int(lst[i])

for i in lst:
    if i not in out:
        out.append(int(i))
print('Input list:', lst)
print('Modified list:', out)

# task_11
List_1 = [1, 4, 3, 2, 6]
List_2 = [8, 7, 6, 9]
count=False
for i in List_1:
    if i in List_2:
        print('True')
        count=True
        break
if count==False:
    print('False')

# task_12
myList = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
index1 = 0
index2 = 0 
index1 = 1
while(index1<10):
  myList[index1] = index1+4
  index2 = 1
  while(index2<index1):
    myList[index1] = myList[index1] + myList[index2]-index1
    index2 = index2+1
  print(myList[index1])
  index1 = index1+1

# task_13
myList = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
index1 = 0
index2 = 0
index1 = 1
while (index1 < 10):
  myList[index1] = index1 + 4
  index2 = 1
  while (index2 < index1):
    myList[index1] = myList[index1-1] - myList[index2-1] - index1
    index2 = index2 + 1
  print(myList[index1])
  index1 = index1 + 1

# task_14
myList = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
b = []
index1 = 0
index2 = 0
index1 = 1
b = myList
while(index1<10):
  myList[index1] = index1+2
  index2 = 1
  while(index2<index1):
    myList[index1] = b[index1]+myList[index2]-index1
    index2 = index2+1
  print(myList[index1])
  index1 = index1+1

# task_15
myList = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
b = []
index1 = 0
index2 = 0
index1 = 1
b = myList
while (index1 < 10):
  myList[index1] = index1 + 1
  index2 = 1
  while (index2 < index1):
    myList[index1] = b[index2-1] + myList[index2] - index1
    index2 = index2 + 1
  print(myList[index1])
  index1 = index1 + 1

# task_16 by me
user=input()
user=user.split(', ')
lst_1=[]
lst=[]
for i in user:
  lst_1.append(int(i))
  lst.append(int(i))

max=-9999999999999999
for i in lst:
  if max<i :
    max=i 
lst.remove(max)
max_1=-99999999999
for i  in lst:
  if max_1<i :
    max_1=i
print('second largest:',max_1,'index: ',lst_1.index(max_1))

# task_16 by big boy
lst=input('Enter a list: ').split(', ')
for i in range(7):
    lst[i]=int(lst[i])

if lst[0]>lst[1]:
   largest = lst[0]
   largest2 = lst[1]
   largest2_id=1
else:
   largest = lst[1]
   largest2 = lst[0]
   largest2_id=0

for i in range(2,7):
    if lst[i]>largest2:
        if lst[i]>largest:
            largest2=largest
            largest2_id=i
            largest=lst[i]
        else:
            largest2=lst[i]
            largest2_id=i
print('My list:', lst)
print(f'Second largest number in the list is {largest2} which was found at index {largest2_id}.')

# task=17
user=input()
lst=[]
user=user.split(', ')
for i in user:
  lst.append(int(i))
print(lst)
max=-99999999

min=9999999999
for i in lst:
  if i>max:
    max=i
  if i<min :
    min=i
print('smallest no: ',min ,'index:',lst.index(min))
print('largest no : ',max,'index: ',lst.index(max))

# task_18
user_1=input()
user_2=input()
user_1=user_1.split(', ')
user_2=user_2.split(', ')
lst=[]
for i in user_1:
  if i in user_2:
    lst.append(i)
print(lst)

# task_19
list_1=[1, 2, 2, 4, 5, 5, 7, 99, 200, 303, 70]
list_2=[1, 1, 2, 3, 3, 3, 4, 5, 200, 500, -5]
lst=[]
for i in list_1:
  if i not in lst:
    lst.append(i)
for i in list_2:
  if i not in lst:
    lst.append(i)
print(lst)



# task_20 big boy
lst= input('Enter a list: ')
print('Original data:', lst)
lst=lst.strip()
lst=lst[1:len(lst)-1]
print('After removing square brackets:', lst)
lst=lst.split(',')
print('Numbers in string format with extra white spaces:', lst)
for i in range(len(lst)):
    lst[i]=int(lst[i].strip())
print('Final data (numbers in list format):', lst)

# task_21 by me
inp=input()
inp=inp.split(',')
lst=[]
lst_1=[]
for i in inp:
  if i!=' ':
    lst.append(int(i))
 
for i in lst:
  if i not in lst_1 :
     lst_1.append(i)
print(lst)
print(lst_1)

# task_21 big boy
out=[]
lst= input('Enter a list: ').split(',')
for i in range(len(lst)):
    lst[i]=lst[i].strip()
for i in lst:
    if i not in out:
        out.append(i)
print('Given numbers in list:', lst)
print('List without any dupliacte values:',out)

inp =input()
print("original data: ", inp)

a = inp.strip(",")
print("after removing []: ", a)

x = inp.split(",")
print("nums in str with extra white spaces: ", x)

lst= []
for i in x:
    print(type(i))
    if i!=",":
        lst.append(int(i))
print("Final data: ", lst)

# lab mid solved by me
n=1000000
s=[]
q=[]
length=[]
sum=0
for i in range(1,n,1) :
    item=input(f'please enter item {i}: ')
    if item=='complete' :
      break
    quantity=int(input('please enter quantity: '))
    s.append(item)
    q.append(quantity)
for i in s:
  length.append(len(i))
for i in range(len(length)):
  sum=sum+length[i]*q[i]
print('the complete list is:')
for i in range(len(s)):
  #  print(s[i],q[i],'=',length[i])
  print(f'{s[i]}: {length[i]} x {q[i]} = {length[i]*q[i]} ')
  
print('total price: ',sum)

# lab mid solved by big boy
counter=1
item_lst=[]
quantity_lst=[]
price_lst=[]
total=0
while True:
    item=input(f"Please enter item {counter}: ")
    if item!='complete' :
        quantity=int(input('please enter quantity: '))
        item_lst.append(item)
        quantity_lst.append(int(quantity))
        price_lst.append(len(item))
        counter+=1
    else:
       break
print("The Complete list is:")
for i in range(len(item_lst)):
  ind=price_lst[i]*quantity_lst[i]
  total+=ind
  print(f"{item_lst[i]}: {price_lst[i]} X {quantity_lst[i]} = {ind}")
print('Total price:',total)