import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("DS2.txt", sep=' ', header=None, names=['x', 'y'])
fig = plt.figure(figsize=(960/100, 540/100)) 
ax = fig.add_axes([0, 0, 1, 1])  
ax.scatter(data['x'], data['y'])
plt.savefig("output.png", dpi=100)
plt.show()