#!/bin/bash
# Script to download official app icons from Google Play Store

echo "Downloading official app icons from Google Play Store..."

# Function to download icon from Play Store
download_icon() {
    local package_id=$1
    local output_file=$2

    echo "Fetching icon for $package_id..."

    # Download the Play Store page
    page_content=$(curl -s "https://play.google.com/store/apps/details?id=$package_id&hl=en")

    # Extract the icon URL (look for the app icon image)
    icon_url=$(echo "$page_content" | grep -oP '(?<=<img[^>]*src=")[^"]*(?="[^>]*alt="Icon image")' | head -1)

    # If the first method doesn't work, try alternative pattern
    if [ -z "$icon_url" ]; then
        icon_url=$(echo "$page_content" | grep -oP 'https://play-lh\.googleusercontent\.com/[^"]*=s512[^"]*' | head -1)
    fi

    if [ -n "$icon_url" ]; then
        # Download the icon
        curl -s "$icon_url" -o "$output_file"
        echo "✓ Downloaded: $output_file"
    else
        echo "✗ Could not find icon URL for $package_id"
        echo "  Manual download URL: https://play.google.com/store/apps/details?id=$package_id"
    fi
}

# Download icons for all apps
download_icon "me.takohi.tronwear" "tronwear-icon.png"
download_icon "com.takohi.mindfulbreath" "zenbreath-icon.png"
download_icon "me.takohi.hourlychime" "timespeak-icon.png"
download_icon "com.studiojona.astrowear" "astrowear-icon.png"
download_icon "com.flappybird.wear" "skybird-free-icon.png"
download_icon "com.flappybird.wear.pro" "skybird-pro-icon.png"
download_icon "me.takohi.iptv" "iptvwatch-icon.png"
download_icon "me.takohi.weargb" "weargb-icon.png"
download_icon "com.takohi.easyprint" "easyprint-icon.png"
download_icon "com.takohi.moodlight" "moodglow-icon.png"

echo ""
echo "Download complete! Check the files above."
echo "If any downloads failed, you can manually download from the Play Store page."
