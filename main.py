def check():
    print("I am calling")

def feature1(age):
    print("feature-1 is enabled")
    print("additional part added in feature1")
    if(age>18):
        print("eligible to vote")
    else:
        print("Not Eligible")
    
def feature4(person_age):
    if(person_age>18):
        print("Eligible for Vote")
    
def feature5():
    print("feature5 added")
    
def feature10(x):
    print(x)

def feature11(x):
    print(x)
    
if __name__=='__main__':
    drive_age=23
    x=89
    feature11(x)
    num=9
    check()
    vote_age=22
    feature1(vote_age)
    feature4(drive_age)