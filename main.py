import numpy as np
import pandas as pd
from scipy import sparse
from sklearn.preprocessing import normalize


df4 = pd.read_csv('lastfm_user_scrobbles.csv')
df2 = pd.read_csv('lastfm_artist_list.csv')

df2.index = df2['artist_id']
title_dict = df2["artist_name"].to_dict()


def find_key(value):
    for key, val in title_dict.items():
        if val.lower() == value.lower():
            return key
    return None


def find_similar(val):
    return [title_dict[i+1] for i in sim[val-1].toarray().argsort()[0][-20:]]

def recommend_to_user(val):
    return [title_dict[i+1] for i in fit[1892].toarray().argsort()[0][-10:].tolist()]

# txt = input("Введите название исполнителя: ")
#
# print(find_similar(find_key(txt)))





txt = input("Введите топ любимых исполнителей: ")
user_list = txt.split(', ')


user_list1 = []

for i in user_list:
    i=find_key(i)
    if ( i!= None):
        user_list1.append(i)

user_scor = []
i=len(user_list1)
while (i>0):

    user_scor.append(i)
    i=i-1

dict = {'user_id':[1893]*len(user_list1),
        'artist_id':user_list1,
        'scrobbles':user_scor
       }
df3 = pd.DataFrame(dict)
df1 = pd.concat([df4, df3], ignore_index = True)
df1.reset_index()

rows, r_pos = np.unique(df1.values[:, 0], return_inverse = True)
cols, c_pos = np.unique(df1.values[:, 1], return_inverse = True)
interaction_sparse = sparse.csr_matrix((df1.values[:, 2], (r_pos, c_pos)))

##Нормализуем и получаем матрицу похожести

Pui = normalize(interaction_sparse, norm='l2', axis=1)
sim = Pui.T * Pui

interaction_sparse_t = interaction_sparse.transpose(copy=True)
Piu = normalize(interaction_sparse_t, norm='l2', axis=1)

fit = Pui * Piu * Pui

print([title_dict[i+1] for i in np.nonzero(interaction_sparse[1892])[1].tolist()])

recommend_list = fit[1892].toarray().argsort()[0][-len(user_list1)-10:].tolist()

recommend_list = [i for i in recommend_list if i not in user_list1]

print( [title_dict[i+1] for i in recommend_list])





