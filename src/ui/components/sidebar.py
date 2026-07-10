"""
sidebar.py

Sidebar navigation component for BioForge.

Responsibilities:
- Display navigation buttons.
- Switch application pages.
- Support sidebar expansion and collapse.

Does not perform:
- Biological sequence
- Sequence validation
- File parsing
- Exporting
- History management
"""

import customtkinter as ctk

class Sidebar(ctk.CTkFrame):
    """
    empty yet
    """

    def __init__(self, parent):
        super().__init__(parent)