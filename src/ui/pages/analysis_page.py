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
from src.services.codon_usage_service import CodonUsageService
from src.core.sequence import Sequence

from src.ui.factories.analysis_factory import AnalysisFactory
from src.ui.factories.ui_factory import UIFactory
from src.ui.factories.widget_factory import WidgetFactory

class AnalysisPage(ctk.CTkFrame):
    """
    Analysis workspace for BioForge.
    """

    def __init__(self, parent, analysis_service: AnalysisService,codon_usage_service: CodonUsageService):
        super().__init__(parent)

        self.analysis_service = analysis_service
        self.codon_usage_service = codon_usage_service
        self.current_sequence = None

        # Panels
        self.left_panel = None
        self.right_panel = None

        # Statistics section
        self.statistics_frame = None

        # Sequence Operations section
        self.sequence_operations_frame = None

        # Gene Expression section
        self.gene_expression_frame = None

        # Codon Analysis Frame
        self.codon_analysis_frame = None

        # Action widgets
        self.analyze_button = None

        # Statistics
        self.length_checkbox = None
        self.gc_checkbox = None
        self.at_checkbox = None
        self.nucleotide_checkbox = None
        self.weight_checkbox = None

        # Transformations
        self.reverse_checkbox = None
        self.complement_checkbox = None
        self.reverse_complement_checkbox = None

        # Gene Expression
        self.transcription_checkbox = None
        self.translation_checkbox = None

        # Codon analysis
        self.codon_usage_checkbox = None
        self.codon_frequency_checkbox = None
        self.organism_selector = None

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
        self.left_panel = WidgetFactory.create_scrollable_frame(self)
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
        self.at_checkbox = statistics["at"]
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

        # Gene Expression
        self.gene_expression_frame, gene = (
            AnalysisFactory.create_gene_expression_section(
                self.left_panel
            )
        )

        self.gene_expression_frame.pack(
            fill="x",
            padx=theme.FRAME_PADX,
            pady=theme.FRAME_PADY,
        )

        self.transcription_checkbox = gene["transcription"]
        self.translation_checkbox = gene["translation"]

        # Codon Analysis
        (
            self.codon_analysis_frame,
            codon,
            self.organism_selector,
        ) = AnalysisFactory.create_codon_analysis_section(
            self.left_panel
        )

        organisms = self.codon_usage_service.list_organisms()

        if organisms:
            self.organism_selector.configure(values=organisms)
            self.organism_selector.set(organisms[0])
        else:
            self.organism_selector.configure(values=["No datasets found"])
            self.organism_selector.set("No datasets found")

        self.codon_analysis_frame.pack(
            fill="x",
            padx=theme.FRAME_PADX,
            pady=theme.FRAME_PADY,
        )

        self.codon_frequency_checkbox = codon["codon_frequency"]
        self.codon_usage_checkbox = codon["codon_usage"]

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
        self.analyze_gene_expression(results)
        self.analyze_codon_analysis(results)

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
            length = self.analysis_service.get_sequence_length(
                self.current_sequence
            )

            self.append_result(results,
                "Sequence Length",
                f"{length} bp",
            )

        # GC Content
        if self.gc_checkbox.get():
            gc = self.analysis_service.get_gc_content(
                self.current_sequence
            )

            self.append_result(results,
                "GC Content",
                f"{gc:.2f} %",
            )

        # AT Content
        if self.at_checkbox.get():
            at = self.analysis_service.get_at_content(
                self.current_sequence
            )

            self.append_result(results,
                "AT Content",
                f"{at:.2f} %",
            )

        # Nucleotide Counts
        if self.nucleotide_checkbox.get():
            counts = self.analysis_service.get_base_counts(self.current_sequence)

            self.add_section(results, "Nucleotide Counts")

            for base, count in counts.items():
                results.append(f"{base:<2}: {count}")

            results.append("")

        # Molecular Weight
        if self.weight_checkbox.get():
            weight = self.analysis_service.get_molecular_weight(
                self.current_sequence
            )

            self.append_result(results,
                "Molecular Weight",
                f"{weight:,.2f} Da",
            )

    def analyze_sequence_operations(self,results: list[str],):
        """Run selected sequence transformations."""

        if self.reverse_checkbox.get():
            reverse = self.analysis_service.get_reverse(
                self.current_sequence
            )

            self.append_result(results,
                "Reverse",
                str(reverse),
            )

        if self.complement_checkbox.get():
            complement = self.analysis_service.get_complement(
                self.current_sequence
            )

            self.append_result(results,
                "Complement",
                str(complement),
            )

        if self.reverse_complement_checkbox.get():
            reverse_complement = (
                self.analysis_service.get_reverse_complement(
                    self.current_sequence
                )
            )

            self.append_result(
                results,
                "Reverse Complement",
                str(reverse_complement),
            )

    def analyze_gene_expression(self,results: list[str],):
        """Run selected Central Dogma analyses."""

        if self.transcription_checkbox.get():
            transcript = self.analysis_service.get_transcribe(
                self.current_sequence
            )

            self.append_result(
                results,
                "Transcription (mRNA)",
                str(transcript),
            )

        if self.translation_checkbox.get():
            protein = self.analysis_service.get_translate(
                self.current_sequence
            )

            self.append_result(
                results,
                "Translation (Protein)",
                str(protein),
            )

            results.append("* = Stop codon")
            results.append("")

    def analyze_codon_analysis(self, results: list[str]):

        if self.codon_frequency_checkbox.get():
            frequency = self.analysis_service.get_codon_frequency(
                self.current_sequence
            )

            self.add_section(results, "Codon Frequency")

            for codon, count in sorted(frequency.items()):
                results.append(f"{codon:<4}: {count:>4}")

            results.append("")

        if self.codon_usage_checkbox.get():
            usage = self.analysis_service.get_codon_usage(
                self.current_sequence
            )

            self.add_section(results, "Codon Usage")

            results.append(
                f"{'Codon':<8}"
                f"{'AA':<4}"
                f"{'Amino Acid':<20}"
                f"{'Count':>5}"
            )

            results.append("-" * 82)

            for item in sorted(usage, key=lambda x: x["codon"]):
                results.append(
                    f"{item['codon']:<8}"
                    f"{item['amino_acid']:<4}"
                    f"{item['amino_acid_name']:<20}"
                    f"{item['count']:>5}"
                )

            results.append("")

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
        results.append("-" * 82)

    def append_result(self,results: list[str],title: str,value: str,):
        """Append a formatted analysis result."""

        self.add_section(results, title)
        results.append(value)
        results.append("")