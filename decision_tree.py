import matplotlib.pyplot as plt
import numpy as np
import math

def gini(a):
	count0 = a.count(0)
	count1 = a.count(1)
	count2 = a.count(2)
	length = len(a)
	p0 = count0/length
	p1 = count1/length
	p2 = count2/length

	gini = 1 - (p0)**2 - (p1)**2 - (p2)**2
	print("gini: 1 - ({0}/{1})^2 - ({2}/{3})^2 - ({4}/{5})^2 = {6}".format(count0, length, count1, length, count2, length, gini))
	return gini

	

def entropy(a):
	count0 = a.count(0)
	count1 = a.count(1)
	count2 = a.count(2)
	length = len(a)
	p0 = count0/length
	p1 = count1/length
	p2 = count2/length

	l0 = math.log(p0,2) if(p0 != 0) else 0
	l1 = math.log(p1,2) if(p1 != 0) else 0
	l2 = math.log(p2,2) if(p2 != 0) else 0

	entropy = - p0*l0 - p1*l1 - p2*l2
	print("entropy: - ({0}/{1})xlog(({0}/{1}) - ({2}/{3})xlog(({2}/{3}) - ({4}/{5})xlog(({4}/{5}) = {6}".format(count0, length, count1, length, count2, length, entropy))
	return entropy

def classification_error(a):
	count0 = a.count(0)
	count1 = a.count(1)
	count2 = a.count(2)
	length = len(a)
	p0 = count0/length
	p1 = count1/length
	p2 = count2/length
	print("p0: {0}/{1}".format(count0, length))
	print("p1: {0}/{1}".format(count1, length))
	print("p2: {0}/{1}".format(count2, length))
	pmax = max(p0, p1, p2)
	clas_err = 1 - pmax
	print("clas_err: 1 - {0} = {1}".format(pmax, clas_err))
	return clas_err

def gini_total(a, out):
	arr0, arr1, arr2 = split(a, out)
	count0 = len(arr0)
	count1 = len(arr1)
	count2 = len(arr2)
	total_count = count0 + count1 + count2
	gini0 = gini(arr0)
	gini1 = gini(arr1)
	if (count2 != 0):
		gini2 = gini(arr2)
	else:
		gini2 = 0
	p0 = count0/total_count
	p1 = count1/total_count
	p2 = count2/total_count

	gini_total = (p0)*gini0 + (p1)*gini1 + (p2)*gini2
	print("({0}/{1})x({2}) + ({3}/{4})x({5}) + ({6}/{7})x({8}) = {9}".format(count0, total_count, gini0, count1, total_count, gini1, count2, total_count, gini2, gini_total))
	return gini_total

def info_gain(a, out):
	arr0, arr1, arr2 = split(a, out)
	count0 = len(arr0)
	count1 = len(arr1)
	count2 = len(arr2)
	total_count = count0 + count1 + count2
	ent0 = entropy(arr0)
	ent1 = entropy(arr1)
	if (count2 != 0):
		ent2 = entropy(arr2)
	else:
		ent2 = 0
	p0 = count0/total_count
	p1 = count1/total_count
	p2 = count2/total_count

	infgain = (p0)*ent0 + (p1)*ent1 + (p2)*ent2
	print("({0}/{1})x({2}) + ({3}/{4})x({5}) + ({6}/{7})x({8}) = {9}".format(count0, total_count, ent0, count1, total_count, ent1, count2, total_count, ent2, infgain))
	return infgain	

def split(a, out):
	arr0 = []
	arr1 = []
	arr2 = []
	for i in range(0,len(a)):
		if(a[i] == 0):
			arr0.append(out[i])
		elif (a[i] == 1):
			arr1.append(out[i])
		else:
			arr2.append(out[i])
	print(arr0, arr1, arr2)

	return arr0, arr1, arr2




a = [1,0,1,1,1,0,1,1,0,1]
out = [1,0,1,1,0,0,0,0,0,1]

# a = ["summer", "winter", summer, summer ...../]

gini_before = gini(out)
gini_after = gini_total(a, out)
print("gini before split: ", gini_before)
print("gini after split: ", gini_after)
print("gain: ", gini_before - gini_after)

# info_before = entropy(out)
# info_after = info_gain(a, out)
# print("info before split: ", info_before)
# print("info after split: ", info_after)
# print("gain: ", info_before - info_after)

# info_before = classification_error(out)