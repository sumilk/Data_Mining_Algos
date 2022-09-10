import numpy as np
import pandas as pd
import scipy.spatial.distance as dist

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('display.width', None)

class KMeans:
    def __init__(self,  points, centroids, distance='Euclidean'):
        self.points = points
        self.centroids = centroids
        self.distance = distance
        self.n_clusters = len(self.centroids)
        self.centroid_list = [self.centroids]

    def cal_distance(self, x1, x2):
        if self.distance == 'Euclidean':
            return round(dist.euclidean(x1,x2),2)
        elif self.distance == 'Manhattan':
            return sum([abs(i-j) for i,j in zip(x1,x2)])

    def cal_new_centroid(self, cluster_df):
        self.cluster_group_df = cluster_df.groupby('Cluster')['Points'].apply(list).reset_index(name='point_list')
        centroids =  self.cluster_group_df['point_list'].apply(lambda x: self.average_tuple(x)).values
        self.cluster_group_df['New Centroid'] = centroids
        return centroids

    def average_tuple(self, points):
        return tuple(map(lambda x: round(sum(x) / float(len(x)),2), zip(*points)))


    def cluster(self):
        iteration = 1
        while len(self.centroid_list) == 1 or self.centroid_list[iteration-1] != self.centroid_list[iteration -2]:
            print(f'\n\nIteration {iteration}:\n')
            cluster_df = pd.DataFrame()
            cluster_df['Points'] = self.points
            for i, centroid in enumerate(self.centroid_list[iteration-1]):
                cluster_df[f'Dist From Centroid {i+1} {centroid}'] = cluster_df['Points'].apply(lambda x: self.cal_distance(x, centroid))
            cluster_df['Cluster'] = cluster_df.drop(columns='Points').apply(np.argmin, axis=1)
            cluster_df['Cluster'] +=1
            iteration+=1
            new_centroid = self.cal_new_centroid(cluster_df)
            self.centroid_list.append(list(new_centroid))
            print(f'Distance Matrix: \n{cluster_df}', end='\n\n')
            print(self.cluster_group_df)
            print(f'\nNew Centroid: {new_centroid}')

if __name__ == '__main__':
    KMeans(points=[(2,10), (2,5), (8,4), (5,8), (7,5),(6,4), (1,2), (4,9)] , centroids=[(2,10), (5,8), (1,2)]).cluster()
    #KMeans(points=[(2, 10), (2, 5), (8, 4), (5, 8), (7, 5), (6, 4), (1, 2), (4, 9)], centroids=[(2, 10), (5, 8), (1, 2)], distance= 'Manhattan').cluster()