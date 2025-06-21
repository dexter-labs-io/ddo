from core.orchestrator import DDOOrchestrator

orchestrator = DDOOrchestrator(agent_id="agent4")
prompt = "Translate this to Italian"  # 'translate' tool not implemented

result = orchestrator.run(prompt)

print("=== Playback 4 – FALLBACK TOOL ===")
print(result)
