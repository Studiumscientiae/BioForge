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
from src.ui.theme import (CHECKBOX_PADX, CHECKBOX_PADY,
                          LEFT_PANEL_PADX, LEFT_PANEL_PADY,
                          RIGHT_PANEL_PADX, RIGHT_PANEL_PADY,
                          CHECKBOX_PADY_END, ACTION_BUTTON_PADX,
                          ACTION_BUTTON_PADY, RESULT_PANEL_PADX,
                          RESULT_PANEL_PADY, RESULT_TITLE_PADY,
                          RESULT_TITLE_PADX, SECTION_TITLE_FONT,
                          RESULT_TITLE_FONT, FRAME_PADY, FRAME_PADX,
                          SECTION_TITLE_PADX, SECTION_TITLE_PADY, FRAME_TOP_PADY)

from src.analysis.analysis_service import AnalysisService
from src.core.sequence import Sequence

class AnalysisPage(ctk.CTkFrame):
    """
    Analysis workspace for BioForge.
    """

    def __init__(self, parent, analysis_service: AnalysisService):
        super().__init__(parent)

        self.analysis_service = analysis_service
        self.current_sequence = None

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
        self.left_panel.grid(row=0,column=0,sticky="nsew",padx=LEFT_PANEL_PADX,pady=LEFT_PANEL_PADY)

        # Right workspace panel
        self.right_panel = ctk.CTkFrame(self)
        self.right_panel.grid(row=0,column=1,sticky="nsew",padx=RIGHT_PANEL_PADX,pady=RIGHT_PANEL_PADY)

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

    def create_checkbox(self, parent, text, pady=CHECKBOX_PADY):
        """Create and pack a standard analysis checkbox."""

        checkbox = ctk.CTkCheckBox(parent, text=text)
        checkbox.pack(
            anchor="w",
            padx=CHECKBOX_PADX,
            pady=pady
        )
        return checkbox

    def create_section(self, title_text, pady):
        """Create a titled analysis section in the left panel."""

        frame = ctk.CTkFrame(self.left_panel)
        frame.pack(fill="x", padx=FRAME_PADX, pady=pady)

        title = ctk.CTkLabel(frame,
                             text=title_text,
                             font=SECTION_TITLE_FONT)

        title.pack(anchor="w",padx=SECTION_TITLE_PADX,pady=SECTION_TITLE_PADY)

        return frame

    def create_statistics_section(self):
        """Build the statistics tools."""

        self.statistics_frame = self.create_section("Statistics",FRAME_TOP_PADY)

        self.length_checkbox = self.create_checkbox(self.statistics_frame,
                                                    text="Sequence Length")

        self.gc_checkbox = self.create_checkbox(self.statistics_frame,
                                           text="GC Content")

        self.nucleotide_checkbox = self.create_checkbox(self.statistics_frame,
                                                   text="Nucleotide Counts")

        self.weight_checkbox = self.create_checkbox(self.statistics_frame,
                                               "Molecular Weight",CHECKBOX_PADY_END)

    def create_sequence_operations_section(self):
        """Build sequence operation tools."""

        self.sequence_operations_frame = self.create_section("Sequence Transformations", FRAME_PADY)

        self.reverse_checkbox = self.create_checkbox(self.sequence_operations_frame,
                                                text="Reverse")

        self.complement_checkbox = self.create_checkbox(self.sequence_operations_frame,
                                                   text="Complement")

        self.reverse_complement_checkbox = self.create_checkbox(self.sequence_operations_frame,
                                                           "Reverse Complement",CHECKBOX_PADY_END)

    def create_central_dogma_section(self):
        """Build Central Dogma analysis tools."""

        self.central_dogma_frame = self.create_section("Central Dogma", FRAME_PADY)

        self.transcription_checkbox = self.create_checkbox(self.central_dogma_frame,
                                                      text="RNA Transcription")

        self.translation_checkbox = self.create_checkbox(self.central_dogma_frame,
                                                    text="Protein Translation")

        self.codon_usage_checkbox = self.create_checkbox(self.central_dogma_frame,
                                                    text="Codon Usage")

        self.codon_frequency_checkbox = self.create_checkbox(self.central_dogma_frame,
                                                        "Codon Frequency", CHECKBOX_PADY_END)

    def create_action_section(self):
        """Build analysis action controls."""

        self.analyze_button = ctk.CTkButton(self.left_panel,
                                            text="Analyze",
                                            command=self.run_analysis)

        self.analyze_button.pack(fill="x",padx=ACTION_BUTTON_PADX,pady=ACTION_BUTTON_PADY)

    # -------------------------
    # Right Panel
    # -------------------------

    def create_right_panel(self):
        """Build the analysis results workspace."""

        self.right_panel.grid_columnconfigure(0, weight=2)
        self.right_panel.grid_rowconfigure(1, weight=2)

        title = ctk.CTkLabel(self.right_panel,
                             text="Analysis Results",
                             font=RESULT_TITLE_FONT)

        title.grid(row=0,column=0,padx=RESULT_TITLE_PADX,pady=RESULT_TITLE_PADY,sticky="w")

        self.result_panel = ctk.CTkTextbox(self.right_panel)

        self.result_panel.grid(row=1,column=0,sticky="nsew",padx=RESULT_PANEL_PADX,pady=RESULT_PANEL_PADY)

    # -------------------------
    # Event Handlers
    # -------------------------

    def run_analysis(self):
        """Run the selected analyses."""

        if self.current_sequence is None:
            self.display_results("No sequence available for analysis.")
            return

        results = []

        # Sequence Length
        if self.length_checkbox.get():
            length = self.analysis_service.sequence_length(self.current_sequence)
            self.add_section(results, "Sequence Length")
            results.append(f"{length} nt")
            results.append("")

        # GC Content
        if self.gc_checkbox.get():
            gc = self.analysis_service.gc_content(self.current_sequence)
            self.add_section(results, "GC Content")
            results.append(f"{gc:.2f} %")
            results.append("")

        # Base Counts
        if self.nucleotide_checkbox.get():
            counts = self.analysis_service.base_counts(self.current_sequence)

            self.add_section(results, "Nucleotide Counts")

            for base, count in counts.items():
                results.append(f"{base} : {count}")
            results.append("")

            # Molecular Weight
            if self.weight_checkbox.get():
                weight = self.analysis_service.molecular_weight(
                    self.current_sequence
                )

                self.add_section(results, "Molecular Weight")
                results.append(f"{weight:.2f} Da")
                results.append("")

        if not results:
            self.display_results("Please select at least one analysis.")
            return

        self.display_results("\n".join(results))


    # -------------------------
    # Utility Methods
    # -------------------------

    def set_sequence(self, sequence: Sequence):
        """Set the current sequence for analysis."""

        self.current_sequence = sequence

    def display_results(self, text: str):
        """Display analysis results."""

        self.result_panel.delete("1.0", "end")
        self.result_panel.insert("1.0", text)

    def add_section(self, results: list[str], title: str):
        """Append a titled results section."""

        results.append(title)
        results.append("-" * len(title))