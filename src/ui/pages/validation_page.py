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
from src.main import process_sequence, load_sequences

class ValidationPage(ctk.CTkFrame):

    def __init__(self, parent):
        super().__init__(parent)

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
        self.left_panel.grid(row=0,column=0,sticky="nsew",padx=(10, 5),pady=10)

        # Right workspace panel
        self.right_panel = ctk.CTkFrame(self)
        self.right_panel.grid(row=0,column=1,sticky="nsew",padx=(5, 10),pady=10)

    # -------------------------
    # Left Panel
    # -------------------------

    def create_left_panel(self):
        """Build the validation controls."""

        self.left_panel.grid_columnconfigure(0, weight=1)

        self.create_sequence_selector()
        self.create_action_buttons()
        self.create_input_section()

    def create_sequence_selector(self):
        """Loaded sequence selector."""

        title = ctk.CTkLabel(self.left_panel,
                             text="Sequence Validation",
                             font=("Arial", 20, "bold"))

        title.pack(pady=(15, 10))

        loaded_label = ctk.CTkLabel(self.left_panel,
                                    text="Loaded Sequences")

        loaded_label.pack(anchor="w", padx=15)

        self.sequence_selector = ctk.CTkComboBox(self.left_panel,
                                                 values=["No sequences loaded"])

        self.sequence_selector.pack(fill="x", padx=15, pady=(5, 20))

    def create_action_buttons(self):
        """Load FASTA, Validate and Validate All buttons."""

        self.load_button = ctk.CTkButton(self.left_panel,
                                         text="Load FASTA",
                                         command=self.load_fasta)

        self.load_button.pack(fill="x", padx=15, pady=5)

        self.validate_button = ctk.CTkButton(self.left_panel,
                                             text="Validate",
                                             command=self.process_input)

        self.validate_button.pack(fill="x", padx=15, pady=5)

        self.validate_all_button = ctk.CTkButton(self.left_panel,
                                                 text="Validate All")

        self.validate_all_button.pack(fill="x", padx=15, pady=(5, 20))

    def create_input_section(self):
        """Sequence name and sequence input."""

        name_label = ctk.CTkLabel(self.left_panel,
                                  text="Sequence Name")

        name_label.pack(anchor="w", padx=15)

        self.name_entry = ctk.CTkEntry(self.left_panel,
                                       placeholder_text="Enter sequence name")

        self.name_entry.pack(fill="x", padx=15, pady=(5, 15))

        sequence_label = ctk.CTkLabel(self.left_panel,
                                      text="Sequence Input")

        sequence_label.pack(anchor="w", padx=15)

        self.sequence_text = ctk.CTkTextbox(self.left_panel,
                                            height=250)

        self.sequence_text.pack(fill="both",expand=True,padx=15,pady=(5, 15))


    # -------------------------
    # Right Panel
    # -------------------------

    def create_right_panel(self):
        """Build the results workspace."""

        self.right_panel.grid_columnconfigure(0, weight=1)
        self.right_panel.grid_rowconfigure(1, weight=1)

        title = ctk.CTkLabel(self.right_panel,
                             text="Validation Results",
                             font=("Arial", 20, "bold"))

        title.grid(row=0, column=0, padx=15, pady=(15, 10), sticky="w")

        self.result_box = ctk.CTkTextbox(self.right_panel)

        self.result_box.grid(row=1,column=0,sticky="nsew",padx=15,pady=(0, 15))

    # -------------------------
    # Event Handlers
    # -------------------------

    def process_input(self):
        """Validate the current sequence."""

        name=self.name_entry.get()
        sequence=self.sequence_text.get("1.0","end-1c")

        try:
            result=process_sequence(name, sequence)

            self.display_result(str(result))

        except ValueError as error:
            self.display_result(str(error))

    def load_fasta(self):
        """Load sequences from a FASTA file."""

        file_path = filedialog.askopenfilename(
            title="Open FASTA file",
            filetypes=[
                ("FASTA files", "*.fasta *.fa *.fna"),
                ("All files", "*.*")
            ]
        )
        if not file_path:
            return

        try:
            sequences = load_sequences(file_path)

            results = ""

            results = "\n\n".join(str(sequence) for sequence in sequences)
            self.display_result(results)

        except ValueError as error:
            self.display_result(str(error))

    # -------------------------
    # Utility Methods
    # -------------------------

    def display_result(self, text):
        """Display results."""

        self.result_box.delete("1.0","end")
        self.result_box.insert("1.0", text)

if __name__ == "__main__":
    app = ctk.CTk()
    app.geometry("1200x700")

    page = ValidationPage(app)
    page.pack(fill="both", expand=True)

    app.mainloop()