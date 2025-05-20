import os #import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

os.chdir("C:/cygwin64/home/29852/IBI1_2024-25/Practical10")
print(os.getcwd())
print(os.listdir())

dalys_data = pd.read_csv("dalys-rate-from-all-causes.csv")
print(dalys_data.head(5))
print(dalys_data.info())
print(dalys_data.describe())
print(dalys_data.iloc[0:10, 2])

dalys_1990 = dalys_data.loc[dalys_data.Year == 1990, "DALYs"]
print(dalys_1990.head())

uk = dalys_data.loc[dalys_data.Entity=="United Kingdom", ["DALYs", "Year"]]
france = dalys_data.loc[dalys_data.Entity == "France", ["DALYs", "Year"]]
print("UK mean:", uk.DALYs.mean())
print("France mean:", france.DALYs.mean())
uk_data = dalys_data[dalys_data["Entity"] == "United Kingdom"]
plt.plot(uk.Year, uk.DALYs, 'b+')
plt.xlabel("Year")
plt.ylabel("DALYs Rate")
plt.title("UK DALYs Over Time")
plt.xticks(rotation=45) 
plt.legend()
plt.show()