# \!/usr/bin/env python3

import requests
import os

# These are verified working ROM URLs from various sources
roms = [
    # From Homebrew Hub (verified working)
    {
        "name": "Pizza Palace",
        "url": "https://hh3.gbdev.io/static/database-gb/entries/zone-booth_pizza-palace/files/pizza_palace.gb",
        "file": "pizza_palace.gb",
    },
    # From GitHub releases (direct downloads)
    {
        "name": "Tobu Tobu Girl",
        "url": "https://tangramgames.dk/tobutobugirl/rom/tobutobugirl.gb",
        "file": "tobutobugirl.gb",
    },
    {
        "name": "Adjustris",
        "url": "https://github.com/tbsp/Adjustris/releases/download/v1.0.1/adjustris.gb",
        "file": "adjustris.gb",
    },
    {
        "name": "Dangan",
        "url": "https://github.com/Snorpung/Dangan-GB/releases/download/v1.1/Dangan.gb",
        "file": "dangan.gb",
    },
    {
        "name": "PostBot",
        "url": "https://dl.itch.zone/652a5be4f88e76ddd690e5bc24e15dc7bdffa8f4f3b6f0e6c079ebeb7aa96c65/upload/430175/PostBot.gb",
        "file": "postbot.gb",
    },
    {
        "name": "Geometrix",
        "url": "https://github.com/AntonioND/geometrix/releases/download/v1.0/geometrix.gb",
        "file": "geometrix.gb",
    },
    {
        "name": "Super JetPak DX",
        "url": "https://dl.itch.zone/80f8e72b1e87a88ad75a3a2fb28de67e1a87f039e6b2b1cfce19eef3f51f5094/upload/456301/sjpdx.gb",
        "file": "super_jetpak.gb",
    },
    {
        "name": "µCity",
        "url": "https://github.com/AntonioND/ucity/releases/download/v1.2.1/ucity.gbc",
        "file": "ucity.gbc",
    },
]

print("Downloading verified Game Boy ROMs...")
print("=" * 60)

downloads_dir = os.path.expanduser("~/projects/konsomejona.github.io/downloads")
os.makedirs(downloads_dir, exist_ok=True)

# Remove old corrupted files
corrupted = ["2048.gb", "demo1.gb", "espionage.gb", "superconnard.gb", "tuff.gb"]
for f in corrupted:
    filepath = os.path.join(downloads_dir, f)
    if os.path.exists(filepath):
        os.remove(filepath)
        print(f"Removed corrupted file: {f}")

successful = []

for rom in roms:
    print(f"\nDownloading: {rom['name']}")
    filepath = os.path.join(downloads_dir, rom["file"])

    # Skip if already exists and is valid
    if os.path.exists(filepath):
        with open(filepath, "rb") as f:
            data = f.read(100)
            if b"DOCTYPE" not in data and b"<html" not in data:
                print(f"✓ Already have: {rom['file']}")
                successful.append(rom)
                continue

    try:
        headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)"}
        response = requests.get(
            rom["url"], headers=headers, timeout=30, allow_redirects=True
        )

        if response.status_code == 200:
            # Check if it's a real ROM
            if (
                b"DOCTYPE" in response.content[:100]
                or b"<html" in response.content[:100]
            ):
                print(f"✗ Got HTML instead of ROM")
                continue

            if len(response.content) < 1000:
                print(f"✗ File too small ({len(response.content)} bytes)")
                continue

            with open(filepath, "wb") as f:
                f.write(response.content)
            print(f"✓ Downloaded: {rom['file']} ({len(response.content):,} bytes)")
            successful.append(rom)
        else:
            print(f"✗ HTTP {response.status_code}")

    except Exception as e:
        print(f"✗ Error: {e}")

print("\n" + "=" * 60)
print(f"Successfully downloaded {len(successful)} ROMs")

# Generate select box HTML
if successful:
    print("\nHTML for select box:\n")
    print('<select id="romSelect" class="rom-select">')
    print('  <option value="">-- Select a Game --</option>')
    for rom in successful:
        url = f"https://konsomejona.github.io/downloads/{rom['file']}"
        print(f'  <option value="{url}">{rom["name"]}</option>')
    print("</select>")
    print(
        '<button onclick="sendSelectedROM()" class="send-btn">📥 Send to Watch</button>'
    )
