import asyncio

from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

from app.agents.mcp_runner import run_mcp_agent


server_params = StdioServerParameters(
    command="python",
    args=["-m", "app.mcp.clinical_server"],
)


async def main():

    async with stdio_client(server_params) as (read, write):

        async with ClientSession(read, write) as session:

            await session.initialize()

            response = await run_mcp_agent(
                """
                Review patient 12345.
                What is the patient's diagnosis and are the available vital signs
                relevant to that condition?
                """,
                session
            )

            print("\nFINAL ANSWER:")
            print(response)


if __name__ == "__main__":
    asyncio.run(main())