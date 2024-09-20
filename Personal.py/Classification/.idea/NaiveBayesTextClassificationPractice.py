
from sklearn.datasets import load_wine
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import seaborn as sns

wine = load_wine()

x = wine.data
y = wine.target

x_train, x_test, y_train, y_test = train_test_split(x, y, random_state=0)

from sklearn.naive_bayes import GaussianNB

gnb = GaussianNB().fit(x_train, y_train)
gnb_predictions = gnb.predict(x_test)

accuracy = gnb.score(x_test, y_test)
print(accuracy)

mat = confusion_matrix(y_test, gnb_predictions)
sns.heatmap(mat, annot=True)
plt.show()
