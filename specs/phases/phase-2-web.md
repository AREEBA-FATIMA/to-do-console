# Phase 2: Web Application - Roadmap

## 1. Objective
Transform the Phase 1 CLI application into a modern Full-Stack Web Application with a React frontend and FastAPI backend.

## 2. Technical Goals
- **API**: Build a restful API using FastAPI.
- **Frontend**: Develop a responsive UI with Next.js and Tailwind CSS.
- **Persistence**: Migrate from in-memory dictionary storage to **PostgreSQL**.
- **Auth**: Implement user-specific task lists via JWT authentication.

## 3. High-Level Architecture
- **Backend (FastAPI)**:
    - Controllers: `/api/auth` and `/api/tasks`.
    - Domain: Shared models based on `skills/model-design-skill.md`.
    - Storage: PostgreSQL via SQLAlchemy.
- **Frontend (Next.js)**:
    - Auth pages: Login/Register.
    - Dashboard: Interactive task list with filtering and search.
    - State Management: React hooks + Context API.

## 4. Feature Checklist
- [ ] User Authentication (Signup/Login)
- [ ] Task CRUD via REST API
- [ ] Database Schema Migration (to SQL)
- [ ] Responsive Dashboard UI
- [ ] Dark Mode Support

## 5. Success Criteria
- [ ] Users can only see their own tasks.
- [ ] All CRUD operations work via the web interface.
- [ ] API endpoints are secured with JWT.
- [ ] Database is permanent (data persists after server restart).
