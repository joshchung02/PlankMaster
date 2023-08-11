def main():
    # Print an intro banner
    print('+----------------------------------------------------------+')
    print('|------------------Welcome to PlankMaster------------------|')
    print('+----------------------------------------------------------+')
    print()

    # Get parameters from user
    numSets = int(input("Please enter the number of sets: "))
    while numSets < 1:
        print("Invalid input")
        numSets = input("Please enter the number of sets: ")

    setLength = input("Please enter the length of each set (format m:ss): ")
    while not validateTime(setLength):
        print("Invalid input")
        setLength = input("Please enter the length of each set (format m:ss): ")

    breakLength = input("Please enter the length of each break (format m:ss): ")
    while not validateTime(breakLength):
        print("Invalid input")
        breakLength = input("Please enter the length of each break (format m:ss): ")

    # Parse time input
    tmp1 = setLength.split(":")
    setLength = []
    setLength.append(int(tmp1[0]))
    setLength.append(int(tmp1[1]))

    tmp2 = breakLength.split(":")
    breakLength = []
    breakLength.append(int(tmp2[0]))
    breakLength.append(int(tmp2[1]))

    # Testing:
    print(numSets)
    print(setLength[0], setLength[1])
    print(breakLength[0], breakLength[1])

    # Create output

def validateTime(time):
    if len(time) != 4:
        return False
    if time[1] != ':':
        return False
    return True

if __name__=='__main__':
    main()