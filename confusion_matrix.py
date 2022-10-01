# Importing the dependancies
from sklearn import metrics
from sklearn.metrics import accuracy_score
# Predicted values
# y_pred = ["x", "x", "x", "y", "y", "y", "z", "z", "z", "z"]
y_pred = [1, 1, 1, 2, 2, 2, 3, 3, 3, 3]
# Actual values
# y_act = ["y", "x", "z", "y", "y", "y", "x", "x", "x", "z"]
y_act = [2, 1, 3, 2, 2, 2, 1, 1, 1, 3]
# Printing the confusion matrix
# The columns will show the instances predicted for each label,
# and the rows will show the actual number of instances for each label.
print(metrics.confusion_matrix(y_act, y_pred))
# Printing the precision and recall, among other metrics
print(metrics.classification_report(y_act, y_pred))

# print("accuracy: ")
# matrix = metrics.confusion_matrix(y_act, y_pred)
# print(matrix.diagonal()/matrix.sum(axis=1))

print("total accuracy: ")
print(accuracy_score(y_act, y_pred))