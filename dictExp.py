dict1 = {
    "name":"Jhon snow",
    "age":"22",
    "gender":"male",
    1:100,
    2:"hi",
    "one":[1,2,3,4],
    [1,2,3]:"hi"
}




dict1["region"]="north"

# del dict1[1]
# dict1.pop(1)

# dict1.popitem()

# dict1.clear()
print(dict1)
print(type(dict1))



# print(dict1["name"])
# print(dict1[1])

# # keys 
# for i in dict1:
#     print(i)

# # values 
# for i in dict1:
#     print(dict1[i])


# for i in dict1.values():
#     print(i)


# for i in dict1.keys():
#     print(i)


# for i,j in dict1.items():
#     print(i, j)

print(dict1.update({"name":"Ned Stark"}))
print(dict1.get("name"))
