'''
import matplotlib.pyplot as plt

x = [1, 2, 3, 4]
y = [10, 20, 25, 30]

plt.plot(x,y)
plt.show() 

#Bar Graph

import matplotlib.pyplot as pit
pit.bar(["TV9", "NDTV" , "SumanTV"], [4, 10, 7])
pit.show()


PIE Graph
---------


import matplotlib.pyplot as pit
pit.pie([30, 40, 20], labels = ["Vidya", "Sangeetha", "Divya"])
pit.show()

HISTOGRAM
---------  
import matplotlib.pyplot as pit
pit.hist([23, 15, 78, 12])
pit.show()

NUMPY
------  
---> Numpy(Numerical Python) is the fondational open-source library for scientific computing in python,
providing high performance, N-dimensional array objects(ndarray)
---> This enables efficient numerical computation linear algebra, and data manipulation, serving as the basis for the tools like Tensorflow and scipy


import matplotlib.pyplot as plt
x = [1, 2, 3, 4]
y = [10, 20, 25, 30]

plt.plot(x, y)
plt.show() 

PANDAS
-------
---> This is used for handling structured data in table format '''

import pandas as pd
data = {"Name" : ["Sangeetha", "Vidhya"], "Marks" : [35, 89,]}
any = pd.DataFrame(data)
print(any)



