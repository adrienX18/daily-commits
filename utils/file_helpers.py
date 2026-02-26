"""
File system utility functions
"""
import os
from typing import List, Optional


def get_file_extension(filename: str) -> str:
    """
    Extract file extension from filename.
    
    Args:
        filename: Name of the file
    
    Returns:
        File extension without the dot, or empty string if no extension
    
    Examples:
        >>> get_file_extension("document.pdf")
        'pdf'
        >>> get_file_extension("archive.tar.gz")
        'gz'
    """
    if not filename or '.' not in filename:
        return ''
    return filename.rsplit('.', 1)[-1]


def get_file_size_mb(filepath: str) -> Optional[float]:
    """
    Get file size in megabytes.
    
    Args:
        filepath: Path to the file
    
    Returns:
        File size in MB, or None if file doesn't exist
    """
    if not os.path.exists(filepath):
        return None
    
    size_bytes = os.path.getsize(filepath)
    return size_bytes / (1024 * 1024)


def list_files_by_extension(directory: str, extension: str) -> List[str]:
    """
    List all files in a directory with a specific extension.
    
    Args:
        directory: Directory path to search
        extension: File extension (without dot)
    
    Returns:
        List of matching filenames
    """
    if not os.path.isdir(directory):
        return []
    
    return [
        f for f in os.listdir(directory)
        if os.path.isfile(os.path.join(directory, f)) and f.endswith(f'.{extension}')
    ]


def create_directory_if_not_exists(directory: str) -> bool:
    """
    Create directory if it doesn't exist.
    
    Args:
        directory: Directory path to create
    
    Returns:
        True if directory was created, False if it already existed
    """
    if os.path.exists(directory):
        return False
    
    os.makedirs(directory, exist_ok=True)
    return True
