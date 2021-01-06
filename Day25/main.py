# with open("Day25/weather_data.csv") as data:
#     val=data.readlines()
#     print(val)

# import csv
# with open("Day25/weather_data.csv") as data_csv:
#     data=csv.reader(data_csv)
#     temperature=[]
#     for val in data:
#         if val[1]!="temp":
#             temperature.append(val[1])
#     print(temperature)

import pandas as pd
data=pd.read_csv("Day25/weather_data.csv")
#show entire table as dataframe
print(data)

#show Columns data as series
print(data.temp) #data["temp"]

#Common Operations
avg=data["temp"].mean()
print(f"Avrage Temp {avg}")
print(data["temp"].max())

#show entire row based on condition
print(data[data["day"]=="Monday"])
print(data[data["temp"]==data.temp.max()])

#convert Raw data to dataframe
data_dict={
    "student":["a","b","c"],
    "marks":[12,34,10]
}
data=pd.DataFrame(data_dict)
print(data)

#Convert Raw DataFrame to Csv
data.to_csv("Day25/test.csv")
