# API Specification: REST Endpoints

## 1. Base URL
`http://localhost:8000/api`

## 2. Authentication Endpoints
| Method | Endpoint | Description |
| :--- | :--- | :--- |
| POST | `/auth/register` | Create a new user account |
| POST | `/auth/login` | Obtain a JWT access token |
| GET | `/auth/me` | Get current user profile |

## 3. Task Endpoints (Protected by JWT)
| Method | Endpoint | Description |
| :--- | :--- | :--- |
| GET | `/tasks` | List all tasks for the user |
| POST | `/tasks` | Create a new task |
| GET | `/tasks/{id}` | Get details of a single task |
| PATCH | `/tasks/{id}` | Update task title, desc, or status |
| DELETE | `/tasks/{id}` | Delete a task |

## 4. Data Schemas
### Task Schema
```json
{
  "id": 1,
  "title": "string",
  "description": "string",
  "status": "Pending | Done",
  "created_at": "ISO-8601"
}
```
