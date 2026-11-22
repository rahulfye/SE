# Lab 4: Brick Breaker Game (AI Vibe Coding)

**Course:** Software Engineering (SE)  
**Topic:** AI-Assisted Iterative Development (Vibe Coding with LLMs)  

---

## 1. Overview

This directory contains the completed assignment for the Pygame Brick Breaker project. The application was developed and refined iteratively using Large Language Model (LLM) guidance to implement enhanced game physics, win/loss states, dynamic difficulty selection, and procedural audio synthesis.

---

## 2. Deliverables & Artifacts

- [Chat_History.pdf](Chat_History.pdf) — Complete exported transcript of the iterative AI prompting session.
- [Videos/before.mov](Videos/before.mov) — Video recording demonstrating baseline gameplay before modifications (~10s).
- [Videos/after.mov](Videos/after.mov) — Video recording demonstrating completed features and gameplay after modifications (~10s).
- [main.py](main.py) — Application entrypoint.
- [game/](game/) — Core game engine, entities, difficulty management, and sound generation modules.

---

## 3. Quick Start & Execution

### Prerequisites
- Python 3.10+
- `pygame`

### Installation & Run
```bash
pip install -r requirements.txt
python main.py
```

---

## 4. Controls

- `Left Arrow` / `A` — Move paddle left
- `Right Arrow` / `D` — Move paddle right
- `Q` / `Esc` — Exit game
- **Post-Game Menu:**
  - `1` — Easy Mode
  - `2` — Medium Mode
  - `3` — Hard Mode
  - `Q` / `Esc` — Exit

---

## 5. Implemented Features

1. **Refined Multi-Directional Collision Detection:**
   - Evaluates previous and current ball bounding boxes to accurately discern edge collisions.
   - Horizontal collisions deflect along `vx`; vertical collisions deflect along `vy`.
   - Dynamic reflection angles based on the point of impact on the paddle.

2. **Interactive Win & Game-Over HUD:**
   - Displays clear win / game over notifications and cumulative score on-screen.
   - Non-blocking keyboard state listeners for seamless replay.

3. **Replay & Configurable Difficulty:**
   - Select between Easy, Medium, and Hard tiers upon game conclusion.
   - Scales ball velocity, paddle width, and traversal speed dynamically.

4. **Procedural Audio Synthesis:**
   - Fully programmatic audio wave generation using Pygame's sound buffer.
   - Zero external audio asset dependencies.
   - Distinct audio effects for boundary bounces, paddle deflection, brick destructions, and victory/defeat events.
