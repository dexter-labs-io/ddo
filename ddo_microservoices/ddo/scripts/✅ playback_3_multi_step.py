from core.orchestrator import DDOOrchestrator

orchestrator = DDOOrchestrator(agent_id="agent3")
prompt = "search something and then echo it"
result = orchestrator.run(prompt)

print("=== Playback 3 – MULTI-STEP PLAN ===")
print(result)
