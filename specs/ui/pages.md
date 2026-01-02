# UI Specification: Pages & Components

## 1. Design System
- **Theme**: Dark Mode (Glassmorphism look).
- **Typography**: Inter / Outfit.
- **Colors**: Slate, Indigo, Cyan.

## 2. Pages
### 2.1. Authentication (`/auth/login`, `/auth/register`)
- Clean, centered form.
- Switch between login and signup.
- Error messages for invalid credentials.

### 2.2. Dashboard (`/dashboard`)
- **Layout**: Sidebar with category filters (All, Pending, Done).
- **Task List**: List of cards showing title, status, and createdAt.
- **Task Form**: Modal or sliding panel for adding/editing tasks.
- **Search**: Top bar search to filter tasks by title.

## 3. Reusable Components
- `Button`: Consistent styling across the app.
- `Input`: Standardized input fields with labels.
- `TaskCard`: Card-based view for individual tasks.
- `StatusBadge`: Visual indicator for Pending/Done (Green/Yellow).
