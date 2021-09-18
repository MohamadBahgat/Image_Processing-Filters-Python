import numpy as np
import pylab as plt
from matplotlib import pyplot as plt2
import cv2


def helperHistogram(arr):
    h = [0.0] * 256
    for i in range(arr.size - 1):
        h[arr[i]] += 1
        # print(arr[i])
    print("arr size: ", arr.size)
    return np.array(h)


def helperSmoothWin3(histo, k, w):
    l = histo.size
    i = 0
    newHisto = [0.0] * (256)
    while i < l:
        sum = histo[i]
        num = 1
        if i + 1 < l:
            num += 1
            sum += histo[i + 1]
        if i + 2 < l:
            num += 1
            sum += histo[i + 2]
        avg = sum / num
        # print(avg/((2*k)+1))
        # print(histo[i])
        newHisto[i] = avg / ((2 * k) + 1)
        i += 1
        num = 0
    c = 0
    while c < ((w + 1) // 2):
        newHisto[c] = 0.0
        c += 1
    return np.array(newHisto)


def helperSmoothWin7(histo, k, w):
    l = histo.size
    i = 0
    newHisto = [0.0] * (256)
    while i < l:
        sum = histo[i]
        num = 1
        if i + 1 < l:
            num += 1
            sum += histo[i + 1]
        if i + 2 < l:
            num += 1
            sum += histo[i + 2]
        if i + 3 < l:
            num += 1
            sum += histo[i + 3]
        if i + 4 < l:
            num += 1
            sum += histo[i + 4]
        if i + 5 < l:
            num += 1
            sum += histo[i + 5]
        if i + 6 < l:
            num += 1
            sum += histo[i + 6]

        avg = sum / num
        # print(avg/((2*k)+1))
        # print(histo[i])
        newHisto[i] = avg / ((2 * k) + 1)
        i += 1
        num = 0
    c = 0
    while c < ((w + 1) // 2):
        newHisto[c] = 0.0
        c += 1
    return np.array(newHisto)


def helperHistoPlot(histo, name, type):
    # show the plotting graph of an image

    # plt.hist(histo,256,[((w+1)/2),255])
    plt.title(name)
    plt.set_cmap("gray")
    if type == 1:
        plt.plot(histo)
        plt2.savefig("Before_Smoothing.jpg")
    elif type == 2:
        plt.xlabel("Before index 1 the values are = 0 'Neglected'")
        plt.plot(histo, label="x < 1 is = 0")
        plt.legend(loc=1, prop={"size": 10})
        plt2.savefig("After_Smoothing_Win3.jpg")
    elif type == 3:
        plt.xlabel("Before index 3 the values are = 0 'Neglected'")
        plt.plot(histo, label="x < 3 is = 0")
        plt.legend(loc=1, prop={"size": 10})
        plt2.savefig("After_Smoothing_Win7.jpg")
    plt.show()


if __name__ == '__main__':
    print("Question 1 in Assignment 1 \n \n")
img = cv2.imread("sphinx.jpeg", 0)
data = img.ravel()

oldH = cv2.calcHist([img], [0], None, [256], [0, 256])  # helperHistogram(data)
helperHistoPlot(oldH, "Original Histogram",1)
plt.style.use('ggplot')

newHistWin3 = helperSmoothWin3(oldH, 3, 3)
helperHistoPlot(newHistWin3, "New Histogram with K = 3 and Window Size = 3",2)

newHistWin7 = helperSmoothWin7(oldH, 11, 7)
helperHistoPlot(newHistWin7, "New Histogram with K = 11 and Window Size = 7",3)

# print (np.array(newHisto.size))
# newH = helperSmoothWin3(oldH,2)

# print("New histo",newHisto, " ,its size: ", newHisto.size)
# print(type(oldH))
# print("old histo", oldH, " ,its size: ", oldH.size)


# newH
