// Firebase Configuration Template for WearGB
// Replace with your actual Firebase project configuration

const firebaseConfig = {
    // Get these values from Firebase Console > Project Settings > General > Your apps > Web app
    apiKey: "YOUR_API_KEY_HERE",
    authDomain: "weargb.firebaseapp.com",
    databaseURL: "https://weargb-default-rtdb.firebaseio.com",
    projectId: "weargb",
    storageBucket: "weargb.appspot.com", 
    messagingSenderId: "YOUR_SENDER_ID",
    appId: "YOUR_APP_ID"
};

// Instructions:
// 1. Go to https://console.firebase.google.com/
// 2. Select your "weargb" project (or create if it doesn't exist)
// 3. Go to Project Settings > General
// 4. Scroll down to "Your apps" section
// 5. Click "Add app" > Web (</>) if no web app exists
// 6. Copy the firebaseConfig object
// 7. Replace the config in weargb-input.html with these real values

// Database Rules (set in Firebase Console > Realtime Database > Rules):
/*
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
*/