import numpy as np 
import matplotlib.pyplot as plt 
import pandas as pd
df = pd.read_csv('C://Thesis/data thesis/combine data hulk generated.csv')

y=df['Time delta from previous captured frame']
x=df['Dataset']
x1=x[:50000]
y1=y[:50000]
x2=x[50000:]
y2=y[50000:]
plt.bar(x1,y1, color='red')
plt.bar(x2,y2, color='blue')
plt.legend(labels=['Attaack', 'Normal'])
plt.ylim(0,0.01)
plt.title('Generated dataset')
plt.ylabel('Time delta from previos capture')
plt.xlabel('Dataset')
plt.show()

