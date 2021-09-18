import numpy as np

scores = [3, 4, 2.7, 3.7, 4, 4, 3.7, 3.7, 4, 3.7, 3.3, 4]
credits = [4 for _ in range(len(scores))]

scores = np.asarray(scores)
credits = np.asarray(credits)

print(np.sum(scores * credits) / np.sum(credits))
