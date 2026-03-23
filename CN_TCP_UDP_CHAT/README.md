# ⚡ SmartChat X Ultra — Decentralized AI-Powered Communication System

> A production-level, startup-grade intelligent communication system combining Computer Networks, AI, WebRTC P2P, Blockchain logging, distributed systems, and futuristic UI design.

---

## 🚀 Features (12 Major Innovations)

| # | Feature | Description |
|---|---------|-------------|
| 1 | 🧠 **AI-Powered Chat Engine** | Smart replies, summarization, toxicity detection, Study Mode tutor |
| 2 | 🌐 **Adaptive Multi-Protocol Routing** | Auto-selects TCP/UDP/Hybrid/WebRTC per message type |
| 3 | 📞 **WebRTC P2P Communication** | Direct browser-to-browser messaging via DataChannels |
| 4 | ⛓️ **Blockchain Message Ledger** | SHA-256 proof-of-work chain, tamper detection, block explorer |
| 5 | 🔐 **Hybrid Encryption** | AES-256 + Diffie-Hellman key exchange simulation |
| 6 | ⚡ **Real-Time Presence** | Online/offline tracking, typing indicators via UDP |
| 7 | 📡 **Intelligent Message Queue** | Priority-based heap with offline storage + reconnect delivery |
| 8 | 📊 **Live Dashboard (Chart.js)** | Real-time protocol charts, latency graphs, routing logs |
| 9 | 🧩 **Plugin Architecture** | AI, Encryption, Blockchain, Analytics as hot-swappable plugins |
| 10 | 🌍 **Distributed Server Simulation** | 3-node cluster, 4 LB algorithms, failover + circuit breaker |
| 11 | 🎮 **Gamified Interaction** | XP, 10 levels, 10 badges, leaderboard |
| 12 | 🧪 **Network Condition Simulator** | Packet loss, latency, jitter, congestion with 7 presets |

---

## 📁 Project Structure

```
SmartChat-X-Ultra/
├── frontend/
│   ├── index.html          # 7-tab UI with WebRTC + Blockchain panels
│   ├── styles.css          # Glassmorphism + neon CSS (400+ lines)
│   └── app.js              # Chart.js + WebRTC + Blockchain + Full Logic
├── server/
│   ├── tcp_server.py       # Enhanced TCP server
│   ├── udp_server.py       # UDP server with presence + heartbeat
│   ├── ws_bridge.py        # Master controller (WebRTC signaling + full pipeline)
│   ├── ai_module.py        # AI engine (sentiment, toxicity, smart replies, tutor)
│   ├── encryption.py       # AES-256 + Diffie-Hellman simulation
│   ├── blockchain.py       # SHA-256 proof-of-work blockchain ← NEW
│   ├── router.py           # Adaptive protocol router
│   ├── queue_manager.py    # Priority message queue
│   ├── network_simulator.py # Network condition simulator
│   ├── gamification.py     # XP, levels, badges engine
│   ├── plugins/
│   │   ├── plugin_base.py  # Abstract plugin system
│   │   ├── ai_plugin.py    # AI analysis plugin
│   │   ├── encryption_plugin.py  # Encryption plugin
│   │   ├── blockchain_plugin.py  # Blockchain logging plugin ← NEW
│   │   └── analytics_plugin.py   # Analytics tracker plugin
│   └── distributed/
│       └── load_balancer.py # Multi-node cluster simulation
├── common/
│   └── config.py           # Centralized configuration
├── run_all.py              # One-command launcher
├── requirements.txt        # Python dependencies
└── README.md               # This file
```

---

## ⚙️ Setup & Run

### Prerequisites
- Python 3.10+

### Step 1: Install dependencies
```bash
pip install websockets
```

### Step 2: Start all servers
```bash
python run_all.py
```

This starts:
- **TCP Server** on port `9000` (reliable chat messages)
- **UDP Server** on port `9001` (typing indicators, presence)
- **WebSocket Bridge** on port `8765` (browser ↔ backend + WebRTC signaling)

### Step 3: Open the frontend
Open `frontend/index.html` in your browser. Multiple tabs = multiple users.

---

## 📞 How WebRTC Signaling Works

```
Browser A                    WS Server                    Browser B
   │                            │                            │
   │ 1. Create Offer (SDP)      │                            │
   │ ────────────────────────>  │                            │
   │                            │  2. Relay Offer             │
   │                            │ ────────────────────────>  │
   │                            │                            │
   │                            │  3. Create Answer (SDP)     │
   │                            │ <────────────────────────  │
   │  4. Relay Answer           │                            │
   │ <────────────────────────  │                            │
   │                            │                            │
   │ 5. ICE Candidates ⟷ ICE Candidates                      │
   │ ──────────────────────────────────────────────────────> │
   │                            │                            │
   ╔═══════════════════════════════════════════════════════╗ │
   ║  6. P2P DataChannel OPEN — Direct communication!     ║ │
   ╚═══════════════════════════════════════════════════════╝ │
   │ <═══════════════════════════════════════════════════>   │
   │       Messages flow PEER-TO-PEER (no server!)         │
```

