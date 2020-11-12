lineCount = 0
correct1000 = 0

with open("testingResults.txt") as f:
    for line in f:
        lineCount = lineCount + 1
        split = line.split(None, 1)
        payment = int(split[0])
        prediction = split[1].strip('\n')
        prediction = int(float(prediction))


        if (payment - prediction < 2000 and payment - prediction > -2000) or (prediction - payment < 2000 and prediction - payment > -2000):
            correct1000 = correct1000 + 1

    print(correct1000)
    print(lineCount)
    print('percentage ' + str((correct1000/lineCount)*100))
