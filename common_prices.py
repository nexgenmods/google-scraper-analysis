# prices of paid apps

import json
import pandas as pd
import matplotlib.pyplot as plt
from google_play_scraper import search

# Sample data for demonstration purposes
queries = [
    "top paid games",
    "premium games",
    "premium video games",
    "paid apps",
]

all_results = []

# Fetch results for each query
for query in queries:
    result = search(
        query,
        lang="en",  # defaults to 'en'
        country="us",  # defaults to 'us'
        n_hits=15  # defaults to 30
    )
    all_results.extend(result)

# Create a DataFrame
df = pd.DataFrame(all_results)

# Filter out free apps
paid_apps = df[df['price'] > 0]

# Group by price and count the number of apps in each price
price_counts = paid_apps['price'].value_counts().sort_index()

# Prepare the output JSON
output_data = {
    "price_counts": price_counts.to_dict()  # Convert Series to dictionary for JSON serialization
}

output_file = "common_prices.json"

# Writing results to JSON file with exception handling
try:
    file = open(output_file, 'w')
    json.dump(output_data, file, indent=4)
    file.close()  # Explicitly closing the file after operation
    print(f"Results written to {output_file}")
except Exception as e:
    print(f"Error writing to {output_file}: {e}")

# Reading values from JSON file with exception handling
try:
    file = open(output_file, 'r')
    app_data = json.load(file)
    file.close()  # Explicitly closing the file after operation
    print(f"Data successfully read from {output_file}")
except Exception as e:
    print(f"Error reading from {output_file}: {e}")
    app_data = {}

# Visualization for price using a bar plot
if "price_counts" in app_data:
    price_counts = pd.Series(app_data["price_counts"])
    plt.figure(figsize=(10, 6))
    plt.bar(price_counts.index.astype(str), price_counts.values)
    plt.title("Common prices of Paid Apps")
    plt.xlabel("Price (USD)")
    plt.ylabel("Number of Apps")
    plt.xticks(rotation=45, ha="right")  # Rotate price labels for better readability
    plt.grid(axis="y", linestyle="--", alpha=0.7)
    plt.show()
else:
    print("No data found to plot.")
