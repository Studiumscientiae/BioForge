# BioForge

BioForge is a Python-based bioinformatics toolkit under active development, designed with a clean, modular, and extensible architecture.

Version **0.4.3** expands BioForge with DNA sequence transformation capabilities, adding reverse, complement, reverse complement, and AT content analysis alongside the existing sequence statistics. The project now provides a modular multi-page GUI, FASTA support, reusable UI factories, and a growing collection of core bioinformatics analysis tools.

The long-term goal of BioForge is to evolve into a comprehensive toolkit for biological sequence analysis, visualization, file handling, and AI-assisted bioinformatics workflows.

---
## Version

**Current Version:** v0.4.3

---
## Development Notice
🚧 BioForge is currently under active development.

Version **0.4.3** extends the biological analysis toolkit with DNA sequence transformation operations, including reverse, complement, reverse complement, and AT content analysis. This release also introduces comprehensive unit testing across the core domain and service layer, strengthening the project's reliability while maintaining its modular architecture.

BioForge continues to evolve toward a comprehensive toolkit for biological sequence analysis, visualization, file handling, and AI-assisted bioinformatics workflows.

---

## Features
BioForge v0.4.3 includes

Core
- DNA sequence validation
- Sequence object creation
- FASTA file parsing
- File loading system
- File writing utilities

GUI
- Multi-page CustomTkinter interface
- Validation workspace
- Analysis workspace
- Sidebar navigation

Sequence Statistics
- Sequence length
- GC content
- AT content
- Nucleotide counts
- Molecular weight

Sequence Operations
- Reverse sequence
- Complement
- Reverse complement

Architecture
- WidgetFactory
- UIFactory
- AnalysisFactory
- ValidationFactory
- Centralized UI theme system
- Modular component architecture
- Clean project structure

Testing
- Sequence model unit tests
- Validator unit tests
- AnalysisService unit tests

---
## Project Structure
``` text
BioForge/
│
├── src/
│   ├── analysis/
│   │   ├── __init__.py
│   │   └── analysis_service.py
│   │
│   ├── core/
│   │   ├── sequence.py
│   │   └── validator.py
│   │
│   ├── io/
│   │   ├── fasta_parser.py
│   │   ├── file_writer.py
│   │   └── loader.py
│   │
│   ├── services/
│   │   ├── __init__.py
│   │   ├── export_service.py
│   │   ├── history_service.py
│   │   └── sequence_service.py
│   │
│   └── ui/
│       ├── branding.py
│       ├── cli.py
│       ├── theme.py
│       │
│       ├── components/
│       │   ├── __init__.py
│       │   ├── analysis_tool_pane.py
│       │   ├── collapsible_section.py
│       │   ├── export_toolbar.py
│       │   ├── history_pane.py
│       │   ├── result_pane.py
│       │   ├── sidebar.py
│       │   └── splitter.py
│       │
│       ├── dialogs/
│       │   ├── __init__.py
│       │   ├── about_dialog.py
│       │   └── export_dialog.py
│       │
│       ├── factories/
│       │   ├── __init__.py
│       │   ├── analysis_factory.py
│       │   ├── ui_factory.py
│       │   ├── validation_factory.py
│       │   └── widget_factory.py
│       │
│       └── pages/
│           ├── __init__.py
│           ├── analysis_page.py
│           └── validation_page.py
│
├── data/
│   └── ten_sequences.fasta
├── docs/
├── reports/
├── tests/
│   ├── test_analysis_service.py
│   ├── test_sequence.py
│   └── test_validator.py
│
├── README.md
├── CHANGELOG.md
├── requirements.txt
└── LICENSE
```
---

## Installation

Clone the repository:

```bash
git clone https://github.com/Studiumscientiae/BioForge.git
```

Move into the project directory:

```bash
cd BioForge
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
python src/ui/cli.py
```

---

## Requirements

- Python 3.11+
- customtkinter 5.2.2 or later
- biopython 1.87
- pytest 9.1.1 or later


---

## Roadmap

BioForge is developed incrementally, with each release building upon a clean, modular, and extensible architecture.

---

### v0.1.0 — Project Initialization ✅

- Project structure
- GitHub repository
- README
- License
- Basic documentation

---

### v0.2.0 — Core Architecture ✅

- DNA sequence validation
- Sequence object
- Application controller
- CustomTkinter GUI
- Modular project architecture

---

### v0.3.0 — File I/O ✅

- FASTA parser
- File loader
- File writer
- File type validation
- GUI file import
- Improved error handling

---

### v0.4.1 — GUI Architecture Refactor ✅

- Multi-page application architecture
- Validation workspace
- Analysis workspace
- Sidebar navigation
- Shared UI theme
- Modular UI components
- Workspace foundation
- Service layer foundation

---

### v0.4.2 — Core Sequence Analysis ✅

- WidgetFactory
- UIFactory
- AnalysisFactory
- ValidationFactory
- Sequence length
- GC content
- Nucleotide counts
- Molecular weight

---

### v0.4.3 — Sequence Operations ✅

- AT content
- Reverse sequence
- Complement
- Reverse complement
- Expanded Analysis workspace
- Automated unit testing

---

### v0.5.0

Advanced sequence analysis

- IUPAC DNA support
- RNA transcription
- Protein translation
- Codon usage
- Codon frequency
- Open Reading Frames (ORFs)
- Start codon identification
- Stop codon identification
- Reading frame analysis

---

### v0.6.0

Restriction analysis

- Restriction enzyme database
- Restriction site search

(Biopython becomes very useful here.)

---

### v0.7.0

Motif analysis

- Motif search
- Consensus sequences
- Pattern matching

---

### v0.8.0

Visualization

- GC plots
- Base composition charts
- Sequence statistics
- Matplotlib graphs

---

### v0.9.0

Reporting

- PDF report
- CSV export
- Excel export
- HTML report

---

### v1.0.0

Stable release

Everything integrated:

- GUI
- FASTA support
- Sequence statistics 
- Sequence operations
- ORFs
- Restriction sites
- Motif search
- Graphs
- Reports
- Good documentation
- Tests
- Stable release

---

### Future Releases

- Multiple sequence analysis
- Sequence alignment
- GenBank support
- Protein sequence analysis
- Interactive visualizations
- Streamlit web interface
- AI-assisted bioinformatics tools
- Plugin architecture
- Workflow automation
- Comprehensive test coverage
---

## Contributing

BioForge is currently under active solo development.

Contributions, pull requests, and code submissions are not being accepted at this stage.

Feature suggestions and bug reports may be considered in future releases.

---

## License

All Rights Reserved.

The source code is publicly available for viewing and educational purposes only. No permission is granted to copy, modify, redistribute, or use this software without prior written permission from the copyright holder.

---

## Author

Developed by **Pranab Singh**

GitHub Username : Studiumscientiae
