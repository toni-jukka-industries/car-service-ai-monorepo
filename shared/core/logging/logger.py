import logging
import json
from logging.handlers import RotatingFileHandler

class JsonFormatter(logging.Formatter):
    def format(self, record: logging.LogRecord) -> str:
        log_record = {
            "timestamp": self.formatTime(record),
            "level": record.levelname,
            "message": record.getMessage(),
            "module": record.module,
            "name": record.name,
            "correlation_id": getattr(record, "correlation_id", None),
        }
        return json.dumps(log_record)

# Configure logger
logger = logging.getLogger("car_service_ai_logger")
logger.setLevel(logging.DEBUG)

# Create handlers
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)
console_handler.setFormatter(JsonFormatter())

file_handler = RotatingFileHandler("car_service_ai.log", maxBytes=5000000, backupCount=5)
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(JsonFormatter())

# Add handlers to the logger
logger.addHandler(console_handler)
logger.addHandler(file_handler)

# Example usage
if __name__ == "__main__":
    logger.info("Logger initialized successfully", extra={"correlation_id": "123456"})