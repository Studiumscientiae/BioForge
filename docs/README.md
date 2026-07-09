# BioForge

BioForge is a Python-based bioinformatics toolkit under active development, designed with a clean, modular, and extensible architecture.

Version **0.2.0** introduces the project's core architecture, including biological sequence validation, sequence representation, a simple graphical user interface, and an application controller.

The long-term goal of BioForge is to evolve into a comprehensive toolkit for biological sequence analysis, visualization, file handling, and AI-assisted bioinformatics workflows.

---
## Version

**Current Version:** v0.3.0

---
## Project Status

🚧 BioForge is currently under active development.

Version 0.2.0 establishes the project's foundation and architecture. New bioinformatics features will be introduced incrementally in future releases.

---

## Features

BioForge v0.3.0 includes

- DNA sequence validation
- Sequence object creation
- FASTA file parsing
- File loading system
- File writing utilities
- CustomTkinter GUI
- Modular IO architecture
- Clean project structure
---
## Project Structure

```text
BioForge/
│
├── src/
│   ├── core/
│   │   ├── sequence.py
│   │   └── validator.py
│   │
│   ├── io/
│   │    ├── fasta_parser.py
│   │    ├── file_writer.py 
│   │    └── loader.py
│   │
│   ├── ui/
│   │   └── cli.py
│   │
│   └── main.py
│
├── data/
│   └── ten_sequences.fasta
│    
├── docs/
├── reports/
├── tests/
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

---
## Roadmap

BioForge is developed incrementally, with each version introducing new functionality while maintaining a clean and modular architecture.

---

### v0.1.0 — Project Initialization ✅

* Project structure
* GitHub repository
* README
* License
* Basic documentation

---

### v0.2.0 — Core Architecture ✅

* Sequence class
* Validator
* Application controller
* CustomTkinter GUI
* Modular project architecture

---

### v0.3.0 — File I/O ✅

* FASTA parser
* File loader
* File writer
* File type validation
* GUI file import
* Improved error handling

---

### v0.4.0 — Basic Sequence Analysis 🚧

* GC content
* Sequence length
* Base composition (A, T, G, C)
* Reverse complement
* DNA → RNA transcription
* DNA → Protein translation

---

### v0.5.0 — Gene Feature Analysis 📋

* Open Reading Frames (ORFs)
* Reading frame analysis
* Start and stop codon detection
* Longest ORF identification

---

### v0.6.0 — Restriction Analysis 📋

* Restriction enzyme database
* Restriction site identification
* Fragment prediction
* Multiple enzyme analysis

---

### v0.7.0 — Motif & Pattern Analysis 📋

* Motif search
* Consensus sequence generation
* Pattern matching
* Regular expression support
* Degenerate nucleotide support

---

### v0.8.0 — Visualization 📋

* GC content plots
* Base composition charts
* Sequence length distribution
* Exportable figures

---

### v0.9.0 — Reporting & Export 📋

* PDF reports
* CSV export
* Excel export
* HTML reports
* Analysis summaries

---

### v1.0.0 — Stable Release 🎯

* Complete graphical interface
* FASTA support
* Sequence analysis toolkit
* ORF detection
* Restriction analysis
* Motif analysis
* Data visualization
* Report generation
* Comprehensive documentation
* Unit tests
* Stable tagged release

### Future Releases
- Multiple sequence analysis
- Sequence alignment
- GenBank file support
- Command-line interface (CLI)
- Streamlit web interface
- Interactive data visualization
- AI-assisted bioinformatics tools
- Comprehensive test coverage
- Complete project documentation
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
