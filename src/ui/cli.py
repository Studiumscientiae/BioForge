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
        # Pages
        # -------------------------

        self.validation_page = None
        self.analysis_page = None
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

        self.sidebar = Sidebar(self)

        self.sidebar.grid(row=0,column=0,sticky="ns",padx=(10, 5),pady=10)

    # -------------------------
    # Page Container
    # -------------------------

    def create_page_container(self):
        """Create the page container."""

        self.page_container = ctk.CTkFrame(self)

        self.page_container.grid(row=0,column=1,sticky="nsew",padx=(5, 10),pady=10)

        self.page_container.grid_rowconfigure(0, weight=1)
        self.page_container.grid_columnconfigure(0, weight=1)

    # -------------------------
    # Pages
    # -------------------------

    def create_pages(self):
        """Create all application pages."""
        self.validation_page = ValidationPage(self.page_container)
        self.validation_page.grid(row=0,column=0,sticky="nsew")

        self.analysis_page = AnalysisPage(self.page_container)
        self.analysis_page.grid(row=0,column=0,sticky="nsew")

        self.pages = {
            "validation": self.validation_page,
            "analysis": self.analysis_page}


    # -------------------------
    # Navigation
    # -------------------------

    def show_page(self, page_name):
        """Display the requested application page."""

        page = self.pages.get(page_name)

        if page:
            page.tkraise()


def main():

    app = BioForgeApp()
    app.mainloop()

if __name__ == "__main__":
    main()