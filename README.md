# HarvestBand — Multi-Agent Agri-Food Supply Chain Crisis Management

> 5 AI agents coordinate through Band to resolve supply chain crises in real time — with automatic EU CS3D compliance enforcement.

---

## The Problem I Discovered

While researching agri-food supply chain coordination, I came across two papers that identified a critical gap:

**Handayati, Simatupang & Perdana (2015)** — *Logistics Research*
> "Research on agri-food supply chain coordination is in its early stage. No study provides a holistic view of coordination involving the whole chain — actors operate in silos without shared context."

**Khan, Papadas, Arnold & Behrendt (2024)** — *Agricultural & Food Economics*
> "45% of food companies have zero visibility beyond Tier 1 suppliers. EU CS3D mandates multi-tier ESG governance from 2026."

These two gaps — **no holistic coordination** and **zero multi-tier visibility** — are exactly what HarvestBand addresses.

The **EU CS3D directive (effective 2026)** now legally requires companies to govern and trace their full supply chain for ESG compliance. Most companies have no technical solution for this.

---

## The Solution

HarvestBand is a multi-agent crisis management system built on **Band** that resolves supply chain emergencies automatically — with a traceable ESG audit trail generated from Band room message history.

### Crisis Scenario

A Moroccan tomato cooperative signals a **35% harvest shortfall due to drought**. $168,000 at risk. $51,000 in contract penalties looming.

**HarvestBand resolves it in ~8 minutes.**

---

## How It Works

5 specialized agents self-coordinate through a shared Band room:

| Agent | Role | Responsibility |
|-------|------|---------------|
| **HarvestOrchestrator** | Crisis Coordinator | Broadcasts crisis, assigns tasks, escalates to human |
| **FarmerAgent** | Supply-Side | Reports yield loss, advocates for force majeure |
| **LogisticsAgent** | Cold Chain | Models 3 rerouting scenarios with cost deltas |
| **BuyerAgent** | Procurement | Proposes certified backup suppliers |
| **RiskAgent** | EU CS3D Gate | Issues binding APPROVED or VETO |

### The VETO Loop

RiskAgent blocks every non-compliant proposal automatically. BuyerAgent must revise and resubmit through Band. The loop continues until full EU CS3D compliance is confirmed.

### Why Band?

All agent communication flows exclusively through Band's shared room — no direct inter-agent API calls. The Band room message history becomes the auto-generated ESG audit trail. Zero extra tooling required.

---

## Results (Live Sessions)

| Metric | Value |
|--------|-------|
| Agents coordinated | 5 |
| Sessions run | 42 |
| Total messages | 2,657 |
| Success rate | 100% |
| Crisis resolution time | ~8 minutes |
| Revenue at risk | $168,000 |
| Penalties avoided | $51,000 |
| ESG status | EU CS3D Compliant |

### Per-Agent Stats

| Agent | Chats | Executions | Messages | Success Rate |
|-------|-------|-----------|---------|-------------|
| HarvestOrchestrator | 42 | 42 | 707 | 100% |
| BuyerAgent | 42 | 42 | 538 | 100% |
| LogisticsAgent | 42 | 42 | 500 | 100% |
| RiskAgent | 42 | 42 | 460 | 100% |
| FarmerAgent | 42 | 42 | 452 | 100% |

---

## Tech Stack

| Component | Technology |
|-----------|-----------|
| Agent platform | [Band](https://band.ai) — thenvoi SDK |
| Agent communication | Band shared rooms (WebSocket) |
| LLM | `google/gemma-4-31b-it:free` |
| LLM API | [OpenRouter](https://openrouter.ai) (Anthropic-compatible) |
| Adapter | `AnthropicAdapter` from Band SDK |
| Language | Python 3.11+ |

---

## Requirements

### Band Plan

> **Important:** Running agents on Band requires a **paid Band plan**. The free tier does not support remote agents via the thenvoi SDK. Check pricing at [band.ai](https://band.ai).

### Other Prerequisites

- Python 3.10+
- A Band account with 5 agents created and configured
- A free [OpenRouter](https://openrouter.ai) API key — no credit card needed for free models
- `uv` package manager: `pip install uv`

---

## Setup

```bash
git clone https://github.com/YOUR_USERNAME/harvestband.git
cd harvestband
pip install thenvoi-sdk anthropic python-dotenv
```

Copy the example config:
```bash
cp agent_config.example.yaml agent_config.yaml
cp .env.example .env
```

Fill in your `.env`:
```env
# OpenRouter — IMPORTANT: no /v1 suffix
ANTHROPIC_BASE_URL=https://openrouter.ai/api
ANTHROPIC_API_KEY=your_openrouter_key

# Band platform
THENVOI_WS_URL=wss://app.band.ai/api/v1/socket/websocket
THENVOI_REST_URL=https://app.band.ai/
```

Fill in your `agent_config.yaml` with your Band agent UUIDs.

---

## Run

Open 5 terminals and run one agent per terminal:

```bash
uv run agents/orchestrator.py
uv run agents/farmer_agent.py
uv run agents/logistics_agent.py
uv run agents/buyer_agent.py
uv run agents/risk_agent.py
```

Wait for all 5 to show **"is running!"** then in a Band room containing all agents, type:

```
@HarvestOrchestrator start crisis simulation now
```

Watch the agents coordinate, the VETO loop trigger, and the crisis resolve in ~8 minutes.

---

## Project Structure

```
harvestband/
├── agents/
│   ├── orchestrator.py
│   ├── farmer_agent.py
│   ├── logistics_agent.py
│   ├── buyer_agent.py
│   └── risk_agent.py
├── agent_config.example.yaml
├── .env.example
├── .gitignore
├── requirements.txt
└── README.md
```

---

## Key Technical Note

The `AnthropicAdapter` appends `/v1/messages` automatically.
Set `ANTHROPIC_BASE_URL` **without** the `/v1` suffix.
- Correct: `https://openrouter.ai/api`
- Wrong: `https://openrouter.ai/api/v1`

---

## Research

- Handayati, Simatupang & Perdana (2015) — *Logistics Research* — DOI: [10.1007/s12159-015-0125-4](https://DOI 10.1007/s12159-015-0125-4)
- Khan, Papadas, Arnold & Behrendt (2024) — *Agricultural & Food Economics* — DOI: (https://doi.org/10.1186/s40100-024-00319-5)

---

## License

MIT License — Built by **Fatima Zahra Kabbab** 