# Using naive bayes classification to define article group.

import numpy as np
import pandas as pd
from sklearn.datasets import fetch_20newsgroups
import matplotlib.pyplot as plt
import seaborn as sns; sns.set()

data = fetch_20newsgroups(subset='all', remove=('headers', 'footers', 'quotes'))
categories = data.target_names

train = fetch_20newsgroups(subset="train", categories=categories)
test = fetch_20newsgroups(subset="test", categories=categories)

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline, make_pipeline

model = make_pipeline(TfidfVectorizer(), MultinomialNB())

model.fit(train.data, train.target)

labels = model.predict(test.data)

from sklearn.metrics import confusion_matrix
mat = confusion_matrix(test.target, labels)
sns.heatmap(mat.T, square = True, annot=True, fmt="d", cbar=False
            , xticklabels = train.target_names
            , yticklabels = train.target_names)

plt.xlabel("True Label")
plt.ylabel("Predicted Label")
plt.show()


def predict_category(s, train=train, model=model):
    pred = model.predict([s])
    print(train.target_names[pred[0]])


predict_category("yamaha engines trouble")

accuracy = model.score(test.data, test.target)
print(accuracy)