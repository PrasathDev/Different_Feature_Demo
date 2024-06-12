def check():
    print("I am calling")

def feature1(age):
    print("feature-1 is enabled")
    print("additional part added in feature1")
    if(age>18):
        print("eligible to vote")
    
if __name__=='__main__':
    check()
    age=22
    feature1(age)