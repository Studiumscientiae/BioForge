"""
export_service.py

Export coordination service for BioForge.

Responsibilities:
- Receive export requests.
- Coordinate export operations.
- Return export status.

Does not perform:
- GUI operations
- Biological analysis
- Sequence validation
- File parsing
- History management
- Export formatting
"""

import customtkinter as ctk

class ExportService(ctk.CTkFrame):
    """
    empty yet
    """

    def __init__(self, parent):
        super().__init__(parent)