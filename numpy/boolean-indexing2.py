import numpy as np
names = np.array(["Cyrus", "Darius", "Xerxes", "Artaxerxes", "Cyrus", "Darius"])
results = np.array([17, 14, 20, 18, 13, 15])
print(results[names == "Darius"])
names = np.array(["Cyrus", "Darius", "Xerxes"])
results = np.array([[17, 14], [20, 18], [13, 15]])
print(results[names == "Darius"])