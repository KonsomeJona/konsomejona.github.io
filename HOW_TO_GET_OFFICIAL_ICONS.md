# How to Get Official App Icons from Google Play Store

Since Google Play Store has anti-scraping protections, here's how to manually get the official icons for your apps:

## Method 1: Direct URL Construction (Easiest)

The official Google Play Store CDN follows this pattern:

```
https://play-lh.googleusercontent.com/[ICON_HASH]=s512-rw
```

### Steps:
1. Visit your app on Play Store: `https://play.google.com/store/apps/details?id=[PACKAGE_ID]`
2. Right-click on the app icon and select "Inspect Element" or "Inspect"
3. In the HTML inspector, find the `<img>` tag for the icon
4. Copy the `src` URL
5. Replace the size parameter at the end with `=s512-rw` to get the highest quality (512x512)
6. Download the image from that URL

## Method 2: Browser Extension

Use a Chrome extension like "Image Downloader" or "Download All Images":
1. Install the extension
2. Visit the Play Store page for your app
3. Use the extension to download all images
4. Select the largest app icon (usually 512x512)

## Method 3: Using DevTools Network Tab

1. Open Chrome DevTools (F12)
2. Go to the Network tab
3. Filter by "Img"
4. Visit the Play Store page for your app
5. Look for the icon image in the network requests
6. Right-click and "Open in new tab"
7. Add `=s512-rw` to the end of the URL for high resolution
8. Save the image

## Your Apps to Download:

### Active Apps:
- **TronWear**: https://play.google.com/store/apps/details?id=me.takohi.tronwear
- **ZenBreath**: https://play.google.com/store/apps/details?id=com.takohi.mindfulbreath
- **Time Speak**: https://play.google.com/store/apps/details?id=me.takohi.hourlychime
- **AstroWear**: https://play.google.com/store/apps/details?id=com.studiojona.astrowear
- **Sky Bird FREE**: https://play.google.com/store/apps/details?id=com.flappybird.wear
- **Sky Bird PRO**: Check your Play Console for correct package ID (404 error encountered)
- **IPTV Watch**: https://play.google.com/store/apps/details?id=me.takohi.iptv
- **WearGB Pro**: Check your Play Console for correct package ID (404 error encountered)
- **EasyPrint**: https://play.google.com/store/apps/details?id=com.takohi.easyprint
- **Mood Glow**: https://play.google.com/store/apps/details?id=com.takohi.moodlight

## Recommended File Names:

Once downloaded, rename the icons to:
- `tronwear-icon.png`
- `zenbreath-icon.png`
- `timespeak-icon.png`
- `astrowear-icon.png`
- `skybird-free-icon.png`
- `skybird-pro-icon.png`
- `iptvwatch-icon.png`
- `weargb-icon.png`
- `easyprint-icon.png`
- `moodglow-icon.png`

## Icon Specifications:

- **Size**: 512x512px (recommended for best quality)
- **Format**: PNG with transparency or WEBP
- **Quality**: Use the highest resolution available

## Note on 404 Errors:

Some package IDs returned 404 errors. Please verify:
1. The app is published (not in draft or testing)
2. The package ID is correct in your Play Console
3. The app is available in the US region (change `&hl=en` to your region if needed)

---

**OctoMouse Icon**: Already created as `octomouse-icon.svg` ✓
