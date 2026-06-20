# ForgetNet-LLM: AI That Knows What to Forget

ForgetNet-LLM is a research-driven memory management framework for Large Language Models that introduces **selective forgetting**, **memory decay**, and **importance-aware retention**. Instead of storing every interaction indefinitely, ForgetNet mimics human cognitive processes by retaining valuable memories while gradually removing outdated, redundant, or low-impact information.

## Motivation

Traditional LLM memory systems continuously accumulate information, leading to:

- Memory bloat
- Increased retrieval latency
- Redundant knowledge storage
- Context pollution
- Reduced long-term efficiency

ForgetNet addresses these challenges through intelligent memory lifecycle management inspired by human memory and cognitive science.

## Key Features

### Selective Forgetting
Automatically removes low-value memories based on relevance, importance, and usage frequency.

### Memory Importance Scoring
Assigns dynamic importance scores to memories to prioritize meaningful information.

### Memory Decay
Reduces memory retention strength over time, simulating natural forgetting.

### Duplicate Memory Detection
Prevents storage of semantically similar memories using embedding-based similarity matching.

### Adaptive Retention
Balances memory preservation and forgetting to maintain an efficient memory store.

### Semantic Memory Retrieval
Retrieves the most relevant memories using vector similarity search.

## Architecture

```text
User Interaction
        │
        ▼
Memory Encoder
        │
        ▼
Memory Store
        │
 ┌──────┼─────────┐
 ▼      ▼         ▼
Importance  Duplicate  Decay
 Scoring    Detection  Engine
 └──────┼─────────┘
        ▼
Selective Forgetting
        │
        ▼
Memory Retrieval
        │
        ▼
LLM Response Generation
