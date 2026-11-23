# Software Requirements Specification (SRS)

## Project: Personal AI Brain

**Version:** 1.0  
**Date:** November 23, 2024  
**Status:** Draft  
**Author:** Hermes Agent

---

## 1. Introduction

### 1.1 Purpose

Personal AI Brain is an AI-powered personal knowledge and productivity management system that:

- Imports and analyzes user's digital learning activities
- Builds a knowledge graph of learned concepts
- Generates adaptive study plans
- Tracks actual work vs planned work
- Automatically reschedules missed tasks

### 1.2 Scope

**In Scope:**
- User authentication and account management
- ChatGPT conversation import and analysis
- Knowledge graph construction
- AI-powered study plan generation
- Activity tracking with timer
- Progress analytics and reporting
- Permission-based data access

**Out of Scope:**
- Browser extension integration
- Desktop application monitoring
- Mobile application
- Multi-user features
- Collaborative features

### 1.3 Definitions, Acronyms, and Abbreviations

| Term | Definition |
|------|------------|
| AI | Artificial Intelligence |
| JWT | JSON Web Token |
| CRUD | Create, Read, Update, Delete |
| CRUD | Create, Read, Update, Delete |
| API | Application Programming Interface |
| MVP | Minimum Viable Product |
| UI | User Interface |
| UX | User Experience |
| REST | Representational State Transfer |

---

## 2. Overall Description

### 2.1 Product Perspective

Personal AI Brain is a **web-based application** built as a monolith, designed to evolve into a distributed system.

**Architecture Type:** Three-tier architecture
- Presentation Layer (React + TypeScript)
- Business Logic Layer (FastAPI + Python)
- Data Layer (PostgreSQL + pgvector)

### 2.2 Product Functions

1. **User Management**
   - Account creation and authentication
   - Profile management
   - Password reset

2. **Data Source Integration**
   - ChatGPT conversation import
   - Source connection management
   - Permission handling

3. **AI Analysis Engine**
   - Topic extraction
   - Knowledge assessment
   - Study plan generation

4. **Knowledge Management**
   - Subject and topic organization
   - Mastery tracking
   - Revision scheduling

5. **Productivity Tracking**
   - Activity timer
   - Plan execution
   - Progress reporting

### 2.3 User Characteristics

**Target Users:**
- Students (undergraduate, graduate)
- Software developers
- Self-learners
- Researchers
- Professionals

**User Skills:**
- Basic computer literacy required
- Internet browsing skills
- Ability to use file systems

### 2.4 Constraints

1. Requires internet connection for AI features
2. OpenAI API key required for AI functionality
3. ChatGPT export needed for full functionality
4. Privacy compliance (GDPR, CCPA)

### 2.5 Assumptions and Dependencies

1. Users have valid OpenAI API access
2. Users can export ChatGPT conversations
3. PostgreSQL 15+ with pgvector extension
4. Docker and Docker Compose for development
5. Node.js 18+ and Python 3.12+

---

## 3. Specific Requirements

### 3.1 External Interfaces

#### 3.1.1 User Interfaces

**Dashboard Page**
- Displays summary cards (study time, progress, streak)
- Shows today's study plan
- Quick access to key features

**ChatGPT Analyzer Page**
- File upload for conversation exports
- Conversation list with metadata
- Topic extraction results
- Analysis approval workflow

**Knowledge Base Page**
- Subject and topic tree view
- Mastery level indicators
- Edit and delete options

**Study Planner Page**
- Goal and timeline input
- Generated plan display
- Task execution and tracking

**Activity Tracker Page**
- Start/pause/stop timer
- Activity categorization
- History view

#### 3.1.2 Hardware Interfaces

- Desktop computer (Windows, macOS, Linux)
- Modern web browser (Chrome, Firefox, Safari, Edge)
- Minimum 4GB RAM, 500MB storage

#### 3.1.3 Software Interfaces

- PostgreSQL database
- OpenAI API (GPT-4, embeddings)
- Redis for caching

#### 3.1.4 Communications Interfaces

- HTTPS REST API
- WebSocket for real-time updates (future)
- Email for notifications (future)

### 3.2 Functional Requirements

#### FR-1: User Management

| ID | Requirement | Priority |
|----|-------------|----------|
| FR-1.1 | User can register with email and password | High |
| FR-1.2 | User can login with credentials | High |
| FR-1.3 | User can logout | High |
| FR-1.4 | User can reset password | Medium |
| FR-1.5 | JWT tokens authenticate API access | High |

