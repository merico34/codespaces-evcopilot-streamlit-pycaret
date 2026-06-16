# Copilot Instructions for This Repository

This file helps Copilot and other AI assistants work effectively in this codebase. **Update this file as your project evolves** to capture important architectural decisions, conventions, and workflows.

## Project Overview

A **Streamlit web application** for automated machine learning using PyCaret. The app provides an interactive UI for loading datasets and running ML classification models without requiring deep ML expertise. It's containerized with Docker for easy deployment and reproducibility.

- **Type**: Web UI for ML automation
- **Tech Stack**: Streamlit, PyCaret, Pandas, NumPy, scikit-learn, Docker
- **Python**: 3.10+

## Build, Test, and Lint Commands

### Install Dependencies
```bash
pip install -r requirements.txt
```

### Run Locally (Direct Python)
```bash
# Install first if needed
pip install -r requirements.txt

# Run the Streamlit app
streamlit run app.py
```
The app will be available at `http://localhost:8501`

### Docker-Based Development
```bash
# Build the image
docker-compose build

# Run the container
docker-compose up

# View logs
docker-compose logs -f pycaret-app

# Stop the container
docker-compose down
```
The app will be available at `http://localhost:8501`

### Testing & Linting
No automated test suite exists. Manual testing through the Streamlit UI is the primary validation method.

## Architecture

### Project Structure
- **app.py**: Single-file Streamlit application (main entry point)
- **requirements.txt**: Python dependencies with pinned versions for reproducibility
- **Dockerfile**: Container setup; installs system dependencies (build-essential, libgomp1 for OpenMP support)
- **docker-compose.yml**: Orchestrates containerized development with live code volume mounting

No complex directory structure—this is a simple, single-page Streamlit app.

### Key Components

**Streamlit Frontend (app.py)**
- Uses Streamlit's built-in UI components for a zero-configuration web interface
- Displays version information for installed packages
- Shows Docker commands for quick reference
- Designed to be extended with data upload and ML model execution flows

**ML Pipeline (via PyCaret)**
- PyCaret abstracts scikit-learn and other ML libraries
- Key functions used: `setup()` (data preprocessing), `compare_models()` (model selection), `pull()` (results)
- Runs classification workflows with automated hyperparameter tuning

### Data Flow
1. User accesses Streamlit app at `http://localhost:8501`
2. User uploads dataset via Streamlit file uploader (typical workflow)
3. PyCaret `setup()` prepares data (encoding, scaling, feature engineering)
4. `compare_models()` trains multiple classifiers and ranks them
5. Results displayed via Streamlit tables/charts

### Docker & Containerization
- **Port**: 8501 (Streamlit default)
- **Healthcheck**: `curl --fail http://localhost:8501/_stcore/health || exit 1`
- **Environment Variables**: `STREAMLIT_SERVER_HEADLESS=true`, `STREAMLIT_SERVER_MAXUPLOADSIZE=200`
- **Volume Mounts**: `.:/app` for live reloading during development
- **System Dependencies**: `build-essential` and `libgomp1` ensure OpenMP (used by scikit-learn) and compilation tools are available

## Code Conventions

### Streamlit-Specific Patterns
- **Page Configuration**: `st.set_page_config()` should be the first Streamlit command
- **Layout**: Use `st.columns()` for multi-column layouts, `st.tabs()` for tab navigation
- **User Input**: Upload data with `st.file_uploader()`, collect parameters with `st.selectbox()`, `st.slider()`, etc.
- **Interactivity**: Use Streamlit's reactive model—script reruns on every user interaction
- **Caching**: Use `@st.cache_data` for expensive computations to avoid recalculation on reruns

### PyCaret Integration
- Always call `pycaret.classification.setup()` before running ML tasks (handles preprocessing)
- Use `compare_models()` for automated model selection
- Use `pull()` to extract results as a Pandas DataFrame for display
- Remember that PyCaret is opinionated—read its documentation on supported data types and missing value handling

### File Organization
- **app.py**: Keep logic simple; add helper functions as needed but within the same file for now
- If the app grows: consider splitting into `pages/` subdirectory (Streamlit's multi-page app feature) and `utils/` for helper functions

### Import Style
- Standard Python imports first, then third-party (streamlit, pycaret, pandas, etc.)
- No complex import aliasing; use standard conventions (`import pandas as pd`, `import numpy as np`)

## Environment Configuration

**No `.env` file needed** for basic operation. If adding configuration:
- Streamlit config: Use `.streamlit/config.toml` (not required for development)
- Python environment: Managed via `docker-compose.yml` environment variables
- Development vs. Production: Currently no distinction; docker-compose is for local dev only

## Common Issues and Solutions

### PyCaret Compatibility
- **Missing OpenMP**: If you see `libgomp1 not found` errors, the Dockerfile already installs `libgomp1` as a system dependency
- **Scikit-learn Warnings**: NumPy and scikit-learn versions are pinned for compatibility; avoid upgrading them independently
- **Memory Issues**: PyCaret's `compare_models()` can be memory-intensive; set `n_select=3` or similar to limit the number of models trained

### Streamlit Quirks
- **Hot Reloads**: Changes to `app.py` trigger script reruns; be aware that top-level code runs on every interaction
- **State Management**: Use `st.session_state` to persist data across reruns
- **Upload Size Limit**: The docker-compose sets `STREAMLIT_SERVER_MAXUPLOADSIZE=200` (MB); adjust in `docker-compose.yml` if needed

### Docker Debugging
- **Port Already in Use**: If `8501` is taken, change the port mapping in `docker-compose.yml`: `- "8502:8501"`
- **Container Won't Start**: Check logs with `docker-compose logs pycaret-app`; often due to missing dependencies or syntax errors in `app.py`
- **Live Volume Mount Not Working**: Ensure `.:/app` is correctly specified; on Windows/Mac, enable file sharing in Docker Desktop settings

## Useful Resources

- **Streamlit Docs**: https://docs.streamlit.io (for UI components, caching, deployment)
- **PyCaret Docs**: https://pycaret.gitbook.io/docs (for ML setup, model comparison, result interpretation)
- **Docker Docs**: https://docs.docker.com (for debugging container issues)
- **Scikit-learn Docs**: https://scikit-learn.org (underlying ML library; useful for hyperparameter understanding)
