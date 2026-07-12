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
from src.ui.branding import APP_NAME, VERSION, APP_TAGLINE
from src.ui.theme import (SIDEBAR_WIDTH, SIDEBAR_CORNER_RADIUS,
                          ACTIVE_BUTTON_COLOR, INACTIVE_BUTTON_COLOR,
                          NAV_BUTTON_HEIGHT, NAV_BUTTON_CORNER_RADIUS,
                          TITLE_FONT_SIZE,SUBTITLE_FONT_SIZE,
                          FOOTER_FONT_SIZE,NAV_BUTTON_PADDING_Y,
                          LOGO_PADDING_X,LOGO_PADDING_Y,
                          NAVIGATION_PADDING_X,NAVIGATION_PADDING_Y,
                          FOOTER_PADDING_X,FOOTER_PADDING_Y)

class Sidebar(ctk.CTkFrame):
    """Sidebar navigation component."""

    NAV_ITEMS = (
        ("Validation", "validation", "normal"),
        ("Analysis", "analysis", "normal"),
        ("History", "history", "disabled"),
        ("Reports", "reports", "disabled"),
        ("Settings", "settings", "disabled"),
    )

    def __init__(self, parent, navigate_callback):
        super().__init__(parent)

        self.navigate_callback = navigate_callback

        self.buttons = {}
        self.active_page = None

        self.configure(width= SIDEBAR_WIDTH,corner_radius= SIDEBAR_CORNER_RADIUS)
        self.pack_propagate(False)

        self.logo_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.navigation_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.footer_frame = ctk.CTkFrame(self, fg_color="transparent")

        self.logo_frame.pack(fill="x", padx=LOGO_PADDING_X, pady=LOGO_PADDING_Y)
        self.navigation_frame.pack(fill="both",expand=True,padx=NAVIGATION_PADDING_X,pady=NAVIGATION_PADDING_Y)
        self.footer_frame.pack(fill="x",padx=FOOTER_PADDING_X,pady=FOOTER_PADDING_Y)

        self.create_logo()
        self.create_navigation()
        self.create_footer()


    def create_logo(self):
        """Create the application logo section."""

        title = ctk.CTkLabel(self.logo_frame,
                             text=APP_NAME,
                             font=ctk.CTkFont(size=TITLE_FONT_SIZE,
                             weight="bold")
                             )

        title.pack(anchor="w")

        subtitle = ctk.CTkLabel(self.logo_frame,
                                text=APP_TAGLINE,
                                font=ctk.CTkFont(size=SUBTITLE_FONT_SIZE)
                                )

        subtitle.pack(anchor="w")

    def _create_nav_button(self, text, page_name, state="normal"):
        """Create a sidebar navigation button."""

        button = ctk.CTkButton(self.navigation_frame,
                               text=text,
                               anchor="w",
                               height= NAV_BUTTON_HEIGHT,
                               corner_radius=NAV_BUTTON_CORNER_RADIUS,
                               border_spacing=12,
                               command=lambda: self.on_navigation(page_name),
                               state=state
                               )

        button.pack(fill="x", pady=NAV_BUTTON_PADDING_Y)

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
                button.configure(fg_color=ACTIVE_BUTTON_COLOR)

            else:
                button.configure(fg_color=INACTIVE_BUTTON_COLOR)

    def create_footer(self):
        """Create the footer section."""

        version = ctk.CTkLabel(self.footer_frame,
                               text=f"{APP_NAME} v{VERSION}",
                               font=ctk.CTkFont(size=FOOTER_FONT_SIZE)
                               )

        version.pack(anchor="w")