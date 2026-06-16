# Copilot Instructions for This Repository

This file helps Copilot and other AI assistants work effectively in this codebase. **Update this file as your project evolves** to capture important architectural decisions, conventions, and workflows.

## Project Overview

**Add a brief description of what this project does.** For example:
- What problem does it solve?
- What type of application is it (API, frontend, CLI tool, library)?
- Main technology stack?

## Build, Test, and Lint Commands

Update these commands based on your project setup. Include variations for common workflows.

### Install Dependencies
```bash
# Node.js projects
npm install
# or
yarn install

# Python projects
pip install -r requirements.txt
# or
poetry install

# Go projects
go mod download
```

### Build
```bash
# Example for Node.js
npm run build

# Example for Python
python setup.py build

# Example for Go
go build ./cmd/myapp
```

### Run Tests
```bash
# Run all tests
npm test
# or
pytest

# Run specific test file
npm test -- src/path/to/test.js
pytest src/path/to/test.py

# Run tests in watch mode (if available)
npm test -- --watch
pytest-watch
```

### Run Linting
```bash
# Lint code
npm run lint

# Fix linting issues (if available)
npm run lint -- --fix
```

### Local Development
```bash
# Start development server (if applicable)
npm run dev
# or
python app.py
```

## Architecture

### Project Structure
Describe the high-level organization:
- **src/**: Source code directory structure
- **tests/**: Test files organization
- **docs/**: Documentation
- List any domain-specific or module-based organization patterns

### Key Components
**Describe the major systems and how they interact.** For example:
- **Authentication Module**: How users are authenticated (JWT, OAuth, etc.)
- **Database Layer**: ORM, migrations, connection pooling approach
- **API Layer**: REST conventions, middleware stack, routing patterns
- **Frontend Architecture**: State management (Redux, Vuex, etc.), component structure

Example format:
> The API layer (src/api/) uses Express middleware to handle routing. Requests flow through auth middleware → validation → business logic → response formatting. Database queries are centralized in src/db/ and use [ORM name] for type safety.

### Data Flow
If relevant, describe key workflows. For example:
- How user requests flow through the system
- How data is transformed between layers
- Async/event-driven patterns used

## Code Conventions

### Naming Conventions
- File naming: (e.g., PascalCase for components, kebab-case for utilities)
- Variable/function naming patterns
- Constants (UPPER_SNAKE_CASE, etc.)

### File Organization
- How files are grouped within directories
- Colocation patterns (e.g., tests next to source files vs. separate test directory)
- Configuration file locations and purposes

### Code Patterns
- Error handling approach (exceptions, error codes, Result types)
- Logging patterns (where to log, what level)
- Comment style and when to use them
- Import/require conventions

### Testing Patterns
- Test naming conventions (e.g., `test_*.py` or `*.test.js`)
- Test structure (arrange-act-assert, BDD style, etc.)
- Mocking approach (manual, libraries like Jest/Sinon, etc.)
- Coverage expectations if applicable

### Commit Conventions
- Commit message format (if using Conventional Commits or similar)
- Branching strategy (git flow, trunk-based, etc.)
- PR review expectations

## Database (if applicable)
- Migrations approach (manual SQL, ORM migrations, etc.)
- Seeding data for development
- Schema documentation location
- Connection pooling configuration

## Environment Configuration
- Required environment variables (document in .env.example)
- How environment differs between development, testing, and production
- Secrets management approach

## External Services / APIs
- Which external services does this project integrate with?
- How to set up credentials locally for development
- Rate limiting or other constraints to be aware of

## Common Issues and Solutions

Document known gotchas or common problems developers encounter:
- Common setup issues and how to resolve them
- Compatibility constraints (Node.js version, Python version, etc.)
- Platform-specific issues (Windows/Mac/Linux differences)

## Useful Resources
- Link to main README if more detailed project info exists
- Link to CONTRIBUTING.md for contribution guidelines
- Architecture decision records (ADRs) location if maintained
- Internal wiki or documentation
