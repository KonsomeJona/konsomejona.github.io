#!/usr/bin/env python3
"""
Script to download official app icons from Google Play Store
Usage: python3 download_play_store_icons.py
"""

import urllib.request
import re
import os

def download_icon(package_id, output_filename):
    """Download app icon from Google Play Store"""
    print(f"Fetching icon for {package_id}...")

    url = f"https://play.google.com/store/apps/details?id={package_id}&hl=en"

    try:
        # Fetch the Play Store page
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}
        req = urllib.request.Request(url, headers=headers)

        with urllib.request.urlopen(req, timeout=10) as response:
            html = response.read().decode('utf-8')

        # Look for the icon URL in the HTML
        # Pattern for high-res icon (512px)
        pattern = r'https://play-lh\.googleusercontent\.com/[^"\']*=s512[^"\']*'
        matches = re.findall(pattern, html)

        if matches:
            icon_url = matches[0]

            # Download the icon
            print(f"  Downloading from: {icon_url[:80]}...")
            urllib.request.urlretrieve(icon_url, output_filename)
            print(f"  ✓ Saved: {output_filename}")
            return True
        else:
            print(f"  ✗ Could not find icon URL")
            print(f"  Manual download: {url}")
            return False

    except Exception as e:
        print(f"  ✗ Error: {str(e)}")
        print(f"  Manual download: {url}")
        return False

def main():
    """Download all app icons"""
    print("=" * 60)
    print("Play Store Icon Downloader")
    print("=" * 60)
    print()

    apps = [
        ("me.takohi.tronwear", "tronwear-icon.png"),
        ("com.takohi.mindfulbreath", "zenbreath-icon.png"),
        ("me.takohi.hourlychime", "timespeak-icon.png"),
        ("com.studiojona.astrowear", "astrowear-icon.png"),
        ("com.flappybird.wear", "skybird-free-icon.png"),
        ("com.flappybird.wear.pro", "skybird-pro-icon.png"),
        ("me.takohi.iptv", "iptvwatch-icon.png"),
        ("me.takohi.weargb", "weargb-icon.png"),
        ("com.takohi.easyprint", "easyprint-icon.png"),
        ("com.takohi.moodlight", "moodglow-icon.png"),
    ]

    success_count = 0
    for package_id, filename in apps:
        if download_icon(package_id, filename):
            success_count += 1
        print()

    print("=" * 60)
    print(f"Downloaded {success_count}/{len(apps)} icons successfully")
    print("=" * 60)

    if success_count < len(apps):
        print("\nNote: Some icons couldn't be downloaded automatically.")
        print("Please download them manually from the Play Store URLs shown above.")

if __name__ == "__main__":
    main()
