"""
about_dialog.py

About dialog for BioForge.

Responsibilities:
- Display application information.
- Display version information.
- Display project information.

Does not perform:
- Biological analysis
- Sequence validation
- File parsing
- Exporting
- History management
"""

import customtkinter as ctk

class AboutDialog(ctk.CTkToplevel):
    """
    empty yet
    """

    def __init__(self, parent):
        super().__init__(parent)