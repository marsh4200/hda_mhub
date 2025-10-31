# 🖥️ HDAnywhere MHUB (Local) — Home Assistant Integration

[![Add to HACS](https://my.home-assistant.io/badges/hacs_repository.svg)](https://my.home-assistant.io/redirect/hacs_repository/?owner=marsh4200&repository=hda_mhub&category=integration)
<a href="https://my.home-assistant.io/redirect/config_flow_start/?domain=hda_mhub" target="_blank">
</a>

---

### Version: `1.1.4`
**Author:** [@marsh4200](https://github.com/marsh4200)

A lightweight, plug-and-play [Home Assistant](https://www.home-assistant.io/) custom integration for controlling your **HDAnywhere MHUB matrix system** over the local LAN API.

Easily power your matrix **ON/OFF**, switch HDMI **inputs to outputs**, and monitor state — all directly from your Home Assistant dashboard, with **no cloud dependency**.

---

## ✨ Features

✅ **Power Control** — Turn the MHUB ON/OFF using a dedicated switch  
🎛️ **Video Routing Buttons** — 16 one-touch buttons representing every input/output combination (Input 1–4 → Output A–D)  
🧠 **Status Polling** — Automatically retrieves power and routing states via:  
- `/api/data/0/`  
- `/api/data/200/`  

🔒 **All communication is local** — no internet access required for control or feedback.

---

## 🧩 Installation

### 🔹 Option 1 — Install via HACS (Custom Repository)

1. In Home Assistant, open **HACS → Integrations**  
2. Click the ⋮ (**three dots**) → **Custom repositories**  
3. Add this repository URL:

