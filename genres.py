# App Genres
# Categorizes apps based on their genres using keywords.

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

output_file = "genre_counts.json"

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
    genre_data = json.load(file)
    file.close()  # Explicitly closing the file after operation
    print(f"Data successfully read from {output_file}")
except Exception as e:
    print(f"Error reading from {output_file}: {e}")
    genre_data = {}

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
