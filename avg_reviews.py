import json
import pandas as pd
import matplotlib.pyplot as plt
from google_play_scraper import app

# List of app IDs
app_ids = [
    'com.fantome.penguinisle',
    'com.nianticlabs.pokemongo',
    'com.spotify.music',
    'jp.pokemon.pokemonunite',
    'com.dena.a12026418',
    'com.whatsapp',
    'com.facebook.katana',
    'com.instagram.android',
    'com.snapchat.android',
    'com.twitter.android',
    'com.netflix.mediaclient',
    'com.amazon.mShop.android.shopping',
    'com.linkedin.android',
    'com.google.android.gms',
    'com.google.android.youtube',
    'com.skype.raider',
    'com.ebay.mobile',
    'com.zhiliaoapp.musically',
    'com.tinder',
    'com.ubercab',
    'com.airbnb.android',
    'com.google.android.googlequicksearchbox',
    'com.rovio.baba',
    'com.king.candycrushsaga',
    'com.supercell.clashofclans',
    'com.supercell.brawlstars',
    'com.gameloft.android.ANMP.GloftA8HM',
    'com.kiloo.subwaysurf',
    'com.mojang.minecraftpe',
    'com.teslacoilsw.launcher',
    'com.king.farmheroessaga',
    'com.redfin.android',
    'com.linkedin.android',
    'com.runtastic.android',
    'com.imangi.templerun',
    'com.gameloft.android.ANMP.GloftA8HM',
    'com.viber.voip',
    'com.simplemobiletools.gallery',
    'com.waze',
    'com.snapdeal.main',
    'com.netflix.ninja',
    'com.webmd.android',
    'com.pixlr.express',
    'com.instagram.android',
    'com.opera.browser'
]

all_results = []

# Fetch app details for each app ID
for app_id in app_ids:
    result = app(app_id, lang="en", country="us")
    all_results.append(result)

# Create a DataFrame
df = pd.DataFrame(all_results)

# Calculate the average reviews per real install
df['avg_reviews_per_install'] = df['reviews'] / df['realInstalls']

# Calculate the average reviews per real install for free and paid apps
free_apps = df[df['free'] == True]
paid_apps = df[df['free'] == False]

avg_reviews_free = free_apps['avg_reviews_per_install'].mean()
avg_reviews_paid = paid_apps['avg_reviews_per_install'].mean()

# Prepare output data
output_data = {
    'Free Apps': avg_reviews_free,
    'Paid Apps': avg_reviews_paid
}

output_file = "average_reviews_per_install_comparison.json"

# Write results to JSON file
try:
    with open(output_file, 'w') as file:
        json.dump(output_data, file, indent=4)
    print(f"Results written to {output_file}")
except Exception as e:
    print(f"Error writing to {output_file}: {e}")

# Read values from JSON file
try:
    with open(output_file, 'r') as file:
        app_data = json.load(file)
    print(f"Data successfully read from {output_file}")
except Exception as e:
    print(f"Error reading from {output_file}: {e}")
    app_data = {}

# Prepare data for visualization
categories = list(app_data.keys())
avg_reviews = list(app_data.values())

# Plot the comparison
plt.figure(figsize=(8, 5))
plt.bar(categories, avg_reviews, color=['lightblue', 'lightcoral'])
plt.xlabel('App Type')
plt.ylabel('Average Reviews per Install')
plt.title('Comparison of Average Reviews per Install: Free vs Paid Apps')
plt.tight_layout()

# Show the graph
plt.show()
