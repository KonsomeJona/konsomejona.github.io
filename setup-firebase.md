# Firebase Setup Instructions

## IMPORTANT: Make sure you're in Realtime Database, NOT Firestore!

### Finding the Right Place:

1. Go to [Firebase Console](https://console.firebase.google.com/)
2. Select the **weargb** project
3. In the left sidebar, look for **"Realtime Database"** (NOT "Cloud Firestore")
   - The icon looks like a lightning bolt ⚡
   - It's usually below "Cloud Firestore" in the menu
4. Click on **Realtime Database**
5. At the top of the page, you'll see tabs: **Data | Rules | Backups | Usage**
6. Click on the **Rules** tab
7. You should see a JSON editor that starts with `{"rules":`
8. Select ALL the text in the editor (Ctrl+A or Cmd+A)
9. Delete it and paste this instead:

```json
{
  "rules": {
    ".read": false,
    ".write": false,
    "url-sessions": {
      ".read": true,
      ".write": true,
      ".indexOn": ["timestamp", "createdAt"]
    },
    "public-feedback": {
      ".read": true,
      ".write": true,
      ".indexOn": ["timestamp_millis", "timestamp"]
    },
    "public-feedback-test": {
      ".read": true,
      ".write": true
    }
  }
}
```

6. Click **Publish**

## Test the Feedback System

1. Open [Test Firebase Connection](https://konsomejona.github.io/test-firebase.html)
2. Click "Test Write" - should show green checkmark
3. Click "Test Read" - should show green checkmark

## Use the Feedback System

- **Submit Feedback**: https://konsomejona.github.io/weargb-feedback.html
- **View Feedback (Admin)**: https://konsomejona.github.io/weargb-feedback-admin.html

The feedback system now uses the `public-feedback` path which allows anonymous read/write access.