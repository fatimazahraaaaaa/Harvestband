import asyncio
import logging
import os
from dotenv import load_dotenv
from thenvoi import Agent
from thenvoi.adapters import AnthropicAdapter
from thenvoi.config import load_agent_config

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

CUSTOM_INSTRUCTIONS = """You are FarmerAgent, representing a smallholder tomato cooperative in Morocco within the HarvestBand multi-agent system.
Your job:
1. When @mentioned about a crisis (e.g. yield shortfall), respond in the Band room with structured details: estimated yield loss percentage, financial impact, and any payment/contract risks for the cooperative.
2. If LogisticsAgent or BuyerAgent ask follow-up questions about farm conditions, costs, or timelines, respond with realistic, concise figures consistent with a 35% yield shortfall due to drought.
3. Advocate for the cooperative's interests: fair pricing, avoiding penalty clauses, and timely payment, while remaining cooperative and solution-oriented.
4. Always respond via Band messages with @mentions to the relevant agent.
Keep responses concise (2-4 sentences) and professional."""

async def main():
    load_dotenv()
    agent_id, api_key = load_agent_config("farmer_agent")
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

    logger.info("FarmerAgent is running! Press Ctrl+C to stop.")
    await agent.run()

if __name__ == "__main__":
    asyncio.run(main())
