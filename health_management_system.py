print("health management system")

def datetime():

    import datetime
    return datetime.datetime.now()


a = int(input(" 1) Harry\n 2) Rohan\n 3) Hammad\n" "enter the number: "))

def fun1():
    b = int(input(" 1) Food\n 2) Excercise \n enter the number:"))
    


    if b ==1:
        c = int(input(" 1) read the data\n 2) write the data \n enter the number:"))
        if c ==1:
            f = open("Harry_Food.txt","r")
            for i in f:
                print(i, end="")
            f.close()
        elif c ==2:
            food  = input("enter the food: ")
            f = open("Harry_Food.txt","a")
            f.write(str([str(datetime())])+":" +food+ "\n")
            f.close()
        else:
            print("enter the correct no")


    elif b ==2:
        c = int(input(" 1) read the data\n 2) write the data \n enter the number:"))
        if c ==1:
            f = open("Harry_Exercise.txt","r")
            for i in f:
                print(i, end="")
            f.close()
        elif c ==2:
            exercise  = input("enter the Exercise: ")
            f = open("Harry_Exercise.txt","a")
            f.write(str([str(datetime())])+":" +exercise+ "\n")
            f.close()
        else:
            print("enter the correct no")
    else:
        print("enter the correct no")



def fun2():
    b = int(input(" 1) Food\n 2) Excercise \n enter the number:"))
    


    if b ==1:
        c = int(input(" 1) read the data\n 2) write the data \n enter the number:"))
        if c ==1:
            f = open("Rohan_Food.txt","r")
            for i in f:
                print(i, end="")
            f.close()
        elif c ==2:
            food  = input("enter the food: ")
            f = open("Rohan_Food.txt","a")
            f.write(str([str(datetime())])+":" +food+ "\n")
            f.close()
        else:
            print("enter the correct no")
    elif b ==2:
        c = int(input(" 1) read the data\n 2) write the data \n enter the number:"))
        if c ==1:
            f = open("Rohan_Exercise.txt","r")
            for i in f:
                print(i, end="")
            f.close()
        elif c ==2:
            exercise  = input("enter the Exercise: ")
            f = open("Rohan_Exercise.txt","a")
            f.write(str([str(datetime())])+":" +exercise+ "\n")
            f.close()
        else:
            print("enter the correct no")
    else:
        print("enter the correct no")




def fun3():
    b = int(input(" 1) Food\n 2) Excercise \n enter the number:"))
    


    if b ==1:
        c = int(input(" 1) read the data\n 2) write the data \n enter the number:"))
        if c ==1:
            f = open("Hammad_Food.txt","r")
            for i in f:
                print(i, end="")
            f.close()
        elif c ==2:
            food  = input("enter the food: ")
            f = open("Hammad_Food.txt","a")
            f.write(str([str(datetime())])+":" +food+ "\n")
            f.close()
        else:
            print("enter the correct no")

    elif b ==2:
        c = int(input(" 1) read the data\n 2) write the data \n enter the number:"))
        if c ==1:
            f = open("Hammad_Exercise.txt","r")
            for i in f:
                print(i, end="")
            f.close()
        elif c ==2:
            exercise  = input("enter the Exercise: ")
            f = open("Hammad_Exercise.txt","a")
            f.write(str([str(datetime())])+":" +exercise+ "\n")
            f.close()
        else:
            print("enter the correct no")
    else:
        print("enter the correct no")








if a==1:
    fun1()

elif a==2:
    fun2()

elif a ==3:
    fun3()

else:
    print("enter the correct no")