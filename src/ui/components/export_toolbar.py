"""
export toolbar.py

Export toolbar component for BioForge.

Responsibilities:
- Display export controls.
- Provide export actions.
- Forward export results.

Does not perform:
- Biological analysis
- Sequence validation
- File parsing
- Exporting
- History management
"""

import customtkinter as ctk

class ExportToolbar(ctk.CTkFrame):
    """
    empty yet
    """

    def __init__(self, parent):
        super().__init__(parent)