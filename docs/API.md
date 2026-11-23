# API Documentation

## Personal AI Brain API v1

All endpoints return JSON responses and accept JSON request bodies unless otherwise specified.

**Base URL:** `https://api.personalaibrain.com/api/v1` (or `http://localhost:8000/api/v1` for development)

**Content-Type:** `application/json`

**Authentication:** Bearer JWT Token in Authorization header

---

## Authentication Endpoints

### POST /api/v1/auth/register

Create a new user account.

**Request Body:**
```json
{
  "email": "user@example.com",
  "password": "securePassword123!",
  "full_name": "John Doe"
}
```

**Response:**
```json
{
  "id": "uuid-string",
  "email": "user@example.com",
  "full_name": "John Doe",
  "created_at": "2024-11-23T10:00:00Z"
}
```

**Status Codes:**
- `201 Created` - User created successfully
- `400 Bad Request` - Invalid input
- `409 Conflict` - Email already registered

---

### POST /api/v1/auth/login

Authenticate user and receive JWT token.

**Request Body:**
```json
{
  "email": "user@example.com",
  "password": "securePassword123!"
}
```

**Response:**
```json
{
  "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
  "token_type": "bearer",
  "expires_in": 1800
}
```

**Status Codes:**
- `200 OK` - Login successful
- `401 Unauthorized` - Invalid credentials

---

### POST /api/v1/auth/logout

Invalidate current JWT token.

**Headers:**
```
Authorization: Bearer <token>
```

**Response:**
```json
{
  "message": "Successfully logged out"
}
```

**Status Codes:**
- `200 OK` - Logout successful

---

### GET /api/v1/auth/me

Get current user information.

**Headers:**
```
Authorization: Bearer <token>
```

**Response:**
```json
{
  "id": "uuid-string",
  "email": "user@example.com",
  "full_name": "John Doe",
  "is_active": true,
  "is_superuser": false,
  "created_at": "2024-11-23T10:00:00Z",
  "updated_at": "2024-11-23T10:00:00Z"
}
```

**Status Codes:**
- `200 OK` - User info retrieved
- `401 Unauthorized` - Invalid or expired token

---

## Data Source Endpoints

### POST /api/v1/sources

Connect a new data source.

**Headers:**
```
Authorization: Bearer <token>
```

**Request Body:**
```json
{
  "source_type": "chatgpt",
  "name": "My ChatGPT History",
  "settings": {
    "import_enabled": true
  }
}
```

**Response:**
```json
{
  "id": "uuid-string",
  "user_id": "uuid-string",
  "source_type": "chatgpt",
  "name": "My ChatGPT History",
  "connection_status": "pending",
  "last_sync": null,
  "created_at": "2024-11-23T10:00:00Z",
  "updated_at": "2024-11-23T10:00:00Z"
}
```

**Status Codes:**
- `201 Created` - Source created
- `400 Bad Request` - Invalid input
- `409 Conflict` - Source already exists

---

### GET /api/v1/sources

List all connected data sources.

**Headers:**
```
Authorization: Bearer <token>
```

**Response:**
```json
[
  {
    "id": "uuid-string",
    "user_id": "uuid-string",
    "source_type": "chatgpt",
    "name": "My ChatGPT History",
    "connection_status": "connected",
    "last_sync": "2024-11-23T09:00:00Z",
    "created_at": "2024-11-23T10:00:00Z",
    "updated_at": "2024-11-23T09:00:00Z"
  }
]
```

**Status Codes:**
- `200 OK` - Sources retrieved

---

### DELETE /api/v1/sources/{source_id}

Disconnect a data source.

**Headers:**
```
Authorization: Bearer <token>
```

**Response:**
```json
{
  "message": "Source disconnected successfully"
}
```

**Status Codes:**
- `200 OK` - Source disconnected
- `404 Not Found` - Source not found

---

## Conversation Endpoints

### POST /api/v1/conversations/upload

Upload ChatGPT conversation export file.

**Headers:**
```
Authorization: Bearer <token>
Content-Type: multipart/form-data
```

**Form Data:**
```
file: <ZIP file>
source_id: uuid (optional, uses default source if omitted)
```

**Response:**
```json
{
  "upload_id": "uuid-string",
  "status": "processing",
  "message": "File received, processing started",
  "estimated_completion": "2024-11-23T10:05:00Z"
}
```

**Status Codes:**
- `202 Accepted` - Upload accepted for processing
- `400 Bad Request` - Invalid file format
- `401 Unauthorized` - Not authenticated

---

### GET /api/v1/conversations

List user's conversations.

**Headers:**
```
Authorization: Bearer <token>
```

**Query Parameters:**
- `source_id` (optional): Filter by source
- `limit` (optional, default 50): Pagination limit
- `offset` (optional, default 0): Pagination offset

