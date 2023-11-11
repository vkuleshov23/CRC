
def dop1(gs, l, p):
	pes = []
	lables = []
	global gx
	for g in gs:
		gx = np.array(g)
		pes.append(getP_Pe_ceil(p,l))
		lables.append("Верхняя граница " + toMath(gx))
		pes.append(getP_Pe(p,l))
		lables.append("Точное вычисление " + toMath(gx))
	plot(pes, p, lables)


def dop2(g, ls, p):
	pes = []
	lables = []
	global gx
	gx = np.array(g)
	for l in ls:
		pes.append(getP_Pe_ceil(p,l))
		lables.append("Верхняя граница (l=" + str(l) + ") " + toMath(gx))
		pes.append(getP_Pe(p,l))
		lables.append("Точное вычисление (l=" + str(l) + ") " + toMath(gx))
	plot(pes, p, lables)	

def dop3(g, ls, p):
	pes = []
	lables = []
	global gx
	gx = np.array(g)
	for l in ls:
		pes.append(getP_Pe_ceil(p,l))
		lables.append("Верхняя граница (l=" + str(l) + ") " + toMath(gx))
		pes.append(getP_Pe(p,l))
		lables.append("Точное вычисление (l=" + str(l) + ") " + toMath(gx))
	plot(pes, p, lables)


# dop1([[1,1], [1,1,1], [1,0,1,1], [1,0,0,1,1], [1,0,1,0,1], [1,1,1,0,1], [1,1,0,0,1], [1,1,1,1,1]], l, p)
# dop1([[1,1,1], [1,0,1,1]], l, p)

# dop2([1,0,1,1], [3,4,5,6,7,8,9], p)


dop2([1,0,1,1], [3,4,5,6,7,8,9], [0.1, 0.2, 0.3])
