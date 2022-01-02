import codecademylib3_seaborn
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Import the CSV files and create the DataFrames:
user_data = pd.read_csv("user_data.csv")
pop_data = pd.read_csv("pop_data.csv")

# Paste print code here:
print(user_data.head(15))

# Paste merge code here:
new_df = pd.merge(user_data, pop_data)

# Paste location code here:
print(new_df.head(15))

new_df.loc[new_df.population_proper < 100000, "location"] = "rural"
new_df.loc[new_df.population_proper >= 100000, "location"] = "urban"

print(new_df.head(15))


import codecademylib3_seaborn
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Import CSVs:
user_data = pd.read_csv("user_data.csv")
pop_data = pd.read_csv("pop_data.csv")

# Merged tables with location data:
new_df = pd.merge(user_data, pop_data)
new_df.loc[new_df.population_proper < 100000, "location"] = "rural"
new_df.loc[new_df.population_proper >= 100000, "location"] = "urban"

# Paste histogram code:
age = new_df["age"]
sns.distplot(age)
plt.show()

# Paste mean age location code:
location_mean_age = new_df.groupby("location").age.mean()
print(location_mean_age)

# Paste barplot code:
plt.close()
sns.barplot(
    data=new_df,
    x= "location",
    y= "age"
)
plt.show()

# Paste violinplot code:
plt.close()
sns.violinplot(x="location", y="age", data=new_df)
plt.show()


import codecademylib3_seaborn
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Import CSVs:
user_data = pd.read_csv("user_data.csv")
pop_data = pd.read_csv("pop_data.csv")

# Merged tables with location data:
new_df = pd.merge(user_data, pop_data)
new_df.loc[new_df.population_proper < 100000, "location"] = "rural"
new_df.loc[new_df.population_proper >= 100000, "location"] = "urban"

# Paste code for scatter plot:
x = new_df["population_proper"]
y = new_df["age"]

plt.scatter(x, y, alpha=0.5)

plt.show()

# Paste code for linear regression:
plt.close()

sns.regplot(x="population_proper", y="age", data=new_df)

plt.show()



import codecademylib3_seaborn
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Import CSVs:
user_data = pd.read_csv("user_data.csv")
pop_data = pd.read_csv("pop_data.csv")

# Merged tables with location data:
new_df = pd.merge(user_data, pop_data)
new_df.loc[new_df.population_proper < 100000, "location"] = "rural"
new_df.loc[new_df.population_proper >= 100000, "location"] = "urban"

# Code for linear regression:
sns.regplot(x="population_proper", y="age", data=new_df)

# Paste code to change the axes:
ax = plt.subplot(1, 1, 1)
ax.set_xticks([100000, 1000000, 2000000, 4000000, 8000000])
ax.set_xticklabels(["100k", "1m", "2m","4m", "8m"])
plt.show()

# Paste code to change the figure style and palette:
plt.close()

sns.set_style("darkgrid")
sns.set_palette("bright")
sns.despine()

sns.regplot(x="population_proper", y="age", data=new_df)
plt.show()


# Paste code to title the axes and the plot:
plt.close()

ax.set_xlabel("City Population")
ax.set_ylabel("User Age")
plt.title("Age vs Population")

sns.regplot(x="population_proper", y="age", data=new_df)
plt.show()