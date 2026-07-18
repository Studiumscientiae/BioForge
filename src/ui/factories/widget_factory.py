"""
src/ui/factories/widget_factory.py

Factory for creating consistently styled CustomTkinter widgets.

Responsibilities:
- Create common UI widgets.
- Apply BioForge theme defaults.
- Replace duplicate widget construction.
- Allow widget customization through keyword arguments.

Does not perform:
- Widget layout (pack/grid/place)
- Business logic
- Event handling beyond assigning callbacks
"""

from __future__ import annotations

import customtkinter as ctk
from src.ui import theme

class WidgetFactory:
    """Factory for creating common BioForge widgets."""

    def __new__(cls):
        raise TypeError("WidgetFactory cannot be instantiated.")

    @staticmethod
    def create_frame(parent, **kwargs) -> ctk.CTkFrame:
        """Create a themed frame."""

        return ctk.CTkFrame(parent,
                            corner_radius=theme.FRAME_CORNER_RADIUS,
                            **kwargs,)

    @staticmethod
    def create_label(parent, *, text: str="", **kwargs) -> ctk.CTkLabel:
        """Create a label."""

        return ctk.CTkLabel(parent,
                            text=text,
                            **kwargs,)

    @staticmethod
    def create_button(parent, *, text:str, command=None ,**kwargs) -> ctk.CTkButton:
        """Create a themed button."""

        return ctk.CTkButton(parent,
                             text=text,
                             command=command,
                             width=theme.BUTTON_WIDTH,
                             height=theme.BUTTON_HEIGHT,
                             corner_radius=theme.BUTTON_CORNER_RADIUS,
                             **kwargs,)

    @staticmethod
    def create_entry(parent, **kwargs) -> ctk.CTkEntry:
        """Create a themed entry."""

        return ctk.CTkEntry(parent,
                            height=theme.ENTRY_HEIGHT,
                            **kwargs,)

    @staticmethod
    def create_textbox(parent, **kwargs) -> ctk.CTkTextbox:
        """Create a textbox."""

        return ctk.CTkTextbox(
            parent,
            height=theme.TEXTBOX_HEIGHT,
            font=theme.TEXTBOX_FONT,
            **kwargs,
        )

    @staticmethod
    def create_checkbox(parent, *,text: str,**kwargs) -> ctk.CTkCheckBox:
        """Create a checkbox."""

        return ctk.CTkCheckBox(parent,
                               text=text,
                               **kwargs,)

    @staticmethod
    def create_combobox(parent, *, values=None,**kwargs) -> ctk.CTkComboBox:
        """Create a themed combobox."""

        return ctk.CTkComboBox(parent,
                               values=[] if values is None else values,
                               height=theme.COMBOBOX_HEIGHT,
                               **kwargs,)

    @staticmethod
    def create_scrollable_frame(parent, **kwargs) -> ctk.CTkScrollableFrame:
        """Create a themed scrollable frame."""

        return ctk.CTkScrollableFrame(
            parent,
            corner_radius=theme.FRAME_CORNER_RADIUS,
            **kwargs,
        )
