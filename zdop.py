import matplotlib.pyplot as plt
import csv
 
# def Plot(ernoP, p, l):

#     pl.plot(p, ernoP)
#     pl.title('l=' + str(l))
#     myfile = 'l' + str(l) + '.png'
#     pl.grid(True)
#     pl.savefig(myfile)

#     pl.grid(True)
#     pl.show()

def getData(filename):
    X = []
    Y = []
    with open(filename) as datafile:
    plotting = csv.reader(datafile, delimiter=' ')

    for ROWS in plotting:
        X.append(float(ROWS[0]))
        Y.append(float(ROWS[1]))
    return X, Y

def DOPB():
    path = "C:\\Users\\user\\source\repos\\NetworkLAb1\\NetworkLAb1\\"
    x, y = getData(path + str(4) + ".txt")
    plt.plot(X, Y)

    for i in range(1,3):
        X, Y = getData(path +'dopB'+ str(i) +'.txt')
        plt.plot(X, Y)
    plt.title('DOP B')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.show()



def main():
    X = []
    Y = []
    path = 'C:\\Users\\user\\source\\repos\\NetworkLAb1\\NetworkLAb1\\'
    for i in range(2,6):
        X, Y = getData(path + str(i) +'.txt')
        plt.plot(X, Y)
        
        plt.title('Line Graph using CSV')
        plt.xlabel('X')
        plt.ylabel('Y')
        plt.show()
        X = []
        Y = []


DOPB()