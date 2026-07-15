"""
validation_page.py

Sequence validation page for BioForge.

Responsibilities:
- Display validation interface.
- Collect user input.
- Display validation results.
- Forward validation requests to the application controller.

Does not perform:
- Sequence validation
- Biological analysis
- File parsing
- Exporting
- History management
"""

import customtkinter as ctk
from tkinter import filedialog

from src.ui.factories.ui_factory import UIFactory
from src.ui.factories.validation_factory import ValidationFactory

from src.ui import theme


class ValidationPage(ctk.CTkFrame):

    def __init__(self, parent, validate_callback, load_fasta_callback):
        super().__init__(parent)

        self.validate_callback = validate_callback
        self.load_fasta_callback = load_fasta_callback

        # Panels
        self.left_panel = None
        self.right_panel = None

        # Left panel widgets
        self.sequence_selector = None
        self.load_button = None
        self.validate_button = None
        self.validate_all_button = None
        self.name_entry = None
        self.sequence_text = None

        # Right panel widgets
        self.result_box = None

        self.create_layout()
        self.create_left_panel()
        self.create_right_panel()

    # -------------------------
    # Layout
    # -------------------------

    def create_layout(self):
        """Create the workspace layout."""

        # Page expands with the application
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=2)

        # Left workspace panel
        self.left_panel = ctk.CTkFrame(self)
        self.left_panel.grid(row=0,column=0,sticky="nsew",padx=theme.LEFT_PANEL_PADX,pady=theme.LEFT_PANEL_PADY)

        # Right workspace panel
        self.right_panel = ctk.CTkFrame(self)
        self.right_panel.grid(row=0,column=1,sticky="nsew",padx=theme.RIGHT_PANEL_PADX,pady=theme.RIGHT_PANEL_PADY)

    # -------------------------
    # Left Panel
    # -------------------------

    def create_left_panel(self):
        """Build the validation controls."""

        self.left_panel.grid_columnconfigure(0, weight=1)

        selector_frame, selector = (
            ValidationFactory.create_sequence_selector(
                self.left_panel
            )
        )

        selector_frame.pack(
            fill="x",
            padx=theme.FRAME_PADX,
            pady=theme.FRAME_TOP_PADY,
        )

        self.sequence_selector = selector["selector"]

        (
            self.load_button,
            self.validate_button,
            self.validate_all_button,
        ) = ValidationFactory.create_action_section(
            self.left_panel,
            load_callback=self.load_fasta,
            validate_callback=self.process_input,
        )

        (
            self.name_entry,
            self.sequence_text,
        ) = ValidationFactory.create_input_section(
            self.left_panel,
        )


    # -------------------------
    # Right Panel
    # -------------------------

    def create_right_panel(self):
        """Build the validation results workspace."""

        self.right_panel.grid_columnconfigure(0, weight=1)
        self.right_panel.grid_rowconfigure(1, weight=1)

        panel, _, self.result_box = UIFactory.create_result_panel(
            self.right_panel,
            title="Validation Results",
        )

        panel.grid(
            row=0,
            column=0,
            rowspan=2,
            sticky="nsew",
            padx=theme.RESULT_PANEL_PADX,
            pady=theme.RESULT_PANEL_PADY,
        )


    # -------------------------
    # Event Handlers
    # -------------------------

    def process_input(self):
        """Forward validation request to the application controller."""

        name = self.name_entry.get()
        sequence = self.sequence_text.get("1.0", "end-1c")

        self.validate_callback(name, sequence)

    def load_fasta(self):
        """Forward FASTA loading request to the application controller."""

        file_path = filedialog.askopenfilename(
            title="Open FASTA file",
            filetypes=[
                ("FASTA files", "*.fasta *.fa *.fna"),
                ("All files", "*.*")
            ]
        )

        if not file_path:
            return

        self.load_fasta_callback(file_path)

    # -------------------------
    # Utility Methods
    # -------------------------

    def display_result(self, text):
        """Display results."""

        self.result_box.delete("1.0","end")
        self.result_box.insert("1.0", text)