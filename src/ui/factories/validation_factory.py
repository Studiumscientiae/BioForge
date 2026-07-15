"""
src/ui/factories/validation_factory.py

Factory for creating Validation Page UI sections.

Responsibilities:
- Create validation-specific UI sections.
- Assemble validation controls.
- Apply consistent validation page styling.

Does not perform:
- Sequence validation
- File parsing
- Event handling
- Layout outside the section itself
"""

from __future__ import annotations

import customtkinter as ctk

from src.ui import theme
from src.ui.factories.widget_factory import WidgetFactory
from src.ui.factories.ui_factory import UIFactory


class ValidationFactory:
    """Factory for Validation Page components."""

    def __new__(cls):
        raise TypeError("ValidationFactory cannot be instantiated.")

    # --------------------------------------------------
    # Sequence Selection
    # --------------------------------------------------

    @staticmethod
    def create_sequence_selector(
        parent,
    ) -> tuple[ctk.CTkFrame, dict[str, ctk.CTkComboBox]]:

        frame, _ = UIFactory.create_section_frame(
            parent,
            title="Sequence Validation",
        )

        WidgetFactory.create_label(
            frame,
            text="Loaded Sequences",
        ).pack(
            anchor="w",
            padx=theme.LABEL_PADX,
        )

        selector = WidgetFactory.create_combobox(
            frame,
            values=["No sequences loaded"],
        )

        selector.pack(
            fill="x",
            padx=theme.COMBOBOX_PADX,
            pady=theme.COMBOBOX_PADY,
        )

        return frame, {
            "selector": selector,
        }

    # --------------------------------------------------
    # Action Buttons
    # --------------------------------------------------

    @staticmethod
    def create_action_section(
        parent,
        *,
        load_callback,
        validate_callback,
    ) -> tuple[ctk.CTkButton, ctk.CTkButton, ctk.CTkButton]:

        load_button = WidgetFactory.create_button(
            parent,
            text="Load FASTA",
            command=load_callback,
        )

        load_button.pack(
            fill="x",
            padx=theme.ACTION_BUTTON_PADX,
            pady=theme.BUTTON_PADY,
        )

        validate_button = WidgetFactory.create_button(
            parent,
            text="Validate",
            command=validate_callback,
        )

        validate_button.pack(
            fill="x",
            padx=theme.ACTION_BUTTON_PADX,
            pady=theme.BUTTON_PADY,
        )

        validate_all_button = WidgetFactory.create_button(
            parent,
            text="Validate All",
        )

        validate_all_button.pack(
            fill="x",
            padx=theme.ACTION_BUTTON_PADX,
            pady=theme.BUTTON_PADY_END,
        )

        return (
            load_button,
            validate_button,
            validate_all_button,
        )

    # --------------------------------------------------
    # Input Section
    # --------------------------------------------------

    @staticmethod
    def create_input_section(
        parent,
    ) -> tuple[ctk.CTkEntry, ctk.CTkTextbox]:

        WidgetFactory.create_label(
            parent,
            text="Sequence Name",
        ).pack(
            anchor="w",
            padx=theme.LABEL_PADX,
        )

        entry = WidgetFactory.create_entry(
            parent,
            placeholder_text="Enter sequence name",
        )

        entry.pack(
            fill="x",
            padx=theme.ENTRY_PADX,
            pady=theme.ENTRY_PADY,
        )

        WidgetFactory.create_label(
            parent,
            text="Sequence Input",
        ).pack(
            anchor="w",
            padx=theme.LABEL_PADX,
        )

        textbox = WidgetFactory.create_textbox(
            parent,
        )

        textbox.pack(
            fill="both",
            expand=True,
            padx=theme.TEXTBOX_PADX,
            pady=theme.TEXTBOX_PADY,
        )

        return entry, textbox