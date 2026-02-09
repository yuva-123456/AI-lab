import math
from collections import Counter
from sklearn.metrics import confusion_matrix

X = ["Rain", "Sunny", "Rain", "Rain", "Sunny"]
y = ["Yes", "No", "Yes", "Yes", "No"]

def entropy(l):
    t = len(l)
    return -sum((c/t) * math.log2(c/t) for c in Counter(l).values())

def gini(l):
    t = len(l)
    return 1 - sum((c/t) ** 2 for c in Counter(l).values())

y_pred = ["Yes" if w == "Rain" else "No" for w in X]
cm = confusion_matrix(y, y_pred, labels=["Yes", "No"])

TP, FN = cm[0]
FP, TN = cm[1]

print("Entropy:", round(entropy(y), 3))
print("Gini Index:", round(gini(y), 3))

print("\nConfusion Matrix")
print("TP   FP")
print(TP, "  ", FP)
print(FN, "  ", TN)
print("FN   TN")
