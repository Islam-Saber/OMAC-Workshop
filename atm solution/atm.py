from __future__ import print_function

balance = 1000
valid_units = [100,50,20,10,2,1]
request = 0

def atm (balance, request):
    request = int(input(["How much money do you need ?"]))
    given = 0

    if request <= 0:
        print("please enter a bigger value !")

    elif request > balance:
        print("insufficient balance !")

    else:
        for unit in valid_units:
            while request >= unit:
             print("Give " + str(unit))
             request -= unit
             balance -= unit
             given += unit

    print(str(given) + " Given")

    print("Your balance is " + str(balance))

    return atm(balance, request)

atm (balance, request)
