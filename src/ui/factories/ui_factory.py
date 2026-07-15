"""
src/ui/factories/ui_factory.py

Factory for creating reusable BioForge UI sections.

Responsibilities:
- Assemble multiple themed widgets into reusable UI components.
- Apply consistent layout and spacing.
- Reduce duplicate UI construction across pages.

Does not perform:
- Business logic
- Event handling
- Navigation
- Widget placement outside the component itself
"""

from __future__ import annotations

import customtkinter as ctk

from src.ui import theme
from src.ui.factories.widget_factory import WidgetFactory


class UIFactory:
    """Factory for creating reusable BioForge UI sections."""

    def __new__(cls):
        raise TypeError("UIFactory cannot be instantiated.")

    @staticmethod
    def create_section_frame(parent,*,title: str,**kwargs,) -> tuple[ctk.CTkFrame, ctk.CTkLabel]:
        """
        Create a titled section frame.

        Returns:
            (frame, title_label)
        """

        frame = WidgetFactory.create_frame(parent, **kwargs)

        title_label = WidgetFactory.create_label(
            frame,
            text=title,
            font=theme.SECTION_TITLE_FONT,
        )

        title_label.pack(
            anchor="w",
            padx=theme.SECTION_TITLE_PADX,
            pady=theme.SECTION_TITLE_PADY,
        )

        return frame, title_label

    @staticmethod
    def create_result_panel(parent,*,title: str = "Results",**kwargs,) -> tuple[
        ctk.CTkFrame,
        ctk.CTkLabel,
        ctk.CTkTextbox,
    ]:
        """
        Create a standard result panel.

        Returns:
            (frame, title_label, textbox)
        """

        frame = WidgetFactory.create_frame(parent, **kwargs)

        title_label = WidgetFactory.create_label(
            frame,
            text=title,
            font=theme.RESULT_TITLE_FONT,
        )

        title_label.pack(
            anchor="w",
            padx=theme.RESULT_TITLE_PADX,
            pady=theme.RESULT_TITLE_PADY,
        )

        textbox = WidgetFactory.create_textbox(frame)

        textbox.pack(
            fill="both",
            expand=True,
            padx=theme.TEXTBOX_PADX,
            pady=theme.TEXTBOX_PADY,
        )

        return frame, title_label, textbox

    @staticmethod
    def create_button_group(parent,*,buttons: list[tuple[str, object]],**kwargs,) -> tuple[ctk.CTkFrame, list[ctk.CTkButton]]:
        """
        Create a vertical button group.

        Args:
            buttons:
                List of (text, command) tuples.

        Returns:
            (frame, button_widgets)
        """

        frame = WidgetFactory.create_frame(parent, **kwargs)

        widgets: list[ctk.CTkButton] = []

        for text, command in buttons:
            button = WidgetFactory.create_button(
                frame,
                text=text,
                command=command,
            )

            button.pack(
                fill="x",
                padx=theme.ACTION_BUTTON_PADX,
                pady=theme.BUTTON_PADY,
            )

            widgets.append(button)

        return frame, widgets