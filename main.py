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
    
if __name__=='__main__':
    check()
    vote_age=22
    feature1(vote_age)