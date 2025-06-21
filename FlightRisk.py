import pandas as pd #tabular data (graphs)
import numpy as np #numerical operators
import matplotlib.pyplot as plt

from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import MinMaxScaler


import random
np.random.seed(70)
print(np.random.randint(1,100))

NumSamples = 1000

data = pd.DataFrame({
    'speed': np.random.randint(0,500 ,NumSamples),
    'altitude': np.random.randint(0,5000 ,NumSamples),
    'fuel_level': np.random.randint(0,100 ,NumSamples),
    'weather': np.random.choice([0,1,2]), #0 = clear, 1 = raining, 2 = stormy
    'angle' :np.random.randint(-10,30, NumSamples)

})


risk_score = (
    (100 - data['fuel_level']) * 0.6 + 
    (data['speed'] < 20).astype(int) * 5 +
    data['weather'] * 9 +
    (data['altitude'] < 50).astype(int) * 4 + 
    ((data['angle'] - 7  ).abs()) * 1.6
)

print(risk_score)

def get_input(prompt, cast_func=int):
    while True:
        try:
            return cast_func(input(prompt))
        except ValueError:
            print("error wrong input")

#Safe scores
scaler = MinMaxScaler(feature_range=(0,100))
data['safescore'] = 100 -scaler.fit_transform(risk_score.values.reshape(-1,1)).flatten()
data['safeLabel'] = (data['safescore'] > 50).astype(int)

#Train data with ML model
features = ["speed", "altitude", "weather", "fuel_level","angle"]#array/list
x = data[features]
y = data['safeLabel']
model = RandomForestClassifier()
model.fit(x,y)


user_input = {
    'speed': get_input("Speed: "),
    'altitude': get_input("Altitude: "),
    'weather': get_input("weather (0= clear, 1= raining, 2= stormy): "),
    'fuel_level': get_input('Fuel Level: '), 
    'angle':get_input('Angle of Flight: ')
}

#predictions

userDF = pd.DataFrame([user_input])
ProbSafe = model.predict_proba(userDF)[0][1]
safePer = round(ProbSafe * 100, 2)
if ProbSafe > 0.5:
    prediction = "SAFE"
else:
    prediction = "RISKY"

print("\n\nFlight report")
print("Safe Flight Percentage : ", safePer, "%")# , or + work
print(f"Prediction: {prediction}")

#Table Test

plt.figure(figsize=(10,5))
plt.hist(data['safescore'], bins=30 , color="red", edgecolor="black")
plt.title("Flight Safety Score")
plt.xlabel("Safe Score (0 = risky , 100 = Safe)")
plt.ylabel("Number of flights")
plt.axvline(safePer, color="purple", linestyle='--', linewidth= 3, label=f"Your Flight: {safePer}%")#--, .. , **
plt.legend()
plt.grid(True)

plt.show()

print(np.min(risk_score))
print(np.max(risk_score))
