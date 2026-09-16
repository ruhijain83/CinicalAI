from app.agents.runner import run_agent


question = "Find the patient's latest MRI report."

result = run_agent(question)

print("\n==============================")
print("FINAL RESPONSE")
print("==============================")
print(result.response)

print("\n==============================")
print("TOOLS CALLED")
print("==============================")

for tool in result.tool_calls:
    print(f"Tool: {tool.name}")
    print(f"Arguments: {tool.arguments}")

    if tool.error:
        print(f"Error: {tool.error}")

print("\n==============================")
print(f"LATENCY: {result.latency_ms:.2f} ms")
print("==============================")

if result.error:
    print(f"\nAGENT ERROR: {result.error}")