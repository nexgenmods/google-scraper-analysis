## genres of top 100 apps - using gradient (cm, numpy incl.)

import json
import pandas as pd
import matplotlib.pyplot as plt
from google_play_scraper import search
import matplotlib.cm as cm
import numpy as np

# Sample data for demonstration purposes
queries = [
    "top 100 games",
    "games",
    "video games",
    "best android games",
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

# Extract genres
genres = df['genre'].dropna()

# Count occurrences of each genre
genre_counts = genres.value_counts()

# Prepare the output JSON
output_data = {
    "genre_counts": genre_counts.to_dict()
}

# Write the result to a file
output_file = "genre_counts.json"
with open(output_file, "w") as file:
    json.dump(output_data, file, indent=4)

# End of scraping and writing to json file
print(f"Results written to {output_file}")

# Reading values from json file
with open('genre_counts.json', 'r') as json_file:
    genre_data = json.load(json_file)

# Directly accessing the genre counts
genre_counts = genre_data['genre_counts']

# Generate a colormap based on the number of genres
num_genres = len(genre_counts)
colors = cm.viridis(np.linspace(0, 1, num_genres))  # Use 'viridis' colormap for gradient

# Visualization using matplotlib
plt.figure(figsize=(10, 6))
bars = plt.bar(genre_counts.keys(), genre_counts.values(), color=colors)

plt.title("App Genres Distribution")
plt.ylabel("Number of Apps")
plt.xlabel("Genre")
plt.xticks(rotation=45, ha="right")  # Rotate genre labels for better readability
plt.grid(axis="y", linestyle="--", alpha=0.7)

# Show the bar chart
plt.tight_layout()
plt.show()
