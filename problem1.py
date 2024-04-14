# M is the number of elements you want to add in list 
list=[]
M=int(input())
add=0
for i in range(0,M):
    element=int(input())
    list.append(element)
    add=add+element
print(*list, sep=';')
print("Addition ",add)

