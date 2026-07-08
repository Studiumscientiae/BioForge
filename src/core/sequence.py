"""
sequence.py

Defines the core Sequence object used throughout BioForge.

Responsibilities:
- Store biological sequence data.
- Normalize sequence format.
- Provide basic metadata such as length.

Non-responsibilities:
- Validation
- Biological analysis
- File parsing
- Reporting
"""

class Sequence:

    def __init__(self,name: str,sequence: str):
        self.name= name
        self.sequence= sequence.upper().strip()

    def length(self) -> int:
        return len(self.sequence)

    def __str__(self) -> str:
        return(
            f"Sequence Name: {self.name}\n"
            f"Sequence: {self.sequence}\n"
            f"Length: {self.length()} bases"
        )
