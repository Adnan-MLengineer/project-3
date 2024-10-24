"""
# **Importing the Dependencies**
"""

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

"""# **Data Collection and Data Processing**"""

# Loading the dataset to a Pandas Dataframe
sonar_data = pd.read_csv('/content/sonar data.csv', header = None)

sonar_data.head()

# Number of Rows and Columns
sonar_data.shape

sonar_data.describe()

sonar_data[60].value_counts()

sonar_data.groupby(60).mean()

# Separating Data and Lables
X = sonar_data.drop(columns = 60, axis = 1)
Y = sonar_data[60]

print(X, Y)

"""# **Training and Testing Data**"""

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.1, stratify=Y, random_state=1)

print(X.shape, X_train.shape, X_test.shape)

"""# **Model Training - Logistic Regression**"""

model = LogisticRegression()

# Training Logistic Regression model with training data
model.fit(X_train, Y_train)

"""# **Model Evaluation**"""

# Accuracy on Training Data
X_train_prediction = model.predict(X_train)
training_data_accuracy = accuracy_score(X_train_prediction, Y_train)

print(f'The accuracy on training data is {training_data_accuracy}')

# Accuracy on Testing Data
X_test_prediction = model.predict(X_test)
testing_data_accuracy = accuracy_score(X_test_prediction, Y_test)

print(f'The accuracy on testing data is {testing_data_accuracy}')

"""# **Making a Predictive System**"""

input_data = (0.0715,0.0849,0.0587,0.0218,0.0862,0.1801,0.1916,0.1896,0.2960,0.4186,0.4867,0.5249,0.5959,0.6855,0.8573,0.9718,0.8693,0.8711,0.8954,0.9922,0.8980,0.8158,0.8373,0.7541,0.5893,0.5488,0.5643,0.5406,0.4783,0.4439,0.3698,0.2574,0.1478,0.1743,0.1229,0.1588,0.1803,0.1436,0.1667,0.2630,0.2234,0.1239,0.0869,0.2092,0.1499,0.0676,0.0899,0.0927,0.0658,0.0086,0.0216,0.0153,0.0121,0.0096,0.0196,0.0042,0.0066,0.0099,0.0083,0.0124)
# Changing the input_data into numpy array
input_data_as_numpy_array = np.asarray(input_data)

# Reshape the numpy array as we are predicting for one instance
input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)
prediction = model.predict(input_data_reshaped)
print(prediction)
if(prediction[0] == 'R'):
  print("The object is a Rock")

else:
  print("It is a Mine")

