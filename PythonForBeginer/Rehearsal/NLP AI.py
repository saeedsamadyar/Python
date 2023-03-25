import nltk
import random
from nltk.corpus import movie_reviews

# Creating a list of documents with their respective categories
documents = [(list(movie_reviews.words(fileid)), category)
             for category in movie_reviews.categories()
             for fileid in movie_reviews.fileids(category)]

# Shuffle the documents to randomize them
random.shuffle(documents)

# Create a list of all words in the movie reviews
all_words = []
for w in movie_reviews.words():
    all_words.append(w.lower())
    
# Create a frequency distribution of all words
all_words = nltk.FreqDist(all_words)

# Use the 1500 most common words as features
word_features = list(all_words.keys())[:1500]

# A function to find the features of a document
def find_features(doc):
    words = set(doc)
    features = {}
    for w in word_features:
        features[w] = (w in words)
    return features

# Create feature sets of features and their respective categories 
featuresets = [(find_features(rev), category) for (rev, category) in documents]

# Split the feature sets into a training and testing set
training_set = featuresets[:1000]
testing_set = featuresets[1000:]

# Train a Naive Bayes classifier on the training set
classifier = nltk.NaiveBayesClassifier.train(training_set)

# Print the accuracy of the classifier on the testing set
print("Classifier accuracy:", (nltk.classify.accuracy(classifier, testing_set))*100)

