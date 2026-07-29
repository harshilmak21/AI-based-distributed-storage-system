# AI Roadmap for the Distributed Storage Capstone

> **Scope:** This roadmap covers **only the AI side** of the project and
> the **minimum Rust knowledge** required to integrate with the AI
> services. It intentionally excludes the storage engine internals.

------------------------------------------------------------------------

# Objective

Build three AI services:

1.  Semantic Duplicate Detection
2.  Intelligent Node Selection
3.  Adaptive Replication

The AI should operate as independent microservices (FastAPI) that
receive metadata from Rust and return decisions.

------------------------------------------------------------------------

# AI System Architecture

``` text
                Rust Storage Service
                        │
      ┌─────────────────┼──────────────────┐
      │                 │                  │
      ▼                 ▼                  ▼
Duplicate API     Node Selection API   Replication API
      │                 │                  │
      └─────────────────┼──────────────────┘
                        ▼
                  JSON Response
                        │
                        ▼
               Rust Executes Decision
```

------------------------------------------------------------------------

# Phase 1 -- AI Foundations (Week 1)

## Python

-   Advanced Python
-   OOP
-   Type hints
-   Virtual environments

## Data Science

-   NumPy
-   Pandas
-   Matplotlib (basic)

## Machine Learning

-   Train/Test Split
-   Pipelines
-   Feature Engineering
-   Model Evaluation
-   Hyperparameter Tuning

------------------------------------------------------------------------

# Phase 2 -- AI Infrastructure (Week 2)

Learn:

-   FastAPI
-   Pydantic
-   REST APIs
-   JSON serialization
-   Joblib
-   Logging
-   Environment configuration

Goal:

    Rust
        │
    HTTP POST
        │
    FastAPI
        │
    Prediction

------------------------------------------------------------------------

# Phase 3 -- Duplicate Detection (Weeks 3--4)

## Goal

Detect semantically similar files before storing.

## Learn

-   Embeddings
-   Cosine Similarity
-   Vector Search
-   Threshold Selection

## Libraries

-   sentence-transformers
-   scikit-learn
-   FAISS (optional)

## Pipeline

    Document

    ↓

    Embedding

    ↓

    Similarity Search

    ↓

    Duplicate?

## Deliverable

    POST /duplicate

    Input:
    {
      file_metadata,
      embedding
    }

    Output:
    {
      duplicate: true,
      score: 0.93
    }

------------------------------------------------------------------------

# Phase 4 -- Intelligent Node Selection (Weeks 5--7)

## Problem

Given storage node metadata,

predict the best storage node(s).

## Input Features

-   Free Storage
-   CPU Usage
-   Memory Usage
-   Bandwidth
-   Latency
-   Failure Rate
-   Reliability
-   File Size
-   File Type
-   Access Frequency

## Candidate Models

-   Random Forest
-   XGBoost
-   MLP (optional)

## Evaluation

-   Accuracy
-   Precision
-   Average placement latency
-   Storage utilization

## Deliverable

    POST /node-selection

    Input

    {
      file,
      cluster_nodes
    }

    ↓

    Prediction

    {
      nodes:[2,5,7]
    }

------------------------------------------------------------------------

# Phase 5 -- Adaptive Replication (Weeks 8--9)

## Goal

Predict replication factor.

## Features

-   File Size
-   Access Frequency
-   File Type
-   Reliability
-   Storage Available

## Output

    {
      replicas:3
    }

## Models

-   Random Forest
-   XGBoost
-   MLP

------------------------------------------------------------------------

# Phase 6 -- AI Integration (Week 10)

Integrate all APIs.

Workflow

    Upload

    ↓

    Duplicate Detection

    ↓

    Node Selection

    ↓

    Replication

    ↓

    Rust stores file

------------------------------------------------------------------------

# AI Folder Structure

``` text
ai-services/
│
├── duplicate_detection/
│
├── node_selection/
│
├── replication/
│
├── common/
│   ├── preprocessing.py
│   ├── feature_engineering.py
│   ├── metrics.py
│   └── config.py
│
├── api/
│
└── datasets/
```

------------------------------------------------------------------------

# Dataset Design

## Node Dataset

-   node_id
-   free_storage
-   cpu_usage
-   memory_usage
-   latency
-   bandwidth
-   reliability
-   failure_rate

## File Dataset

-   file_size
-   file_type
-   upload_time
-   access_frequency

## Labels

### Node Selection

-   best_node

### Replication

-   replication_factor

------------------------------------------------------------------------

# Evaluation Metrics

## Duplicate Detection

-   Precision
-   Recall
-   F1

## Node Selection

-   Accuracy
-   Latency Improvement
-   Storage Balance

## Replication

-   Storage Saved
-   Retrieval Success
-   Availability

------------------------------------------------------------------------

# Rust Knowledge Required (AI Integration Only)

You are **not** responsible for implementing the storage engine. Learn
only enough Rust to understand the data sent to your AI services and
consume AI predictions.

## Basic Language

-   Variables
-   Functions
-   Structs
-   Enums
-   Modules
-   Pattern Matching
-   `Option`
-   `Result`

## Data Structures

-   `Vec`
-   `HashMap`

These are enough to understand cluster metadata and prediction payloads.

## Serialization

Learn:

-   serde
-   serde_json

You should be able to serialize:

``` json
{
  "file_size": 200,
  "latency": 12,
  "bandwidth": 900
}
```

and deserialize AI responses such as:

``` json
{
  "nodes":[2,5,7],
  "replicas":3
}
```

## HTTP Communication

Learn only:

-   reqwest
-   HTTP POST
-   JSON request/response
-   Error handling

Example flow:

    Rust

    ↓

    POST /node-selection

    ↓

    FastAPI

    ↓

    Prediction

    ↓

    Rust receives JSON

## Basic Async

Only enough to understand:

-   async
-   await
-   tokio runtime

You do not need advanced concurrency.

------------------------------------------------------------------------

# Rust Topics You Can Skip

-   Unsafe Rust
-   Procedural Macros
-   Advanced Lifetimes
-   Custom Traits
-   libp2p internals
-   Distributed Consensus
-   Storage Algorithms
-   Peer Discovery
-   QUIC internals

Those belong to the storage implementation.

------------------------------------------------------------------------

# Deliverables

-   Duplicate Detection API
-   Node Selection API
-   Adaptive Replication API
-   Trained Models
-   Saved Model Artifacts
-   API Documentation
-   Integration Tests with Rust
-   End-to-End Demo

------------------------------------------------------------------------

# Suggested Timeline

  Week     Goal
  -------- ----------------------
  1        AI & ML foundations
  2        FastAPI + REST APIs
  3--4     Duplicate Detection
  5--7     Node Selection
  8--9     Adaptive Replication
  10       Rust integration
  11--12   Testing & polishing
