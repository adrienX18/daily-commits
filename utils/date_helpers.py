"""Date and time utility functions."""

from datetime import datetime, timedelta


def get_current_timestamp() -> str:
    """Return the current timestamp in ISO format."""
    return datetime.now().isoformat()


def days_until(target_date: datetime) -> int:
    """Calculate days until a target date."""
    delta = target_date - datetime.now()
    return delta.days


def format_date(date: datetime, fmt: str = "%Y-%m-%d") -> str:
    """Format a datetime object to a string."""
    return date.strftime(fmt)
