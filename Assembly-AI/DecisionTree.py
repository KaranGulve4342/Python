import numpy as np
from collections import Counter

class Node:
    def __init__(self, feature = None, threshold = None, left = None, right = None, *, value = None):
        self.feature = feature
        self.threshold = threshold
        self.left = left
        self.right = right
        self.value = value

    def is_leaf_node(self):
        return self.value is not None
    

class DecisionTree:
    def __init__(self, min_samples_split = 2, max_depth = 100, n_features = None):
        self.min_samples_split = min_samples_split
        self.max_depth = max_depth
        self.n_features = n_features
        self.root = None

    def fit(self, X, y):
        self.n_features = X.shape[1] if not self.n_features else min(self.n_features, X.shape[1])
        self.root = self.grow_tree(X, y)

    def grow_tree(self, X, y, depth = 0):
        n_samples, n_features = X.shape
        n_labels = len(np.unique(y))

        ## Check the stopping criteria
        if(depth >= self.max_depth or n_labels == 1 or n_samples < self.min_samples_split):
            leaf_value = self._most_common_label(y)
            return Node(value=leaf_value)
        
        feature_idx = np.random.choice(n_features, self.n_features, replace=False)

        ## Find the best split
        best_feature, best_threshold = self._best_split(X, y, feature_idx)

        ## Create child Nodes
        left_idx, right_idx = self._split(X[:, best_feature], best_threshold)
        left = self.grow_tree(X[left_idx, :], y[left_idx], depth+1)
        right = self.grow_tree(X[right_idx, :], y[right_idx], depth+1)

        return Node(best_feature, best_threshold, left, right)

    def _best_split(self, X, y, feature_idx):
        best_gain = -1
        split_idx, split_threshold = None, None

        for feature in feature_idx:
            feature_values = X[:, feature]
            thresholds = np.unique(feature_values)

            for threshold in thresholds:
                gain = self._information_gain(y, feature_values, threshold)

                if gain > best_gain:
                    best_gain = gain
                    split_idx = feature
                    split_threshold = threshold

        return split_idx, split_threshold

    def _most_common_label(self, y):
        counter = Counter(y)
        return counter.most_common(1)[0][0]
    
    def _information_gain(self, y, feature_values, threshold):
        ## Parent entropy
        parent_entropy = self._entropy(y)
        ## Create children
        left_idx, right_idx = self._split(feature_values, threshold)
        if len(left_idx) == 0 or len(right_idx) == 0:
            return 0
        ## Calculate the child entropy
        n = len(y)
        n_left, n_right = len(left_idx), len(right_idx)
        entropy_left = self._entropy(y[left_idx])
        entropy_right = self._entropy(y[right_idx])
        child_entropy = (n_left/n)*entropy_left + (n_right/n)*entropy_right
        ## Calculate the information gain
        information_gain = parent_entropy - child_entropy
        return information_gain


    def _split(self, feature_values, threshold):
        left_idx = np.argwhere(feature_values <= threshold).flatten()
        right_idx = np.argwhere(feature_values > threshold).flatten()
        return left_idx, right_idx

    def _entropy(self, y):
        counter = Counter(y)
        entropy = 0
        for label in counter:
            p = counter[label] / len(y)
            entropy += -p * np.log2(p)
        return entropy
    
    def _traverse_tree(self, x, node):
        if node.is_leaf_node():
            return node.value
        
        if x[node.feature] <= node.threshold:
            return self._traverse_tree(x, node.left)
        return self._traverse_tree(x, node.right)

    def predict(self, X):
        return np.array([self._traverse_tree(x, self.root) for x in X])
