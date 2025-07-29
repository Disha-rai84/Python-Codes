# int_set = {12, 1, 8 , 9, 11, 10,"hi",5,12,True} 
# print(int_set)  
  
# str_set = {'one', 'two', 'three', 'four', 'five'}
# print(str_set)  
  
# mixed_set = {12, 'one', 10.2, 6e2} 
# print(mixed_set)  

# # print(int_set[0])
# int_set.add(100)
# int_set.update([100,200,300])
# # # int_set.remove(1000)
# # # int_set.discard(1000)
# # int_set.pop()
# # print(int_set)

# # # dict2={"name":"disha"}
# # set1={}

# # # print(type(dict2))
# # print(type(set1))

# # newSet={1,"hello", True}

# # newSet.clear()
# # print(newSet)

# A = {1, 2, 3,10}
# B = {2, 3, 4, 5}

# print( A | B)
# print(A.union(B))


# print( A & B)
# print(A.intersection(B))



# print(B.symmetric_difference(A))
# # print( B-A)
# # print(B.difference_update(A))

# print("B:",B)


days = {"Sunday","Monday","Tuesday","Friday"}

holiday = {"Sunday","Tuesday","Friday","Monday","wednesday"}

print(holiday.issubset(days))


print(holiday.isdisjoint(days))


# temp = frozenset([1,2,3,4])

# print(temp)
# print(type(temp))

# # temp.add(10)



# copyTemp = temp.copy()

# print(copyTemp)