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
from src.ui import theme

from src.analysis.analysis_service import AnalysisService
from src.core.sequence import Sequence

from src.ui.factories.analysis_factory import AnalysisFactory
from src.ui.factories.ui_factory import UIFactory
from src.ui.factories.widget_factory import WidgetFactory

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
        self.left_panel = WidgetFactory.create_frame(self)
        self.left_panel.grid(row=0,column=0,sticky="nsew",padx=theme.LEFT_PANEL_PADX,pady=theme.LEFT_PANEL_PADY)

        # Right workspace panel
        self.right_panel = WidgetFactory.create_frame(self)
        self.right_panel.grid(row=0,column=1,sticky="nsew",padx=theme.RIGHT_PANEL_PADX,pady=theme.RIGHT_PANEL_PADY)

    # -------------------------
    # Left Panel
    # -------------------------

    def create_left_panel(self):
        """Build the analysis controls."""

        self.left_panel.grid_columnconfigure(0, weight=1)

        # Statistics
        self.statistics_frame, statistics = (
            AnalysisFactory.create_statistics_section(
                self.left_panel
            )
        )

        self.statistics_frame.pack(
            fill="x",
            padx=theme.FRAME_PADX,
            pady=theme.FRAME_TOP_PADY,
        )

        self.length_checkbox = statistics["length"]
        self.gc_checkbox = statistics["gc"]
        self.nucleotide_checkbox = statistics["nucleotide"]
        self.weight_checkbox = statistics["weight"]

        # Sequence Transformations
        self.sequence_operations_frame, operations = (
            AnalysisFactory.create_sequence_operations_section(
                self.left_panel
            )
        )

        self.sequence_operations_frame.pack(
            fill="x",
            padx=theme.FRAME_PADX,
            pady=theme.FRAME_PADY,
        )

        self.reverse_checkbox = operations["reverse"]
        self.complement_checkbox = operations["complement"]
        self.reverse_complement_checkbox = operations["reverse_complement"]

        # Central Dogma
        self.central_dogma_frame, dogma = (
            AnalysisFactory.create_central_dogma_section(
                self.left_panel
            )
        )

        self.central_dogma_frame.pack(
            fill="x",
            padx=theme.FRAME_PADX,
            pady=theme.FRAME_PADY,
        )

        self.transcription_checkbox = dogma["transcription"]
        self.translation_checkbox = dogma["translation"]
        self.codon_usage_checkbox = dogma["codon_usage"]
        self.codon_frequency_checkbox = dogma["codon_frequency"]

        # Analyze Button
        self.analyze_button = AnalysisFactory.create_action_section(
            self.left_panel,
            command=self.run_analysis,
        )

    # -------------------------
    # Right Panel
    # -------------------------

    def create_right_panel(self):
        """Build the analysis results workspace."""

        self.right_panel.grid_columnconfigure(0, weight=2)
        self.right_panel.grid_rowconfigure(1, weight=2)

        panel, _, self.result_panel = UIFactory.create_result_panel(self.right_panel,
                                                                    title="Analysis Results",)

        panel.grid(row=0,column=0,rowspan=2,sticky="nsew",padx=theme.RESULT_PANEL_PADX,pady=theme.RESULT_PANEL_PADY)

    # -------------------------
    # Event Handlers
    # -------------------------

    def run_analysis(self):
        """Run the selected analyses."""

        if self.current_sequence is None:
            self.display_results("No sequence available for analysis.")
            return

        results = []

        self.analyze_statistics(results)
        self.analyze_sequence_operations(results)
        self.analyze_central_dogma(results)

        if not results:
            self.display_results("Please select at least one analysis.")
            return

        self.display_results("\n".join(results))

    # -------------------------
    # Analysis Methods
    # -------------------------

    def analyze_statistics(self, results: list[str]):
        """Run selected statistical analyses."""

        # Sequence Length
        if self.length_checkbox.get():
            length = self.analysis_service.sequence_length(
                self.current_sequence
            )

            self.append_result(results,
                "Sequence Length",
                f"{length} nt",
            )

        # GC Content
        if self.gc_checkbox.get():
            gc = self.analysis_service.gc_content(
                self.current_sequence
            )

            self.append_result(results,
                "GC Content",
                f"{gc:.2f} %",
            )

        # Nucleotide Counts
        if self.nucleotide_checkbox.get():
            counts = self.analysis_service.base_counts(self.current_sequence)

            self.add_section(results, "Nucleotide Counts")

            for base, count in counts.items():
                results.append(f"{base}: {count}")

            results.append("")

        # Molecular Weight
        if self.weight_checkbox.get():
            weight = self.analysis_service.molecular_weight(
                self.current_sequence
            )

            self.append_result(results,
                "Molecular Weight",
                f"{weight:.2f} Da",
            )

    def analyze_sequence_operations(self,results: list[str],):
        """Run selected sequence transformations."""

        pass

    def analyze_central_dogma(self,results: list[str],):
        """Run selected Central Dogma analyses."""

        pass

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

    def append_result(self,results: list[str],title: str,value: str,):
        """Append a formatted analysis result."""

        self.add_section(results, title)
        results.append(value)
        results.append("")