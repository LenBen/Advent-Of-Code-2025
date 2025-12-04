dial = 50
status = "left"
numOfZeros = 0

with open("input1a.txt", "r") as input:
    for line in input:
        # See if the dial should be turned left or right
        if line[0] == "L":
            status = "left"
        elif line[0] == "R":
            status = "right"

        # Turn the dial 
        number = int(line[1:])

        match(status):
            case "left":
                dial -= number
            case "right":
                dial += number
        
        # Align the dial
        while (dial > 99 or dial < 0):
            if dial > 99:
                dial -= 100
            elif dial < 0:
                dial += 100
        
        #Check if dial is 0
        if dial == 0:
            numOfZeros += 1


print(numOfZeros)