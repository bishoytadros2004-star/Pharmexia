# Pharmexia

**AI-Assisted Pharmacogenomics Decision-Support Platform**

[![Python](https://img.shields.io/badge/python-3.10%2B-blue.svg)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/API-FastAPI-009688.svg)](https://fastapi.tiangolo.com/)
[![PySide6](https://img.shields.io/badge/GUI-PySide6-41CD52.svg)](https://doc.qt.io/qtforpython/)
[![License: TODO](https://img.shields.io/badge/license-TODO-lightgrey.svg)](#license)
[![Status: Manuscript under review](https://img.shields.io/badge/manuscript-under%20review-yellow.svg)](#citation)

> **Note on repository completeness.** This README and the accompanying documentation were prepared from the single-file build artifact `oncox.py` (the project's stated "single-file source of truth") and the submitted manuscript. Several imports in `oncox.py` (`src.branding`, `src.database_clients` package init) reference modules that are **not present** in this artifact, meaning the full multi-file repository contains additional source files not covered here. See [Reproducibility Notes](docs/USER_MANUAL.md#reproducibility-notes-and-known-gaps) for the complete list of items that require confirmation from the author before submission.

## Who Built This Pipeline

The Pharmexia pipeline (`oncox.py` and all `src/` modules described in this repository) was developed by **Bishoy Tadros**, School of Biotechnology, Badr University in Cairo (BUC), Egypt, as part of the wider Pharmexia project described in the manuscript *"Pharmexia: Artificial Intelligence Application for DNA-Based Drug Response Prediction"* (full author list in [Citation](#citation)). See [Author](#author) below for full attribution, and [AI-Assisted Development Statement](#ai-assisted-development-statement) for the role generative AI tools played in building it.

## Table of Contents

- [Who Built This Pipeline](#who-built-this-pipeline)
- [Project Description](#project-description)
- [Features](#features)
- [Pipeline Overview](#pipeline-overview)
- [Repository Structure](#repository-structure)
- [Installation](#installation)
- [Quick Start](#quick-start)
- [Example Usage](#example-usage)
- [Output Files](#output-files)
- [Documentation](#documentation)
- [How to Reproduce Results](#how-to-reproduce-results)
- [Author](#author)
- [License](#license)
- [Citation](#citation)
- [Contact Information](#contact-information)
- [Acknowledgments](#acknowledgments)
- [AI-Assisted Development Statement](#ai-assisted-development-statement)

## Project Description

Pharmexia is a decision-support application that interprets DNA variant data (VCF or tabular genotype files) against curated pharmacogenomic (PGx) knowledge and returns evidence-graded, drug-specific findings. It targets six core pharmacogenes (**CYP2C19, CYP2C9, VKORC1, SLCO1B1, TPMT, NUDT15**) across a curated panel of clinically actionable loci, and maps findings to thirteen drugs spanning five therapeutic families, using rules sourced from CPIC, PharmGKB, NCBI Medical Genetics Summaries, and DailyMed, with optional remote lookups against ClinVar, dbSNP, and UniProt.

Every output is assigned to one of four confidence tiers (`EVIDENCE_BASED`, `MODEL_ASSISTED`, `INSUFFICIENT_EVIDENCE`, `EXPLORATORY_ONLY`) so that guideline-backed conclusions are never visually indistinguishable from exploratory, model-assisted ones. The system explicitly does not compute drug dosages and is described in the manuscript as a decision-support aid, not a replacement for clinical judgment.

## Features

- Dual input support: VCF (`.vcf`, `.vcf.gz`) and tabular genotype files (`.csv`, `.tsv`, `.txt`, `.json`)
- A twelve-step, explicitly contracted analysis pipeline (input validation → export preparation), with a hard safety halt on failed input validation
- Rule-based diplotype/phenotype interpretation for six pharmacogenes at curated loci
- Evidence aggregation across curated (CPIC/NCBI/DailyMed) and optional remote (ClinVar/dbSNP/UniProt) sources, with conflict downgrading to `INSUFFICIENT_EVIDENCE`
- Drug–drug and drug–gene interaction screening on a five-level severity scale (`CONTRAINDICATED → MAJOR → MODERATE → …`)
- Optional, clearly labeled `MODEL_ASSISTED` machine-learning layer (logistic regression by default) that never overrides guideline-based, `EVIDENCE_BASED` findings
- Leakage-audited exploratory ML validation framework (stratified train/validation/test split, adaptive k-fold cross-validation, calibration and confusion-matrix reporting)
- Two interchangeable interfaces: a PySide6 desktop GUI and a FastAPI REST service (`/health`, `/analyze/variants`) built on the same `AnalysisService`
- JSON/CSV export of every analysis and validation artifact for downstream review

## Pipeline Overview

Pharmexia executes analysis as twelve explicitly ordered, independently testable steps (`src/analysis_pipeline.py`), each returning a structured `PipelineStepResult` with status, warnings, and errors so a run can be audited end to end:

| # | Step key | Purpose |
|---|---|---|
| 1 | `input_validation` | Validates file presence, structure, and required fields; **halts the run on failure** |
| 2 | `file_type_classification` | Classifies the input as VCF or tabular |
| 3 | `extraction` | Extracts raw variant records from the source file |
| 4 | `variant_normalization` | Normalizes chromosome/position/allele representation |
| 5 | `pharmacogene_filtering` | Retains only variants overlapping the curated pharmacogene panel |
| 6 | `evidence_annotation` | Annotates variants against curated + optional remote evidence sources |
| 7 | `diplotype_phenotype` | Resolves star alleles into diplotypes and predicted phenotypes |
| 8 | `rule_based_interpretation` | Applies CPIC/NCBI-derived drug-gene rules to produce clinical findings |
| 9 | `optional_ml_assistance` | Adds `MODEL_ASSISTED` findings only where rule-based evidence is insufficient |
| 10 | `confidence_assignment` | Assigns each finding to one of the four confidence tiers |
| 11 | `report_generation` | Builds the structured analysis report |
| 12 | `export_preparation` | Prepares the JSON/CSV export payload |

This corresponds to the manuscript's Figure 2 (12-step pipeline with phase bands: Input Processing, PGx Processing, Interpretation, Output) and Figure 1 (five-layer architecture). See [`docs/USER_MANUAL.md`](docs/USER_MANUAL.md#pipeline-overview) for the full module-by-module explanation.

## Repository Structure

**As delivered in this artifact** (`oncox.py` is a merged, single-file build):

```
oncox.py                  # Merged build: every module below, concatenated with
                           # "# --- begin/end merged module: <path> ---" markers
```

**Inferred original multi-file layout**, reconstructed from the merge markers inside `oncox.py` (module boundaries are exact; file contents are exact; the surrounding project scaffolding below is not confirmed — see note):

```
src/
├── constants.py
├── oncox_bridge.py
├── schemas.py
├── input_validation.py
├── variant_processing.py
├── pgx_annotation.py
├── evidence_integration.py
├── data_pipeline.py
├── features.py
├── interpret.py
├── ml_pipeline.py
├── risk_logic.py
├── reporting.py
├── analysis_pipeline.py
├── api.py
├── branding.py                      # TODO — referenced, not present in oncox.py
├── core/
│   ├── variant_effects.py
│   ├── star_alleles.py
│   ├── diplotype_interpreter.py
│   ├── evidence_schema.py
│   ├── evidence_aggregator.py
│   ├── drug_interactions.py
│   └── patient_profile.py
├── services/
│   ├── variant_annotation_service.py
│   ├── evidence_service.py
│   ├── interaction_service.py
│   ├── patient_context_service.py
│   ├── validation_service.py
│   ├── export_service.py
│   ├── report_service.py
│   └── analysis_service.py
├── ml/
│   ├── metrics.py
│   └── validation.py
├── models/
│   └── view_models.py
├── ui/
│   ├── controller.py
│   ├── report_views.py
│   └── main_window.py
└── database_clients/
    ├── base.py
    ├── remote_sources.py
    └── __init__.py                  # TODO — referenced, not present in oncox.py
```

> **Information Required From Author:** `docs/`, `examples/`, `sample_data/`, `figures/`, `tests/`, `requirements.txt`, and `LICENSE` are recommended by the target journal's reproducibility checklist but their current contents/presence were not part of the reviewed artifact. Please confirm or supply these before submission — see the [Reviewer Checklist](docs/REVIEWER_CHECKLIST.md).

## Installation

```bash
git clone <REPOSITORY_URL>            # TODO: insert repository URL
cd pharmexia
python -m venv .venv
source .venv/bin/activate             # Windows: .venv\Scripts\activate
pip install -r requirements.txt       # TODO — requirements.txt not present in reviewed artifact
```

**Observed runtime dependencies** (imported directly by `oncox.py`; exact pinned versions require author confirmation):

`PySide6`, `fastapi`, `pydantic`, `pandas`, `numpy`, `scikit-learn`, `joblib`, `requests`, plus an ASGI server such as `uvicorn` to serve the FastAPI app (imported by the deployment process, not by `oncox.py` itself).

See [`docs/USER_MANUAL.md`](docs/USER_MANUAL.md#software-dependencies) for the full dependency table and rationale.

## Quick Start

**Desktop application:**
```bash
python oncox.py
```
Launches the PySide6 desktop GUI (`main()` → `launch_app()`), backed by the shared `AnalysisService`.

**REST API:**
```bash
uvicorn oncox:app --reload
```
Exposes `GET /health` and `POST /analyze/variants` on `http://127.0.0.1:8000`.

## Example Usage

**Health check:**
```bash
curl http://127.0.0.1:8000/health
```

**Submit variants for analysis:**
```bash
curl -X POST http://127.0.0.1:8000/analyze/variants \
  -H "Content-Type: application/json" \
  -d '{
    "variants": [
      {"chrom": "10", "pos": 96541616, "ref": "G", "alt": "A", "rsid": "rs4244285", "genotype": "G/A", "gene": "CYP2C19"}
    ],
    "selected_drugs": ["clopidogrel"],
    "enable_remote_lookup": false
  }'
```

> Sample input files (VCF/CSV/TSV/JSON) suitable for a first run are not included in the reviewed artifact. **Information Required From Author.**

## Output Files

Each analysis produces a structured JSON export (`ExportService.export_json`) containing every `DrugFinding` with its confidence tier, evidence provenance, and safety notes. Each exploratory ML validation run (`ValidationService.validate_classifier`) additionally produces:

- `<stem>.json` — full validation report (metrics, confusion matrices, calibration, data-leakage audit)
- `<stem>.cross_validation.csv`
- `<stem>.confusion_matrix.csv`
- `<stem>.calibration_curves.csv`
- `<stem>.predictions.csv`

See [Output Directory Structure](docs/USER_MANUAL.md#output-directory-structure) for full field-level detail.

## Documentation

- [User Manual](docs/USER_MANUAL.md) — full installation, usage, module reference, and troubleshooting guide
- [How to Use the Pipeline](docs/HOW_TO_USE_PIPELINE.md) — step-by-step walkthrough of the desktop GUI, REST API, and direct Python service usage
- [Figure 5 Visualization Guide](docs/FIGURE_5_VISUALIZATION_GUIDE.md) — runnable script and instructions for generating the Figure 5 statistical-analysis figure from pipeline output
- [Reviewer Checklist](docs/REVIEWER_CHECKLIST.md) — point-by-point mapping of editorial requirements to their location in this repository

## How to Reproduce Results

See [Reproducing Figure 5](docs/USER_MANUAL.md#reproducing-figure-5) for the full, evidence-based walkthrough, including an explicit note on what is and is not reproducible from the current artifact.

## Author

**Pipeline developer / repository maintainer:**

**Bishoy Tadros**
School of Biotechnology, Badr University in Cairo (BUC), Badr City, Cairo 11829, Egypt
*Responsible for: software architecture, pipeline implementation (`oncox.py` / `src/`), and repository maintenance.*

**Full manuscript author list** (School of Biotechnology, Badr University in Cairo): Abanoub A. S. Shaker, Bishoy Tadros, Girges Salama, Abanoub Abdelmalak, Youssef Hegazy, Wafaa Elsayed, Marina Emil, Jousan Mofeed, Asala Nazeh, Rawan Hamdi, Alaa Ahmed, Shrouk Sherine, Rowida ElSobkey, Hagar AlShehaby.

For citing the scientific work as a whole, use the full author list under [Citation](#citation). For questions about the codebase specifically, Bishoy Tadros is the point of contact pending confirmation of a corresponding-author email (see [Contact Information](#contact-information)).

## License

**TODO — Information Required From Author.** No `LICENSE` file was present in the reviewed artifact. An OSI-approved license (e.g., MIT, Apache-2.0, or GPL-3.0) is typically required by Springer Nature software-article policy before publication.

## Citation

**TODO — Information Required From Author.** Insert the final citation once the manuscript DOI/volume/issue are assigned, e.g.:

> Shaker, A. A. S., Tadros, B., et al. (Year). Pharmexia: Artificial Intelligence Application for DNA-Based Drug Response Prediction. *[Journal name]*, DOI pending.

## Contact Information

**TODO — Information Required From Author.** Please supply a corresponding-author email address for the repository README.

## Acknowledgments

This work draws on curated pharmacogenomic knowledge from CPIC, PharmGKB, NCBI Medical Genetics Summaries, ClinVar, dbSNP, DailyMed, and UniProt. **TODO — Information Required From Author** for funding sources, institutional acknowledgments, or additional third-party data acknowledgments required by the journal.

## AI-Assisted Development Statement

Generative AI agents — specifically **OpenAI ChatGPT** and **Anthropic Claude** — assisted in the development of this pipeline and its repository. Their use was **assistive and tool-level only**, applied to:

- documentation drafting and formatting
- code refactoring suggestions
- debugging assistance
- general software engineering suggestions
- code optimization suggestions

All scientific design, biological and pharmacogenomic interpretation, machine learning methodology, validation strategy, experimental decisions, and final verification of all outputs were performed and approved by the author(s). No AI tool made scientific, clinical, or statistical judgments on behalf of the authors, and all AI-assisted contributions were reviewed and verified by the author(s) prior to inclusion.