**Key Points:**
- WebSocket is used ONLY for signaling (offer/answer/ICE exchange)
- Once the DataChannel is open, data flows directly between browsers
- Uses Google's public STUN servers for NAT traversal

---

## ⛓️ How Blockchain Validation Works

```
GENESIS BLOCK                    BLOCK #1                      BLOCK #2
┌─────────────┐  hash link  ┌─────────────┐  hash link  ┌─────────────┐
│ Index: 0    │────────────>│ Index: 1    │────────────>│ Index: 2    │
│ Prev: 000.. │             │ Prev: abc.. │             │ Prev: def.. │
│ Hash: abc.. │             │ Hash: def.. │             │ Hash: 789.. │
│ Nonce: 47   │             │ Nonce: 12   │             │ Nonce: 83   │
│ Data: start │             │ Data: msg   │             │ Data: msg   │
└─────────────┘             └─────────────┘             └─────────────┘
```

**Validation Process:**
1. For each block, recalculate its SHA-256 hash
2. Compare with stored hash → detects content tampering
3. Check `previous_hash` matches the previous block's hash → detects chain breaks
4. **Tamper Demo**: Modify a block's data without recalculating → validation catches it!

**Mining (Proof-of-Work):**
- Difficulty = 2 → hash must start with "00"
- Nonce is incremented until a valid hash is found
- This simulates real blockchain mining behavior

---

## 🎮 How to Use

### Chat
1. Enter a username and click **ESTABLISH CONNECTION**
2. Type messages and see routing decisions, encryption badges, blockchain hashes

### Study Mode
Type `/study <topic>` for CN tutoring:
- `/study tcp`, `/study udp`, `/study websocket`
- `/study osi`, `/study encryption`, `/study routing`

### WebRTC P2P (📞 Tab)
1. Open 2 browser tabs with different usernames
2. Go to the **📞 P2P** tab
3. Click **Connect P2P** next to a peer
4. Once the DataChannel opens, type in the P2P chat box
5. Messages flow directly browser-to-browser (no server relay!)

### Blockchain Explorer (⛓️ Tab)
1. Go to the **⛓️ BLOCKCHAIN** tab
2. See all message blocks with hashes and nonces
3. Click **✅ Validate Chain** to verify integrity
4. Click **⚠️ Tamper Demo** to modify a block and see detection

### Network Simulator (🧪 Tab)
- Select presets: Perfect, Good WiFi, 4G, Poor WiFi, Congested, Satellite, **Chaos Mode**
- Use custom sliders for packet loss, latency, jitter, congestion

### Dashboard (📊 Tab)
- **Doughnut chart**: TCP vs UDP vs Hybrid distribution
- **Line chart**: Message timeline with real-time updates
- Real-time stats for AI, encryption, queue, analytics

### Cluster (🌍 Tab)
- 3 server nodes with CPU/memory metrics
- Change LB algorithm, simulate failures

---

## 🏗️ Architecture

```
Browser (HTML/CSS/JS + Chart.js + WebRTC)
    ↕ WebSocket (:8765)
WS Bridge (Python asyncio — Master Controller)
    ├── → AI Pipeline (sentiment, toxicity, smart replies, tutor)
    ├── → Encryption Engine (AES-256, key exchange)
    ├── → Blockchain Ledger (SHA-256, proof-of-work)     ← NEW
    ├── → WebRTC Signaling Relay (offer/answer/ICE)      ← NEW
    ├── → Adaptive Router (TCP/UDP/Hybrid selection)
    ├── → Message Queue (priority heap, offline storage)
    ├── → Network Simulator (packet loss, delay, congestion)
    ├── → Gamification (XP, badges, leaderboard)
    ├── → Plugin Manager (AI, Encryption, Blockchain, Analytics)
    ├── → Load Balancer (3-node cluster simulation)
    ├── → TCP Server (:9000) — reliable messages
    └── → UDP Server (:9001) — typing/presence

Browser ←═══ WebRTC DataChannel ═══→ Browser (P2P, no server)
```

---

## 🧪 Testing

| Test | How |
|------|-----|
| Multi-user | Open 3+ browser tabs, login with different names |
| AI analysis | Send messages, watch smart reply suggestions |
| Toxicity | Send a flagged word — gets blocked |
| Study mode | Type `/study tcp` for educational content |
| WebRTC P2P | Connect P2P in 📞 tab, send messages directly |
| Blockchain | View chain in ⛓️ tab, run validation + tamper demo |
| Network sim | Enable "Chaos Mode" in 🧪 tab, watch packet drops |
| Cluster | Click "FAIL" on a node in 🌍 tab, watch failover |
| Gamification | Send messages to earn XP and unlock badges |
| Dashboard | View Chart.js graphs updating in real-time |

---

## 📝 License

Educational project — SmartChat X Ultra © 2024
