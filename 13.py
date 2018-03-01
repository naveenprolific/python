while True:
    try:
       num = int(input("enter a num :"))
       break

    except ValueError:
        print("u didnt enter a num")
    except:
        print("an unknown error occured")
print("thank u")
print(num)
