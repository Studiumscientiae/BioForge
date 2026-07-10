"""
history_service.py

History coordination service for BioForge.

Responsibilities:
- Receive history requests.
- Manage analysis sessions.
- Provide stored history.

Does not perform:
- GUI operations
- Biological analysis
- Sequence validation
- File parsing
- Exporting
- History presentation
"""

import customtkinter as ctk

class HistoryService(ctk.CTkFrame):
    """
    empty yet
    """

    def __init__(self, parent):
        super().__init__(parent)