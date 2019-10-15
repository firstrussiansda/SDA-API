from django.db import migrations, models
import requests
import re



def derive_track_id(apps, schema_editor):
    SoundCloudAsset = apps.get_model('media', 'SoundCloudAsset')

    for asset in SoundCloudAsset.objects.filter(track_id=""):
        try:
            r = requests.get(f"https://soundcloud.com/oembed?url=https://soundcloud.com/{asset.object_id}&format=json")
        except requests.RequestException:
            print("Could not connect to external oembed service")

        try:
            data = r.json()
        except ValueError:
            print("Received invalid json response from external oembed")
        
        track_id = ""
        track_id_search = re.search(r"tracks%2F(\d+)", data.get("html", ""))
        if track_id_search:
            track_id = track_id_search.group(1)

        asset.track_id = track_id
        asset.save()
 

class Migration(migrations.Migration):

    dependencies = [("media", "0002_adding_track_id")]

    operations = [
        migrations.RunPython(derive_track_id)
    ]
