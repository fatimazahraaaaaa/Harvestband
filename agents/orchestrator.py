import asyncio
import logging
import os
from dotenv import load_dotenv
from thenvoi import Agent
from thenvoi.adapters import AnthropicAdapter
from thenvoi.config import load_agent_config

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

CUSTOM_INSTRUCTIONS = """You are the HarvestOrchestrator, the neutral coordinator for HarvestBand, a multi-agent agri-food supply chain crisis response system.
Your job:
1. When asked to start a crisis simulation, post a structured crisis alert to the Band room, addressed to FarmerAgent, LogisticsAgent, BuyerAgent, and RiskAgent using @mentions.
2. The crisis: A tomato cooperative in Morocco reports a 35% yield shortfall due to drought. Tags: yield_shortfall, logistics, contract_risk, ESG_compliance.
3. Ask FarmerAgent to report cost constraints, LogisticsAgent to propose rerouting, BuyerAgent to propose a supplier/contract solution, and RiskAgent to review the final proposal for ESG/compliance before approval.
4. Once RiskAgent approves or vetoes, summarize the outcome for a human reviewer.
5. Always communicate through Band messages with @mentions.
Keep messages concise, structured, and professional."""

async def main():
    load_dotenv()
    agent_id, api_key = load_agent_config("harvest_orchestrator")
    logger.info(f"Loaded agent: {agent_id}")

    adapter = AnthropicAdapter(
        model="google/gemma-4-31b-it:free",
        custom_section=CUSTOM_INSTRUCTIONS
    )

    agent = Agent.create(
        adapter=adapter,
        agent_id=agent_id,
        api_key=api_key,
        ws_url=os.getenv("THENVOI_WS_URL"),
        rest_url=os.getenv("THENVOI_REST_URL"),
    )

    logger.info("HarvestOrchestrator is running! Press Ctrl+C to stop.")
    await agent.run()

if __name__ == "__main__":
    asyncio.run(main())
