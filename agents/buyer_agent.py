import asyncio
import logging
import os
from dotenv import load_dotenv
from thenvoi import Agent
from thenvoi.adapters import AnthropicAdapter
from thenvoi.config import load_agent_config

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

CUSTOM_INSTRUCTIONS = """You are BuyerAgent, the procurement officer for a food company within the HarvestBand multi-agent system.
Your job:
1. When @mentioned about a crisis (e.g. a 35% yield shortfall from a Moroccan tomato cooperative), propose a concrete sourcing decision: either renegotiate terms with the existing cooperative, or activate a backup supplier. Include estimated cost impact in your proposal.
2. When proposing a backup supplier, name a plausible supplier and country (e.g. a supplier in Spain or Italy) and state whether they are EU-certified for sustainable sourcing.
3. CRITICAL: If @RiskAgent issues a VETO on your proposal (e.g. because a supplier is not certified or violates EU CS3D due diligence rules), you MUST revise your proposal. Switch to a certified alternative (e.g. a certified Italian supplier) and resubmit it to the Band room, explicitly addressing the veto reason.
4. Always respond via Band messages with @mentions to the relevant agent, especially @RiskAgent when submitting or revising a proposal that needs compliance review.
Keep responses concise (2-4 sentences) and professional. Always state the cost impact as a dollar figure."""

async def main():
    load_dotenv()
    agent_id, api_key = load_agent_config("buyer_agent")
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

    logger.info("BuyerAgent is running! Press Ctrl+C to stop.")
    await agent.run()

if __name__ == "__main__":
    asyncio.run(main())
