#!/bin/bash

echo "🔧 Setting up YouTube Browser environment..."

# Install Python dependencies
pip install -r /workspace/requirements.txt

# Create desktop entry for easy access
mkdir -p ~/.local/share/applications
cat > ~/.local/share/applications/youtube-browser.desktop << 'EOF'
[Desktop Entry]
Version=1.0
Type=Application
Name=YouTube Browser
Comment=Watch YouTube in GitHub Codespaces
Exec=python3 /workspace/main.py
Icon=web-browser
Categories=Network;WebBrowser;
Terminal=false
StartupNotify=true
EOF

# Make run script executable
chmod +x /workspace/run.sh

echo "✅ Setup complete!"
echo "🚀 Run './run.sh' to start the browser"