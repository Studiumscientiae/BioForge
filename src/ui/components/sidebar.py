"""
ui/components/sidebar.py

Sidebar navigation for BioForge.

Responsibilities
----------------
- Display application branding.
- Display navigation buttons.
- Notify the application controller when the user changes pages.
- Highlight the active page.

Does NOT
---------
- Switch pages itself.
- Perform biological analysis.
- Store application state.
"""

import customtkinter as ctk
from src.version import APP_NAME, VERSION

class Sidebar(ctk.CTkFrame):
    """Sidebar navigation component."""

    NAV_ITEMS = (
        ("Validation", "validation", "normal"),
        ("Analysis", "analysis", "normal"),
        ("History", "history", "disabled"),
        ("Reports", "reports", "disabled"),
        ("Settings", "settings", "disabled"),
    )

    ACTIVE_COLOR = ("gray70", "gray30")
    INACTIVE_COLOR = ("gray25", "gray25")

    def __init__(self, parent, navigate_callback):
        super().__init__(parent)

        self.navigate_callback = navigate_callback

        self.buttons = {}
        self.active_page = None

        self.configure(width=220,corner_radius=12)
        self.pack_propagate(False)

        self.logo_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.navigation_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.footer_frame = ctk.CTkFrame(self, fg_color="transparent")

        self.logo_frame.pack(fill="x", padx=15, pady=(20, 10))
        self.navigation_frame.pack(fill="both",expand=True,padx=10,pady=10)
        self.footer_frame.pack(fill="x",padx=15,pady=(10, 20))

        self.create_logo()
        self.create_navigation()
        self.create_footer()


    def create_logo(self):
        """Create the application logo section."""

        title = ctk.CTkLabel(self.logo_frame,
                             text="BioForge",
                             font=ctk.CTkFont(size=24,
                             weight="bold")
                             )

        title.pack(anchor="w")

        subtitle = ctk.CTkLabel(self.logo_frame,
                                text="Biological Sequence Analysis",
                                font=ctk.CTkFont(size=12)
                                )

        subtitle.pack(anchor="w")

    def _create_nav_button(self, text, page_name, state="normal"):
        """Create a sidebar navigation button."""

        button = ctk.CTkButton(self.navigation_frame,
                               text=text,
                               anchor="w",
                               height=40,
                               corner_radius=8,
                               border_spacing=12,
                               command=lambda: self.on_navigation(page_name),
                               state=state
                               )

        button.pack(fill="x", pady=4)

        self.buttons[page_name] = button

        return button

    def create_navigation(self):
        """Create navigation buttons."""

        for text, page_name, state in self.NAV_ITEMS:
            self._create_nav_button(text, page_name, state)

    def on_navigation(self, page_name):
        """Handle navigation button clicks."""

        self.navigate_callback(page_name)

    def set_active_page(self, page_name):
        """Highlight the active page."""

        self.active_page = page_name

        for name, button in self.buttons.items():

            if name == page_name:
                button.configure(fg_color=self.ACTIVE_COLOR)

            else:
                button.configure(fg_color=self.INACTIVE_COLOR)

    def create_footer(self):
        """Create the footer section."""

        version = ctk.CTkLabel(self.footer_frame,
                               text=f"{APP_NAME} v{VERSION}",
                               font=ctk.CTkFont(size=12)
                               )

        version.pack(anchor="w")