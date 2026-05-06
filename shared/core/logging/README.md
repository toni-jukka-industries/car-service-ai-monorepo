# Logging Module

The logging module provides a structured, centralized logging system for the Car Service AI OS platform. It supports the following features:

- **Structured JSON Logs**: Includes `correlation_id`, `request_id`, `user_id`, and more.
- **Rotating File Handlers**: Logs are stored in multiple files with size limits.
- **Middleware Integration**: Automatically logs requests and responses in FastAPI applications.
- **AI Event Logging**: Dedicated logger for AI-specific activities.

## Usage

1. Import the logger:
   ```python
   from core.logging import get_logger

   logger = get_logger()
   logger.info("Log message")
   ```

2. Add LoggingMiddleware to your FastAPI app:
   ```python
   from core.logging.middleware import LoggingMiddleware
   app.add_middleware(LoggingMiddleware)
   ```

3. Log AI events:
   ```python
   from core.logging.ai_events import log_ai_event
   log_ai_event("ai-prompt", {"model": "GPT-4", "duration": 200})
   ```