import numpy as np
names = np.array(["Roxana", "Statira", "Roxana", "Statira", "Roxana"])
scores = np.array([126, 115, 130, 141, 132])
# Extract all test scores that are smaller than 130
print(scores[scores < 130])
# Extract all test scores by Statira
print(scores[names == "Statira"])
# Add 10 points to Roxana’s scores. (You need to extract it first.)
scores[names == "Roxana"] += 10
print(scores)