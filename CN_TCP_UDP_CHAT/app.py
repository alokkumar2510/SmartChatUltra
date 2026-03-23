#!/usr/bin/env python3
"""
run_all.py — SmartChat X Master Launcher
════════════════════════════════════════
Starts ALL servers and the WebSocket bridge in one command.

Usage:
  python run_all.py

This will start:
  1. TCP Server  (port 9000) — Reliable chat messages
  2. UDP Server  (port 9001) — Typing indicators, presence
  3. WS Bridge   (port 8765) — Browser ↔ backend bridge

Then open frontend/index.html in your browser.
"""

import threading
import asyncio
import sys
import os
import time
import logging

# Ensure project root is in path
sys.path.insert(0, os.path.dirname(__file__))

# Configure root logger
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s [%(name)s] %(message)s',
    datefmt='%H:%M:%S'
)
logger = logging.getLogger("SmartChatX.Launcher")

from server.tcp_server import start_tcp_server
from server.udp_server import start_udp_server


def start_ws_bridge():
    """Start the WebSocket bridge in its own event loop."""
    from server.ws_bridge import main as ws_main
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(ws_main())


if __name__ == "__main__":
    print()
    print("╔═══════════════════════════════════════════════════════════════╗")
    print("║                                                               ║")
    print("║   ⚡ SmartChat X ULTRA — Decentralized AI Communication ⚡   ║")
    print("║                                                               ║")
    print("║   Features:                                                   ║")
    print("║   🧠 AI-Augmented Messaging                                  ║")
    print("║   🌐 Adaptive Multi-Protocol Routing                         ║")
    print("║   📞 WebRTC Peer-to-Peer Communication      ← NEW           ║")
    print("║   ⛓️  Blockchain Message Ledger               ← NEW           ║")
    print("║   🔐 Hybrid Encryption (RSA+AES Simulation)                  ║")
    print("║   📡 Intelligent Message Queue                               ║")
    print("║   📊 Network Intelligence Dashboard (Chart.js)               ║")
    print("║   🧩 Plugin Architecture                                     ║")
    print("║   🌍 Distributed Server Simulation                           ║")
    print("║   🎮 Gamified Interaction                                    ║")
    print("║   🧪 Network Condition Simulator                             ║")
    print("║   ⚡ Real-Time Presence Engine                               ║")
    print("║                                                               ║")
    print("╠═══════════════════════════════════════════════════════════════╣")
    print("║                                                               ║")
    print("║   Starting servers...                                         ║")
    print("║   TCP Server  → port 9000 (Reliable Messages)                ║")
    print("║   UDP Server  → port 9001 (Typing/Presence)                  ║")
    print("║   WS Bridge   → port 8765 (Browser + WebRTC Signaling)       ║")
    print("║                                                               ║")
    print("║   Open frontend/index.html in your browser                   ║")
    print("║   Press Ctrl+C to stop all servers                            ║")
    print("║                                                               ║")
    print("╚═══════════════════════════════════════════════════════════════╝")
    print()

    # 1. UDP server in daemon thread
    udp_thread = threading.Thread(target=start_udp_server, daemon=True, name="UDP-Server")
    udp_thread.start()
    time.sleep(0.3)

    # 2. WebSocket bridge in daemon thread
    ws_thread = threading.Thread(target=start_ws_bridge, daemon=True, name="WS-Bridge")
    ws_thread.start()
    time.sleep(0.3)

    # 3. TCP server on main thread
    try:
        start_tcp_server()
    except KeyboardInterrupt:
        print()
        logger.info("🛑 Shutting down all SmartChat X servers...")
        print()
        print("╔═══════════════════════════════════════════════════════════╗")
        print("║   All servers stopped. Thank you for using SmartChat X!  ║")
        print("╚═══════════════════════════════════════════════════════════╝")
