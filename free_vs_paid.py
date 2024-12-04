#free vs paid apps

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
    "best strategy game"
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

with open("raw_output.json", 'w') as file:
    json.dump(all_results, file, indent=4)

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

# Write the result to a file
output_file = "free_vs_paid.json"
with open(output_file, "w") as file:
    json.dump(output_data, file, indent=4)

# End of scraping and writing to json file
print(f"Results written to {output_file}")

# Reading values from json file
with open('free_vs_paid.json', 'r') as json_file:
    app_data = json.load(json_file)

# Directly accessing the values
free_apps = app_data['free_apps']
paid_apps = app_data['paid_apps']

# Visualization using matplotlib
categories = ["Free Apps", "Paid Apps"]
counts = [free_apps, paid_apps]

plt.figure(figsize=(8, 6))
plt.bar(categories, counts, color=["blue", "orange"])
plt.title("Free vs Paid Apps")
plt.ylabel("Number of Apps")
plt.xlabel("App Category")
plt.grid(axis="y", linestyle="--", alpha=0.7)

# Show the bar chart
plt.tight_layout()
plt.show()


