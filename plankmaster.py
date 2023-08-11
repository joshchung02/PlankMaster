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

    # Print output banner
    print()
    print('+----------------------------------------------------------+')
    print('|-------------------Here are your times--------------------|')
    print('+----------------------------------------------------------+')
    print()

    # Create output
    currTime = [0, 0]

    for s in range(numSets):
        # Set
        addTime(currTime, setLength)
        
        if currTime[1] > 9:
            print(f"Set {s+1}:    {currTime[0]}:{currTime[1]}")
        else:
            print(f"Set {s+1}:    {currTime[0]}:0{currTime[1]}")
        
        addTime(currTime, breakLength)

        # Break
        if s == numSets - 1: break # Fencepost
        if currTime[1] > 9:
            print(f"Break {s+1}:  {currTime[0]}:{currTime[1]}")
        else:
            print(f"Break {s+1}:  {currTime[0]}:0{currTime[1]}")

def validateTime(time):
    if len(time) != 4:
        return False
    if time[1] != ':':
        return False
    return True

def addTime(time, timeToAdd):
    res = time
    res[0] += timeToAdd[0]
    res[1] += timeToAdd[1]

    if res[1] > 59:
        res[0] += 1
        res[1] -= 60
    
    return res

if __name__=='__main__':
    main()
