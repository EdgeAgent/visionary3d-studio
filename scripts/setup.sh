#!/bin/bash
echo "🚀 Initializing Visionary3D Studio Environment..."
# Install Python requirements if needed
python3 -m pip install --upgrade pip
echo "📦 Setting up MCP server and dependencies..."
cd /home/ubuntu/visionary3d-studio/mcp-server
echo "✨ Visionary3D Studio is ready to deploy!"
echo "To run the MCP server: python3 server.py"
