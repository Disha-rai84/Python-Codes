# import matplotlib.pyplot as plt
# import numpy as np
# # print(matplotlib.__version__)

# xpoints = np.array([1, 2, 6, 8])
# ypoints = np.array([3, 8, 1, 10])


# plt.plot(xpoints, ypoints)
# plt.show()

# #Three lines to make our compiler able to draw:
# import sys
# import matplotlib
# matplotlib.use('Agg')

# import matplotlib.pyplot as plt
# import numpy as np

# ypoints = np.array([3, 8, 1, 10])

# plt.plot(ypoints, marker = ',', ms = 20, mec = 'r')
# plt.show()

# #Two  lines to make our compiler able to draw:
# plt.savefig(sys.stdout.buffer)
# sys.stdout.flush()



# import matplotlib.pyplot as plt
# import numpy as np

# ypoints = np.array([3, 8, 1, 10])

# plt.plot(ypoints, color = 'r',linestyle = 'dotted',marker = 'H', ms = 15, mfc='w', mec = 'm')
# plt.show()

# num=12
# for i in range(1,10):
#     print(num,'x',num,'=',num*i)





# num = 7 
# factorial = 1

# if num < 0:
#     print("sorry, factorial don't exist for negative numbers")
# elif num == 0:
#     print(" the factorial for 0 is 1")
# else:
#     for i in range(1,num + 1):
#         factorial = factorial*i
#     print("The factorial of",num ,"is", factorial)  

# 


# num = float(input(" Enter any value in kilometers you need to convert"))
# conv_fac=0.621
# miles= (conv_fac*num)
# print(" %0.1f kilometers is equal to %0.1f miles"%(num,miles))


# celsius=37.5
# # fahrenheit = (celsius*1.8)+32
# # print( "%0.1f celsius is equale to %0.1f fahrenheit" %(celsius, fahrenheit))

# num= float( input("Entet any value"))
# if (num%2==0):
#     print(" The number is even")
# else:
#     print(" The number is an odd number")


num = 4
if num > 1:
    for i in range(2,num):
        if num % i==0:
            print(num,"is not a prime number")
            break
    else:
        print(num,"is a prime number")
else:
    print(num,"is not a prime number")