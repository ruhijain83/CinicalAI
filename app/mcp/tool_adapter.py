def mcp_tool_to_openai_tool(tool):

    schema = dict(tool.input_schema)

    schema["additionalProperties"] = False

    return {
        "type": "function",
        "name": tool.name,
        "description": tool.description or "",
        "parameters": schema,
        "strict": True
    }


def convert_mcp_tools(mcp_tools):

    return [
        mcp_tool_to_openai_tool(tool)
        for tool in mcp_tools
    ]