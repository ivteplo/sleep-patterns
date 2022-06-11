#!/usr/bin/env python
# coding: utf-8

# In[2]:


import matplotlib.pyplot
import numpy
import pandas

from sklearn import tree, metrics


# In[3]:


# Function to replace 'yes' or 'no' with 1.0 or 0.0 in a dataframe row
def replace_yes_no(row):
    def update_value(value):
        if value in ("Yes", "No"):
            return 1.0 if value == "Yes" else 0.0
        return float(value)
    
    return [ update_value(x) for x in row ]

# Load a dataset, convert 'yes' or 'no' to 1.0 or 0.0, and remove NaN values
def load_dataset(path):
    return pandas.read_csv(path).apply(replace_yes_no).dropna()


# In[4]:


dataframe = load_dataset("datasets/SleepStudyData.csv")
dataframe


# In[5]:


def get_data(dataframe):
    # Remove column with answers to create the input dataframe
    input_data = dataframe.drop(columns = ["Enough"])

    # Just grab the column with answers to create the expected output dataframe
    output_data = dataframe["Enough"]
    
    return input_data, output_data


# In[6]:


input_data, output_data = get_data(dataframe)


# In[7]:


# Pass training data to the decision tree classifier
classifier = tree.DecisionTreeClassifier()
classifier.fit(input_data, output_data)


# In[8]:


# Set the image size (in inches)
matplotlib.pyplot.figure(figsize = (25, 20))

# Generate the image
output = tree.plot_tree(classifier, feature_names = input_data.columns, 
                        fontsize = 8, rounded = True, class_names = ["Not Enough", "Enough"])


# In[9]:


# Run the test dataset
test_dataset = load_dataset("datasets/SleepStudyPilot.csv")
test_input_data, test_output_data = get_data(test_dataset)

# Get the predictions
predictions = classifier.predict(test_input_data)

# Calculate the accuracy score
metrics.accuracy_score(test_output_data, predictions)


# In[14]:


enough = dataframe[dataframe["Enough"] == 1]
not_enough = dataframe[dataframe["Enough"] == 0]


# In[11]:


enough.mean()


# In[15]:


not_enough.mean()

