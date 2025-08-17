"""PDF Knowledgebase MCP Server

A Model Context Protocol server for managing PDF documents with vector search capabilities.
"""

__version__ = "0.5.0"

from .config import ServerConfig

# Core components
from .document_processor import DocumentProcessor  # Backward compatibility
from .document_processor import DocumentProcessor as PDFProcessor
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
from .vector_store import VectorStore

# Web server integration
from .web_server import IntegratedPDFKnowledgebaseServer, run_integrated_server, run_web_only_server

__all__ = [
    # Version
    "__version__",
    # Core server and configuration
    "PDFKnowledgebaseServer",
    "ServerConfig",
    # Web server integration
    "IntegratedPDFKnowledgebaseServer",
    "run_integrated_server",
    "run_web_only_server",
    # Data models
    "Document",
    "Chunk",
    "SearchResult",
    "SearchQuery",
    "ProcessingResult",
    # Core components
    "DocumentProcessor",
    "PDFProcessor",  # Backward compatibility
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
