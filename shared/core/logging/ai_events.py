from .logger import get_logger

def log_ai_event(event_type: str, metadata: dict):
    logger = get_logger()
    logger.info("AI event logged", extra={"event_type": event_type, "metadata": metadata})