#!/bin/bash
# Automated Firebase Setup for WearGB
# Like AWS CLI but for Firebase!

set -e  # Exit on error

echo "🔥 Firebase CLI Setup for WearGB"
echo "================================"

# Step 1: Login to Firebase
echo "📱 Step 1: Firebase Login"
echo "This will open your browser to authenticate..."
firebase login

# Step 2: List existing projects or create new one
echo ""
echo "📋 Step 2: Firebase Projects"
echo "Your existing Firebase projects:"
firebase projects:list

echo ""
read -p "Do you want to use existing 'weargb' project or create new one? (existing/new): " PROJECT_CHOICE

if [ "$PROJECT_CHOICE" = "new" ]; then
    echo "🆕 Creating new Firebase project..."
    read -p "Enter project ID (e.g., weargb-12345): " PROJECT_ID
    firebase projects:create "$PROJECT_ID" --display-name "WearGB Emulator"
    PROJECT_ID="$PROJECT_ID"
else
    read -p "Enter existing project ID (e.g., weargb): " PROJECT_ID
fi

# Step 3: Initialize Firebase in current directory
echo ""
echo "🚀 Step 3: Initialize Firebase Project"
firebase init database hosting --project "$PROJECT_ID"

# Step 4: Set up Realtime Database rules
echo ""
echo "📝 Step 4: Configure Database Rules"
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

# Step 5: Deploy database rules
echo "🚀 Deploying database rules..."
firebase deploy --only database --project "$PROJECT_ID"

# Step 6: Get project configuration
echo ""
echo "⚙️  Step 5: Getting Project Configuration"
PROJECT_INFO=$(firebase projects:list --json | jq -r ".[] | select(.projectId == \"$PROJECT_ID\")")

if [ -z "$PROJECT_INFO" ]; then
    echo "❌ Project not found. Please check the project ID."
    exit 1
fi

# Step 7: Create web app configuration
echo "🌐 Step 6: Creating Web App Configuration"
WEB_APP_ID=$(firebase apps:list web --json --project "$PROJECT_ID" | jq -r '.[0].appId' 2>/dev/null || echo "")

if [ "$WEB_APP_ID" = "" ] || [ "$WEB_APP_ID" = "null" ]; then
    echo "Creating new web app..."
    firebase apps:create web --project "$PROJECT_ID" --display-name "WearGB Web Interface"
    WEB_APP_ID=$(firebase apps:list web --json --project "$PROJECT_ID" | jq -r '.[0].appId')
fi

# Get web app config
echo "Getting web app configuration..."
WEB_CONFIG=$(firebase apps:sdkconfig web "$WEB_APP_ID" --project "$PROJECT_ID")

# Step 8: Update web interface with real config
echo ""
echo "🔧 Step 7: Updating Web Interface Configuration"

# Extract config values using sed/grep (more portable than jq for config)
API_KEY=$(echo "$WEB_CONFIG" | grep -o '"apiKey": "[^"]*"' | cut -d'"' -f4)
AUTH_DOMAIN=$(echo "$WEB_CONFIG" | grep -o '"authDomain": "[^"]*"' | cut -d'"' -f4)
DATABASE_URL=$(echo "$WEB_CONFIG" | grep -o '"databaseURL": "[^"]*"' | cut -d'"' -f4)
PROJECT_ID_CONFIG=$(echo "$WEB_CONFIG" | grep -o '"projectId": "[^"]*"' | cut -d'"' -f4)
STORAGE_BUCKET=$(echo "$WEB_CONFIG" | grep -o '"storageBucket": "[^"]*"' | cut -d'"' -f4)
MESSAGING_SENDER_ID=$(echo "$WEB_CONFIG" | grep -o '"messagingSenderId": "[^"]*"' | cut -d'"' -f4)
APP_ID=$(echo "$WEB_CONFIG" | grep -o '"appId": "[^"]*"' | cut -d'"' -f4)

# Update the web interface file
sed -i.bak "s/apiKey: \"YOUR_API_KEY\"/apiKey: \"$API_KEY\"/" weargb-input.html
sed -i.bak "s/authDomain: \"weargb.firebaseapp.com\"/authDomain: \"$AUTH_DOMAIN\"/" weargb-input.html  
sed -i.bak "s|databaseURL: \"https://weargb-default-rtdb.firebaseio.com\"|databaseURL: \"$DATABASE_URL\"|" weargb-input.html
sed -i.bak "s/projectId: \"weargb\"/projectId: \"$PROJECT_ID_CONFIG\"/" weargb-input.html
sed -i.bak "s/storageBucket: \"weargb.appspot.com\"/storageBucket: \"$STORAGE_BUCKET\"/" weargb-input.html
sed -i.bak "s/messagingSenderId: \"YOUR_SENDER_ID\"/messagingSenderId: \"$MESSAGING_SENDER_ID\"/" weargb-input.html
sed -i.bak "s/appId: \"YOUR_APP_ID\"/appId: \"$APP_ID\"/" weargb-input.html

# Step 9: Create Android configuration  
echo ""
echo "🤖 Step 8: Creating Android App Configuration"

ANDROID_APP_ID=$(firebase apps:list android --json --project "$PROJECT_ID" | jq -r '.[] | select(.packageName == "me.takohi.weargb") | .appId' 2>/dev/null || echo "")

if [ "$ANDROID_APP_ID" = "" ] || [ "$ANDROID_APP_ID" = "null" ]; then
    echo "Creating Android app..."
    firebase apps:create android me.takohi.weargb --project "$PROJECT_ID" --display-name "WearGB Android"
    ANDROID_APP_ID=$(firebase apps:list android --json --project "$PROJECT_ID" | jq -r '.[] | select(.packageName == "me.takohi.weargb") | .appId')
fi

# Download google-services.json
echo "Downloading google-services.json..."
firebase apps:sdkconfig android "$ANDROID_APP_ID" --project "$PROJECT_ID" > google-services.json

# Step 10: Test the setup
echo ""
echo "🧪 Step 9: Testing Firebase Setup"
DATABASE_TEST_URL="${DATABASE_URL}/url-sessions.json"
echo "Testing database access: $DATABASE_TEST_URL"

# Test write access
TEST_DATA='{"test": {"url": "https://example.com/test.gbc", "timestamp": '$(date +%s000)', "consumed": false}}'
curl -X PUT -d "$TEST_DATA" "$DATABASE_TEST_URL"

echo ""
echo "✅ Firebase Setup Complete!"
echo "=========================="
echo ""
echo "📋 Summary:"
echo "Project ID: $PROJECT_ID_CONFIG"
echo "Database URL: $DATABASE_URL"  
echo "Web App ID: $WEB_APP_ID"
echo "Android App ID: $ANDROID_APP_ID"
echo ""
echo "📁 Files Updated:"
echo "- weargb-input.html (with real Firebase config)"
echo "- google-services.json (for Android app)"
echo "- database.rules.json (database security rules)"
echo ""
echo "🚀 Next Steps:"
echo "1. Copy google-services.json to your Android app"
echo "2. Commit and push weargb-input.html updates"  
echo "3. Test the QR code system end-to-end"
echo ""
echo "🔗 Test URLs:"
echo "Web Interface: https://konsomejona.github.io/weargb-input.html?session=test123"
echo "Database: $DATABASE_TEST_URL"
echo ""
echo "🎉 Your QR code system is now fully configured!"