#### FR-2: ChatGPT Integration

| ID | Requirement | Priority |
|----|-------------|----------|
| FR-2.1 | User can upload ChatGPT ZIP export | High |
| FR-2.2 | System parses JSON conversation data | High |
| FR-2.2.1 | Extracts conversation titles and timestamps | High |
| FR-2.2.2 | Extracts user questions and assistant responses | High |
| FR-2.3 | Duplicate detection via checksum | High |
| FR-2.4 | Conversation displayed in searchable list | High |

#### FR-3: AI Analysis

| ID | Requirement | Priority |
|----|-------------|----------|
| FR-3.1 | AI extracts topics from conversations | High |
| FR-3.2 | AI identifies mastery levels | High |
| FR-3.3 | AI detects weak concepts | High |
| FR-3.4 | AI generates study recommendations | High |
| FR-3.5 | Analysis requires user approval | High |

#### FR-4: Study Planning

| ID | Requirement | Priority |
|----|-------------|----------|
| FR-4.1 | User sets learning goals | High |
| FR-4.2 | User sets available time | High |
| FR-4.3 | System generates daily schedule | High |
| FR-4.4 | System generates weekly milestones | High |
| FR-4.5 | System accounts for topic dependencies | Medium |
| FR-4.6 | Plan can be edited by user | Medium |

#### FR-5: Knowledge Management

| ID | Requirement | Priority |
|----|-------------|----------|
| FR-5.1 | Subjects can be created | High |
| FR-5.2 | Topics can be organized hierarchically | High |
| FR-5.3 | Mastery level can be updated | High |
| FR-5.4 | Revision dates can be scheduled | Medium |
| FR-5.5 | Knowledge is linked to evidence | Medium |

#### FR-6: Activity Tracking

| ID | Requirement | Priority |
|----|-------------|----------|
| FR-6.1 | User can start activity timer | High |
| FR-6.2 | User can pause/resume timer | High |
| FR-6.3 | User can stop timer | High |
| FR-6.4 | Activities can be categorized | High |
| FR-6.5 | Duration is auto-calculated | High |

### 3.3 Non-Functional Requirements

#### NFR-1: Performance

| Requirement | Target |
|-------------|--------|
| Dashboard load time | < 3 seconds |
| API response time | < 500ms |
| Concurrent users | 1,000 |
| Database queries | < 100ms avg |

#### NFR-2: Security

| Requirement | Implementation |
|-------------|----------------|
| Data in transit | TLS 1.3 |
| Passwords | bcrypt hash |
| API authentication | JWT |
| Authorization | Role-based |

#### NFR-3: Privacy

| Requirement | Implementation |
|-------------|----------------|
| User consent | Explicit opt-in |
| Data export | Full export capability |
| Data deletion | Complete removal |
| Access logs | Audit trail |

#### NFR-4: Reliability

| Requirement | Target |
|-------------|--------|
| Uptime | 99.9% |
| Backup frequency | Daily |
| Recovery time | < 1 hour |
| Error reporting | Automated |

---

## 4. Other Requirements

### 4.1 Regulatory Requirements

- GDPR compliance for EU users
- CCPA compliance for California users
- HIPAA not applicable

### 4.2 Quality Requirements

- Code review required for all changes
- Unit test coverage > 80%
- Integration test coverage > 70%
- Security scan in CI pipeline

---

## 5. Appendices

### Appendix A: Use Case Diagram

```
Users
  │
  ├── Login ────────── System
  │
  ├── Upload ChatGPT Export ── System ── Display Conversations
  │
  ├── Select for Analysis ── System ── Generate Summary
  │
  ├── Create Study Plan ── System ── Display Plan
  │
  └── Track Activity ── System ── Record Progress
```

### Appendix B: Data Flow

```
User Input → API → Business Logic → Database → Response
     │          │          │          │        │
     └─ File ───┴──────────┴──────────┘        │
                                               │
     AI Request ────────────────────────────────┘
```

### Appendix C: Acronyms

| Acronym | Full Form |
|---------|-----------|
| API | Application Programming Interface |
| CRUD | Create, Read, Update, Delete |
| JWT | JSON Web Token |
| MVP | Minimum Viable Product |
| UI | User Interface |
| UX | User Experience |