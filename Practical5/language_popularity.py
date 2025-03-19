language_popularity={"JavaScript": 62.3,"HTML": 52.9,"Python": 51,"SQL": 51,"TypeScript": 38.5}#define a dictionary of the percentage of 5 programming languages
print("The statistics about popularity of programming languages",language_popularity)#print the dictionary
inquire_language="Python"# a variable that can be modified
if inquire_language in language_popularity:#determine whether the language is in the dictionary
    print("The usage of",inquire_language,"is",{language_popularity[inquire_language]},"%")#print the usage of this language
else:
    print("The statistic about",inquire_language,"cannot be found")

import matplotlib.pyplot as plt
import numpy as np
languages = list(language_popularity.keys())#get the languages
percentages = list(language_popularity.values())#get the percentages 
plt.bar(languages, percentages, color=["thistle", "plum", "orchid", "m", "purple"])#create a bar chart
plt.xlabel("programming languages")#add labels
plt.ylabel("popularity percentages (%)")
plt.title("The Popularity of Programming Languages Globally")#add title
plt.show()#draw the bar chart