# Feature: User Authentication

## 1. Description
Provide secure access to user-specific to-do lists using JWT tokens.

## 2. Requirements
- **Registration**: Users provide email and password.
- **Password Security**: Passwords must be hashed using `bcrypt` before storage.
- **JWT Tokens**: Login returns a Bearer token with expiration (e.g., 30 mins).
- **Session Management**: Auth state persisted in `localStorage` or `httpOnly` cookies.
- **Authorization**: Only authenticated users can access `/tasks` endpoints.

## 3. Acceptance Criteria
- [ ] User cannot register twice with the same email.
- [ ] Incorrect password returns 401 Unauthorized.
- [ ] Token is required for all task operations.
- [ ] Frontend redirects to `/login` if not authenticated.
