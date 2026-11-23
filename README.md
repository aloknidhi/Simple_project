# Personal AI Brain

An AI-powered personal knowledge & productivity management system that understands your learning activities, builds a knowledge graph, and generates adaptive study plans.

## 🎯 Vision
Transform scattered digital learning activities into structured knowledge, actionable plans, and measurable progress.

## 🏗️ Architecture

```
personal-ai-brain/
├── frontend/              # React + TypeScript + Tailwind
├── backend/               # Python FastAPI
├── database/              # PostgreSQL + pgvector
├── docs/                  # Documentation
└── storage/               # Imported files cache
```

## 🚀 Technology Stack

| Layer | Technology |
|-------|------------|
| Frontend | React + TypeScript + Tailwind CSS + Recharts |
| Backend | Python 3.12 + FastAPI |
| Database | PostgreSQL + pgvector |
| AI | OpenAI API (GPT-4, embeddings) |
| Auth | JWT + OAuth2 |
| Deployment | Docker + Render/Vercel |

## 📋 Development Roadmap

### Phase 1: Foundation (Days 1-7)
1. Project configuration & Docker setup
2. Database schema & migrations  
3. User authentication system
4. ChatGPT importer module
5. AI analyzer module
6. Knowledge graph models
7. Study planner module

### Phase 2: Core Features (Days 8-14)
8. Activity tracking & timer
9. Analytics & reporting
10. Dashboard & visualization
11. Permission management
12. Source integration framework
13. Testing suite
14. Production deployment

## 🛠️ Getting Started

```bash
# Clone repository
git clone https://github.com/aloknidhi/Simple_project.git
cd Simple_project

# Setup backend
cd backend
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# Setup frontend  
cd ../frontend
npm install

# Start services
docker-compose up
```

## 📚 Documentation

- [Software Requirements Specification](docs/SRS.md)
- [System Architecture](docs/ARCHITECTURE.md)
- [API Documentation](docs/API.md)
- [Development Guide](docs/DEVELOPMENT.md)

## 🔐 Privacy & Security

- Explicit user consent for all data sources
- End-to-end encryption for sensitive data
- No hidden data collection
- GDPR-compliant data deletion

## 🤝 Contributing

This is a personal project. Open issues for bugs or feature requests.