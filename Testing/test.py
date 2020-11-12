import csv
import numpy as np
import pandas as pd
import pickle

#read into dataframe
header_list = ['PaymentAmount', 'AD', 'DD', 'Days', 'DC1', 'DC2', 'DC3', 'DC4']
df = pd.read_csv('DGNS_1_4.csv', names = header_list)

#drop utilization day count in column 3
df = df.drop(columns = ['Days'], axis =1)

#drop NaN values
df = df.dropna()

#open pickle file with model
pickle_in = open('TwentyModel.pickle', 'rb')
model = pickle.load(pickle_in)

#fill array with values to pass to model
def fill_array(dd,ad,dc1,dc2,dc3,dc4):

    #deductible
    outputList.insert(0, int(dd))

    #admitting diagnosis
    #1 - 20
    ad = str(ad)
    if ad == '389':
        outputList.insert(1, 1)
    if ad == '41401':
        outputList.insert(2, 1)
    if ad == '42731':
        outputList.insert(3, 1)
    if ad == '4280':
        outputList.insert(4, 1)
    if ad == '43491':
        outputList.insert(5, 1)
    if ad == '486':
        outputList.insert(6, 1)
    if ad == '49121':
        outputList.insert(7, 1)
    if ad == '51881':
        outputList.insert(8, 1)
    if ad == '5789':
        outputList.insert(9, 1)
    if ad == '5990':
        outputList.insert(10, 1)
    if ad == '71536':
        outputList.insert(11, 1)
    if ad == '7802':
        outputList.insert(12, 1)
    if ad == '78079':
        outputList.insert(13, 1)
    if ad == '78097':
        outputList.insert(14, 1)
    if ad == '78605':
        outputList.insert(15, 1)
    if ad == '78609':
        outputList.insert(16, 1)
    if ad == '78650':
        outputList.insert(17, 1)
    if ad == '78659':
        outputList.insert(18, 1)
    if ad == '78900':
        outputList.insert(19, 1)
    if ad == 'V5789':
        outputList.insert(20, 1)

    #diagnosis code 1
    #21 - 40
    dc1 = str(dc1)
    if dc1 == '389':
        outputList.insert(21, 1)
    if dc1 == '41071':
        outputList.insert(22, 1)
    if dc1 == '41401':
        outputList.insert(23, 1)
    if dc1 == '42731':
        outputList.insert(24, 1)
    if dc1 == '4280':
        outputList.insert(25, 1)
    if dc1 == '42823':
        outputList.insert(26, 1)
    if dc1 == '42833':
        outputList.insert(27, 1)
    if dc1 == '43491':
        outputList.insert(28, 1)
    if dc1 == '486':
        outputList.insert(29, 1)
    if dc1 == '49121':
        outputList.insert(30, 1)
    if dc1 == '49122':
        outputList.insert(31, 1)
    if dc1 == '5070':
        outputList.insert(32, 1)
    if dc1 == '51881':
        outputList.insert(33, 1)
    if dc1 == '5849':
        outputList.insert(34, 1)
    if dc1 == '5990':
        outputList.insert(35, 1)
    if dc1 == '71536':
        outputList.insert(36, 1)
    if dc1 == '7802':
        outputList.insert(37, 1)
    if dc1 == '78650':
        outputList.insert(38, 1)
    if dc1 == '78659':
        outputList.insert(39, 1)
    if dc1 == 'V5789':
        outputList.insert(40, 1)

    #diagnosis code 2
    #41 - 60
    dc2 = str(dc2)
    if dc2 == '2449':
        outputList.insert(41, 1)
    if dc2 == '25000':
        outputList.insert(42, 1)
    if dc2 == '2720':
        outputList.insert(43, 1)
    if dc2 == '2724':
        outputList.insert(44, 1)
    if dc2 == '2761':
        outputList.insert(45, 1)
    if dc2 == '27651':
        outputList.insert(46, 1)
    if dc2 == '2859':
        outputList.insert(47, 1)
    if dc2 == '3051':
        outputList.insert(48, 1)
    if dc2 == '4019':
        outputList.insert(49, 1)
    if dc2 == '40390':
        outputList.insert(50, 1)
    if dc2 == '41400':
        outputList.insert(51, 1)
    if dc2 == '41401':
        outputList.insert(52, 1)
    if dc2 == '42731':
        outputList.insert(53, 1)
    if dc2 == '4280':
        outputList.insert(54, 1)
    if dc2 == '486':
        outputList.insert(55, 1)
    if dc2 == '496':
        outputList.insert(56, 1)
    if dc2 == '53081':
        outputList.insert(57, 1)
    if dc2 == '5849':
        outputList.insert(58, 1)
    if dc2 == '5859':
        outputList.insert(59, 1)
    if dc2 == '5990':
        outputList.insert(60, 1)

    #diagnosis code 3
    #61 - 80
    dc3 = str(dc3)
    if dc3 == '2449':
        outputList.insert(61, 1)
    if dc3 == '25000':
        outputList.insert(62, 1)
    if dc3 == '2724':
        outputList.insert(63, 1)
    if dc3 == '2761':
        outputList.insert(64, 1)
    if dc3 == '27651':
        outputList.insert(65, 1)
    if dc3 == '2859':
        outputList.insert(66, 1)
    if dc3 == '3051':
        outputList.insert(67, 1)
    if dc3 == '4019':
        outputList.insert(68, 1)
    if dc3 == '40390':
        outputList.insert(69, 1)
    if dc3 == '41400':
        outputList.insert(70, 1)
    if dc3 == '41401':
        outputList.insert(71, 1)
    if dc3 == '42731':
        outputList.insert(72, 1)
    if dc3 == '4280':
        outputList.insert(73, 1)
    if dc3 == '486':
        outputList.insert(74, 1)
    if dc3 == '496':
        outputList.insert(75, 1)
    if dc3 == '53081':
        outputList.insert(76, 1)
    if dc3 == '5849':
        outputList.insert(77, 1)
    if dc3 == '5859':
        outputList.insert(78, 1)
    if dc3 == '5990':
        outputList.insert(79, 1)
    if dc3 == '71590':
        outputList.insert(80, 1)

    #diagnosis code 4
    #81 - 100
    dc4 = str(dc4)
    if dc4 == '2449':
        outputList.insert(81, 1)
    if dc4 == '25000':
        outputList.insert(82, 1)
    if dc4 == '2720':
        outputList.insert(83, 1)
    if dc4 == '2724':
        outputList.insert(84, 1)
    if dc4 == '2761':
        outputList.insert(85, 1)
    if dc4 == '2768':
        outputList.insert(86, 1)
    if dc4 == '2859':
        outputList.insert(87, 1)
    if dc4 == '2948':
        outputList.insert(88, 1)
    if dc4 == '3051':
        outputList.insert(89, 1)
    if dc4 == '4019':
        outputList.insert(90, 1)
    if dc4 == '40390':
        outputList.insert(91, 1)
    if dc4 == '41400':
        outputList.insert(92, 1)
    if dc4 == '41401':
        outputList.insert(93, 1)
    if dc4 == '42731':
        outputList.insert(94, 1)
    if dc4 == '4280':
        outputList.insert(95, 1)
    if dc4 == '496':
        outputList.insert(96, 1)
    if dc4 == '53081':
        outputList.insert(97, 1)
    if dc4 == '5849':
        outputList.insert(98, 1)
    if dc4 == '5859':
        outputList.insert(99, 1)
    if dc4 == '5990':
        outputList.insert(100, 1)

if __name__ == "__main__":

    file1 = open("testingResults.txt", "w")
    testingArray = df.values
    print(testingArray)

    for row in testingArray:

        #clear outputList
        outputList = [0] * 101

        payment = row[0]
        ad = row[1]
        dd = row[2]
        dc1 = row[3]
        dc2 = row[4]
        dc3 = row[5]
        dc4 = row[6]

        fill_array(dd,ad,dc1,dc2,dc3,dc4)

        #pop off 0 values created by insert
        outputList.pop()
        outputList.pop()
        outputList.pop()
        outputList.pop()
        outputList.pop()
        outputList.pop()

        # convert to numpy array
        outputArray = np.array(outputList)

        # convert to 2d array
        outputArray = outputArray.reshape(1, (len(outputArray)))

        # get prediction array
        predictionArray = model.predict(outputArray)

        # get actual prediction
        prediction = predictionArray[0][0]

        file1.write(str(payment) + " " + str(prediction) + "\n")






