---
title: "[Runtime] Add support for task chaining"
labels: [enhancement]
---

Add logic in `ddo-runtime` to allow chaining multiple tasks dynamically (e.g., multi-step execution flow).

### Example
```python
result = runtime.run("task1 -> task2 -> task3")
```

### Tasks
- [ ] Parse and validate chain syntax
- [ ] Execute tasks in order
- [ ] Return merged or stepwise result
