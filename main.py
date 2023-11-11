import numpy as np
import numpy.random as random
import itertools as it
import matplotlib.pyplot as plt

def toMath(polynom):
	if 1 not in polynom:
		return "0"
	string = ""
	for i in range(len(polynom)):
		if polynom[i] != 0:
			if i != len(polynom)-1:
				string += "x^" + str(len(polynom)-1-i) + " + "
			else:
				string += "1 + "
	return string[:len(string)-3]

def clearBegin(g):
	indexes = []
	for i in range(len(g)-1):
		if g[i] == 0:
			indexes.append(i)
		else:
			break
	g = np.delete(g, indexes)
	return g

def deg():
	index = 0
	for i in range(len(gx)):
		if gx[i] == 1:
			break
		index = i
	return len(gx)-index-1

def getXr():
	index = deg()
	xr = []
	for i in range(index):
		xr.append(0)
	return np.array(xr)

def mul_xr(m):
	return np.append(m, getXr())

def bin_mod(m):
	for i in range(len(m)):
		if np.isnan(m[i]):
			m[i] = 0
		m[i] = (int)(m[i]%2)
	return m

def code(msg):
	mxr = mul_xr(msg)
	_,c = np.polydiv(mxr, gx)
	c = bin_mod(c)
	return np.polyadd(mxr, c)

def plot(pes, p, legends):
	for pe in pes:
		plt.plot(p, pe)
	plt.legend(legends)
	plt.grid(True)
	plt.show()

def C(n, k):
	return len(list(it.combinations(range(0, n), k)))

def getMsgsOld(l):
	msgs = np.zeros((2**l, l))
	for r in range(2**l):
		msg = np.unpackbits(np.uint8(r))
		msgs[r] = np.array(msg[len(msg)-l:])
	return msgs

def getbit(num, index):
	if (num & (1 << index)) == 0:
		return 0
	else:
		return 1

def getMsgs(l):
	msgs = []
	for i in range(2**l):
		msg = []
		for x in range(l):
			msg.insert(0,getbit(i, x))
		msgs.append(msg)
	return np.array(msgs)

def getWords(l):
	words = np.zeros((2**l, l+deg()))
	msgs = getMsgs(l)
	for i in range(len(msgs)):
		words[i] = code(msgs[i])
	return words

def isNull(word):
	for i in range(len(word)):
		if word[i] == 1:
			return False
	return True

def getAllD(words):
	d = []
	for i in range(len(words)):
		if False == isNull(words[i]):
			d.append(getWeight(words[i]))
	return np.array(d)

def calculateD(l):
	words = getWords(l)
	d = getAllD(words)
	return np.min(d)

def Pe_ceil(d, n, p):
	summ = 0
	for i in range(0, d):
		summ += C(n, i)*(p**i)*((1-p)**(n-i))
	return 1-summ

def getP_Pe_ceil(p, l):
	Pe_c = np.zeros(len(p))
	d = calculateD(l)
	print("gx:", gx)
	print("d:", d)
	print("n:", l+deg())
	for i in range(len(p)):
		Pe_c[i] = Pe_ceil(d, l+deg(), p[i])
		# print(Pe_c[i])
	return Pe_c


def getWeight(word):
	d = 0
	for i in range(len(word)):
		if (word[i] == 1):
			d += 1
	return d

def Ai(words, i):
	ai = 0
	for x in range(len(words)):
		if getWeight(words[x]) == i:
			ai += 1
	return ai

def Pe(d, n, p, words):
	summ = 0
	for i in range(d, n+1):
		summ += Ai(words, i)*(p**i)*((1-p)**(n-i))
	return summ

def getP_Pe(p, l):
	Pe_ = np.zeros(len(p))
	d = calculateD(l)
	# print("d:", d)
	words = getWords(l)
	for i in range(len(p)):
		Pe_[i] = Pe(d, len(words[0]), p[i], words)
		# print(Pe_[i])
	return Pe_

def dopusk5task():
	words = getWords(5)
	for word in words:
		if(getWeight(word) < 3):
			print(word)


def mainCode(g, l, p):
	global gx
	gx = clearBegin(np.array(g))
	pe_ceil = getP_Pe_ceil(p, l) # Если w(e(x)) > d -> (w(e(x)) - вес вектора ошибок) ; (d - минимальное расстояние кода)
	pe = getP_Pe(p, l) # Если e(x) == a(x) -> если вектор ошибок является кодовым словом
	plot([pe_ceil, pe], p, ["Верхняя граница l=" +str(l), "Точное вычисление l=" + str(l)])

def main(gx, p):
	for i in range(2,7):
		print("Messages:")
		print(getMsgs(i))
		print()
		print("Code:")
		print(getWords(i))
		mainCode(gx, i, p)

def printW(words):
	for word in words:
		print(getWeight(word))

p = []
for i in range(0,1001, 1):
	p.append(i/1000)
p = np.array(p)
# p = np.array([0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0])

def dop(p,l):
	global gx
	pe_ceils = []
	pe_ceils_labels = []
	pes = []
	pes_labels = []
	Dmins = []
	Dmins_labels = []
	Dmins_x = []
	gxs = getMsgs(l)
	for i in range(2,len(gxs)):

		# printW(getWords(l))
		# print()

		gx = clearBegin(np.array(gxs[i]))

		pe_ceils.append(getP_Pe_ceil(p, l))
		pe_ceils_labels.append("Верхняя граница " + str(gx))
		
		pes.append(getP_Pe(p, l))
		pes_labels.append("Точное вычисление " + str(gx))
		
		Dmins.append(int(calculateD(l)))
		Dmins_x.append(str(gx))
		Dmins_labels.append("Dmin " + str(gx))
	
	plot(pe_ceils, p, pe_ceils_labels)
	plot(pes, p, pes_labels)
	plt.plot(Dmins_x, Dmins)
	plt.show()	


gx = clearBegin(np.array([1,0,1,1]))
l = 5

main(gx, p)
# dop(p, 4)
# dopusk5task()