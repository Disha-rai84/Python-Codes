# * * * *
# * * * *
# * * * *
# * * * *

for i in range(1,5):
    for j in range(1,5):
        print(" * ",end="")
    print("")    

# * 
# * *
# * * * 
# * * * *

for i in range(1,7):
    for j in range(1,i):
        print(" * ",end="")
    print("")    

# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 
count =0
for i in range(1,7):

    for j in range(1,i):
        print(count,end=" ")
        count+=1
    print("")    
