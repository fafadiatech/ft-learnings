#Simple Spam Filter for SMS based on Random Forests

import os
import re
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.cross_validation import train_test_split
from sklearn.metrics import accuracy_score, f1_score, precision_score, recall_score, classification_report, confusion_matrix

def gen_features(df):
    """
    This method generates features given a data frame
    """
    upper_case_expression = re.compile(r"[A-Z]{2,}")
    numeric_expression = re.compile(r"\d+", re.IGNORECASE)
    specialchar_expression = re.compile(r"[^a-z0-9\s]", re.IGNORECASE)

    #List of transform functions that will compute features for us
    #1. Length of SMS
    #2. Number of Special Characters in SMS
    #3. Number of Uppercase Words
    #4. Number of Numeric Expressions in SMS
    #5. Number of Tokens in Marketing dictionary
    transform_functions = [
        lambda x: len(x),
        lambda x: len([result.group(0) for result in specialchar_expression.finditer(x)]),
        lambda x: len([result.group(0) for result in upper_case_expression.finditer(x)]),
        lambda x: len([result.group(0) for result in numeric_expression.finditer(x)]),
    ]

    columns = []
    for func in transform_functions:
        columns.append(df[df.columns[1]].apply(func))
    features = np.asarray(columns).T
    return features

spam_or_ham = lambda x: 1 if x.strip() == "ham" else -1
df = pd.read_csv(os.path.join("dataset", "SMSSpamCollection"), sep="\t")

train, test = train_test_split(df, test_size=0.2)
print "Total Instances in training :%d" % len(train)
print "Total Instances in testing :%d" % len(test)

train_features = gen_features(train)
train_target = train[train.columns[0]].apply(spam_or_ham)

print "Training RF"
clf = RandomForestClassifier(n_jobs=5)
clf.fit(train_features, train_target)
print "Completed Training RF"

test_features = gen_features(test)
preds = clf.predict(test_features)
test_actual = test[test.columns[0]].apply(spam_or_ham)

print "Metrics:"
print "F1 Score:", f1_score(test_actual, preds, average="binary")
print "Precision:", precision_score(test_actual, preds, average="binary")
print "Recall:", recall_score(test_actual, preds, average="binary")