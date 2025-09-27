# Firebase Setup Instructions

## Update Firebase Realtime Database Rules

1. Go to [Firebase Console](https://console.firebase.google.com/)
2. Select the **weargb** project
3. Go to **Realtime Database** in the left menu
4. Click on the **Rules** tab
5. Replace the existing rules with:

```json
{
  "rules": {
    "rom-sessions": {
      ".read": true,
      ".write": true
    },
    "public-feedback": {
      ".read": true,
      ".write": true
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