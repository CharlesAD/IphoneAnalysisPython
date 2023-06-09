import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go

data = pd.read_csv("apple_products.csv")
print(data.head())

## Checking to see if the data set has any null values. Unknown or missing values
print(data.isnull().sum())

## Here are the Top 10 iPhone Ratings in the console
highest_rated = data.sort_values(by=["Star Rating"], ascending=False)
highest_rated = highest_rated.head(10)
print(highest_rated['Product Name'])



## Number of Ratings of Highest Rated iPhones
iphones = highest_rated["Product Name"].value_counts()
label = iphones.index
counts = highest_rated["Number Of Ratings"]
figure = px.bar(highest_rated, x=label, y = counts, 
            title="Number of Ratings of Highest Rated iPhones")
figure.show()
## As you can see from this graph the iPhone 8 Plus Gold is the highest rated iPhone

## This graph shows the relationship between Sale Price and Number of Ratings of iPhones
figure = px.scatter(data_frame = data, x="Number Of Ratings", y="Sale Price", size="Discount Percentage", trendline="ols", title="Relationship between Sale Price and Number of Ratings of iPhones")
figure.show()
## From the above graph you can see that there is a negative linear relationship between the sale 
# price of iPhones and the number of ratings. It means iPhones with lower sale prices are sold 
# more.