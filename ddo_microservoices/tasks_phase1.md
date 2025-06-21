# Phase 1 – DDO Core Runtime & Orchestration Tasks

## Overview

This document outlines all tasks required to implement, test, and document the Phase 1 core runtime for the DDO platform. The goal is to establish a functioning THINK → PLAN → ACT → REFLECT loop using in-memory components and a single-agent interface.

---

## 2. Core Logic – Orchestration Pipeline

### 2.1. Implement `core/orchestrator.py`
- Create `DDOOrchestrator` class
- Define `run(prompt: str)` method
- Wire in planner, memory manager, and executor
- Handle input/output data structures

**Deliverable:** Working orchestrator object coordinating subcomponents

---

### 2.2. Implement `core/planner.py`
- Create `Planner` class
- Define `generate_plan(prompt, context)` method
- Hardcode simple linear plan (1–3 steps) using "echo" tool

**Deliverable:** Basic plan generator for mock tools

---

### 2.3. Implement `core/executor.py`
- Create `Executor` class
- Define `execute_plan(plan)` method
- Stub out echo tool handler
- Handle unknown tool fallback gracefully

**Deliverable:** Executor capable of multi-step execution and fallback handling

---

### 2.4. Implement `core/memory_manager.py`
- Create `MemoryManager` class
- Define `store_context(agent_id, prompt, result)`
- Define `retrieve_context(agent_id)`
- Use a Python dictionary for in-memory storage

**Deliverable:** Agent-scoped memory context management

---

## 3. Testing and Demonstration

### 3.1. Create `scripts/run_demo.py`
- Instantiate a `DDOOrchestrator`
- Send a prompt and print the response
- Validate THINK → PLAN → ACT → REFLECT loop

**Deliverable:** Manual test script

---

### 3.2. Add Functional Use Case Tests

Each test demonstrates a key sequence behavior:

#### Test 1: THINK → PLAN → ACT orchestration
- Prompt: `"What is the capital of France?"`
- Use Case: Verifies full orchestration cycle
- Actors: User, Orchestrator, Planner, Executor, MemoryManager

#### Test 2: In-memory agent memory management
- Prompt: `"Remind me to take vitamins"`
- Use Case: Ensures memory persistence
- Actors: User, Orchestrator, MemoryManager

#### Test 3: Planner returns multiple tool steps
- Prompt: `"Generate title, then write a paragraph"`
- Use Case: Tests planner sequencing and executor flow
- Actors: User, Orchestrator, Planner, Executor

#### Test 4: Tool execution with fallback handling
- Prompt: `"Use unknown_tool to analyze data"`
- Use Case: Tests error handling and system resilience
- Actors: User, Orchestrator, Executor

#### Test 5: Agent-specific orchestration and memory
- Prompts: `"Agent A: What's my name?"`, `"Agent B: What's my name?"`
- Use Case: Verifies per-agent memory isolation
- Actors: User A, User B, Orchestrator, MemoryManager

#### Test 6: Reflection loop (replan based on result)
- Prompt: `"Search news, then summarize"`
- Use Case: Triggers follow-up plan based on intermediate result
- Actors: User, Orchestrator, Planner, Executor, MemoryManager

**Deliverable:** Full set of unit + functional sequence tests  
**Location:** `scripts/` or `tests/`

---

## 4. Configuration and Dev Tools

### 4.1. Create `.env` and `config/settings.py`
- Define runtime variables (e.g., `DEFAULT_AGENT_ID`)
- Use `python-dotenv` or `os.environ`

**Deliverable:** Configurable local environment

---

## 5. Documentation

### 5.1. Update `README.md`
- Describe architecture and component roles
- Explain how to run the demo script
- Include a THINK → PLAN → ACT diagram

### 5.2. Write `docs/phase1_notes.md`
- Document internal structure and logic
- List interfaces and data flow
- Summarize test coverage and core capabilities

**Deliverable:** Developer-facing documentation

---

## Optional (Stretch Goals)

- Replace print() with logging
- Add CLI via `argparse`
- Add tracing/timing to orchestrator phases
- Add unit test scaffolding with mock tools

---

## Summary Table

| Task ID | Name                             | Folder           | Priority |
|---------|----------------------------------|------------------|----------|
| 1.1     | Create base project structure    | root             | High     |
| 2.1     | Build Orchestrator               | core/            | High     |
| 2.2     | Build Planner                    | core/            | High     |
| 2.3     | Build Executor                   | core/            | High     |
| 2.4     | Build MemoryManager              | core/            | High     |
| 3.1     | Demo script                      | scripts/         | High     |
| 3.2     | Write functional use case tests  | scripts/, tests/ | High     |
| 4.1     | Environment + config setup       | config/          | Medium   |
| 5.1     | Write README                     | root             | Medium   |
| 5.2     | Write developer docs             | docs/            | Medium   |

---
