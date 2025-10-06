import matplotlib.pyplot as plt
import pandas

# Read the CSV file into a DataFrame and check its contents
# This is a dataset provided in another course
df = pandas.read_csv("data/raw/hotel_vienna.csv")
print(df.head())

# Calculate average price for each neighborhood
avg_rating_per_neighborhood = df.groupby("neighbourhood")["price"].mean().reset_index()

# Now sort by price descending and print it
avg_rating_per_neighborhood.sort_values(by="price", ascending=False)
print(avg_rating_per_neighborhood.sort_values(by="price", ascending=False))

# Save the average price per neighborhood to a CSV file
avg_rating_per_neighborhood.to_csv("data/derived/average_price_per_neighborhood.csv", index=False)

# Plot the price of all hotels on a histogram and save it to a file
plt.hist(df["price"], bins=50)
plt.xlabel("Price")
plt.ylabel("Number of hotels")
plt.title("Price distribution of hotels in Vienna")
plt.savefig("reports/figures/price_distribution.png")