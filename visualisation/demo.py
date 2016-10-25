import matplotlib.pyplot as plt

# The slices will be ordered and plotted counter-clockwise.
pie1_labels = 'Democratic -74 countires','Non-Democratic - 134 countries'
sizes = []

Democratic_total = 3052
Non_Democratic_total = 1556	

total = Democratic_total+Non_Democratic_total

sizes.append((Democratic_total/total)*100)
sizes.append((Non_Democratic_total/total)*100)




colors = ['yellowgreen', 'gold']
explode = (0.1, 0.1)  # only "explode" the 2nd slice (i.e. 'Hogs')

plt.pie(sizes, explode=explode, labels=pie1_labels, colors=colors,
        autopct='%1.1f%%', shadow=True, startangle=90)


plt.axis('equal')

plt.show()