from fastapi import APIRouter, Query

from agnet_api.service.agent_service_impl import AgentServiceImpl

agentRouter = APIRouter()
agent_service = AgentServiceImpl()

# 의존성 주입
async def injectAgentService() -> AgentServiceImpl:
    return AgentServiceImpl()

@agentRouter.get("/ask")
async def ask_agent(companyName: str = Query(...), situation: str = Query(...), questions: str = Query(...)):
    # 그러니까 companyName, questions, situation(metadata 인가봐, RAG에서 사용함) 를 받아야 한다는 거잖아.
    result = await agent_service.run_agent(companyName, situation, questions)
    return {"result": result}
