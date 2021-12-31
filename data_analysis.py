import pandas as pd

df2=pd.read_hdf("data.h5","df")

print("Number of people that are Overweight is ",df2["bmi_category"].value_counts()["Overweight"])


print(print("statistics \n",df2.groupby("gender").describe()))