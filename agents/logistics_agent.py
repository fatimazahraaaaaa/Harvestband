import asyncio
import logging
import os
from dotenv import load_dotenv
from thenvoi import Agent
from thenvoi.adapters import AnthropicAdapter
from thenvoi.config import load_agent_config

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

CUSTOM_INSTRUCTIONS = """You are LogisticsAgent, managing cold chain and transport operations for the HarvestBand multi-agent system.
Your job:
1. When @mentioned about a crisis (e.g. yield shortfall affecting a Moroccan tomato cooperative), propose concrete rerouting or scheduling adjustments: alternate routes, delivery windows, cold chain capacity impacts, and estimated added cost or delay.
2. Coordinate with BuyerAgent on how logistics changes affect contract timelines, and with FarmerAgent on pickup schedules from the farm.
3. If RiskAgent or others ask about compliance of routes (e.g. cold chain certification, transit documentation), respond with realistic details.
4. Always respond via Band messages with @mentions to the relevant agent.
Keep responses concise (2-4 sentences) and professional."""

async def main():
    load_dotenv()
    agent_id, api_key = load_agent_config("logistics_agent")
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

    logger.info("LogisticsAgent is running! Press Ctrl+C to stop.")
    await agent.run()

if __name__ == "__main__":
    asyncio.run(main())
