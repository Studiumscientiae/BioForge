"""
export_dialog.py

Export dialog for BioForge.

Responsibilities:
- Collect export options.
- Collect export destination.
- Confirm export settings.

Does not perform:
- Biological analysis
- Sequence validation
- File parsing
- Exporting
- History management
"""

import customtkinter as ctk

class ExportDialog(ctk.CTkToplevel):
    """
    empty yet
    """

    def __init__(self, parent):
        super().__init__(parent)