"""
cli.py

Application shell for BioForge.

Responsibilities:
- Create the main application window.
- Create the application layout.
- Create the sidebar.
- Create the page container.
- Create application pages.
- Manage page navigation.
- Start the application.

Does not perform:
- Sequence validation
- Biological analysis
- File parsing
- Exporting
- History management
"""

import customtkinter as ctk

from src.ui.components.sidebar import Sidebar
from src.ui.pages.validation_page import ValidationPage
from src.ui.pages.analysis_page import AnalysisPage
from src.analysis.analysis_service import AnalysisService
from src.services.sequence_service import SequenceService
from src.services.codon_usage_service import CodonUsageService

class BioForgeApp(ctk.CTk):
    """Main application shell."""

    def __init__(self):
        super().__init__()

        # -------------------------
        # Window
        # -------------------------

        self.title("BioForge")
        self.geometry("1200x700")

        # -------------------------
        # Layout
        # -------------------------

        self.sidebar = None
        self.page_container = None

        # -------------------------
        # Services
        # -------------------------

        self.sequence_service = SequenceService()
        self.analysis_service = AnalysisService()
        self.codon_usage_service = CodonUsageService()

        # -------------------------
        # Pages
        # -------------------------

        self.pages = {}

        # -------------------------
        # Build Application
        # -------------------------

        self.create_layout()
        self.create_sidebar()
        self.create_page_container()
        self.create_pages()

        self.show_page("validation")

    # -------------------------
    # Layout
    # -------------------------

    def create_layout(self):
        """Create the main application layout."""

        self.grid_rowconfigure(0, weight=1)

        # Sidebar column
        self.grid_columnconfigure(0, weight=0)

        # Workspace column
        self.grid_columnconfigure(1, weight=1)

    # -------------------------
    # Sidebar
    # -------------------------

    def create_sidebar(self):
        """Create the navigation sidebar."""

        self.sidebar = Sidebar(parent=self,
                               navigate_callback= self.show_page)

        self.sidebar.grid(row=0,column=0,sticky="ns",padx=(10, 5),pady=10)

    # -------------------------
    # Page Container
    # -------------------------

    def create_page_container(self):
        """Create the page container."""

        self.page_container = ctk.CTkFrame(self,
                                           fg_color="transparent")

        self.page_container.grid(row=0,column=1,sticky="nsew",padx=(5, 10),pady=10)

        self.page_container.grid_rowconfigure(0, weight=1)
        self.page_container.grid_columnconfigure(0, weight=1)

    # -------------------------
    # Pages
    # -------------------------

    def create_pages(self):
        """Create all application pages."""

        self.pages = {
            "validation": ValidationPage(
                self.page_container,
                self.process_validation,
                self.process_fasta
            ),
            "analysis": AnalysisPage(
                self.page_container,
                self.analysis_service,
                self.codon_usage_service
            ),
        }

        for page in self.pages.values():
            page.grid(row=0, column=0, sticky="nsew")


    # -------------------------
    # Navigation
    # -------------------------

    def show_page(self, page_name):
        """Display the requested application page."""

        page = self.pages.get(page_name)

        if page:
            page.tkraise()

            if self.sidebar:
                self.sidebar.set_active_page(page_name)

    def process_validation(self, name: str, sequence: str):
        """Process sequence validation."""

        try:
            sequence = self.sequence_service.validate_sequence(name,sequence)

            self.pages["validation"].display_result(str(sequence))
            self.pages["analysis"].set_sequence(sequence)

        except ValueError as error:
            self.pages["validation"].display_result(str(error))

    def process_fasta(self, file_path: str):
        """Process FASTA file loading."""

        try:
            sequences = self.sequence_service.load_sequences(file_path)

            results = "\n\n".join(
                str(sequence)
                for sequence in sequences
            )

            self.pages["validation"].display_result(results)

            if sequences:
                self.pages["analysis"].set_sequence(
                    sequences[0]
                )

        except ValueError as error:
            self.pages["validation"].display_result(str(error))

def main():

    app = BioForgeApp()
    app.mainloop()

if __name__ == "__main__":
    main()