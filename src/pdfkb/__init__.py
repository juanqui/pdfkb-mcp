"""PDF Knowledgebase MCP Server

A Model Context Protocol server for managing PDF documents with vector search capabilities.
"""

__version__ = "0.1.2"

from .config import ServerConfig
from .embeddings import EmbeddingService

# Exceptions
from .exceptions import (
    ChunkingError,
    ConfigurationError,
    DocumentNotFoundError,
    EmbeddingError,
    FileSystemError,
    PDFKnowledgebaseError,
    PDFProcessingError,
    RateLimitError,
    ValidationError,
    VectorStoreError,
)
from .file_monitor import FileMonitor

# Core server and configuration
from .main import PDFKnowledgebaseServer

# Data models
from .models import Chunk, Document, ProcessingResult, SearchQuery, SearchResult

# Core components
from .pdf_processor import PDFProcessor
from .vector_store import VectorStore

__all__ = [
    # Version
    "__version__",
    # Core server and configuration
    "PDFKnowledgebaseServer",
    "ServerConfig",
    # Data models
    "Document",
    "Chunk",
    "SearchResult",
    "SearchQuery",
    "ProcessingResult",
    # Core components
    "PDFProcessor",
    "VectorStore",
    "EmbeddingService",
    "FileMonitor",
    # Exceptions
    "PDFKnowledgebaseError",
    "ConfigurationError",
    "PDFProcessingError",
    "EmbeddingError",
    "VectorStoreError",
    "FileSystemError",
    "DocumentNotFoundError",
    "ValidationError",
    "RateLimitError",
    "ChunkingError",
]
