# 🔥 Firebase Setup for WearGB QR System

## Quick Setup (5 minutes)

### 1. Create/Access Firebase Project

1. Go to [Firebase Console](https://console.firebase.google.com/)
2. Either:
   - **Create New Project**: "WearGB" or "weargb" 
   - **Use Existing**: If you have "weargb" project already

### 2. Enable Realtime Database

1. In Firebase Console → **Realtime Database**
2. Click **"Create Database"**  
3. **Start in test mode** (allows read/write for 30 days)
4. Choose location: **us-central1** (or closest to you)

### 3. Set Database Rules

Go to **Realtime Database → Rules** and paste:

```json
{
  "rules": {
    "url-sessions": {
      "$sessionId": {
        ".read": true,
        ".write": true,
        ".validate": "newData.hasChildren(['url', 'timestamp', 'consumed'])"
      }
    }
  }
}
```

Click **"Publish"**

### 4. Get Web App Configuration

1. **Project Settings** → **General**
2. Scroll to **"Your apps"**
3. Click **"Add app"** → **Web (</>) ** 
4. App nickname: **"WearGB Web Interface"**
5. Copy the `firebaseConfig` object

### 5. Update Web Interface

Replace the Firebase config in `weargb-input.html`:

```javascript
const firebaseConfig = {
    apiKey: "YOUR_ACTUAL_API_KEY",
    authDomain: "weargb.firebaseapp.com",
    databaseURL: "https://weargb-default-rtdb.firebaseio.com", 
    projectId: "weargb",
    storageBucket: "weargb.appspot.com",
    messagingSenderId: "123456789",
    appId: "1:123456789:web:abcdef123"
};
```

### 6. Get Android Configuration  

1. **Project Settings** → **General**
2. Click **"Add app"** → **Android**
3. Package name: **`me.takohi.weargb`**
4. Download **`google-services.json`**
5. Replace the file in: `app-wear/google-services.json`

## 🧪 Test Firebase Setup

### Test Database Access:
Visit: `https://weargb-default-rtdb.firebaseio.com/url-sessions.json`
- Should show `null` or `{}` (empty database)
- Should NOT show "Permission denied"

### Test Web Interface:
1. Update `weargb-input.html` with real config
2. Visit: `https://konsomejona.github.io/weargb-input.html?session=test123`
3. Enter a test URL → Click "Send to Watch"
4. Should see success message

### Test Database Write:
Check: `https://weargb-default-rtdb.firebaseio.com/url-sessions/test123.json`
- Should show the test data you just sent

## 🔒 Security Notes

- **API Key**: Safe to include in client-side code (Firebase handles security via database rules)
- **Database Rules**: Control who can read/write data
- **Test Mode**: Remember to update rules before 30-day expiry

## ✅ Ready for Production

Once configured:
- ✅ Users scan QR codes from watch
- ✅ Web interface opens on phone  
- ✅ URLs sync instantly via Firebase
- ✅ Watch receives URLs in real-time
- ✅ Zero server maintenance needed

## 🚨 Current Status

The web interface is live but needs real Firebase configuration. The placeholder config won't work for actual data transfer.

**Next Steps:**
1. Follow steps 1-6 above
2. Test the system end-to-end  
3. Enjoy QR code URL entry! 🎉