# Shared Core Module

The Shared Core module provides critical utilities, middleware, and shared configurations for the "Car Service AI OS" platform. It is built with reusability and enterprise-grade practices in mind.

## Features

### 1. Centralized Configuration
- Manages application-wide configurations and environment settings.

### 2. Environment Manager
- Handles environment-specific settings and loading `.env` files.

### 3. Enterprise Logging
- Provides structured JSON logging and supports different log levels.

### 4. JWT Authentication
- Manages JSON Web Token (JWT)-based authentication.

### 5. Role-Based Permissions
- Provides utilities for managing user roles and enforcing access control.

### 6. Middleware
- Allows for centralized implementation of middleware such as rate limiting, request tracing, and custom headers.

### 7. Audit Logging
- Maintains logging of all critical actions for audit purposes.

### 8. AI Configuration Loader
- Dynamically loads configurations specifically tuned for AI services.

### 9. Rate Limiting
- Implements API rate limiting utilities.

### 10. Request Tracing
- Offers support for distributed tracing with unique trace IDs.

---

## Getting Started

1. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
2. **Import utilities into your module**:
   ```python
   from core.config import app_config
   from core.logger import logger
   ```

---

This module is critical for ensuring standardization across all platform components.