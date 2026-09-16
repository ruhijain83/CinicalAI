import json

from app.clients.openai_client import client
from app.config import AI_MODEL

from app.agents.tool_definitions import TOOLS
from app.agents.tool_registry import TOOL_REGISTRY
from dataclasses import dataclass, field
from typing import Any
import time


@dataclass
class ToolCallRecord:
    name: str
    arguments: dict[str, Any]
    result: Any = None
    error: str | None = None


@dataclass
class AgentResult:
    response: str
    tool_calls: list[ToolCallRecord] = field(default_factory=list)
    latency_ms: float = 0.0
    error: str | None = None


def run_agent(question: str) -> AgentResult:
    start_time = time.perf_counter()

    tool_calls = []
    response = client.responses.create(
        model=AI_MODEL,
        input=question,
        tools=TOOLS
    )

    while True:

        tool_called = False

        for item in response.output:

            if item.type != "function_call":
                continue

            tool_called = True

            tool_name = item.name
            arguments = json.loads(item.arguments)

            print("Tool requested:", tool_name)
            print("Arguments:", arguments)

            tool_function = TOOL_REGISTRY[tool_name]

            result = tool_function(**arguments)

            print("Tool result:", result)
            print("------------")

            # Send the tool result back to the model
            response = client.responses.create(
                model=AI_MODEL,
                previous_response_id=response.id,
                input=[
                    {
                        "type": "function_call_output",
                        "call_id": item.call_id,
                        "output": json.dumps(result)
                    }
                ],
                tools=TOOLS
            )

            break
        if not tool_called:

            latency_ms = (
                time.perf_counter() - start_time
            ) * 1000

            return AgentResult(
                response=response.output_text,
                tool_calls=tool_calls,
                latency_ms=latency_ms
            )