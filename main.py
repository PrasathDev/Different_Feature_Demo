def check():
    print("I am calling")

def feature2(drive_age):
    print("feature-2 is implemeted")
    if (drive_age>20):
        print("Eligible for applying driving license")
    else:
        print("Not Eligible")
  
def feature3():
    print("feature-3 is just created")
    
def feature4(person_age):
    if(person_age>18):
        print("Eligible for Vote")

def feature6(num):
    if(num%2==0):
        print("Even Number")
    
if __name__=='__main__':
    drive_age=23
    num=9
    feature6(num)
    check()
    feature2(drive_age)
    feature3()
