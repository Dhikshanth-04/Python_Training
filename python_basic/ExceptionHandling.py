try:
    a = int(input("Enter A :"))
    b = int(input("Enter b: "))
    print(a/b)
except Exception as e:
    print("The exception :",e)
finally:
    print("Try with better values next time")