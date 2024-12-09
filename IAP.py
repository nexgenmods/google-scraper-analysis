# In-App Advertisements (IAP)
# Highlights the number of apps with and without in-app advertisements.

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

# Fetch data for each app
results = []
for app_id in app_ids:
    result = app(
        app_id,
        lang='en',  # defaults to 'en'
        country='us'  # defaults to 'us'
    )
    results.append(result)

# Create a DataFrame from the results
df = pd.DataFrame(results)

# Count IAP and no IAP apps
offersIAP = df[df["offersIAP"]].shape[0]
noIAP = df[~df["offersIAP"]].shape[0]

# Prepare the output JSON
output_data = {
    "offersIAP": offersIAP,
    "noIAP": noIAP
}

output_file = "IAP_vs_NoIAP.json"

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
offersIAP = app_data['offersIAP']
noIAP = app_data['noIAP']

# Visualization using matplotlib
categories = ["offersIAP", "noIAP"]
counts = [offersIAP, noIAP]

plt.figure(figsize=(8, 6))
plt.bar(categories, counts, color=["#384860", "#97a6c4"]) # shades of gray medium blues
plt.title("Apps Offering In-App Purchases (IAP)")
plt.ylabel("Number of Apps")
plt.xlabel("IAP Availability")
plt.grid(axis="y", linestyle="--", alpha=0.7)

# Show the bar chart
plt.tight_layout()
plt.show()


