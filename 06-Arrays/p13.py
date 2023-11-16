import matplotlib.pyplot as plt
'''
13.	In a certain company, 25 employees commute by car, 19 employees commute by public transport, 32 people commute by bike, and 7 people commute on foot.
Write a program that displays this data in a bar chart. Remember to add a title for the chart and a description of the chart axes. Sample result:
'''
transport = [25,19,32,7]
formyTransportu = ["samochody","transport publiczny","rower","pieszo"]
formy=[1,2,3,4]

plt.scatter(formy,transport)
plt.ylabel("Ilość pracownikó")
plt.xlabel("Sposób transportu: 1.Samochody 2.Transport publiczny 3.Rower 4.Pieszo")
plt.show()