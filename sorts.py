######################
#Searching algorithms
#By Wahne and Maxfield
######################

#Bubble Sort

import random
import time

#funNums = [12948.7, 2002.2, 0.0004, 3, 4, 9, 8, 12, 59, 32, 1, 2, 2836.5, 1284.3, 98735.7, 3546238, 128534]
#funNums = [25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]



def insertion(funList):
    start_time = time.time()
    outList = list(funList)
    i = 1
    j = 0

    while i < len(outList):
        j = i

        while j > 0 and outList[j-1] > outList[j]:
            tmp = outList[j]
            outList[j] = outList[j-1]
            outList[j-1] = tmp
            j = j - 1

        i = i + 1
        #print("[ pass", i, "]", "outList is currently:", outList)
    print("Number of passes:", i)

    print("Total elapsed time:", time.time() - start_time, "seconds.")

    return outList
    

def bubble(funList):
    start_time = time.time()
    outList = list(funList)
    isSorted = False
    passes = 0

    while (isSorted == False):
        wasChanged = False
        for i in range(0, len(outList) - 1): 
            if outList[i] > outList[i + 1]:
               tmp = outList[i]
               outList[i] = outList[i + 1]
               outList[i + 1] = tmp
               wasChanged = True

        passes = passes + 1
        #print("[ pass", i, "]", "outList is currently:", outList)

        if (wasChanged == False):
            isSorted = True
    print("Number of passes:", passes)
    
    print("Total elapsed time:", time.time() - start_time, "seconds.")

    return outList

def shell(funList):
    start_time = time.time()
    outList = list(funList)
    passes = 0
    n = len(outList)

    if len(outList) < 1:
        print("Length of list is too small to shell sort! Aborting sort!")
        return funList
    
    gap = int(n // 2)

    while gap > 0:
        for i in range(gap,n):
            tmp = outList[i]
            j = i

            while j >= gap and outList[j-gap] > tmp:
                outList[j] = outList[j-gap]
                j -= gap

            outList[j] = tmp
            passes += 1

        gap = gap // 2
        passes = passes + 1

    print("Number of passes:", passes)
    
    print("Total elapsed time:", time.time() - start_time, "seconds.")

    return outList

def changeList(funList):
    quits = ["q", "Q", "quit", "Quit"]
    cancels = ["c", "C", "cancel", "Cancel"]
    clears = ["clr", "CLR", "clear", "Clear"]
    pops = ["pop", "Pop"]
    newList = list(funList)
    usrIn = ""


    print("\n*****List Changing Menu*****",
            "\n Type 'clr' to clear the list.",
            "\n Type 'pop' to remove the last item from the list.",
            "\n Type 'grow' to quickly populate the list with new integers.",
            "\n Type 'q' to save changes and return to the main menu.",
            "\n Type 'c' to cancel and undo list changes."
            )

    while usrIn not in quits:
        print("\n  Value of the current list: ", newList)
        usrIn = input("\nEnter a number to append it to the list: ")

        if usrIn.isdigit() == True:
            newList.append(int(usrIn))
        elif usrIn in quits:
            return newList
        elif usrIn in cancels:
            return funNums
        elif usrIn == "grow":
            newList = growList(newList)
            continue
        elif usrIn in clears:
            print("Clearing list...")
            newList = []
            continue
        elif usrIn in pops:
            if newList:
                print("Popping off list...")
                newList.pop()
            else:
                print("Pop operation failed! List is already empty!")
        else:
            print("Input not recognized.")

def growList(funList):
    digits = ""
    upperLimit = ""
    lowerLimit = ""
    outList = list(funList)

    print("\n*****Grow List*****"
            "\n\n  Value of the current list: ", outList)

    while digits.isdigit() == False:
        digits = input("\nEnter amount of new integers to be added: ")
        if digits.isdigit() == False:
            print("Non-integer detected. Please try again.")
        else:
            digits = int(digits)
            break

    while lowerLimit.isdigit() == False:
        lowerLimit = input("Enter lower-limit (inclusive) of generated numbers: ")
        if lowerLimit.isdigit() == False:
            print("Non-integer detected. Please try again.")
        else:
            lowerLimit = int(lowerLimit)
            break

    while upperLimit.isdigit() == False:
        upperLimit = input("Enter upper-limit (inclusive) of generated numbers: ")
        if upperLimit.isdigit() == False:
            print("Non-integer detected. Please try again.")
        else:
            upperLimit = int(upperLimit)
            break
    
    try:
        for i in range(0, digits):
            outList.append(random.randrange(lowerLimit, upperLimit + 1))
    except:
        print("Error during append process! Cancelling growth!")
        return funList

    print("\nThe new length of the list is:", len(outList),
    "\n  Value of the new list:", outList)

    return outList

def benchmark(funList):
    x = ""


def main():
    option = "origin"
    quits = ["q", "Q", "quit", "Quit"]
    funNums = [10, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    
    print("\nWelcome to Sorting Algorithms Demonstrator, written by Maxfield Gordon.")

    while option not in quits:
        print( 
        "\n*****Algorithm Menu*****",
        "\n 1. Insertion Sort [ins]",
        "\n 2. Bubble Sort [bub]",
        "\n 3. Shell sort [she]",
        "\n Type 'bench' to benchmark every sort available.",
        "\n Type 'mod' to modify the input list.",
        "\n Type 'q' to quit."
        "\n Type 'shuf' to shuffle the list.",
        "\n\n   Value of the current list:", funNums
        )

        option = input("\nPlease select a choice: ")

        if option == "ins":
            result = insertion(funNums)
            print("\n Final contents of result list: ", result)
        elif option == "bub":
            result = bubble(funNums)
            print("\n Final contents of result list: ", result)
        elif option == "she":
            result = shell(funNums)
            print("\n Final contents of result list: ", result)
        elif option == "mod":
            funNums = changeList(funNums)
        elif option == "shuf":
            random.shuffle(funNums)
        elif option == "bench":
            x= "emtpy string"
            #TODO
            #IMPLEMENT THIS
        elif option in quits:
            print("Closing the program. Good bye!")
        else:
            print("Option not recognized!")
main()
