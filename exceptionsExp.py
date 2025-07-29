a=10

try:
    raise ZeroDivisionError()
except ZeroDivisionError :
  print("error")
except:
    print("something went wrong")
finally:
    print("i always execute ")