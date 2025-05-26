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

print(dalys_data.iloc[9,2])#the 10th year in Afghanistan

dalys_1990 = dalys_data.loc[dalys_data["Year"] == 1990, "DALYs"]
print("DALYs for all countries in 1990:")
print(dalys_1990)#use a Boolean to show DALYs for all countries in 1990

uk = dalys_data.loc[dalys_data.Entity=="United Kingdom", ["DALYs", "Year"]]
france = dalys_data.loc[dalys_data.Entity == "France", ["DALYs", "Year"]]
print("UK mean:", uk.DALYs.mean())
print("France mean:", france.DALYs.mean())
uk_data = dalys_data[dalys_data["Entity"] == "United Kingdom"]
plt.plot(uk.Year, uk.DALYs, 'b+')
plt.xticks(uk.Year,rotation=-90)
plt.xlabel("Year")
plt.ylabel("DALYs")
plt.title("UK DALYs Over Time")
plt.legend()
plt.show()

#question: Plot a boxplot of DALYs across countries in 1990.
dalys_1990_ = dalys_data[dalys_data["Year"] == 1990]

plt.figure(figsize=(10, 6))
plt.boxplot(dalys_1990_["DALYs"], vert=True, patch_artist=True)
plt.title("Boxplot of DALYs Across Countries in 1990")
plt.ylabel("DALYs")
plt.xticks([1], ["1990"])
plt.tight_layout()
plt.show()