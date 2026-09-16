from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client


server_params = StdioServerParameters(
    command="python",
    args=["-m", "app.mcp.clinical_server"],
)


async def get_mcp_tools(session):

    result = await session.list_tools()

    return result.tools


async def call_mcp_tool(
    session,
    tool_name: str,
    arguments: dict
):

    result = await session.call_tool(
        tool_name,
        arguments=arguments
    )

    return result