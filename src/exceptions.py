class DashboardError(Exception):
    """Base application exception."""


class SensorError(DashboardError):
    """Raised when a sensor cannot provide data."""


class StorageError(DashboardError):
    """Raised when storage operations fail."""
