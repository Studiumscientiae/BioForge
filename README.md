# BioForge

BioForge is a Python-based bioinformatics toolkit under active development, designed with a clean, modular, and extensible architecture.

Version **0.2.0** introduces the project's core architecture, including biological sequence validation, sequence representation, a simple graphical user interface, and an application controller.

The long-term goal of BioForge is to evolve into a comprehensive toolkit for biological sequence analysis, visualization, file handling, and AI-assisted bioinformatics workflows.

---
## Version

**Current Version:** v0.2.0

---
## Project Status

🚧 BioForge is currently under active development.

Version 0.2.0 establishes the project's foundation and architecture. New bioinformatics features will be introduced incrementally in future releases.

---

## Features

BioForge v0.2.0 includes:

- DNA sequence validation
- Sequence object creation
- Central application controller
- CustomTkinter graphical user interface
- Modular project architecture
- Clean and documented source code

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
│   ├── ui/
│   │   └── cli.py
│   │
│   └── main.py
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

### v0.3.0
- RNA sequence validation
- Protein sequence validation
- Improved error handling
- Additional unit tests

### v0.4.0
- FASTA file support
- File import functionality
- Sequence metadata support

### v0.5.0
- GC content calculation
- Reverse complement generation
- DNA transcription
- Basic sequence statistics

### v0.6.0
- DNA to protein translation
- Motif searching
- Sequence comparison utilities

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
