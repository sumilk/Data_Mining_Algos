from operator import index
import numpy as np
from scipy.spatial import distance_matrix



def k_dist_matrix(dist, indices, k):
	k_dist = []
	print("\n Calculate all the dist(0) with k = ", k)
	for i in range(0, len(dist[0])):
		res = dict(zip(indices, dist[i]))
		res = sorted((value, key) for (key,value) in res.items())
		sortdict = dict([(k,v) for v,k in res])
		key_list = list(sortdict.keys())
		val_list = list(sortdict.values())
		# print(sortdict)
		print("Dist-", k, "(", indices[i], ") = dist(", indices[i], ", ", key_list[k], ") = ", val_list[k])
		k_dist.append(val_list[k])
	return k_dist

def k_dist_neighbor(dist, k_dist, indices):
	print("\n Calculate all the Nk(o). k-distance neighborhood of o, Nk(o) = {o'|o' in D, dist(o, o') distk(o)}")
	k_neigh = []
	temp = []
	k_neigh_val = []
	temp_val = []
	for i in range(0, len(dist[0])):
		for j in range(0, len(dist[0])):
			if dist[i][j] <= k_dist[i] and dist[i][j] != 0:
				# print(indices[j])
				temp_val.append(dist[i][j])
				temp.append(indices[j])
		k_neigh.append(temp)
		k_neigh_val.append(temp_val)
		print("N", k, "(", indices[i], ") = ", temp, "val = ", temp_val)
		temp_val = []
		temp = []
		
	# print(k_neigh)
	# print(k_neigh_val)
	return k_neigh, k_neigh_val


def reachdist(to_ind, fom_ind, k_dist, dist, indices):
	to = indices.index(to_ind)
	fom = indices.index(fom_ind)
	max_ = max(k_dist[to], dist[to, fom])
	print("reachdistk(", indices[to], "<--", indices[fom], ") = max{distk(", indices[to], ", dist(", indices[to], ",", indices[fom], ")} = max(", k_dist[to], ",", dist[to, fom], ") = ", max_)
	return max_


def lrd(dist, k_neigh, k_dist, indices, k):
	print("\n Calculating lrd:")
	lrd_arr = []
	for num, i in enumerate(k_neigh):
		denom = 0
		for j in i:
			denom = denom + reachdist(j, indices[num], k_dist, dist, indices)
		lrd_val = len(i)/denom
		lrd_arr.append(lrd_val)
		print("   - Lrd-",k,"(",indices[num],") = ", len(i), "/" ,denom, " = ", lrd_val)
	return lrd_arr
		


def dist_matrix(x, y, type):
	dist_mat = distance_matrix(x, y, p=type)
	print("\n Calculate all the distances between each two points:")
	print(dist_mat)
	return dist_mat



# k = 2
# # p = 1, Manhattan Distance
# # p = 2, Euclidean Distance
# # p = ∞, Chebychev Distance
# type = 1
# indices = ['a', 'b', 'c', 'd']
# points = [[0, 0], [0, 1], [1, 1], [3, 0]]

k = 3
type = 1
indices = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
points = [[1.0, 2.0], [2.0, 1.5], [1.0, 1.5], [2.0, 2.75], [7.0, 2.25], [7.0, 2.5], [7.0, 2.0], [7.5, 2.25], [6.0, 2.5]]

dist = dist_matrix(points, points, 1)
k_dist = k_dist_matrix(dist, indices, k)
k_neigh, kneigh_val = k_dist_neighbor(dist, k_dist, indices)
lrd(dist, k_neigh, k_dist, indices, k)

