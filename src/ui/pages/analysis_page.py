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

        # Panels
        self.left_panel = None
        self.right_panel = None

        # Statistics section
        self.statistics_frame = None

        # Sequence Operations section
        self.sequence_operations_frame = None

        # Gene Expression section
        self.central_dogma_frame = None

        # Action widgets
        self.analyze_button = None

        # Statistics
        self.length_checkbox = None
        self.gc_checkbox = None
        self.nucleotide_checkbox = None
        self.weight_checkbox = None

        # Transformations
        self.reverse_checkbox = None
        self.complement_checkbox = None
        self.reverse_complement_checkbox = None

        # Central Dogma
        self.transcription_checkbox = None
        self.translation_checkbox = None
        self.codon_usage_checkbox = None
        self.codon_frequency_checkbox = None

        # Results
        self.result_panel = None

        self.create_layout()
        self.create_left_panel()
        self.create_right_panel()

    # -------------------------
    # Layout
    # -------------------------

    def create_layout(self):
        """Create the analysis workspace layout."""

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
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
        """Build the analysis controls."""

        self.left_panel.grid_columnconfigure(0, weight=1)

        self.create_statistics_section()
        self.create_sequence_operations_section()
        self.create_central_dogma_section()
        self.create_action_section()

    def create_statistics_section(self):
        """Build the statistics tools."""

        self.statistics_frame = ctk.CTkFrame(self.left_panel)
        self.statistics_frame.pack(fill="x", padx=15, pady=(15, 10))

        title = ctk.CTkLabel(self.statistics_frame,
                             text="Statistics",
                             font=("Arial", 16, "bold"))

        title.pack(anchor="w", padx=10, pady=(10, 5))

        self.length_checkbox = ctk.CTkCheckBox(self.statistics_frame,
                                               text="Sequence Length")

        self.length_checkbox.pack(anchor="w", padx=15, pady=2)

        self.gc_checkbox = ctk.CTkCheckBox(self.statistics_frame,
                                           text="GC Content")

        self.gc_checkbox.pack(anchor="w", padx=15, pady=2)

        self.nucleotide_checkbox = ctk.CTkCheckBox(self.statistics_frame,
                                                   text="Nucleotide Count")

        self.nucleotide_checkbox.pack(anchor="w", padx=15, pady=2)

        self.weight_checkbox = ctk.CTkCheckBox(self.statistics_frame,
                                               text="Molecular Weight")

        self.weight_checkbox.pack(anchor="w", padx=15, pady=(2, 10))

    def create_sequence_operations_section(self):
        """Build sequence operation tools."""

        self.sequence_operations_frame = ctk.CTkFrame(self.left_panel)
        self.sequence_operations_frame.pack(fill="x", padx=15, pady=10)

        title = ctk.CTkLabel(self.sequence_operations_frame,
                             text="Sequence Transformations",
                             font=("Arial", 16, "bold"))

        title.pack(anchor="w", padx=10, pady=(10, 5))

        self.reverse_checkbox = ctk.CTkCheckBox(self.sequence_operations_frame,
                                                text="Reverse")

        self.reverse_checkbox.pack(anchor="w", padx=15, pady=2)

        self.complement_checkbox = ctk.CTkCheckBox(self.sequence_operations_frame,
                                                   text="Complement")

        self.complement_checkbox.pack(anchor="w", padx=15, pady=2)

        self.reverse_complement_checkbox = ctk.CTkCheckBox(self.sequence_operations_frame,
                                                           text="Reverse Complement")

        self.reverse_complement_checkbox.pack(anchor="w", padx=15, pady=2)

    def create_central_dogma_section(self):
        """Build Central Dogma analysis tools."""

        self.central_dogma_frame = ctk.CTkFrame(self.left_panel)
        self.central_dogma_frame.pack(fill="x", padx=15, pady=10)

        title = ctk.CTkLabel(self.central_dogma_frame,
                             text="Central Dogma",
                             font=("Arial", 16, "bold"))

        title.pack(anchor="w", padx=10, pady=(10, 5))

        self.transcription_checkbox = ctk.CTkCheckBox(self.central_dogma_frame,
                                                      text="RNA Transcription")

        self.transcription_checkbox.pack(anchor="w", padx=15, pady=2)

        self.translation_checkbox = ctk.CTkCheckBox(self.central_dogma_frame,
                                                    text="Protein Translation")

        self.translation_checkbox.pack(anchor="w", padx=15, pady=2)

        self.codon_usage_checkbox = ctk.CTkCheckBox(self.central_dogma_frame,
                                                    text="Codon Usage")

        self.codon_usage_checkbox.pack(anchor="w", padx=15, pady=2)

        self.codon_frequency_checkbox = ctk.CTkCheckBox(self.central_dogma_frame,
                                                        text="Codon Frequency")

        self.codon_frequency_checkbox.pack(anchor="w", padx=15, pady=(2, 10))



    def create_action_section(self):
        """Build analysis action controls."""

        self.analyze_button = ctk.CTkButton(self.left_panel,
                                            text="Analyze",
                                            command=self.run_analysis)

        self.analyze_button.pack(fill="x",padx=15,pady=(15, 15))

    # -------------------------
    # Right Panel
    # -------------------------

    def create_right_panel(self):
        """Build the analysis results workspace."""

        self.right_panel.grid_columnconfigure(0, weight=1)
        self.right_panel.grid_rowconfigure(1, weight=1)

        title = ctk.CTkLabel(self.right_panel,
                             text="Analysis Results",
                             font=("Arial", 20, "bold"))

        title.grid(row=0,column=0,padx=15,pady=(15, 10),sticky="w")

        self.result_panel = ctk.CTkTextbox(self.right_panel)

        self.result_panel.grid(row=1,column=0,sticky="nsew",padx=15,pady=(0, 15))

    # -------------------------
    # Event Handlers
    # -------------------------

    def run_analysis(self):
        """Run the selected analyses."""

        self.display_results(
            "Analysis functionality will be available in v0.4.2.")

    # -------------------------
    # Utility Methods
    # -------------------------

    def display_results(self, text):
        """Display analysis results."""
        self.result_panel.delete("1.0", "end")
        self.result_panel.insert("1.0", text)
