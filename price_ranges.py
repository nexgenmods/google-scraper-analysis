# price ranges of paid apps

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

# Group by price and count the number of apps in each price range
price_counts = paid_apps['price'].value_counts().sort_index()

# Visualization for price ranges using a bar plot
plt.figure(figsize=(10, 6))
plt.bar(price_counts.index.astype(str), price_counts.values)
plt.title("Price Ranges of Paid Apps")
plt.xlabel("Price (USD)")
plt.ylabel("Number of Apps")
plt.xticks(rotation=45, ha="right")  # Rotate price labels for better readability
plt.grid(axis="y", linestyle="--", alpha=0.7)
plt.show()

# Prepare the output JSON
output_data = paid_apps.to_dict(orient='records')

# Write the result to a file
output_file = "free_vs_paid_with_prices.json"
with open(output_file, "w") as file:
    json.dump(output_data, file, indent=4)

# End of scraping and writing to json file
print(f"Results written to {output_file}")
