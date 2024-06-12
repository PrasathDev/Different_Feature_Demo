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
    
if __name__=='__main__':
    drive_age=23
    check()
    feature2(drive_age)
    feature3()
