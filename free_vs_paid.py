# Free vs Paid Apps
# Compares the number of free and paid apps in the pulled data.

import json
import pandas as pd
import matplotlib.pyplot as plt
from google_play_scraper import search

# Sample data for demonstration purposes
queries = [
    "best Pikachu game",
    "best Pokemon game",
    "best adventure game",
    "best RPG game",
    "best strategy game",
    "free apps",
    "paid apps"
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

# Count free and paid apps
free_apps = df[df["free"]].shape[0]
paid_apps = df[~df["free"]].shape[0]

# Prepare the output JSON
output_data = {
    "free_apps": free_apps,
    "paid_apps": paid_apps
}

output_file = "free_vs_paid.json"

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

# Directly accessing the values
free_apps = app_data['free_apps']
paid_apps = app_data['paid_apps']

# Visualization using matplotlib
categories = ["Free Apps", "Paid Apps"]
counts = [free_apps, paid_apps]

plt.figure(figsize=(8, 6))
plt.bar(categories, counts, color=["teal", "orange"])
plt.title("Free vs Paid Apps")
plt.ylabel("Number of Apps")
plt.xlabel("App Category")
plt.grid(axis="y", linestyle="--", alpha=0.7)

# Show the bar chart
plt.tight_layout()
plt.show()


