str1='12345679'
str2="Hello World"
str3=""" Hello World """
str4=''' Hello World'''

print(id(str1))
print(id(str1+str3))
print(id(str3))

print( (str1),type(str1))
print((str3),type(str3))
print(str1[0])
for i in str1: 
    print(i)

print(len(str1))
print(str1[::2])

string="Hello disha" 
count=0

vowels= ['a','e','i','o','u''A','E','I','O','U']
for i in string:
    if(i in vowels):
        count+=1
print("count:",count)



msg = "tpointtech"
print("Given string:", msg .upper())
print(id(msg))
msg = "T" + msg[1:6] + "T" + msg [7:]

print("new string:", msg.lower())
print(id(msg))


#given string  
str_1 = "Tpoint"  
str_2 = "Tech"

str_3=str_1+" "+str_2
print(str_3)
print(str_1*3)
