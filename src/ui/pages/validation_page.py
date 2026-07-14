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
from src.ui.theme import (LEFT_PANEL_PADX,LEFT_PANEL_PADY,
                          RIGHT_PANEL_PADX,RIGHT_PANEL_PADY,
                          LABEL_PADX, ENTRY_PADX, ENTRY_PADY,
                          COMBOBOX_PADX, COMBOBOX_PADY,
                          TEXTBOX_PADX, TEXTBOX_PADY,
                          TEXTBOX_HEIGHT, BUTTON_PADY,
                          BUTTON_PADY_END, ACTION_BUTTON_PADX,
                          RESULT_TITLE_FONT,SECTION_TITLE_PADY,
                          RESULT_TITLE_PADX, RESULT_TITLE_PADY,
                          RESULT_PANEL_PADX, RESULT_PANEL_PADY
                          )


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
        self.left_panel.grid(row=0,column=0,sticky="nsew",padx=LEFT_PANEL_PADX,pady=LEFT_PANEL_PADY)

        # Right workspace panel
        self.right_panel = ctk.CTkFrame(self)
        self.right_panel.grid(row=0,column=1,sticky="nsew",padx=RIGHT_PANEL_PADX,pady=RIGHT_PANEL_PADY)

    # -------------------------
    # Left Panel
    # -------------------------

    def create_left_panel(self):
        """Build the validation controls."""

        self.left_panel.grid_columnconfigure(0, weight=1)

        self.create_sequence_selector()
        self.create_action_buttons()
        self.create_input_section()

    def create_label(self, parent, text):
        """Create a standard form label."""

        label = ctk.CTkLabel(parent, text=text)
        label.pack(anchor="w", padx=LABEL_PADX)

        return label

    def create_entry(self, parent, placeholder):
        """Create and pack a standard entry widget."""

        entry = ctk.CTkEntry(parent,
                             placeholder_text=placeholder)

        entry.pack(fill="x",padx=ENTRY_PADX,pady=ENTRY_PADY)

        return entry

    def create_button(self, parent, text, command=None, pady=BUTTON_PADY):
        """Create and pack a standard button."""

        button = ctk.CTkButton(parent,
                               text=text,
                               command=command)

        button.pack(fill="x",padx=ACTION_BUTTON_PADX,pady=pady)

        return button

    def create_combobox(self, parent, values):
        """Create and pack a standard combobox."""

        combobox = ctk.CTkComboBox(parent,
                                   values=values)

        combobox.pack(fill="x",padx=COMBOBOX_PADX,pady=COMBOBOX_PADY)

        return combobox

    def create_textbox(self, parent, height):
        """Create and pack a standard textbox."""

        textbox = ctk.CTkTextbox(parent,
                                 height=height)

        textbox.pack(fill="both",expand=True,padx=TEXTBOX_PADX,pady=TEXTBOX_PADY)

        return textbox

    def create_sequence_selector(self):
        """Build the sequence selection controls."""

        title = ctk.CTkLabel(self.left_panel,
                             text="Sequence Validation",
                             font=RESULT_TITLE_FONT)

        title.pack(pady=SECTION_TITLE_PADY)

        self.create_label(self.left_panel, "Loaded Sequences")

        self.sequence_selector = self.create_combobox(
            self.left_panel,
            ["No sequences loaded"]
        )

    def create_action_buttons(self):
        """Load FASTA, Validate and Validate All buttons."""

        self.load_button = self.create_button(
            self.left_panel,
            "Load FASTA",
            command=self.load_fasta
        )

        self.validate_button = self.create_button(
            self.left_panel,
            "Validate",
            command=self.process_input
        )

        self.validate_all_button = self.create_button(
            self.left_panel,
            "Validate All",
            pady=BUTTON_PADY_END
        )

    def create_input_section(self):
        """Sequence name and sequence input."""

        self.create_label(self.left_panel, "Sequence Name")

        self.name_entry = self.create_entry(
            self.left_panel,
            "Enter sequence name"
        )

        self.create_label(self.left_panel, "Sequence Input")

        self.sequence_text = self.create_textbox(
            self.left_panel,
            TEXTBOX_HEIGHT
        )


    # -------------------------
    # Right Panel
    # -------------------------

    def create_right_panel(self):
        """Build the results workspace."""

        self.right_panel.grid_columnconfigure(0, weight=1)
        self.right_panel.grid_rowconfigure(1, weight=1)

        self.create_result_title("Validation Results")
        self.create_result_box()

    def create_result_title(self, text):
        """Create the results panel title."""

        title = ctk.CTkLabel(self.right_panel,
                             text=text,
                             font=RESULT_TITLE_FONT)

        title.grid(row=0, column=0, padx=RESULT_TITLE_PADX, pady=RESULT_TITLE_PADY, sticky="w")

        return title

    def create_result_box(self):
        """Create the results textbox."""

        self.result_box = ctk.CTkTextbox(self.right_panel)

        self.result_box.grid(row=1,column=0,sticky="nsew",padx=RESULT_PANEL_PADX,pady=RESULT_PANEL_PADY)

        return self.result_box

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