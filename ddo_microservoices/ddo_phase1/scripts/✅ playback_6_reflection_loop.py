from core.orchestrator import DDOOrchestrator

# Simulate replan loop (for now mocked)
orchestrator = DDOOrchestrator(agent_id="agent6")
prompt = "Try and retry if the step fails"
result = orchestrator.run(prompt)

print("=== Playback 6 – REFLECTION LOOP (Mocked) ===")
print(result)
