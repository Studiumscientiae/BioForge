# BioForge

BioForge is an open-source Python project for building clean, modular, and extensible bioinformatics tools.

Version **0.2.0** introduces the project's core architecture, including biological sequence validation, sequence representation, a simple graphical user interface, and an application controller.

The long-term goal of BioForge is to evolve into a comprehensive toolkit for biological sequence analysis, visualization, file handling, and AI-assisted bioinformatics workflows.

## Features

BioForge v0.2.0 includes:

- DNA sequence validation
- Sequence object creation
- Central application controller
- CustomTkinter graphical user interface
- Modular project architecture
- Clean and documented source code

## Project Structure

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
python ui/cli.py
```

---

## Requirements

* Python 3.11 or later
* customtkinter>=5.2.2
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


## License

This project is licensed under the MIT License.

---

## Author

Developed by **Pranab Singh / Studiumscientiae**
