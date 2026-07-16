# Changelog

All notable changes to this project will be documented in this file.

---

## [v0.4.3] - 2026-07-16

### Added

- DNA sequence reverse operation
- DNA complement operation
- DNA reverse complement operation
- AT content calculation
- AnalysisService support for sequence transformation operations
- Unit tests for the Sequence model
- Unit tests for the DNA validator
- Unit tests for the AnalysisService

### Changed

- Extended the Analysis workspace with AT content analysis
- Integrated sequence transformation operations into the Analysis workflow
- Expanded the analysis interface to support additional DNA sequence operations

### Improved

- Increased automated test coverage across the core domain and service layer
- Improved reliability of sequence analysis features through unit testing
- Enhanced maintainability of the analysis pipeline with comprehensive verification
- Strengthened the foundation for future biological sequence analysis features

---

## [v0.4.2] - 2026-07-15

### Added

- WidgetFactory for consistent CustomTkinter widget creation
- UIFactory for reusable generic UI sections
- AnalysisFactory for analysis-specific UI construction
- ValidationFactory for validation-specific UI construction
- Molecular weight analysis using Biopython
- Analysis workflow organized into modular analysis methods

### Changed

- Refactored AnalysisPage to delegate UI construction to factories
- Refactored ValidationPage to delegate UI construction to factories
- Replaced duplicated widget creation with reusable factory methods
- Centralized widget styling through the shared theme configuration
- Simplified page classes by separating UI construction from event handling

### Improved

- Cleaner layered UI architecture
- Reduced code duplication across pages
- Better separation of responsibilities between pages and factories
- Easier maintenance and extension of the GUI
- Improved readability and consistency of the UI codebase
- Established a scalable foundation for future analysis and validation features

---

## [v0.4.1] - 2026-07-13

### Added

- Multi-page application architecture
- Validation workspace page
- Analysis workspace page
- Reusable sidebar navigation component
- Centralized UI theme configuration (`theme.py`)
- Analysis workspace layout with placeholder tools
- Export toolbar component foundation
- Modular UI component structure

### Changed

- Refactored the application into a page-based architecture
- Moved navigation management to the application shell
- Replaced direct window management with centralized page navigation
- Standardized UI styling using shared theme constants
- Simplified widget creation through reusable UI helper methods

### Improved

- Better separation of UI responsibilities
- Cleaner project architecture following the Single Responsibility Principle
- Improved maintainability and scalability
- Consistent application-wide styling
- Prepared foundation for future analysis algorithms and services

---

## [v0.3.0] - 2026-07-09

### Added

- FASTA file parser
- File loader module
- File writer utilities
- GUI support for importing FASTA files
- Multiple sequence loading
- Improved application workflow

### Improved

- Modular IO architecture
- Separation of parser and loader responsibilities
- Better error handling
- Cleaner project structure

---

## [v0.2.0] - 2026-07-08

### Added

- DNA sequence validation
- Sequence object representation
- Application controller
- CustomTkinter GUI
- Initial project architecture
- README
- License
- Requirements