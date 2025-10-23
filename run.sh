#!/bin/bash

echo "🎬 Starting YouTube Browser..."
echo "🖥️  Setting up environment..."

# Use Desktop Lite display
export DISPLAY=:0
export QT_QPA_PLATFORM=xcb

# Fix potential issues
export QT_DEBUG_PLUGINS=0
export QTWEBENGINE_CHROMIUM_FLAGS="--no-sandbox --disable-web-security"

echo "🔧 Environment:"
echo "   DISPLAY: $DISPLAY"
echo "   QT_PLATFORM: $QT_QPA_PLATFORM"

echo "🚀 Launching browser..."
python3 main.py