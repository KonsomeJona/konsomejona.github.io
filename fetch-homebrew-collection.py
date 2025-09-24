# \!/usr/bin/env python3

import os
import requests

# Try these homebrew games with direct download links
games_to_try = [
    # Games from gbdev with known working paths
    ("Snake", "https://hh3.gbdev.io/static/database-gb/entries/snake/files/snake.gb"),
    ("2048", "https://hh3.gbdev.io/static/database-gb/entries/2048gb/files/2048.gb"),
    (
        "Petris",
        "https://hh3.gbdev.io/static/database-gb/entries/petris/files/petris.gb",
    ),
    ("Pong", "https://hh3.gbdev.io/static/database-gb/entries/pong/files/pong.gb"),
    (
        "Lumberjack",
        "https://hh3.gbdev.io/static/database-gb/entries/lumberjack/files/lumberjack.gb",
    ),
    (
        "Bouncing Ball",
        "https://hh3.gbdev.io/static/database-gb/entries/bouncing-ball/files/bouncing-ball.gb",
    ),
    (
        "PlantBoy",
        "https://hh3.gbdev.io/static/database-gb/entries/plantboy/files/plantboy.gb",
    ),
    ("Outi", "https://hh3.gbdev.io/static/database-gb/entries/outi/files/outi.gb"),
    (
        "Skinke",
        "https://hh3.gbdev.io/static/database-gb/entries/skinke/files/skinke.gb",
    ),
    (
        "They Came From Outer Space",
        "https://hh3.gbdev.io/static/database-gb/entries/they-came-from-outer-space/files/they-came-from-outer-space.gb",
    ),
    (
        "Adjustris",
        "https://hh3.gbdev.io/static/database-gb/entries/adjustris/files/Adjustris.gb",
    ),
    (
        "Airaki",
        "https://hh3.gbdev.io/static/database-gb/entries/airaki/files/airaki.gb",
    ),
    (
        "Burly Bear",
        "https://hh3.gbdev.io/static/database-gb/entries/burly-bear-vs-the-mean-foxes/files/burly-bear.gb",
    ),
    (
        "Cavern",
        "https://hh3.gbdev.io/static/database-gb/entries/cavern/files/cavern.gb",
    ),
    (
        "Deep Forest",
        "https://hh3.gbdev.io/static/database-gb/entries/deep-forest/files/deep-forest.gb",
    ),
    ("Fire", "https://hh3.gbdev.io/static/database-gb/entries/fire/files/fire.gb"),
    (
        "Flappy Boy",
        "https://hh3.gbdev.io/static/database-gb/entries/flappy-boy/files/flappyboy.gb",
    ),
    (
        "Magic Floor",
        "https://hh3.gbdev.io/static/database-gb/entries/magic-floor/files/magic-floor.gb",
    ),
    (
        "Mean Mr Mustard",
        "https://hh3.gbdev.io/static/database-gb/entries/mean-mr-mustard/files/mean-mr-mustard.gb",
    ),
    (
        "Nervous",
        "https://hh3.gbdev.io/static/database-gb/entries/nervous/files/nervous.gb",
    ),
    ("Paint", "https://hh3.gbdev.io/static/database-gb/entries/paint/files/paint.gb"),
    (
        "Rocket Man",
        "https://hh3.gbdev.io/static/database-gb/entries/rocket-man/files/rocketman.gb",
    ),
    (
        "Sheep It Up",
        "https://hh3.gbdev.io/static/database-gb/entries/sheep-it-up/files/sheepitup.gb",
    ),
    (
        "Skoardy Cat",
        "https://hh3.gbdev.io/static/database-gb/entries/skoardy-cat/files/skoardy-cat.gb",
    ),
    (
        "Space Waste",
        "https://hh3.gbdev.io/static/database-gb/entries/space-waste/files/space-waste.gb",
    ),
    ("T-Rex", "https://hh3.gbdev.io/static/database-gb/entries/t-rex/files/t-rex.gb"),
    (
        "Tobu Tobu Girl",
        "https://hh3.gbdev.io/static/database-gb/entries/tobu-tobu-girl/files/tobutobugirl.gb",
    ),
    ("Tuff", "https://hh3.gbdev.io/static/database-gb/entries/tuff-gb/files/tuff.gb"),
    (
        "Wheat and Saber",
        "https://hh3.gbdev.io/static/database-gb/entries/wheat-and-saber/files/wheat-and-saber.gb",
    ),
    (
        "Wozzie",
        "https://hh3.gbdev.io/static/database-gb/entries/wozzie/files/wozzie.gb",
    ),
]

print("Testing Homebrew Hub Game Boy ROMs...")
print("=" * 60)

downloads_dir = os.path.expanduser("~/projects/konsomejona.github.io/downloads")
os.makedirs(downloads_dir, exist_ok=True)

successful = []

for name, url in games_to_try:
    filename = url.split("/")[-1]
    filepath = os.path.join(downloads_dir, filename)

    # Check if already exists
    if os.path.exists(filepath):
        size = os.path.getsize(filepath)
        if size > 1000:
            print(f"✓ Have: {name} ({filename})")
            successful.append((name, filename))
            continue

    # Try to download
    try:
        response = requests.head(url, timeout=2, allow_redirects=True)
        if response.status_code == 200:
            # Actually download the file
            response = requests.get(url, timeout=10)
            if (
                len(response.content) > 1000
                and b"DOCTYPE" not in response.content[:100]
            ):
                with open(filepath, "wb") as f:
                    f.write(response.content)
                print(f"✓ Downloaded: {name} ({len(response.content):,} bytes)")
                successful.append((name, filename))
            else:
                print(f"✗ {name}: Invalid content")
        else:
            print(f"✗ {name}: HTTP {response.status_code}")
    except Exception as e:
        print(f"✗ {name}: {type(e).__name__}")

print("\n" + "=" * 60)
print(f"Found {len(successful)} working ROMs")

if successful:
    print("\nWorking games:")
    for name, filename in successful:
        print(f"  • {name}: {filename}")
