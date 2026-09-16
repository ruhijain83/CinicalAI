import json

from app.clients.openai_client import client
from app.config import AI_MODEL

from app.mcp.mcp_client import (
    get_mcp_tools,
    call_mcp_tool
)

from app.mcp.tool_adapter import (
    convert_mcp_tools
)


async def run_mcp_agent(question: str, session):

    # 1. Discover MCP tools
    mcp_tools = await get_mcp_tools(session)

    # 2. Convert MCP tools to OpenAI format
    tools = convert_mcp_tools(mcp_tools)

    print("\nAvailable agent tools:")

    for tool in tools:
        print(f"- {tool['name']}")

    # 3. Initial user input
    input_items = [
        {
            "role": "user",
            "content": question
        }
    ]

    # 4. Agent loop
    while True:

        response = client.responses.create(
            model=AI_MODEL,
            input=input_items,
            tools=tools
        )

        tool_calls = [
            item
            for item in response.output
            if item.type == "function_call"
        ]

        # No tool requested → final answer
        if not tool_calls:

            return response.output_text

        # Preserve model output
        input_items.extend(response.output)

        # Execute requested tools
        for tool_call in tool_calls:

            tool_name = tool_call.name

            arguments = json.loads(
                tool_call.arguments
            )

            print(
                f"\nTool requested: {tool_name}"
            )

            print(
                f"Arguments: {arguments}"
            )

            # Execute through MCP
            result = await call_mcp_tool(
                session,
                tool_name,
                arguments
            )

            print("\nMCP Tool result:")
            print(result)

            # Give result back to model
            input_items.append(
                {
                    "type": "function_call_output",
                    "call_id": tool_call.call_id,
                    "output": str(result)
                }
            )