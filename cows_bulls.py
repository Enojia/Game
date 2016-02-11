import random

def NumberGen():
    return random.randint(0,9999)

def main():
    num = NumberGen()
    numArray = map(int, str(num))
    print numArray
    userInput = raw_input("Enter a number")
    while userInput != num:
        cow=0
        bull=0
        inputArray = map(int, str(userInput))
        print inputArray
        for i in range(0, 4):
            if inputArray[i] in numArray:
                if inputArray[i] == numArray[i]:
                    cow+=1
                else:
                    bull+=1

        if cow == 4:
            break
        else:
            print "%d cow" %(cow)
            print "%d bull" %(bull)
            userInput = raw_input("enter another number   ")

    print "Gratz u found the answer"




main()
