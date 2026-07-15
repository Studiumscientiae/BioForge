"""
src/ui/factories/analysis_factory.py

Factory for creating Analysis Page UI sections.

Responsibilities:
- Create analysis-specific UI sections.
- Assemble analysis controls.
- Apply consistent analysis page styling.

Does not perform:
- Biological analysis
- Event handling
- Layout outside the section itself
"""

from __future__ import annotations

import customtkinter as ctk

from src.ui import theme
from src.ui.factories.widget_factory import WidgetFactory
from src.ui.factories.ui_factory import UIFactory


class AnalysisFactory:
    """Factory for Analysis Page components."""

    def __new__(cls):
        raise TypeError("AnalysisFactory cannot be instantiated.")

    # --------------------------------------------------
    # Statistics
    # --------------------------------------------------

    @staticmethod
    def create_statistics_section(parent,) -> tuple[ctk.CTkFrame, dict[str, ctk.CTkCheckBox]]:

        frame, _ = UIFactory.create_section_frame(
            parent,
            title="Statistics",
        )

        length_checkbox = WidgetFactory.create_checkbox(
            frame,
            text="Sequence Length",
        )

        gc_checkbox = WidgetFactory.create_checkbox(
            frame,
            text="GC Content",
        )

        at_checkbox = WidgetFactory.create_checkbox(
            frame,
            text="AT Content",
        )

        nucleotide_checkbox = WidgetFactory.create_checkbox(
            frame,
            text="Nucleotide Counts",
        )

        weight_checkbox = WidgetFactory.create_checkbox(
            frame,
            text="Molecular Weight",
        )

        checkboxes = [
            length_checkbox,
            gc_checkbox,
            at_checkbox,
            nucleotide_checkbox,
        ]

        for checkbox in checkboxes:
            checkbox.pack(
                anchor="w",
                padx=theme.CHECKBOX_PADX,
                pady=theme.CHECKBOX_PADY,
            )

        weight_checkbox.pack(
            anchor="w",
            padx=theme.CHECKBOX_PADX,
            pady=theme.CHECKBOX_PADY_END,
        )

        return frame, {
            "length": length_checkbox,
            "gc": gc_checkbox,
            "at": at_checkbox,
            "nucleotide": nucleotide_checkbox,
            "weight": weight_checkbox,
        }

    # --------------------------------------------------
    # Sequence Operations
    # --------------------------------------------------

    @staticmethod
    def create_sequence_operations_section(parent,) -> tuple[ctk.CTkFrame, dict[str, ctk.CTkCheckBox]]:

        frame, _ = UIFactory.create_section_frame(
            parent,
            title="Sequence Transformations",
        )

        reverse_checkbox = WidgetFactory.create_checkbox(
            frame,
            text="Reverse",
        )

        complement_checkbox = WidgetFactory.create_checkbox(
            frame,
            text="Complement",
        )

        reverse_complement_checkbox = WidgetFactory.create_checkbox(
            frame,
            text="Reverse Complement",
        )

        controls = [
            reverse_checkbox,
            complement_checkbox,
            reverse_complement_checkbox,
        ]

        for i, checkbox in enumerate(controls):
            checkbox.pack(
                anchor="w",
                padx=theme.CHECKBOX_PADX,
                pady=(
                    theme.CHECKBOX_PADY_END
                    if i == len(controls) - 1
                    else theme.CHECKBOX_PADY
                ),
            )

        return frame, {
            "reverse": reverse_checkbox,
            "complement": complement_checkbox,
            "reverse_complement": reverse_complement_checkbox,
        }

    # --------------------------------------------------
    # Central Dogma
    # --------------------------------------------------

    @staticmethod
    def create_central_dogma_section(parent,) -> tuple[ctk.CTkFrame, dict[str, ctk.CTkCheckBox]]:

        frame, _ = UIFactory.create_section_frame(
            parent,
            title="Central Dogma",
        )

        transcription_checkbox = WidgetFactory.create_checkbox(
            frame,
            text="RNA Transcription",
        )

        translation_checkbox = WidgetFactory.create_checkbox(
            frame,
            text="Protein Translation",
        )

        codon_usage_checkbox = WidgetFactory.create_checkbox(
            frame,
            text="Codon Usage",
        )

        codon_frequency_checkbox = WidgetFactory.create_checkbox(
            frame,
            text="Codon Frequency",
        )

        controls = [
            transcription_checkbox,
            translation_checkbox,
            codon_usage_checkbox,
        ]

        for checkbox in controls:
            checkbox.pack(
                anchor="w",
                padx=theme.CHECKBOX_PADX,
                pady=theme.CHECKBOX_PADY,
            )

        codon_frequency_checkbox.pack(
            anchor="w",
            padx=theme.CHECKBOX_PADX,
            pady=theme.CHECKBOX_PADY_END,
        )

        return frame, {
            "transcription": transcription_checkbox,
            "translation": translation_checkbox,
            "codon_usage": codon_usage_checkbox,
            "codon_frequency": codon_frequency_checkbox,
        }

    # --------------------------------------------------
    # Action Section
    # --------------------------------------------------

    @staticmethod
    def create_action_section(parent,*,command,) -> ctk.CTkButton:

        button = WidgetFactory.create_button(
            parent,
            text="Analyze",
            command=command,
        )

        button.pack(
            fill="x",
            padx=theme.ACTION_BUTTON_PADX,
            pady=theme.ACTION_BUTTON_PADY,
        )

        return button