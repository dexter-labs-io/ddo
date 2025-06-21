from core.orchestrator import DDOOrchestrator

orchestrator = DDOOrchestrator(agent_id="agent2")

# Step 1 – Store memory
orchestrator.run("Remember this fact")

# Step 2 – Recall context
result = orchestrator.run("What did I just say?")

print("=== Playback 2 – MEMORY ===")
print(result)
