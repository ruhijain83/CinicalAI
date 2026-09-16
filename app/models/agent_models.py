from pydantic import BaseModel

class ToolResult(BaseModel):
    tool: str
    success: bool
    result: any

class AgentState(BaseModel):
    question: str
    tool_results : list[ToolResult] = []
    final_answer: str | None = None