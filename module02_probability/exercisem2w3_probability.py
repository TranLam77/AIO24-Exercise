# -*- coding: utf-8 -*-
"""ExerciseM2W3.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1kn9a8_08HtJHaND-XTA60Au0O2opl5h5

#4.1 create_train_data()
"""

# ########################
# Create data
# ########################
import numpy as np

def create_train_data () :
    data = [['Sunny','Hot','High','Weak','no'],
            ['Sunny','Hot','High','Strong','no'],
            ['Overcast','Hot','High','Weak','yes'],
            ['Rain','Mild','High','Weak','yes'],
            ['Rain','Cool','Normal','Weak','yes'],
            ['Rain','Cool','Normal','Strong','no'],
            ['Overcast','Cool','Normal','Strong','yes'],
            ['Overcast','Mild','High','Weak','no'],
            ['Sunny','Cool','Normal','Weak','yes'],
            ['Rain','Mild','Normal','Weak','yes']]

    return np.array(data)

train_data = create_train_data()
print (train_data)

"""# 4.2. compute_prior_probablity()"""

def compute_prior_probablity(train_data):
    y_unique = ['no', 'yes']
    prior_probability = np.zeros(len(y_unique))
    # your code here ******************
    prior_probability[0] = len(train_data[train_data[:, -1] == 'no']) / len(train_data)
    prior_probability[1] = len(train_data[train_data[:, -1] == 'yes']) / len(train_data)
    return prior_probability

prior_probablity = compute_prior_probablity (train_data)
print("P(play tennis = No) =", prior_probablity[0])
print("P(play tennis = Yes) =", prior_probablity[1])

"""# 4.3 compute_conditional_probability()"""

def compute_conditional_probability(train_data):
    y_unique = ['no', 'yes']
    conditional_probability = []
    list_x_name = []

    for i in range(0, train_data.shape[1]-1):
        x_unique = np.unique(train_data[:,i])
        list_x_name.append(x_unique)
        # your code here ********************
        x_conditional_probability = np.zeros((len(y_unique), len(x_unique)))
        for j in range(len(x_unique)):
            x_conditional_probability[0, j] = len(train_data[(train_data[:, i] == x_unique[j]) & (train_data[:, -1] == y_unique[0])]) / len(train_data[train_data[:, -1] == y_unique[0]])
            x_conditional_probability[1, j] = len(train_data[(train_data[:, i] == x_unique[j]) & (train_data[:, -1] == y_unique[1])]) / len(train_data[train_data[:, -1] == y_unique[1]])
        conditional_probability.append(x_conditional_probability)

    return conditional_probability, list_x_name

conditional_probability , list_x_name = compute_conditional_probability(train_data)
print ("x1 = ", list_x_name[0])
print ("x2 = ", list_x_name[1])
print ("x3 = ", list_x_name[2])
print ("x4 = ", list_x_name[3])

"""# 4.4 get_index_from_value()"""

# This function is used to return the index of the feature name
def get_index_from_value (feature_name, list_features):
    return list_features.where(feature_name)[0][0]

outlook = list_x_name[0]
i1 = get_index_from_value ("Overcast", outlook)
i2 = get_index_from_value ("Rain", outlook)
i3 = get_index_from_value ("Sunny", outlook)

print (i1, i2, i3)

"""# P(’Outlook’=’Sunny’|Play Tennis’=’Yes’)"""

train_data = create_train_data()
conditional_probability, list_x_name = compute_conditional_probability(train_data)
# Compute P(" Outlook "=" Sunny "| Play Tennis "=" Yes ")
x1 = get_index_from_value ("Sunny", list_x_name[0])

print("P('Outlook' = 'Sunny'|Play Tennis = 'Yes') = ", np.round(conditional_probability[0][1,x1],2))

"""# P(’Outlook’=’Sunny’|Play Tennis’=’No’)"""

train_data = create_train_data()
conditional_probability, list_x_name = compute_conditional_probability(train_data)

# Compute P(" Outlook "=" Sunny "| Play Tennis "=" No ")
x1 = get_index_from_value ("Sunny", list_x_name[0])
print ("P('Outlook' = 'Sunny'| Play Tennis = 'No') = ", np.round(conditional_probability[0][0,x1], 2))

"""# 4.5 train_naive_bayes()"""

# ##########################
# Train Naive Bayes Model
# ##########################
def train_naive_bayes(train_data):
    # Step 1: Calculate Prior Probability
    prior_probability = compute_prior_probablity(train_data)

    # Step 2: Calculate Conditional Probability
    conditional_probability , list_x_name = compute_conditional_probability(train_data)

    return prior_probability , conditional_probability , list_x_name

"""# 4.6 prediction_play_tennis()"""

# ###################
# Prediction
# ###################
def prediction_play_tennis(x, list_x_name, prior_probability, conditional_probability):

    x1 = get_index_from_value(x[0], list_x_name[0])
    x2 = get_index_from_value(x[1], list_x_name[1])
    x3 = get_index_from_value(x[2], list_x_name[2])
    x4 = get_index_from_value(x[3], list_x_name[3])

    p0 = 0
    p1 = 0

    # your code here ***********************
    p0 = conditional_probability[0][0,x1] * conditional_probability[1][0,x2] * conditional_probability[2][0,x3] * conditional_probability[3][0,x4] * prior_probability[0]
    p1 = conditional_probability[0][1,x1] * conditional_probability[1][1,x2] * conditional_probability[2][1,x3] * conditional_probability[3][1,x4] * prior_probability[1]

    if p0 > p1 :
        y_pred = 0
    else :
        y_pred = 1

    return y_pred

"""# X = ['Sunny','Cool','High','Strong']"""

X = ['Sunny','Cool','High','Strong']
data = create_train_data ()
prior_probability , conditional_probability , list_x_name = train_naive_bayes(data)
pred = prediction_play_tennis(X, list_x_name, prior_probability, conditional_probability)

if(pred) :
    print("Ad should go!")
else :
    print("Ad should not go!")