import pandas
data=pandas.read_csv("Day25/Squirrel_census_DA/2018_Central_Park_Squirrel_Census_Data.csv")
# print(data.head(5))
GraySquirel_count=len(data[data["Primary Fur Color"]=="Gray"])
CinnamonSquirel_count=len(data[data["Primary Fur Color"]=="Cinnamon"])
BlackSquirel_count=len(data[data["Primary Fur Color"]=="Black"])

print(GraySquirel_count)
print(CinnamonSquirel_count)
print(BlackSquirel_count)

#data frame

data_dict={
    "Fur Color":["Gray","Cinnamon","Black"],
    "Count":[GraySquirel_count,CinnamonSquirel_count,BlackSquirel_count]
}

# print(data_dict)

df=pandas.DataFrame(data_dict)
print(df)
df.to_csv("Day25/Squirrel_census_DA/Squirel_Census_data.csv")