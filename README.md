# Portfolio Backend

This is the backend code for my personal portfolio website. It provides REST API to manage the content on the frontend.

## Technologies

- Python 3.12
- FastAPI - A modern, high-performance web framework
- MongoDB - Document database to store portfolio content
- Motor - Asynchronous Python driver for MongoDB
- Pydantic - Data validation using Python type annotations

## Features

- [x] GET API for homepage content
- [ ] CRUD API for portfolio content

## TODO

- [ ] Implement authentication
- [ ] Implement CRUD operations to create, update and delete data
- [ ] Write tests for API endpoints (TESTS ADDED FOR GET DATA ENDPOINTS)
- [ ] Containerize application using Docker
- [ ] Add API usage tracking and analytics

## Why backend for portfolio?

The goal of this project is to decouple the frontend UI from the underlying portfolio data and content. By exposing the data through a REST API, the frontend code can be modified or rewritten without affecting the core portfolio information.

Some key benefits of this approach:

- **Flexibility** - The frontend can be rewritten using different frameworks or designs without changing any data storage code.

- **Maintainability** - Portfolio content can be managed in a central place without touching frontend code. New projects, experience, certificates etc... can be added/updated/removed easily.

- **Separation of Concerns** - Clear separation between frontend presentation logic and backend data management.

- **Accessibility** - API could be used to support alternate frontend frameworks, or other client applications.

## Getting Started

### Installing

```bash
git clone https://github.com/kishor1445/portfolio-backend.git
cd portfolio-backend
pip install -r requirements.txt
```

### Configuration

The app uses a `.env` file for configuration:

```
MONGODB_URI=Your MongoDB URI
```

### Run the server

```bash
uvicorn app.main:app
```

## License

This project is licensed under the MIT License - see the [LICENSE](https://github.com/kishor1445/portfolio-backend/blob/main/LICENSE) file for more details.
