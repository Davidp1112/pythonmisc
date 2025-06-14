import pandas as pd #tabular data (graphs)
import numpy as np #numerical operators
import matplotlib.pyplot as plt

from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import MinMaxScaler


import random
np.random.seed(10)
print(np.random.randint(1,100))

NumSamples = 5

data = pd.DataFrame({
    'speed': np.random.randint(0,20 ,NumSamples),
    'altitude': np.random.randint(0,50 ,NumSamples),
    'fuel_level': np.random.randint(0,100 ,NumSamples),
    'weather': np.random.choice([0,1,2]) #0 = clear, 1 = raining, 2 = stormy

})


risk_score = (
    (100 - data['fuel_level']) * 0.6 + 
    (data['speed'] < 20).astype(int) * 5 +
    data['weather'] * 9 +
    (data['altitude'] < 50).astype(int) * 4
)

print(risk_score)

def get_input(prompt, cast_func=int):
    while True:
        try:
            return cast_func(input(prompt))
        except ValueError:
            print("error wrong input")

user_input = {
    'speed': get_input("Speed: "),
    'altitude': get_input("Altitude: "),
    'weater': get_input("weather (0= clear, 1=raining, 2= stormy): "),
    'fuel_level': get_input('Fuel Level: ')
}

userDF = pd.DataFrame([user_input])



#Table Test
BC = pd.DataFrame(np.random.rand(10,4), columns=["a", "b", "c", "d"])
BC.plot.bar()
plt.show()
