import json
import os
from pprint import pprint
from tag import count_words
import sys
import random
from sklearn import svm
import numpy as np
import pickle
from sklearn.externals import joblib

pkl_file = open(os.path.join(os.path.dirname(__file__),'matrix.pkl'), 'rb')
#itemplist = pickle.load(pkl_file, encoding='latin1')
pkl_file.close()
#a = itemplist.todense().tolist()

clf = joblib.load(os.path.join(os.path.dirname(__file__),'clf.pkl'))

def predict(json):

    # with open('projects_with_users.json') as data_file:
    #    data = json.load(data_file)

    # pprint([x for x in data if x['winner'] == True])
    # print(len(data))
    #random.shuffle(data)
    # Win vector
    #win_vector = [1 if x['winner'] else 0 for x in data]
    #print(win_vector)

    #data = data[:100]
    # data2 = []
    # for proj in data:
    #     if proj['winner']:
    #         data
    # data = [y for y in data if y['winner'] == True]
    # print(len(data))
    # cv_win = [1 if x['winner'] else 0 for x in data]

    data = [json]
    count_vectors = [count_words(x['description']) for x in data]

    pkl_file = open(os.path.join(os.path.dirname(__file__),'words.pkl'), 'rb')
    words = pickle.load(pkl_file, encoding='latin1')
    pkl_file.close()

    # maxOcc = [ ]
    # minOcc = [ ]
    # for j in range(0, len(words) + 3):
    #     maxOcc.append(0)
    #     minOcc.append(0)

    matrix = [ ]
    for i in range(0, len(count_vectors)):
        row = [ ]
        for j in range(0, len(words)):
            cnt = 0
            for item in count_vectors[i]:
                if words[j] == item[0]:
                    cnt = item[1]
            row.append(cnt)
            # if cnt > maxOcc[j]:
            #     maxOcc[j] = cnt
            # if cnt < minOcc[j]:
            #     minOcc[j] = cnt
        matrix.append(row)

    row = 0
    for element in data:
        nr_wins = 0
        nr_projects = 0
        nr_hacks = 0
        for author in element["authors"]:
            nr_wins = nr_wins + author["wins"]
            nr_projects = nr_projects + author["projects"]
            nr_hacks = nr_hacks + author["hackathons"]

        if nr_projects == 0:
            matrix[row].append(0)
        else:
            matrix[row].append(float(nr_wins) / nr_projects)
        matrix[row].append(nr_wins)
        matrix[row].append(nr_hacks)

        row = row + 1

    pkl_file = open(os.path.join(os.path.dirname(__file__),'maxOcc.pkl'), 'rb')
    maxOcc = pickle.load(pkl_file, encoding='latin1')
    pkl_file.close()


    for i in range(0, len(matrix)):
        for j in range(0, len(matrix[i])):
            matrix[i][j] = float(matrix[i][j]) / maxOcc[j]

    win_vector = np.loadtxt(os.path.join(os.path.dirname(__file__),'win_vector.txt')).tolist()


    #n_matrix = np.array(matrix, size=[100,len(matrix[0])])
    # print(len(matrix[0]) == len(matrix[1]))
    # print(len(win_vector))
    #print(n_matrix[0])
    #n_win_vector = np.int64(win_vector)
    # print(win_vector[0])

    #print(len(a),len(win_vector))
    # x,y = a, win_vector


    # clf = svm.SVC(gamma=0.001, C=100)
    # clf.fit(x,y)
    # joblib.dump(clf, 'clf.pkl')


    hits = 0;
    hits_0 = 0;

    return (clf.predict([matrix[0]])[0] == 1.0)

# print(matrix)
# np.savetxt('maxOcc.txt', maxOcc)
# np.savetxt('words.txt', words)
# np.savetxt('matrix.txt', matrix, fmt="%.6f")

# print(len(win_vector))
#
# for i in range(0, len(win_vector)):
#     if (win_vector[i] != data[i]):
#         print(i)

# print("prediction:", clf.predict(matrix[-10])[0])
# print("actual:", win_vector[-10])


# print matrix[1]
#

#with open('projects_with_users.json') as data_file:
#   data = json.load(data_file)

#win_vector = [1 if x['winner'] else 0 for x in data]
#
#for i in range(0,len(data)):
#    print(predict(data[i]), win_vector[i])
