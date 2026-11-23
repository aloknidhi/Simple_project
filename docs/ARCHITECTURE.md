# System Architecture

## Overview

Personal AI Brain follows a **modular monolith architecture** with clear separation of concerns, designed to scale into a distributed system as it grows.

## High-Level Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                    USER INTERFACE (Frontend)                      │
│  ┌─────────────────┐  ┌─────────────────┐  ┌─────────────────┐ │
│  │   Dashboard     │  │  Knowledge Base │  │  Study Planner  │ │
│  │                 │  │                 │  │                 │ │
│  │ - Statistics    │  │ - Subjects      │  │ - Plans         │ │
│  │ - Charts        │  │ - Topics        │  │ - Tasks         │ │
│  │ - Quick Access  │  │ - Mastery       │  │ - Scheduling    │ │
│  └─────────────────┘  └─────────────────┘  └─────────────────┘ │
│                                                                 │
│  React + TypeScript + Tailwind CSS + Recharts                   │
└────────────────────────┬────────────────────────────────────────┘
                         │ REST API
                         │ (HTTPS)
                         ▼
┌─────────────────────────────────────────────────────────────────┐
│                    BACKEND (API Layer)                            │
│  ┌─────────────────┐  ┌─────────────────┐  ┌─────────────────┐ │
│  │ Authentication  │  │ Source Manager  │  │ ChatGPT Import  │ │
│  │                 │  │                 │  │                 │ │
│  │ - JWT auth      │  │ - Connect/      │  │ - ZIP parsing   │ │
│  │ - OAuth         │  │   Disconnect    │  │ - JSON extract  │ │
│  │ - Sessions      │  │ - Permissions   │  │ - Deduplication │ │
│  └─────────────────┘  └─────────────────┘  └─────────────────┘ │
│                                │                                │
│  ┌─────────────────┐  ┌─────────────────┐  ┌─────────────────┐ │
│  │ AI Engine       │  │ Knowledge Mgmt  │  │ Activity Track  │ │
│  │                 │  │                 │  │                 │ │
│  │ - Topic         │  │ - Subjects      │  │ - Timer         │ │
│  │   Extraction    │  │ - Topics        │  │ - Sessions      │ │
│  │ - Analysis      │  │ - Mastery       │  │ - History       │ │
│  │ - Planning      │  │ - Revision      │  │ - Progress      │ │
│  └─────────────────┘  └─────────────────┘  └─────────────────┘ │
│                                                                 │
│  Python FastAPI + SQLAlchemy + Redis + OpenAI SDK              │
└────────────────────────┬────────────────────────────────────────┘
                         │ SQL Queries
                         ▼
┌─────────────────────────────────────────────────────────────────┐
│                    DATA LAYER (Database)                          │
│  ┌─────────────────┐  ┌─────────────────┐  ┌─────────────────┐ │
│  │   Users         │  │ Conversations   │  │ Activities      │ │
│  │                 │  │                 │  │                 │ │
│  │ - Auth          │  │ - Messages      │  │ - Timer data    │ │
│  │ - Preferences   │  │ - Analysis refs │  │ - Progress      │ │
│  └─────────────────┘  └─────────────────┘  └─────────────────┘ │
│                                │                                │
│  ┌─────────────────┐  ┌─────────────────┐  ┌─────────────────┐ │
│  │ Knowledge       │  │ Plans & Tasks   │  │ Embeddings      │ │
│  │                 │  │                 │  │                 │ │
│  │ - Subjects      │  │ - Schedules     │  │ - Vector store  │ │
│  │ - Topics        │  │ - Dependencies  │  │ - Similarity    │ │
│  │ - Mastery       │  │ - Rescheduling  │  │ - Search        │ │
│  └─────────────────┘  └─────────────────┘  └─────────────────┘ │
│                                                                 │
│  PostgreSQL + pgvector                                          │
└─────────────────────────────────────────────────────────────────┘
```

## Component Details

### 1. Frontend (React + TypeScript)

**Technology Stack:**
- React 18 with TypeScript
- Vite for build tooling
- Tailwind CSS for styling
- React Router for routing
- Recharts for data visualization
- Axios for API communication
- React Query for state management

**Key Components:**
- Dashboard: Summary cards and charts
- ChatGPT Analyzer: File upload and conversation view
- Knowledge Base: Topic tree and mastery indicators
- Study Planner: Plan creation and execution
- Activity Tracker: Timer and session management
- Analytics: Progress reports and statistics

### 2. Backend (Python + FastAPI)

**Technology Stack:**
- FastAPI for REST API
- SQLAlchemy ORM
- Alembic for migrations
- Pydantic for validation
- JWT for authentication
- Redis for caching
- OpenAI SDK for AI features

**API Endpoints Structure:**

```
/api/v1/
├── auth/
│   ├── register
│   ├── login
│   └── logout
├── sources/
│   ├── connect
│   ├── list
│   └── disconnect
├── conversations/
│   ├── upload
│   ├── list
│   └── analyze
├── knowledge/
│   ├── subjects
│   ├── topics
│   └── mastery
├── plans/
│   ├── generate
│   ├── list
│   └── execute
├── activities/
│   ├── start
│   ├── pause
│   ├── stop
│   └── history
└── analytics/
    ├── daily
    ├── weekly
    └── progress
