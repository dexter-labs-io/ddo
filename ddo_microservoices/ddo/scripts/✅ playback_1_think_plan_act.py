from core.orchestrator import DDOOrchestrator

orchestrator = DDOOrchestrator(agent_id="agent1")
prompt = "Say hello world"
result = orchestrator.run(prompt)

print("=== Playback 1 – THINK → PLAN → ACT ===")
print(result)
