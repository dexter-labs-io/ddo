# scripts/run_playback.py

import argparse
from core.orchestrator import DDOOrchestrator

def run_playback(scenario):
    if scenario == 1:
        orchestrator = DDOOrchestrator(agent_id="agent1")
        result = orchestrator.run("Say hello world")
        print("=== Playback 1 – THINK → PLAN → ACT ===")

    elif scenario == 2:
        orchestrator = DDOOrchestrator(agent_id="agent2")
        orchestrator.run("Remember this fact")
        result = orchestrator.run("What did I just say?")
        print("=== Playback 2 – MEMORY ===")

    elif scenario == 3:
        orchestrator = DDOOrchestrator(agent_id="agent3")
        result = orchestrator.run("search something and then echo it")
        print("=== Playback 3 – MULTI-STEP PLAN ===")

    elif scenario == 4:
        orchestrator = DDOOrchestrator(agent_id="agent4")
        result = orchestrator.run("Translate this to Italian")  # Fallback
        print("=== Playback 4 – FALLBACK TOOL ===")

    elif scenario == 5:
        agent_a = DDOOrchestrator(agent_id="agentA")
        agent_b = DDOOrchestrator(agent_id="agentB")
        agent_a.run("Agent A stores this")
        result = agent_b.run("Agent B input")
        print("=== Playback 5 – MULTI-AGENT MEMORY ISOLATION ===")

    elif scenario == 6:
        orchestrator = DDOOrchestrator(agent_id="agent6")
        result = orchestrator.run("Try and retry if the step fails")
        print("=== Playback 6 – REFLECTION LOOP ===")

    else:
        print("Unknown scenario. Use 1–6.")
        return

    print(result)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run DDO playback scenarios (1–6)")
    parser.add_argument('--scenario', type=int, required=True, help="Scenario number")
    args = parser.parse_args()

    run_playback(args.scenario)



    # python scripts/run_playback.py --scenario 1 or 2 - 6