**Response:**
```json
{
  "conversations": [
    {
      "id": "uuid-string",
      "source_id": "uuid-string",
      "title": "C++ Inheritance Discussion",
      "started_at": "2024-11-20T14:30:00Z",
      "ended_at": "2024-11-20T15:45:00Z",
      "message_count": 25,
      "has_analysis": true
    }
  ],
  "total": 1,
  "limit": 50,
  "offset": 0
}
```

---

### GET /api/v1/conversations/{conversation_id}

Get detailed conversation data.

**Headers:**
```
Authorization: Bearer <token>
```

**Response:**
```json
{
  "id": "uuid-string",
  "source_id": "uuid-string",
  "title": "C++ Inheritance Discussion",
  "started_at": "2024-11-20T14:30:00Z",
  "ended_at": "2024-11-20T15:45:00Z",
  "messages": [
    {
      "id": "uuid-string",
      "role": "user",
      "content": "Explain inheritance in C++",
      "created_at": "2024-11-20T14:30:00Z"
    },
    {
      "id": "uuid-string",
      "role": "assistant",
      "content": "In C++, inheritance allows a class to inherit properties...",
      "created_at": "2024-11-20T14:31:00Z"
    }
  ]
}
```

---

### POST /api/v1/conversations/{conversation_id}/analyze

Request AI analysis of a conversation.

**Headers:**
```
Authorization: Bearer <token>
```

**Request Body:**
```json
{
  "analysis_types": ["topic_extraction", "knowledge_assessment"],
  "auto_approve": false
}
```

**Response:**
```json
{
  "analysis_id": "uuid-string",
  "status": "pending",
  "analysis_types": ["topic_extraction", "knowledge_assessment"],
  "created_at": "2024-11-23T10:10:00Z"
}
```

---

## Knowledge Base Endpoints

### GET /api/v1/knowledge/subjects

List all subjects for current user.

**Headers:**
```
Authorization: Bearer <token>
```

**Response:**
```json
[
  {
    "id": "uuid-string",
    "user_id": "uuid-string",
    "name": "C++ Programming",
    "description": "Object-oriented programming in C++",
    "color": "#3B82F6",
    "icon": "code",
    "topics_count": 12,
    "created_at": "2024-11-20T10:00:00Z",
    "updated_at": "2024-11-20T10:00:00Z"
  }
]
```

---

### POST /api/v1/knowledge/subjects

Create a new subject.

**Headers:**
```
Authorization: Bearer <token>
```

**Request Body:**
```json
{
  "name": "Java Programming",
  "description": "Object-oriented programming and Java ecosystem",
  "color": "#EA580C",
  "icon": "coffee"
}
```

**Response:**
```json
{
  "id": "uuid-string",
  "user_id": "uuid-string",
  "name": "Java Programming",
  "description": "Object-oriented programming and Java ecosystem",
  "color": "#EA580C",
  "icon": "coffee",
  "created_at": "2024-11-23T10:15:00Z",
  "updated_at": "2024-11-23T10:15:00Z"
}
```

---

### GET /api/v1/knowledge/subjects/{subject_id}/topics

List topics for a subject.

**Headers:**
```
Authorization: Bearer <token>
```

**Response:**
```json
[
  {
    "id": "uuid-string",
    "subject_id": "uuid-string",
    "name": "Inheritance",
    "description": "Class inheritance and polymorphism",
    "order_index": 3,
    "estimated_hours": 2.5,
    "mastery_level": "learning",
    "confidence_score": 0.65,
    "last_studied": "2024-11-22T16:00:00Z",
    "next_review": "2024-11-30T16:00:00Z"
  }
]
```

---

### PATCH /api/v1/knowledge/topics/{topic_id}

Update topic mastery level.

**Headers:**
```
Authorization: Bearer <token>
```

**Request Body:**
```json
{
  "mastery_level": "practiced",
  "confidence_score": 0.85,
  "notes": "Completed 10 practice problems"
}
```

**Response:**
```json
{
  "id": "uuid-string",
  "user_id": "uuid-string",
  "topic_id": "uuid-string",
  "mastery_level": "practiced",
  "confidence_score": 0.85,
  "last_studied": "2024-11-23T10:20:00Z",
  "next_review": "2024-12-03T10:20:00Z",
  "evidence_count": 15,
  "created_at": "2024-11-20T10:00:00Z",
  "updated_at": "2024-11-23T10:20:00Z"
}
```

---

## Study Planner Endpoints

### POST /api/v1/plans/generate

Generate a new study plan from AI.

**Headers:**
```
Authorization: Bearer <token>
```

