limit = int(input("enter the limit:"))
# for i in range(1,(limit+1)):
#     print("*" *i)
# j=limit
# print("Inverted trinagle")
# for j in range(j,0,-1):
#     print("*" *j)
print("Number triangle")

for i in range(1,(limit+1)):
    j=1
    for j in range(1,(i+1)):
        print(j,end="")
    print()
print("Inverted number triangle")
for i in range(limit,0,-1):
    j=i
    for j in range(i,0,-1):
        print(j,end="")
    print()

print("Inverted number triangle 2 version")
for i in range(limit,0,-1):
    j=1
    for j in range(1,(i+1)):
        print(j,end="")
    print()
 