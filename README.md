# BioForge

BioForge is a Python-based bioinformatics toolkit under active development, designed with a clean, modular, and extensible architecture.

Version **0.4.1** introduces the project's core architecture, including biological sequence validation, sequence representation, FASTA file loader, a simple graphical user interface, and an application controller.

The long-term goal of BioForge is to evolve into a comprehensive toolkit for biological sequence analysis, visualization, file handling, and AI-assisted bioinformatics workflows.

---
## Version

**Current Version:** v0.4.1

---
🚧 BioForge is currently under active development.

Version 0.4.1 establishes the application's modular GUI architecture and workspace foundation. The project now provides separate Validation and Analysis workspaces with a reusable navigation system and centralized UI theming.

Biological analysis algorithms will be introduced in subsequent releases.

---

## Features

BioForge v0.4.1 includes

- DNA sequence validation
- Sequence object creation
- FASTA file parsing
- File loading system
- File writing utilities
- Multi-page CustomTkinter interface
- Validation workspace
- Analysis workspace
- Reusable sidebar navigation
- Centralized UI theme system
- Modular component architecture
- Clean project structure
---
## Project Structure

BioForge/
│
├── src/
│   ├── analysis/
│   │   ├── __init__.py
│   │   └── analysis_services.py
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
│       └── pages/
│           ├── __init__.py
│           ├── analysis_page.py
│           └── validation_page.py
│
├── data/
├── docs/
├── reports/
├── tests/
│
├── README.md
├── CHANGELOG.md
├── requirements.txt
└── LICENSE
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

---
## Roadmap

BioForge is developed incrementally, with each version introducing new functionality while maintaining a clean and modular architecture.

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

### v0.5.0 — Validation Workspace Implementation 🚧

- Validation engine integration
- Connect GUI with validation logic
- Validation report generation
- Sequence cleaning tools
- Invalid nucleotide detection
- Automatic sequence normalization
- Batch validation support
- Validation statistics

---

### v0.6.0 — Basic Sequence Analysis 📋

- GC content
- Sequence length
- Base composition (A, T, G, C)
- Reverse complement
- DNA → RNA transcription
- DNA → Protein translation

---

### v0.7.0 — Gene Feature Analysis 📋

- Open Reading Frames (ORFs)
- Reading frame analysis
- Start codon detection
- Stop codon detection
- Longest ORF identification

---

### v0.8.0 — Restriction Analysis 📋

- Restriction enzyme database
- Restriction site identification
- Fragment prediction
- Multiple enzyme analysis

---

### v0.9.0 — Motif & Pattern Analysis 📋

- Motif search
- Consensus sequence generation
- Pattern matching
- Regular expression support
- Degenerate nucleotide support

---

### v1.0.0 — Stable Release 🎯

- Complete graphical interface
- Validation workspace
- Analysis toolkit
- Gene feature analysis
- Restriction analysis
- Motif analysis
- File I/O utilities
- Export system
- Comprehensive documentation
- Unit tests
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
