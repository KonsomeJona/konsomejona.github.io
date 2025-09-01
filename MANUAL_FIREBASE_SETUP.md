# 🔥 Manual Firebase CLI Setup for WearGB

Since the automated script needs interactive authentication, here's the step-by-step process:

## Step 1: Authentication 🔐

```bash
cd /Users/jona/projects/konsomejona.github.io
firebase login
```
- This opens your browser
- Sign in with your Google account
- Authorize Firebase CLI

## Step 2: Check Existing Projects 📋

```bash
firebase projects:list
```

Look for an existing "weargb" project or note if you need to create one.

## Step 3a: Use Existing Project (if you have one)

```bash
firebase use weargb
```

## Step 3b: Create New Project (if needed)

```bash
firebase projects:create weargb-$(date +%s) --display-name "WearGB Emulator"
# Note the project ID it creates
firebase use PROJECT_ID_FROM_ABOVE
```

## Step 4: Initialize Database 💾

```bash
firebase init database
```

Choose:
- Use existing project (select your weargb project)
- Database rules file: `database.rules.json`
- Don't overwrite if it exists

## Step 5: Set Up Database Rules 📝

Create rules file:
```bash
cat > database.rules.json << 'EOF'
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
EOF
```

Deploy rules:
```bash
firebase deploy --only database
```

## Step 6: Create Web App 🌐

```bash
firebase apps:create web --display-name "WearGB Web Interface"
```

Get the app ID from the output, then get config:
```bash
firebase apps:list web
# Note the App ID, then:
firebase apps:sdkconfig web YOUR_APP_ID
```

## Step 7: Update Web Interface ⚙️

Copy the config output and manually update `weargb-input.html`:

Replace this section:
```javascript
const firebaseConfig = {
    apiKey: "YOUR_API_KEY", // Replace with real value
    authDomain: "weargb.firebaseapp.com", // Replace with real value
    databaseURL: "https://weargb-default-rtdb.firebaseio.com", // Replace with real value
    projectId: "weargb", // Replace with real value
    storageBucket: "weargb.appspot.com", // Replace with real value
    messagingSenderId: "YOUR_SENDER_ID", // Replace with real value
    appId: "YOUR_APP_ID" // Replace with real value
};
```

## Step 8: Create Android App 🤖

```bash
firebase apps:create android me.takohi.weargb --display-name "WearGB Android"
```

Download config:
```bash
firebase apps:list android
# Note the App ID, then:
firebase apps:sdkconfig android YOUR_ANDROID_APP_ID > google-services.json
```

## Step 9: Test Setup 🧪

Test database access:
```bash
curl "https://YOUR_PROJECT_ID-default-rtdb.firebaseio.com/url-sessions.json"
```

Should return `null` (empty database) not "Permission denied"

## Step 10: Deploy Updated Files 🚀

```bash
git add .
git commit -m "Configure Firebase for WearGB QR system"
git push origin main
```

## 🎉 Success!

Your QR code system will now be fully functional:

1. **Watch**: Shows QR code with session ID
2. **Phone**: Scans → Opens GitHub Pages site
3. **Web**: Reads session, user enters URL, Firebase stores it
4. **Watch**: Receives URL instantly via Firebase
5. **Result**: ROM downloads successfully

## 🔗 Test URLs

- **Web Interface**: `https://konsomejona.github.io/weargb-input.html?session=test123`
- **Database**: `https://YOUR_PROJECT_ID-default-rtdb.firebaseio.com/url-sessions.json`

---

**Run these commands one by one and let me know if you need help with any step!** 🚀