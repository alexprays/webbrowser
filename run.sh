#!/bin/bash

# Set display for virtual desktop
export DISPLAY=:1
export QT_QPA_PLATFORM=xcb

# Start the browser
echo "🚀 Starting YouTube Browser..."
echo "📺 The browser will open in the virtual desktop"
echo "🌐 Access it via: Ports tab → 6080 → Open in Browser"
echo "🔑 Password: codespaces"
echo ""

python main.py