<<<<<<< HEAD
<<<<<<< HEAD
""""
To use this notebook for your in-class assignment, you will need these 
files, which you shoujld have downloaded:
* mhu.csv -- Lake Michigan and Lake Huron
* sup.csv -- Lake Superior
* eri.csv -- Lake Erie
* ont.csv -- Lake Ontario

As instructed in the in-class activity notebook for today, you are 
only expected to complete one PART below. Do not worry if your group 
is not big enough to finish all parts below, but if you have extra 
time, you're welcome to do so.
""""
<<<<<<< HEAD
=======
>>>>>>> Dang
=======

>>>>>>> yu
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
=======
>>>>>>> bommarito


# PART 1
# Using the Michigan/Huron Dataset, plot the Water Level, the second 
# column, as a function of time years

<<<<<<< HEAD
<<<<<<< HEAD

=======
mhu = pd.read_csv("mhu.csv")
plt.plot(mhu["time"], mhu["lake average"])
plt.xlabel("Time(Years)")
plt.ylabel("Water Levels(m)")
plt.title("Michigan/Huron Water Levels over Time")
>>>>>>> Dang
=======

>>>>>>> yu

# PART 2
# Using the Superior Dataset, plot the Water Level, the second column, 
# as a function of time years
sup = pd.read_csv("sup.csv")

year = sup["year"]
water_levels = sup["lake levels"]

plt.plot(year, water_levels)
plt.xlabel("Time")
plt.ylabel("Water Level")
plt.title("Lake Superior Water Level over Time")



# PART 3
# Using the Erie Dataset, plot the Water Level, the second column, 
# as a function of time years
<<<<<<< HEAD

=======
eri = pd.read_csv('eri.csv')
plt.plot(eri['time'], eri['water level'])
plt.xlabel('Time(years)')
plt.ylabel('Water Level')
plt.title('Water Level in Lake Erie')
>>>>>>> yu


# PART 4
# Using the Ontario Dataset, plot the Water Level, the second column, 
# as a function of time years
<<<<<<< HEAD
ont = pd.read_csv('ont.csv')
plt.plot(ont['year'], ont['Lake Ontario annual averages'])
plt.xlabel('Year')
plt.ylabel('Annual Averages')
plt.title('Lake Ontario Annual Averages')
=======

>>>>>>> yu


# PART 5
# Using the Michigan/Huron and Superior Datasets, plot the 
# Michigan/Hurion Water Level vs Superior Water Level to see if there 
# is any correlation between the water levels.

<<<<<<< HEAD
# +
mhu = pd.read_csv("mhu.csv")
mhu_average = mhu["lake average"]

superior = pd.read_csv("sup.csv")
sup_average = superior["lake levels"]

plt.scatter(mhu_average, sup_average)
plt.title("Correlations Between Michigan/Huron and Superior")
plt.xlabel("Michigan Huron")
plt.ylabel("Superior")

# -
=======

>>>>>>> yu

# PART 6
# Using the Michigan/Hurion and Erie Datasets, plot the 
# Michigan/Huron Water Level vs Erie Water Level to see if there is 
# any correlation between the water levels.

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

mhu = pd.read_csv("mhu.csv")
mhu.head()

erie = pd.read_csv("eri.csv")
erie.head()

# +
mhu_average = mhu["lake average"]

erie = pd.read_csv("eri.csv")
erie_average = erie["water level"]

plt.scatter(mhu_average, erie_average)
plt.title("Correlation Betweeen Michigan/Huron and Erie")
plt.xlabel("Michigan Huron")
plt.ylabel("Erie")
# -

# PART 7
# Using the Superior and Ontario Datasets, plot the Superior Water 
# Level vs Ontario Water Level to see if there is any correlation 
# between the water levels.


