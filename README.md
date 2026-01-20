# Workflow Management Backend

Backend API for a workflow and task management system built with **FastAPI**, **SQLAlchemy**, and **PostgreSQL**.

This project provides authentication, project management, role-based access control, and task workflows, designed to be consumed by a frontend application.

---

## Features

### Authentication
- User registration
- JWT-based login
- Protected routes

### Projects
- Create projects
- Project ownership
- Project members with roles (OWNER, MEMBER)
- List projects per user

### Project Members
- Add members to projects
- Role-based permissions
- List project members

### Tasks
- Create tasks within projects
- Assign tasks (owners only)
- Update task status (TODO, IN_PROGRESS, DONE)
- List tasks by project
- Filter tasks by status and assignee
- Soft delete tasks

---

## Tech Stack

- **FastAPI**
- **SQLAlchemy**
- **Alembic**
- **PostgreSQL**
- **JWT Authentication**
- **Pydantic**

---

## Project Structure

```
backend/
├── app/
│   ├── api/
│   │   ├── deps.py
│   │   ├── v1/
│   │   │   ├── auth.py
│   │   │   ├── projects.py
│   │   │   ├── tasks.py
│   │   │   └── users.py
│   │   └── __init__.py
│   ├── core/
│   │   ├── config.py
│   │   └── security.py
│   ├── db/
│   │   ├── session.py
│   │   └── __init__.py
│   ├── models/
│   │   ├── project.py
│   │   ├── project_member.py
│   │   ├── task.py
│   │   ├── user.py
│   │   └── __init__.py
│   ├── repositories/
│   │   ├── project_repository.py
│   │   ├── project_member_repository.py
│   │   ├── task_repository.py
│   │   └── user_repository.py
│   ├── schemas/
│   │   ├── project.py
│   │   ├── project_member.py
│   │   ├── task.py
│   │   ├── user.py
│   │   └── __init__.py
│   ├── services/
│   │   ├── project_service.py
│   │   ├── project_member_service.py
│   │   ├── task_service.py
│   │   └── user_service.py
│   └── __init__.py
├── alembic/
│   ├── versions/
│   └── __init__.py
├── requirements.txt
└── README.md
```

---

## Database Migrations

Alembic is used for database migrations.

Create a migration:
```bash
alembic revision --autogenerate -m "migration message"
```

Apply migrations:
```bash
alembic upgrade head
```

---

## Running the Project

1. Create a virtual environment:
```bash
python -m venv venv
```

2. Activate the virtual environment:
```bash
venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```
4. Configure environment variables:
create a .env file in the root directory of the project and add the following variables:
```bash
DATABASE_URL=postgresql://user:password@localhost:5432/db_name
SECRET_KEY=your_secret_key

```

5. Set up the database:
```bash
alembic upgrade head
```

6. Run the server:
```bash
uvicorn app.main:app --reload
```

The server will be available at `http://localhost:8000`.

The API documentation will be available at `http://localhost:8000/docs`.

---

## Permissions

### Owner
- Create projects
- Add members to projects
- Update project members
- Delete projects
- List projects
- List project members
- List tasks
- Update tasks
- Delete tasks

### Member
- List projects
- List project members
- List tasks
- Update tasks
- Delete tasks

---

## Status

This backend represents a complete MVP and is ready to be integrated with a frontend application.

---

## License

This project is licensed under the MIT License.


