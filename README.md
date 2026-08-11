<div align="center">

# 🌌 Visionary3D Studio

### *Conversational AI-Driven 3D Asset & Animation Generation Engine*

[![GitHub Stars](https://img.shields.io/github/stars/EdgeAgent/visionary3d-studio?style=flat-square&color=blue)](https://github.com/EdgeAgent/visionary3d-studio)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=flat-square)](https://opensource.org/licenses/MIT)
[![Python 3.10+](https://img.shields.io/badge/python-3.10%2B-blue.svg?style=flat-square)](https://www.python.org/downloads/)
[![Langflow Ready](https://img.shields.io/badge/Langflow-Orchestrated-orange?style=flat-square)](https://langflow.org)
[![Blender API](https://img.shields.io/badge/Blender-4.x%2B-green?style=flat-square)](https://www.blender.org)

*Bridge the gap between natural language intent and professional 3D production.*

</div>

---

## 🎯 Overview

**Visionary3D Studio** is an advanced generative AI mashup that combines **Langflow**'s visual agent orchestration with **Blender**'s robust Python API (`bpy`) through a secure **Model Context Protocol (MCP)** bridge. 

Instead of dealing with complex node trees, vertex modeling, and keyframe timelines manually, users simply describe what they want in natural language. Visionary3D Studio's multi-agent swarm handles prompt decomposition, procedural script generation, shader setup, and rendering validation automatically.

---

## 🏗️ Architecture & Data Flow

```text
+-------------------------------------------------------------------+
|                        User Prompt Interface                      |
+-------------------------------------------------------------------+
                                  |
                                  v
+-------------------------------------------------------------------+
|                  Langflow Orchestration Tier                      |
|           (Intent Decomposition & Multi-Agent Swarm)              |
+-------------------------------------------------------------------+
                                  |
                                  v
+-------------------------------------------------------------------+
|                 Model Context Protocol (MCP) Bridge               |
|            (AST Verification & Secure Code Transmission)          |
+-------------------------------------------------------------------+
                                  |
                                  v
+-------------------------------------------------------------------+
|                  Blender Execution Engine (bpy)                   |
|           (Procedural Modeling, PBR Materials & Rendering)        |
+-------------------------------------------------------------------+
```

---

## 📂 Project Structure

```text
visionary3d-studio/
├── mcp-server/
│   └── server.py             # FastAPI / HTTP MCP server for Blender bridging
├── blender-addon/
│   └── generator_template.py # Procedural generation & shader scripts
├── langflow/
│   └── visionary_flow.json   # Exported Langflow multi-agent workflow
├── scripts/
│   └── setup.sh              # Environment setup & launcher script
└── README.md
```

---

## 🚀 Quick Start Guide

### Prerequisites

- Python 3.10 or higher
- Blender 4.x installed on your system (`blender` command available in PATH)

### Installation & Execution

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/EdgeAgent/visionary3d-studio.git
   cd visionary3d-studio
   ```

2. **Run the Setup Script**:
   ```bash
   chmod +x scripts/setup.sh
   ./scripts/setup.sh
   ```

3. **Start the MCP Server**:
   ```bash
   cd mcp-server
   python3 server.py
   ```

4. **Test Generation**:
   You can trigger a test render or script execution by sending a POST request to the MCP server:
   ```bash
   curl -X POST http://localhost:8080/execute \
     -H "Content-Type: application/json" \
     -d '{"script": "import bpy; bpy.ops.mesh.primitive_cube_add()"}'
   ```

---

## 💡 Use Cases & Game-Changing Potential

- **Instant Prototyping**: Game developers can generate entire environmental blockouts and prop libraries using conversational prompts.
- **Automated E-Commerce Rendering**: Generate product placement scenes and studio lighting setups programmatically.
- **Educational 3D Tooling**: Lower the barrier to entry for students learning 3D computer graphics and procedural programming.

---

## 🛡️ License

Distributed under the **MIT License**. See `LICENSE` for more information.

---

*Built with ❤️ by Manus AI for EdgeAgent.*
