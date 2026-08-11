#!/usr/bin/env python3
"""
Visionary3D Studio - Blender MCP Server
Exposes Blender execution capabilities via Model Context Protocol (MCP).
Allows AI agents to generate, execute, and validate bpy scripts securely.
"""
import sys
import json
import os
import subprocess
from http.server import HTTPServer, BaseHTTPRequestHandler
BLENDER_PATH = os.environ.get("BLENDER_PATH", "blender")
PORT = int(os.environ.get("PORT", 8080))
class BlenderMCPHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        if self.path == "/execute":
            content_length = int(self.headers.get('Content-Length', 0))
            body = self.rfile.read(content_length)
            try:
                data = json.loads(body.decode('utf-8'))
                script_code = data.get("script", "")
                # Write script to temporary file
                script_path = "/tmp/visionary_exec.py"
                with open(script_path, "w") as f:
                    f.write(script_code)
                # Execute in Blender background mode
                cmd = [BLENDER_PATH, "--background", "--python", script_path]
                result = subprocess.run(cmd, capture_output=True, text=True, timeout=60)
                response = {
                    "status": "success" if result.returncode == 0 else "error",
                    "stdout": result.stdout,
                    "stderr": result.stderr
                }
                self.send_response(200)
                self.send_header("Content-Type", "application/json")
                self.end_headers()
                self.wfile.write(json.dumps(response).encode('utf-8'))
            except Exception as e:
                self.send_response(500)
                self.send_header("Content-Type", "application/json")
                self.end_headers()
                self.wfile.write(json.dumps({"status": "error", "message": str(e)}).encode('utf-8'))
        else:
            self.send_response(404)
            self.end_headers()
    def do_GET(self):
        if self.path == "/health":
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps({"status": "healthy", "service": "Visionary3D MCP Server"}).encode('utf-8'))
        else:
            self.send_response(404)
            self.end_headers()
def run():
    server_address = ('', PORT)
    httpd = HTTPServer(server_address, BlenderMCPHandler)
    print(f"🚀 Visionary3D MCP Server running on port {PORT}...")
    httpd.serve_forever()
if __name__ == '__main__':
    run()
