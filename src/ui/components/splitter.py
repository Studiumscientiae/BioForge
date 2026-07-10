"""
splitter.py

Reusable pane splitter component for BioForge.

Responsibilities:
- Resize interface panes.
- Separate workspace components.
- Support pane expansion and collapse

Does not perform:
- Biological analysis
- Sequence validation
- File parsing
- Exporting
- History management
"""

import customtkinter as ctk

class Splitter(ctk.CTkFrame):
    """
    empty yet
    """

    def __init__(self, parent):
        super().__init__(parent)