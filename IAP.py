# offers IAP or not using app ids

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

# Write the result to a file
output_file = "IAP_vs_NoIAP.json"
with open(output_file, "w") as file:
    json.dump(output_data, file, indent=4)

# End of scraping and writing to json file
print(f"Results written to {output_file}")

# Reading values from json file
with open('IAP_vs_NoIAP.json', 'r') as json_file:
    app_data = json.load(json_file)

# Directly accessing the values
offersIAP = app_data['offersIAP']
noIAP = app_data['noIAP']

# Visualization using matplotlib
categories = ["offersIAP", "noIAP"]
counts = [offersIAP, noIAP]

plt.figure(figsize=(8, 6))
plt.bar(categories, counts, color=["green", "red"])
plt.title("Apps Offering In-App Purchases (IAP)")
plt.ylabel("Number of Apps")
plt.xlabel("IAP Availability")
plt.grid(axis="y", linestyle="--", alpha=0.7)

# Show the bar chart
plt.tight_layout()
plt.show()


