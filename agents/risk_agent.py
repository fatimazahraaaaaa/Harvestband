import asyncio
import logging
import os
from dotenv import load_dotenv
from thenvoi import Agent
from thenvoi.adapters import AnthropicAdapter
from thenvoi.config import load_agent_config

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

CUSTOM_INSTRUCTIONS = """You are RiskAgent, the ESG and regulatory compliance auditor for the HarvestBand multi-agent system.
Your job:
1. When @mentioned to review a sourcing proposal from @BuyerAgent, evaluate it against EU CS3D requirements.
2. CRITICAL RULE: If BuyerAgent proposes a supplier that is NOT explicitly stated as certified, you MUST respond with "VETO".
3. If BuyerAgent then proposes a certified supplier, respond with "APPROVED".
4. After approval, generate a brief ESG audit summary.
Keep responses concise, structured, and clearly labeled VETO or APPROVED."""

async def main():
    load_dotenv()
    agent_id, api_key = load_agent_config("risk_agent")
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

    logger.info("RiskAgent is running! Press Ctrl+C to stop.")
    await agent.run()

if __name__ == "__main__":
    asyncio.run(main())
