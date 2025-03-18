uk_countries=[57.11, 3.13, 1.91, 5.45]#the statistics about the population of countries of UK
uk_names=["England", "Wales", "Northern Ireland", "Scotland"]#the names of countries in UK
china_provinces=[65.77, 41.88, 45.28, 61.27, 85.15]#the statistics about the population of provinces in China
china_names=["Zhejiang", "Fujian", "Jiangxi", "Anhui", "Jiangsu"]#the names of provinces in China
uk_countries_sorted=sorted(uk_countries)#sort according to the values of UK countries population
china_provinces_sorted=sorted(china_provinces)#sort according to the values of China provinces population
print(uk_countries_sorted)#print the result
print(china_provinces_sorted)
import matplotlib.pyplot as plt
labels1 ="England", "Wales", "Northern Ireland", "Scotland"#add labels
sizes1 = [57.11,3.13,1.91,5.45]#add the sizes of different countries
plt.pie(sizes1, labels=labels1)#draw a pie plot
plt.axis('equal')#define the plot to be round
plt.show()#print the plot 
labels2="Zhejiang", "Fujian", "Jiangxi", "Anhui", "Jiangsu"#add labels
sizes2 = [65.77, 41.88, 45.28, 61.27, 85.15]#add the sizes of different provinces
plt.pie(sizes2, labels=labels2)#draw a pie plot
plt.axis('equal')#define the plot to be round
plt.show()#print the plot 