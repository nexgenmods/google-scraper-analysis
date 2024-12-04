import json
import pandas as pd
import matplotlib.pyplot as plt
from google_play_scraper import search, permissions

# Define categories
queries = [
    "social media",
    "games",
    "education",
    "shopping",
    "entertainment",
    "Finance",
    "Health"
]

# Create an empty list to store app data
results = []

# Loop through each category and get apps
for query in queries:
    print(f"Fetching apps for category: {query}")
    
    # Search for apps in the current category
    apps = search(query, lang='en', country='us', n_hits=5)  # Change num if needed
    
    # Get permissions for each app and collect them
    for app in apps:
        app_id = app['appId']
        
        # Fetch permissions for the app
        result = permissions(app_id, lang='en', country='us')
        
        # Collect data
        permission_count = len(result.keys())
        results.append({
            "category": query,
            "app_id": app_id,
            "permission_count": permission_count
        })

# Create a Pandas DataFrame from the collected data
df = pd.DataFrame(results)

# Calculate the mean number of permissions for each category
mean_permissions = df.groupby('category')['permission_count'].mean().to_dict()

# Prepare output data for JSON
output_data = {
    "mean_permissions": mean_permissions
}

# Write to JSON file
output_file = "permissions.json"
with open(output_file, "w") as file:
    json.dump(output_data, file, indent=4)

# End of scraping and writing to JSON file
print(f"Results written to {output_file}")

# Reading values from the JSON file
with open('permissions.json', 'r') as json_file:
    app_data = json.load(json_file)

# Extract mean_permissions directly
mean_permissions = app_data["mean_permissions"]

# Convert mean_permissions dictionary to a DataFrame
df_permissions = pd.DataFrame(mean_permissions.items(), columns=["Category", "Average_Permissions"])

# Sort the DataFrame by Average_Permissions in descending order
df_permissions = df_permissions.set_index("Category")["Average_Permissions"].sort_values(ascending=False)

# Extract sorted categories and permissions for plotting
categories = df_permissions.index
permissions = df_permissions.values

# Creating the bar chart
plt.figure(figsize=(10, 6))
plt.bar(categories, permissions, color='skyblue')
plt.xlabel('Categories')
plt.ylabel('Average Number of Permissions')
plt.title('Average Number of Permissions by Category')
plt.xticks(rotation=45, ha='right')  # Rotate category labels for better readability
plt.tight_layout()

# Show the plot
plt.show()