```

### 3. Database (PostgreSQL + pgvector)

**Key Tables:**
- `users`: Authentication and profile
- `data_sources`: Connected sources
- `conversations`: Imported ChatGPT data
- `messages`: Conversation content
- `subjects`: Learning subjects
- `topics`: Individual topics
- `knowledge_records`: Mastery tracking
- `plans`: Generated study plans
- `tasks`: Plan tasks
- `activities`: User activities
- `embeddings`: AI embeddings for search

**Vector Search:**
- pgvector extension for semantic similarity
- 1536-dimensional embeddings (OpenAI text-embedding-3-large)
- IVFFlat index for fast similarity search
- Used for: topic similarity, conversation retrieval

## Data Flow Architecture

### 3-Layer Data Pipeline

```
                    External Sources
                         │
                         ▼
┌─────────────────────────────────────────────────┐
│           DATA INGESTION LAYER                   │
├─────────────────────────────────────────────────┤
│ 1. File Upload                                   │
│    - ChatGPT ZIP export                          │
│    - Validation & parsing                        │
│                                                 │
│ 2. Database Import                               │
│    - Deduplication via checksums                 │
│    - Transaction-safe writes                     │
│                                                 │
│ 3. Permission Check                              │
│    - User consent verification                   │
│    - Access control enforcement                │
└────────────────────────┬────────────────────────┘
                         │
                         ▼
┌─────────────────────────────────────────────────┐
│           ANALYSIS & PROCESSING LAYER            │
├─────────────────────────────────────────────────┤
│ 1. AI Processing                                 │
│    - Topic extraction                            │
│    - Knowledge assessment                        │
│    - Plan generation                             │
│                                                 │
│ 2. Embedding Generation                          │
│    - Text chunking                               │
│    - OpenAI embedding API                        │
│    - Vector storage                              │
│                                                 │
│ 3. Knowledge Graph Update                        │
│    - Mastery level updates                       │
│    - Topic relationships                         │
│    - Revision scheduling                         │
└────────────────────────┬────────────────────────┘
                         │
                         ▼
┌─────────────────────────────────────────────────┐
│           PRESENTATION LAYER                     │
├─────────────────────────────────────────────────┤
│ 1. API Responses                                 │
│    - JSON data structures                        │
│    - Real-time WebSocket updates (future)        │
│                                                 │
│ 2. UI State Management                           │
│    - React Query cache                           │
│    - Local storage for offline                   │
└─────────────────────────────────────────────────┘
```

## Security Architecture

### Authentication Flow

```
User Login
    │
    ▼
┌─────────────────┐
│  Login Request  │
└─────────────────┘
    │
    ▼
┌─────────────────┐
│  Validate Creds │
│  - bcrypt check │
└─────────────────┘
    │
    ▼
┌─────────────────┐
│  Generate JWT   │
│  - HS256 algo   │
│  - 30min expiry │
└─────────────────┘
    │
    ▼
┌─────────────────┐
│  Return Token   │
└─────────────────┘
    │
    ▼
┌─────────────────┐
│  API Requests   │
│  - Authorization│
│  - JWT verify   │
└─────────────────┘
```

### Data Protection

1. **At Rest:**
   - Passwords: bcrypt hashed
   - Secrets: Environment variables
   - Sensitive data: Encrypted columns

2. **In Transit:**
   - HTTPS/TLS 1.3
   - Certificate pinning (future)

3. **Access Control:**
   - Row-level security via user_id
   - Source permissions
   - Audit logging

## Scalability Considerations

### Current (Monolith)
- Single FastAPI application
- Single PostgreSQL instance
- Shared Redis cache

### Future (Microservices)
```
┌─────────────────┐  ┌─────────────────┐  ┌─────────────────┐
│   Auth Service  │  │  AI Service     │  │  Web Service    │
│  (FastAPI)      │  │  (FastAPI)      │  │  (React)        │
└─────────────────┘  └─────────────────┘  └─────────────────┘
        │                    │                    │
        └────────────────────┼────────────────────┘
                             │
                    ┌─────────────────┐
                    │   PostgreSQL    │
                    │   Cluster       │
                    └─────────────────┘
```

## Deployment Architecture

```
                    Internet
                        │
                        ▼
┌─────────────────────────────────────────────┐
│           Load Balancer (Render)             │
└────────────────┬────────────────────────────┘
                   │
        ┌──────────┴──────────┐
        │                     │
        ▼                     ▼
┌───────────────┐     ┌───────────────┐
│ Frontend      │     │ Backend       │
│ (Vercel)      │     │ (Render)      │
└───────────────┘     └───────┬───────┘
                              │
                              ▼
                    ┌─────────────────┐
                    │ PostgreSQL (DB) │
                    │ Render/Neon     │
                    └─────────────────┘
```

## Development Environment

```
docker-compose up
    │
    ├─> Frontend: http://localhost:3000
    ├─> Backend:  http://localhost:8000
    ├─> Database: localhost:5432
    └─> pgAdmin:  http://localhost:5050
```

**Services:**
- `frontend`: React dev server with hot reload
- `backend`: FastAPI with auto-reload
- `db`: PostgreSQL with init scripts
- `redis`: Caching layer
- `pgadmin`: Database admin interface

---

*Architecture Version: 1.0*  
*Last Updated: November 23, 2024*