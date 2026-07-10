"""
analysis_page.py

Analysis workspace page for BioForge.

Responsibilities:
- Arrange analysis workspace components.
- Display the analysis workspace.
- Forward user interactions to the application controller.

Does not perform:
- Biological analysis
- Sequence validation
- File parsing
- Exporting
- History management
"""

import customtkinter as ctk

class AnalysisPage(ctk.CTkFrame):
    """
    Analysis workspace for BioForge.
    """

    def __init__(self, parent):
        super().__init__(parent)