**Request Body:**
```json
{
  "title": "C++ OOP Mastery Plan",
  "description": "Complete Object-Oriented Programming in C++",
  "goals": [
    "Understand classes and objects",
    "Master inheritance and polymorphism",
    "Practice operator overloading"
  ],
  "start_date": "2024-11-25",
  "end_date": "2024-12-15",
  "total_hours": 30,
  "daily_hours": 2,
  "current_level": "beginner",
  "preferred_time": "evening"
}
```

**Response:**
```json
{
  "id": "uuid-string",
  "user_id": "uuid-string",
  "title": "C++ OOP Mastery Plan",
  "description": "Complete Object-Oriented Programming in C++",
  "start_date": "2024-11-25",
  "end_date": "2024-12-15",
  "total_hours": 30,
  "actual_hours": 0,
  "status": "active",
  "created_by": "ai",
  "tasks": [
    {
      "id": "uuid-string",
      "plan_id": "uuid-string",
      "title": "C++ Classes and Objects",
      "estimated_duration_minutes": 120,
      "scheduled_start": "2024-11-25T18:00:00Z",
      "scheduled_end": "2024-11-25T20:00:00Z",
      "status": "pending",
      "priority": 1
    }
  ],
  "created_at": "2024-11-23T10:25:00Z",
  "updated_at": "2024-11-23T10:25:00Z"
}
```

---

### GET /api/v1/plans

List user's study plans.

**Headers:**
```
Authorization: Bearer <token>
```

**Query Parameters:**
- `status` (optional): Filter by status (active, completed, draft)
- `limit` (optional, default 50)
- `offset` (optional, default 0)

---

## Activity Tracking Endpoints

### POST /api/v1/activities/start

Start tracking an activity.

**Headers:**
```
Authorization: Bearer <token>
```

**Request Body:**
```json
{
  "title": "Studying C++ Inheritance",
  "task_id": "uuid-string (optional)",
  "subject_id": "uuid-string",
  "topic_id": "uuid-string"
}
```

**Response:**
```json
{
  "id": "uuid-string",
  "user_id": "uuid-string",
  "task_id": "uuid-string",
  "title": "Studying C++ Inheritance",
  "description": null,
  "subject_id": "uuid-string",
  "topic_id": "uuid-string",
  "started_at": "2024-11-23T10:30:00Z",
  "ended_at": null,
  "duration_minutes": null,
  "status": "in_progress",
  "device_type": "web",
  "created_at": "2024-11-23T10:30:00Z",
  "updated_at": "2024-11-23T10:30:00Z"
}
```

---

### POST /api/v1/activities/{activity_id}/stop

Stop tracking an activity.

**Headers:**
```
Authorization: Bearer <token>
```

**Response:**
```json
{
  "id": "uuid-string",
  "user_id": "uuid-string",
  "task_id": "uuid-string",
  "title": "Studying C++ Inheritance",
  "started_at": "2024-11-23T10:30:00Z",
  "ended_at": "2024-11-23T11:30:00Z",
  "duration_minutes": 60,
  "status": "completed"
}
```

---

## Analytics Endpoints

### GET /api/v1/analytics/daily

Get daily productivity analytics.

**Headers:**
```
Authorization: Bearer <token>
```

**Query Parameters:**
- `date` (optional, default today): Date in YYYY-MM-DD format

**Response:**
```json
{
  "date": "2024-11-23",
  "total_study_time_minutes": 120,
  "target_time_minutes": 180,
  "completion_percentage": 67,
  "activities_count": 3,
  "topics_studied": 2,
  "focus_score": 0.85
}
```

---

## Error Responses

All endpoints may return the following error responses:

### 400 Bad Request
```json
{
  "detail": "Validation error: email already registered"
}
```

### 401 Unauthorized
```json
{
  "detail": "Not authenticated"
}
```

### 403 Forbidden
```json
{
  "detail": "Insufficient permissions"
}
```

### 404 Not Found
```json
{
  "detail": "Source not found"
}
```

### 422 Unprocessable Entity
```json
{
  "detail": [
    {
      "loc": ["body", "email"],
      "msg": "invalid email format",
      "type": "value_error.email"
    }
  ]
}
```

### 500 Internal Server Error
```json
{
  "detail": "Internal server error"
}
```

---

## Rate Limiting

API requests are rate-limited:
- **Authenticated users:** 100 requests per minute
- **Unauthenticated:** 10 requests per minute

Rate limit headers are included in responses:
```
X-RateLimit-Limit: 100
X-RateLimit-Remaining: 95
X-RateLimit-Reset: 1697904000
```

---

## Pagination

List endpoints support pagination via query parameters:
- `limit`: Number of items per page (default: 50, max: 100)
- `offset`: Number of items to skip (default: 0)

Response includes pagination metadata:
```json
{
  "items": [...],
  "total": 125,
  "limit": 50,
  "offset": 0
}
```

---

## Versioning

API version is included in URL path: `/api/v1/`

Future versions will be backward-compatible and documented separately.