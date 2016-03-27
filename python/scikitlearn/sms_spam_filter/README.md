Basic SMS Filter Based on Random Forests
========================================

[Dataset](https://archive.ics.uci.edu/ml/datasets/SMS+Spam+Collection) from UCI repo. Relevant papers are also mentioned there. 

Features that we can use
------------------------
- Length of SMS - DONE
- Number of Special Characters - DONE
- Number of Uppercase Words - DONE
- Number of Numeric Expressions - DONE
- Number of tokens present in marketing dictionary
- Ratio of UPPERCASE to LOWERCASE tokens in message
- Ratio of Numeric to Non-Numeric tokens in SMS
- BOW Counts for all Words
- TF-IDF for all Words
- BOW Counts for all Lowercase Words
- TF-IDF for all Lowercase Words
- Character Bigram & Trigrams
- Word Bigrams in Rolling window of 5 words

Feature Selection
-----------------
- Information Gain

Algorithms to Try
-----------------
- Random Forests - DONE
- XGBoost
- Naive Bayes Classifier
- C4.5
- SVM

Readings
--------
- [Random Forests in Python](http://blog.yhathq.com/posts/random-forests-in-python.html#)
- [NLP in Python](https://www.dataquest.io/blog/predicting-upvotes/)
- [The Unreasonable effectiveness of Random Forests](https://medium.com/rants-on-machine-learning/the-unreasonable-effectiveness-of-random-forests-f33c3ce28883#.kboq3p8mm)

Resource
---------
- [Subject Line Spam Trigger Words](http://www.mequoda.com/articles/audience-development/subject-line-spam-trigger-words/)