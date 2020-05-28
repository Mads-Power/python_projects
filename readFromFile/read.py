def main():
        userReady = input("you will be given some options. write [yes] to continue or [No] to quit")        

        if userReady == "no":
                exit()
        else:
                mainQuestions()               
                  

def openFile():
        
        f = open("demofile.txt", "r")
        print(f.readline())
        for x in f:
                print(x)
                

def createNewFile():
        userCreatesFile = input("Create new file? [yes] [No]")
        try:
         createFile = open("hello.txt", "x")
        except:
                print("The file you have created already exist" + createFile)

def mainQuestions():
        userRequest = input("open demofile.txt ? [yes] [No]")

        if userRequest == "no":
                exit()
        else:
                openFile()


main()
