"""Single-file source of truth for the Pharmexia DNA pharmacogenomics application."""

from __future__ import annotations

import sys

if __name__ == "__main__":
    sys.modules.setdefault("oncox", sys.modules[__name__])

# --- begin merged module: src/constants.py ---
"""Central constants and curated local PGx knowledge."""


from typing import Any

# ── Branding constants (formerly src/branding.py) ────────────────────────────
APP_NAME = "Pharmexia"
APP_VERSION = "2.0.1"
API_TITLE = "Pharmexia PGx API"
DESKTOP_WINDOW_TITLE = "Pharmexia — DNA Pharmacogenomics"
EXPORT_BASENAME = "pharmexia_report"


# ── Inline stub for all_source_descriptors (formerly src/database_clients/__init__.py)
# Returns an empty list when no external database descriptors are configured.
class _SourceDescriptor:
    """Minimal evidence-source descriptor used by extract_oncox_metadata."""

    def __init__(self, name: str, url: str) -> None:
        self.name = name
        self.url = url

    def to_dict(self) -> dict:
        return {"name": self.name, "url": self.url}


def all_source_descriptors() -> "list[_SourceDescriptor]":
    """Return the curated list of external evidence-source descriptors."""
    return [
        _SourceDescriptor("ClinVar", "https://www.ncbi.nlm.nih.gov/clinvar/"),
        _SourceDescriptor("dbSNP", "https://www.ncbi.nlm.nih.gov/snp/"),
        _SourceDescriptor("UniProt", "https://www.uniprot.org/"),
        _SourceDescriptor("PharmGKB", "https://www.pharmgkb.org/"),
        _SourceDescriptor("PharmVar", "https://www.pharmvar.org/"),
    ]

SUPPORTED_VCF_EXTENSIONS = {".vcf", ".gz"}
SUPPORTED_TABLE_EXTENSIONS = {".csv", ".tsv", ".txt", ".json"}

SUPPORTED_INPUT_EXTENSIONS = SUPPORTED_VCF_EXTENSIONS | SUPPORTED_TABLE_EXTENSIONS

SUPPORTED_CONFIDENCE_CATEGORIES = {
    "EVIDENCE_BASED",
    "MODEL_ASSISTED",
    "INSUFFICIENT_EVIDENCE",
    "EXPLORATORY_ONLY",
}

REPORT_DISCLAIMER = (
    "This software is a pharmacogenomics decision-support aid. It does not replace "
    "clinical judgment, confirmatory laboratory validation, or drug labeling review."
)

REFERENCE_SOURCES: dict[str, dict[str, str]] = {
    "CPIC_WARFARIN": {
        "label": "CPIC guideline for warfarin and CYP2C9/VKORC1/CYP4F2",
        "url": "https://cpicpgx.org/guidelines/guideline-for-warfarin-and-cyp2c9-and-vkorc1/",
    },
    "CPIC_CLOPIDOGREL": {
        "label": "CPIC guideline for clopidogrel and CYP2C19",
        "url": "https://cpicpgx.org/guidelines/guideline-for-clopidogrel-and-cyp2c19/",
    },
    "CPIC_SSRI": {
        "label": "CPIC guideline for serotonin reuptake inhibitors and CYP2C19/CYP2D6/CYP2B6",
        "url": "https://cpicpgx.org/guidelines/guideline-for-selective-serotonin-reuptake-inhibitors-and-cyp2d6-and-cyp2c19/",
    },
    "CPIC_PPI": {
        "label": "CPIC guideline for proton pump inhibitors and CYP2C19",
        "url": "https://cpicpgx.org/guidelines/cpic-guideline-for-proton-pump-inhibitors-and-cyp2c19/",
    },
    "CPIC_VORICONAZOLE": {
        "label": "CPIC guideline for voriconazole and CYP2C19",
        "url": "https://cpicpgx.org/guidelines/guideline-for-voriconazole-and-cyp2c19/",
    },
    "CPIC_STATINS": {
        "label": "CPIC guideline for statins and SLCO1B1/ABCG2/CYP2C9",
        "url": "https://cpicpgx.org/guidelines/cpic-guideline-for-statins/",
    },
    "CPIC_THIOPURINES": {
        "label": "CPIC guideline for thiopurines and TPMT/NUDT15",
        "url": "https://cpicpgx.org/guidelines/guideline-for-thiopurines-and-tpmt/",
    },
    "CPIC_TACROLIMUS": {
        "label": "CPIC guideline for tacrolimus and CYP3A5",
        "url": "https://cpicpgx.org/guidelines/guideline-for-tacrolimus-and-cyp3a5/",
    },
    "CPIC_FLUOROPYRIMIDINES": {
        "label": "CPIC guideline for fluoropyrimidines and DPYD",
        "url": "https://cpicpgx.org/guidelines/guideline-for-fluoropyrimidines-and-dpyd/",
    },
    "PHARMGKB": {
        "label": "PharmGKB pharmacogenomics knowledge base",
        "url": "https://www.pharmgkb.org/",
    },
    "PHARMVAR": {
        "label": "PharmVar pharmacogene allele nomenclature",
        "url": "https://www.pharmvar.org/",
    },
    "NCBI_WARFARIN": {
        "label": "NCBI Medical Genetics Summary for warfarin therapy",
        "url": "https://www.ncbi.nlm.nih.gov/books/NBK84174/",
    },
    "NCBI_CLOPIDOGREL": {
        "label": "NCBI Medical Genetics Summary for clopidogrel therapy",
        "url": "https://www.ncbi.nlm.nih.gov/books/NBK84114/",
    },
    "NCBI_SIMVASTATIN": {
        "label": "NCBI Medical Genetics Summary for simvastatin therapy",
        "url": "https://www.ncbi.nlm.nih.gov/books/NBK602238/",
    },
    "NCBI_THIOPURINES": {
        "label": "NCBI Medical Genetics Summary for thiopurine therapy",
        "url": "https://www.ncbi.nlm.nih.gov/books/NBK100660/",
    },
    "DAILYMED_CITALOPRAM": {
        "label": "DailyMed label search for citalopram",
        "url": "https://dailymed.nlm.nih.gov/dailymed/search.cfm?query=citalopram",
    },
    "DAILYMED_ESCITALOPRAM": {
        "label": "DailyMed label search for escitalopram",
        "url": "https://dailymed.nlm.nih.gov/dailymed/search.cfm?query=escitalopram",
    },
    "DAILYMED_SERTRALINE": {
        "label": "DailyMed label search for sertraline",
        "url": "https://dailymed.nlm.nih.gov/dailymed/search.cfm?query=sertraline",
    },
    "DAILYMED_CLOPIDOGREL": {
        "label": "DailyMed label search for clopidogrel",
        "url": "https://dailymed.nlm.nih.gov/dailymed/search.cfm?query=clopidogrel",
    },
    "DAILYMED_OMEPRAZOLE": {
        "label": "DailyMed label search for omeprazole",
        "url": "https://dailymed.nlm.nih.gov/dailymed/search.cfm?query=omeprazole",
    },
    "DAILYMED_LANSOPRAZOLE": {
        "label": "DailyMed label search for lansoprazole",
        "url": "https://dailymed.nlm.nih.gov/dailymed/search.cfm?query=lansoprazole",
    },
    "DAILYMED_PANTOPRAZOLE": {
        "label": "DailyMed label search for pantoprazole",
        "url": "https://dailymed.nlm.nih.gov/dailymed/search.cfm?query=pantoprazole",
    },
    "DAILYMED_VORICONAZOLE": {
        "label": "DailyMed label search for voriconazole",
        "url": "https://dailymed.nlm.nih.gov/dailymed/search.cfm?query=voriconazole",
    },
    "DAILYMED_WARFARIN": {
        "label": "DailyMed label search for warfarin",
        "url": "https://dailymed.nlm.nih.gov/dailymed/search.cfm?query=warfarin",
    },
    "DAILYMED_SIMVASTATIN": {
        "label": "DailyMed label search for simvastatin",
        "url": "https://dailymed.nlm.nih.gov/dailymed/search.cfm?query=simvastatin",
    },
    "DAILYMED_TACROLIMUS": {
        "label": "DailyMed label search for tacrolimus",
        "url": "https://dailymed.nlm.nih.gov/dailymed/search.cfm?query=tacrolimus",
    },
    "DAILYMED_FLUOROURACIL": {
        "label": "DailyMed label search for fluorouracil",
        "url": "https://dailymed.nlm.nih.gov/dailymed/search.cfm?query=fluorouracil",
    },
    "DAILYMED_CAPECITABINE": {
        "label": "DailyMed label search for capecitabine",
        "url": "https://dailymed.nlm.nih.gov/dailymed/search.cfm?query=capecitabine",
    },
}

ALLELE_DEFINITIONS: dict[str, list[dict[str, Any]]] = {
    "CYP2C19": [
        {
            "rsid": "rs4244285",
            "alt": "A",
            "allele": "*2",
            "function": "no_function",
            "effect": "reduced_cyp2c19_activity",
            "sources": ["CPIC_CLOPIDOGREL", "NCBI_CLOPIDOGREL"],
        },
        {
            "rsid": "rs4986893",
            "alt": "A",
            "allele": "*3",
            "function": "no_function",
            "effect": "reduced_cyp2c19_activity",
            "sources": ["CPIC_CLOPIDOGREL", "NCBI_CLOPIDOGREL"],
        },
        {
            "rsid": "rs12248560",
            "alt": "T",
            "allele": "*17",
            "function": "increased_function",
            "effect": "increased_cyp2c19_activity",
            "sources": ["CPIC_CLOPIDOGREL", "NCBI_CLOPIDOGREL"],
        },
    ],
    "CYP2C9": [
        {
            "rsid": "rs1799853",
            "alt": "T",
            "allele": "*2",
            "function": "decreased_function",
            "effect": "reduced_warfarin_clearance",
            "sources": ["CPIC_WARFARIN", "NCBI_WARFARIN"],
        },
        {
            "rsid": "rs1057910",
            "alt": "C",
            "allele": "*3",
            "function": "decreased_function",
            "effect": "reduced_warfarin_clearance",
            "sources": ["CPIC_WARFARIN", "NCBI_WARFARIN"],
        },
    ],
    "CYP2D6": [
        {
            "rsid": "rs3892097",
            "alt": "A",
            "allele": "*4",
            "function": "no_function",
            "effect": "reduced_or_absent_cyp2d6_activity",
            "sources": ["CPIC_SSRI", "PHARMVAR"],
        },
        {
            "rsid": "rs1065852",
            "alt": "T",
            "allele": "*10",
            "function": "decreased_function",
            "effect": "reduced_cyp2d6_activity",
            "sources": ["CPIC_SSRI", "PHARMVAR"],
        },
    ],
    "CYP3A5": [
        {
            "rsid": "rs776746",
            "alt": "G",
            "allele": "*3",
            "function": "no_function",
            "effect": "reduced_cyp3a5_expression",
            "sources": ["CPIC_TACROLIMUS", "PHARMVAR"],
        }
    ],
    "VKORC1": [
        {
            "rsid": "rs9923231",
            "alt": "A",
            "effect": "increased_warfarin_sensitivity",
            "sources": ["CPIC_WARFARIN", "NCBI_WARFARIN"],
        }
    ],
    "SLCO1B1": [
        {
            "rsid": "rs4149056",
            "alt": "C",
            "allele": "*5",
            "effect": "increased_simvastatin_myopathy_risk",
            "function": "decreased_function",
            "sources": ["CPIC_STATINS", "NCBI_SIMVASTATIN"],
        }
    ],
    "DPYD": [
        {
            "rsid": "rs3918290",
            "alt": "T",
            "allele": "*2A",
            "function": "no_function",
            "effect": "reduced_dpyd_activity",
            "sources": ["CPIC_FLUOROPYRIMIDINES", "PHARMVAR"],
        },
        {
            "rsid": "rs67376798",
            "alt": "T",
            "allele": "c.2846A>T",
            "function": "decreased_function",
            "effect": "reduced_dpyd_activity",
            "sources": ["CPIC_FLUOROPYRIMIDINES", "PHARMVAR"],
        },
    ],
    "TPMT": [
        {
            "rsid": "rs1800462",
            "alt": "C",
            "allele": "*2",
            "function": "no_function",
            "effect": "thiopurine_toxicity_risk",
            "sources": ["CPIC_THIOPURINES", "NCBI_THIOPURINES"],
        },
        {
            "rsid": "rs1800460",
            "alt": "A",
            "allele": "*3B_component",
            "function": "no_function",
            "effect": "thiopurine_toxicity_risk",
            "sources": ["CPIC_THIOPURINES", "NCBI_THIOPURINES"],
        },
        {
            "rsid": "rs1142345",
            "alt": "G",
            "allele": "*3C_component",
            "function": "no_function",
            "effect": "thiopurine_toxicity_risk",
            "sources": ["CPIC_THIOPURINES", "NCBI_THIOPURINES"],
        },
    ],
    "NUDT15": [
        {
            "rsid": "rs116855232",
            "alt": "T",
            "allele": "*3",
            "function": "no_function",
            "effect": "thiopurine_toxicity_risk",
            "sources": ["CPIC_THIOPURINES", "NCBI_THIOPURINES"],
        }
    ],
}


# Strand handling. Rule-file ALT alleles are written on the gene (coding) strand.
# TPMT and VKORC1 are encoded on the reverse strand of GRCh38, so a standard VCF
# reports these loci on the forward strand. Map: rsID -> (forward REF, forward ALT).
FORWARD_STRAND_ALLELES: dict[str, tuple[str, str]] = {
    "rs1800462": ("C", "G"),  # TPMT *2
    "rs1800460": ("C", "T"),  # TPMT *3B/*3A component
    "rs1142345": ("T", "C"),  # TPMT *3C/*3A component
    "rs9923231": ("C", "T"),  # VKORC1 -1639G>A
}
_COMPLEMENT = {"A": "T", "T": "A", "C": "G", "G": "C"}


def alt_matches_definition(variant_ref: str | None, variant_alt: str | None, definition: dict[str, Any]) -> bool:
    """True when the observed ALT equals the rule ALT, on either the gene strand or the forward strand."""
    if variant_alt is None:
        return False
    alt = str(variant_alt).upper()
    ref = str(variant_ref).upper() if variant_ref else None
    coding_alt = str(definition.get("alt")).upper()
    forward = FORWARD_STRAND_ALLELES.get(str(definition.get("rsid")))
    if forward is None:
        return alt == coding_alt
    fwd_ref, fwd_alt = forward
    if alt == fwd_alt and (ref is None or ref == fwd_ref):
        return True
    # gene-strand notation: REF must be the complement of the forward REF when supplied
    return alt == coding_alt and (ref is None or ref == _COMPLEMENT[fwd_ref])

RSID_TO_GENE = {
    definition["rsid"]: gene
    for gene, definitions in ALLELE_DEFINITIONS.items()
    for definition in definitions
}

GENE_TARGET_LOCI = {
    gene: sorted({definition["rsid"] for definition in definitions})
    for gene, definitions in ALLELE_DEFINITIONS.items()
}

SUPPORTED_PHARMACOGENES = sorted(ALLELE_DEFINITIONS)

DRUG_GENE_RULES: dict[str, dict[str, Any]] = {
    "warfarin": {
        "genes": ["CYP2C9", "VKORC1"],
        "headline": "Warfarin exposure and dose requirements are affected by CYP2C9 and VKORC1.",
        "limitations": [
            "Do not emit a numeric dose without a validated clinical dosing algorithm and INR context.",
            "CYP4F2 and ancestry-specific warfarin modifiers are not inferred by the local rule set.",
        ],
    },
    "clopidogrel": {
        "genes": ["CYP2C19"],
        "headline": "Clopidogrel activation depends on CYP2C19 function.",
        "limitations": [
            "Therapy selection depends on indication, clinical urgency, and competing bleeding or thrombosis risks.",
        ],
    },
    "citalopram": {
        "genes": ["CYP2C19"],
        "headline": "CYP2C19 function can alter citalopram exposure.",
        "limitations": [
            "This local rule reflects CYP2C19 only and does not model broader antidepressant selection context or QT-related safety factors.",
            "Do not auto-adjust dose or switch antidepressant therapy from this application alone.",
        ],
    },
    "escitalopram": {
        "genes": ["CYP2C19"],
        "headline": "CYP2C19 function can alter escitalopram exposure.",
        "limitations": [
            "This local rule reflects CYP2C19 only and does not model broader antidepressant selection context or QT-related safety factors.",
            "Do not auto-adjust dose or switch antidepressant therapy from this application alone.",
        ],
    },
    "sertraline": {
        "genes": ["CYP2C19"],
        "headline": "CYP2C19 function can alter sertraline exposure.",
        "limitations": [
            "This local rule reflects CYP2C19 only and does not model CYP2B6 or broader antidepressant selection context.",
            "Do not auto-adjust dose or switch antidepressant therapy from this application alone.",
        ],
    },
    "omeprazole": {
        "genes": ["CYP2C19"],
        "headline": "CYP2C19 function can alter omeprazole exposure and acid suppression.",
        "limitations": [
            "This local rule reflects CYP2C19 only and does not account for indication, treatment duration, or interacting medications.",
            "Do not auto-adjust proton pump inhibitor dose or duration from this application alone.",
        ],
    },
    "lansoprazole": {
        "genes": ["CYP2C19"],
        "headline": "CYP2C19 function can alter lansoprazole exposure and acid suppression.",
        "limitations": [
            "This local rule reflects CYP2C19 only and does not account for indication, treatment duration, or interacting medications.",
            "Do not auto-adjust proton pump inhibitor dose or duration from this application alone.",
        ],
    },
    "pantoprazole": {
        "genes": ["CYP2C19"],
        "headline": "CYP2C19 function can alter pantoprazole exposure and acid suppression.",
        "limitations": [
            "This local rule reflects CYP2C19 only and does not account for indication, treatment duration, or interacting medications.",
            "Do not auto-adjust proton pump inhibitor dose or duration from this application alone.",
        ],
    },
    "voriconazole": {
        "genes": ["CYP2C19"],
        "headline": "CYP2C19 function can alter voriconazole exposure.",
        "limitations": [
            "Voriconazole use requires clinical context, therapeutic drug monitoring when appropriate, and review of the current indication.",
            "Do not auto-select an antifungal regimen or dose from this application alone.",
        ],
    },
    "simvastatin": {
        "genes": ["SLCO1B1"],
        "headline": "SLCO1B1 reduced function increases simvastatin-associated muscle toxicity risk.",
        "limitations": [
            "This local rule uses rs4149056 as a proxy and does not reconstruct full SLCO1B1 star alleles.",
        ],
    },
    "tacrolimus": {
        "genes": ["CYP3A5"],
        "headline": "CYP3A5 expression status is relevant to tacrolimus pharmacokinetics.",
        "limitations": [
            "This local rule covers only the CYP3A5 rs776746 (*3) marker and does not reconstruct *6, *7, or ancestry-specific haplotypes.",
            "Do not emit a tacrolimus dose without transplant context, therapeutic drug monitoring, interacting-medication review, and validated clinical implementation.",
        ],
    },
    "fluorouracil": {
        "genes": ["DPYD"],
        "headline": "Reduced DPYD function is associated with fluoropyrimidine toxicity risk.",
        "limitations": [
            "This local rule covers only a limited DPYD variant subset and does not compute a complete DPD activity score.",
            "Do not emit fluoropyrimidine dosing recommendations without validated DPYD testing and oncology clinical context.",
        ],
    },
    "capecitabine": {
        "genes": ["DPYD"],
        "headline": "Reduced DPYD function is associated with fluoropyrimidine toxicity risk.",
        "limitations": [
            "This local rule covers only a limited DPYD variant subset and does not compute a complete DPD activity score.",
            "Do not emit fluoropyrimidine dosing recommendations without validated DPYD testing and oncology clinical context.",
        ],
    },
    "azathioprine": {
        "genes": ["TPMT", "NUDT15"],
        "headline": "Thiopurine toxicity risk is increased by reduced TPMT or NUDT15 activity.",
        "limitations": [
            "Dose guidance requires validated TPMT/NUDT15 testing and clinical blood-count monitoring.",
        ],
    },
    "mercaptopurine": {
        "genes": ["TPMT", "NUDT15"],
        "headline": "Thiopurine toxicity risk is increased by reduced TPMT or NUDT15 activity.",
        "limitations": [
            "Dose guidance requires validated TPMT/NUDT15 testing and clinical blood-count monitoring.",
        ],
    },
    "thioguanine": {
        "genes": ["TPMT", "NUDT15"],
        "headline": "Thiopurine toxicity risk is increased by reduced TPMT or NUDT15 activity.",
        "limitations": [
            "Dose guidance requires validated TPMT/NUDT15 testing and clinical blood-count monitoring.",
        ],
    },
}

DRUG_FAMILY_LABELS = {
    "warfarin": "Anticoagulant",
    "clopidogrel": "Antiplatelet",
    "citalopram": "SSRI",
    "escitalopram": "SSRI",
    "sertraline": "SSRI",
    "omeprazole": "Proton Pump Inhibitor",
    "lansoprazole": "Proton Pump Inhibitor",
    "pantoprazole": "Proton Pump Inhibitor",
    "voriconazole": "Antifungal",
    "simvastatin": "Statin",
    "tacrolimus": "Calcineurin Inhibitor",
    "fluorouracil": "Fluoropyrimidine",
    "capecitabine": "Fluoropyrimidine",
    "azathioprine": "Thiopurine",
    "mercaptopurine": "Thiopurine",
    "thioguanine": "Thiopurine",
}

DRUG_REFERENCE_SOURCE_KEYS: dict[str, list[str]] = {
    "warfarin": ["CPIC_WARFARIN", "NCBI_WARFARIN"],
    "clopidogrel": ["CPIC_CLOPIDOGREL", "NCBI_CLOPIDOGREL"],
    "citalopram": ["CPIC_SSRI", "DAILYMED_CITALOPRAM"],
    "escitalopram": ["CPIC_SSRI", "DAILYMED_ESCITALOPRAM"],
    "sertraline": ["CPIC_SSRI", "DAILYMED_SERTRALINE"],
    "omeprazole": ["CPIC_PPI", "DAILYMED_OMEPRAZOLE"],
    "lansoprazole": ["CPIC_PPI", "DAILYMED_LANSOPRAZOLE"],
    "pantoprazole": ["CPIC_PPI", "DAILYMED_PANTOPRAZOLE"],
    "voriconazole": ["CPIC_VORICONAZOLE", "DAILYMED_VORICONAZOLE"],
    "simvastatin": ["CPIC_STATINS", "NCBI_SIMVASTATIN"],
    "tacrolimus": ["CPIC_TACROLIMUS", "DAILYMED_TACROLIMUS"],
    "fluorouracil": ["CPIC_FLUOROPYRIMIDINES", "DAILYMED_FLUOROURACIL"],
    "capecitabine": ["CPIC_FLUOROPYRIMIDINES", "DAILYMED_CAPECITABINE"],
    "azathioprine": ["CPIC_THIOPURINES", "NCBI_THIOPURINES"],
    "mercaptopurine": ["CPIC_THIOPURINES", "NCBI_THIOPURINES"],
    "thioguanine": ["CPIC_THIOPURINES", "NCBI_THIOPURINES"],
}


def drug_display_label(drug: str) -> str:
    """Return a user-facing drug label for the supported local PGx contexts."""
    return str(drug).replace("_", " ").title()


def supported_drug_catalog() -> list[dict[str, object]]:
    """Expose the locally supported drug contexts as stable UI metadata."""
    catalog: list[dict[str, object]] = []
    for drug in sorted(DRUG_GENE_RULES):
        rule = DRUG_GENE_RULES[drug]
        genes = list(rule["genes"])
        variants = sorted({rsid for gene in genes for rsid in GENE_TARGET_LOCI.get(gene, [])})
        source_keys = list(DRUG_REFERENCE_SOURCE_KEYS.get(drug, []))
        evidence_sources = [REFERENCE_SOURCES[key]["label"] for key in source_keys if key in REFERENCE_SOURCES]
        catalog.append(
            {
                "key": drug,
                "label": drug_display_label(drug),
                "family": DRUG_FAMILY_LABELS.get(drug, "Pharmacogenomics"),
                "genes": genes,
                "variants": variants,
                "evidence_sources": evidence_sources,
                "evidence_source_keys": source_keys,
                "support_tier": "PARTIAL_EVIDENCE_SUPPORT",
                "support_confidence": "Moderate local evidence coverage",
                "last_updated": None,
                "headline": str(rule["headline"]),
                "evidence_summary": (
                    "Curated local PGx rule support exists for this drug context, but Pharmexia does not claim "
                    "full FDA-wide evidence coverage or complete clinical implementation."
                ),
                "limitations": list(rule["limitations"]),
            }
        )
    return catalog

# --- end merged module: src/constants.py ---

# --- begin merged module: src/oncox_bridge.py ---
"""Compact project metadata bridge for scripts and tests."""




def extract_oncox_metadata() -> dict[str, object]:
    """Return stable package metadata without importing the desktop UI."""
    return {
        "app_name": APP_NAME,
        "app_version": APP_VERSION,
        "supported_drugs": sorted(DRUG_GENE_RULES),
        "supported_drug_catalog": supported_drug_catalog(),
        "evidence_source_catalog": [descriptor.to_dict() for descriptor in all_source_descriptors()],
    }

# --- end merged module: src/oncox_bridge.py ---

# --- begin merged module: src/schemas.py ---
"""Dataclasses used across the Pharmexia PGx codebase."""


from dataclasses import asdict, dataclass, field
from pathlib import Path
from typing import Any, Literal


OutputCategory = Literal[
    "EVIDENCE_BASED",
    "MODEL_ASSISTED",
    "INSUFFICIENT_EVIDENCE",
    "EXPLORATORY_ONLY",
]

ResultKind = Literal[
    "CONFIRMED_PGX_FINDING",
    "PREDICTIVE_MODEL_SUGGESTION",
    "RESEARCH_ONLY_HYPOTHESIS",
    "SAFETY_BLOCK",
]

PipelineStepStatus = Literal["success", "warning", "failed", "skipped"]
EvidenceAvailabilityStatus = Literal["available", "partial", "unavailable"]
EvidenceOrigin = Literal["evidence_based", "model_assisted", "review_only"]
InteractionType = Literal["drug_drug", "drug_gene", "drug_enzyme", "drug_transporter", "unsupported_drug", "medication_context"]
InteractionSeverity = Literal[
    "CONTRAINDICATED",
    "MAJOR",
    "MODERATE",
    "MINOR",
    "UNKNOWN",
    "HIGH",
    "LOW",
    "INFORMATIONAL",
    "UNSUPPORTED",
]
InteractionStatus = Literal["supported", "insufficient_evidence", "unsupported"]
InteractionEvidenceCategory = Literal[
    "EVIDENCE_BASED",
    "DATABASE_SUPPORTED",
    "GENERAL_PHARMACOLOGY_ONLY",
    "INSUFFICIENT_EVIDENCE",
]
VariantEffectType = Literal["SYNONYMOUS", "MISSENSE", "NONSENSE", "FRAMESHIFT", "REGULATORY", "UNKNOWN_EFFECT"]
VariantEffectConfidence = Literal["HIGH", "MODERATE", "LIMITED", "UNKNOWN"]
PathogenicityLabel = Literal[
    "PATHOGENIC",
    "LIKELY_PATHOGENIC",
    "BENIGN",
    "LIKELY_BENIGN",
    "UNCERTAIN_SIGNIFICANCE",
    "UNSPECIFIED",
]


@dataclass(slots=True)
class FileValidationResult:
    is_valid: bool
    detected_format: str
    input_mode: str
    message: str = ""
    warnings: list[str] = field(default_factory=list)

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


@dataclass(slots=True)
class ObservedVariant:
    chrom: str | None
    pos: int | None
    ref: str | None
    alt: str | None
    rsid: str | None
    genotype: str
    genotype_code: int | None
    sample_id: str | None = None
    gene: str | None = None
    source: str = "input"
    info: dict[str, Any] = field(default_factory=dict)

    @property
    def token(self) -> str:
        if self.rsid:
            return self.rsid
        if self.chrom and self.pos and self.ref and self.alt:
            return f"{self.chrom}:{self.pos}:{self.ref}>{self.alt}"
        return "unknown_variant"

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


@dataclass(slots=True)
class AlleleMatch:
    gene: str
    rsid: str
    alt: str
    allele: str | None
    function: str | None
    effect: str
    genotype: str
    genotype_code: int
    sources: list[str]

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


@dataclass(slots=True)
class GeneAssessment:
    gene: str
    observed_target_loci: list[str] = field(default_factory=list)
    expected_target_loci: list[str] = field(default_factory=list)
    matched_alleles: list[AlleleMatch] = field(default_factory=list)
    local_panel_call: str | None = None
    phenotype: str | None = None
    call_confidence: str = "INCONCLUSIVE"
    coverage_complete: bool = False
    ambiguous: bool = False
    limitations: list[str] = field(default_factory=list)

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


@dataclass(slots=True)
class EvidenceRecord:
    source: str
    label: str
    assertion: str
    source_module: str
    evidence_type: str
    url: str | None = None
    status: str = "available"
    details: dict[str, Any] = field(default_factory=dict)

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


@dataclass(slots=True)
class StructuredEvidence:
    source_name: str
    source_record_id: str | None
    evidence_type: str
    clinical_relevance: str
    confidence: str
    citation_url: str | None = None
    normalized_gene: str | None = None
    normalized_variant: str | None = None
    normalized_drug: str | None = None
    protein_id: str | None = None
    interpretation_text: str = ""
    source_module: str = ""
    status: str = "available"
    details: dict[str, Any] = field(default_factory=dict)

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)

    def to_evidence_record(self) -> EvidenceRecord:
        label = self.normalized_gene or self.normalized_variant or self.normalized_drug or self.source_name
        return EvidenceRecord(
            source=self.source_name,
            label=label,
            assertion=self.interpretation_text,
            source_module=self.source_module or "src.evidence_integration",
            evidence_type=self.evidence_type,
            url=self.citation_url,
            status=self.status,
            details={
                "source_record_id": self.source_record_id,
                "clinical_relevance": self.clinical_relevance,
                "confidence": self.confidence,
                "normalized_gene": self.normalized_gene,
                "normalized_variant": self.normalized_variant,
                "normalized_drug": self.normalized_drug,
                "protein_id": self.protein_id,
                **self.details,
            },
        )


@dataclass(slots=True)
class EvidenceConflict:
    context_key: str
    issue: str
    conflicting_values: list[str] = field(default_factory=list)
    source_names: list[str] = field(default_factory=list)
    resolution: str = ""

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


@dataclass(slots=True)
class EvidenceAggregate:
    normalized_gene: str | None = None
    normalized_variant: str | None = None
    normalized_drug: str | None = None
    local_rule_evidence: list[StructuredEvidence] = field(default_factory=list)
    external_annotation: list[StructuredEvidence] = field(default_factory=list)
    merged_evidence: list[StructuredEvidence] = field(default_factory=list)
    conflicts: list[EvidenceConflict] = field(default_factory=list)
    final_evidence_summary: str = ""
    availability_status: EvidenceAvailabilityStatus = "unavailable"

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


@dataclass(slots=True)
class NormalizedEvidenceRecord:
    source_name: str
    source_type: str
    source_record_id: str | None
    drug_name: str | None = None
    normalized_drug_name: str | None = None
    drug_status: str = "unknown"
    gene_symbol: str | None = None
    variant_id: str | None = None
    protein_id: str | None = None
    pathway_id: str | None = None
    evidence_type: str = "unspecified"
    evidence_strength: str = "unknown"
    clinical_relevance: str = ""
    pk_relevance: str = ""
    pd_relevance: str = ""
    pharmacology_relevance: str = ""
    pharmacognosy_relevance: str = ""
    interpretation_text: str = ""
    citation_url: str | None = None
    last_updated: str | None = None
    confidence_score: float | None = None
    coverage_status: str = "partial"
    source_module: str = ""
    evidence_origin: EvidenceOrigin = "evidence_based"
    status: str = "available"
    clinical_grade: bool = False
    exploratory: bool = False
    details: dict[str, Any] = field(default_factory=dict)

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


@dataclass(slots=True)
class MergedEvidenceBundle:
    normalized_drug_name: str | None = None
    gene_symbol: str | None = None
    variant_id: str | None = None
    records: list[NormalizedEvidenceRecord] = field(default_factory=list)
    evidence_based_records: list[NormalizedEvidenceRecord] = field(default_factory=list)
    model_assisted_records: list[NormalizedEvidenceRecord] = field(default_factory=list)
    review_only_records: list[NormalizedEvidenceRecord] = field(default_factory=list)
    source_summary: dict[str, int] = field(default_factory=dict)
    strength_summary: dict[str, int] = field(default_factory=dict)
    conflict_messages: list[str] = field(default_factory=list)
    conflict_details: list[dict[str, Any]] = field(default_factory=list)
    output_category: OutputCategory = "INSUFFICIENT_EVIDENCE"
    availability_status: EvidenceAvailabilityStatus = "unavailable"
    summary: str = ""
    has_actionable_evidence: bool = False
    model_assistance_allowed: bool = True

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


@dataclass(slots=True)
class InteractionProvenance:
    source_name: str
    source_record_id: str | None
    evidence_type: str
    citation_url: str | None = None
    source_module: str = ""
    note: str = ""

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


@dataclass(slots=True)
class DrugInteractionFinding:
    interaction_id: str
    interaction_type: InteractionType
    subject_drug: str
    interacting_entity: str
    entity_type: str
    severity: InteractionSeverity
    status: InteractionStatus
    confidence: str
    summary: str
    clinical_relevance: str
    evidence_category: InteractionEvidenceCategory = "INSUFFICIENT_EVIDENCE"
    mechanism: str = ""
    recommendation: str | None = None
    evidence_based: bool = True
    provenance: list[InteractionProvenance] = field(default_factory=list)
    limitations: list[str] = field(default_factory=list)

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


@dataclass(slots=True)
class ConfidenceAssessment:
    category: OutputCategory
    evidence_strength: str
    data_completeness: str
    rationale: list[str] = field(default_factory=list)

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


@dataclass(slots=True)
class DrugFinding:
    drug: str
    gene: str
    category: OutputCategory
    result_kind: ResultKind
    summary: str
    recommendation: str
    confidence: ConfidenceAssessment
    source_module: str
    evidence_type: str
    clinical_grade: bool = False
    exploratory: bool = False
    provenance: list[EvidenceRecord] = field(default_factory=list)
    phenotype: str | None = None
    diplotype: str | None = None
    matched_variants: list[str] = field(default_factory=list)
    explanation: dict[str, Any] | None = None
    safety_notes: list[str] = field(default_factory=list)
    limitations: list[str] = field(default_factory=list)

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


@dataclass(slots=True)
class FeatureProvenance:
    name: str
    description: str
    source_stage: str
    feature_group: str
    derived_from: list[str] = field(default_factory=list)
    role: str = "exploratory_model_only"

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


@dataclass(slots=True)
class VariantEffectPrediction:
    variant_token: str
    gene: str
    effect_type: VariantEffectType = "UNKNOWN_EFFECT"
    effect_confidence: VariantEffectConfidence = "UNKNOWN"
    pathogenicity_label: PathogenicityLabel = "UNSPECIFIED"
    pathogenicity_confidence: VariantEffectConfidence = "UNKNOWN"
    normalized_variant: str | None = None
    protein_effect: str | None = None
    protein_id: str | None = None
    transcript_id: str | None = None
    consequence_terms: list[str] = field(default_factory=list)
    annotation_source: str = "unavailable"
    availability_status: EvidenceAvailabilityStatus = "unavailable"
    summary: str = ""
    reasoning: list[str] = field(default_factory=list)

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


@dataclass(slots=True)
class VariantEvidenceAnnotation:
    variant_token: str
    gene: str
    rsid: str | None = None
    variant_effect: VariantEffectPrediction | None = None
    matched_alleles: list[str] = field(default_factory=list)
    matched_effects: list[str] = field(default_factory=list)
    evidence_records: list[EvidenceRecord] = field(default_factory=list)
    structured_evidence: list[StructuredEvidence] = field(default_factory=list)
    conflicts: list[EvidenceConflict] = field(default_factory=list)
    final_evidence_summary: str = ""
    availability_status: EvidenceAvailabilityStatus = "unavailable"

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


@dataclass(slots=True)
class PipelineStepResult:
    order: int
    key: str
    label: str
    status: PipelineStepStatus
    message: str
    metadata: dict[str, Any] = field(default_factory=dict)
    warnings: list[str] = field(default_factory=list)
    errors: list[str] = field(default_factory=list)

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


@dataclass(slots=True)
class PipelineExecutionSummary:
    overall_status: PipelineStepStatus
    message: str
    step_results: list[PipelineStepResult] = field(default_factory=list)
    total_steps: int = 0
    completed_steps: int = 0
    warning_steps: int = 0
    failed_steps: int = 0
    skipped_steps: int = 0
    can_export: bool = False

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


@dataclass(slots=True)
class ExportArtifact:
    filename: str
    media_type: str
    payload: dict[str, Any] = field(default_factory=dict)

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


@dataclass(slots=True)
class PatientClinicalProfile:
    age: int | None = None
    sex: str | None = None
    diagnosis: str | None = None
    liver_function: str | None = None
    kidney_function: str | None = None
    current_medications: list[str] = field(default_factory=list)
    allergies: list[str] = field(default_factory=list)
    dose: str | None = None

    def used_fields(self) -> list[str]:
        fields: list[str] = []
        if self.age is not None:
            fields.append("age")
        if self.sex:
            fields.append("sex")
        if self.diagnosis:
            fields.append("diagnosis")
        if self.liver_function:
            fields.append("liver_function")
        if self.kidney_function:
            fields.append("kidney_function")
        if self.current_medications:
            fields.append("current_medications")
        if self.allergies:
            fields.append("allergies")
        if self.dose:
            fields.append("dose")
        return fields

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


@dataclass(slots=True)
class PatientProfileValidationResult:
    is_valid: bool
    status: str
    message: str
    warnings: list[str] = field(default_factory=list)
    used_fields: list[str] = field(default_factory=list)
    model_feature_fields: list[str] = field(default_factory=list)

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


@dataclass(slots=True)
class AnalysisPipelineRequest:
    path: Path | None = None
    input_variants: list[ObservedVariant] = field(default_factory=list)
    selected_drugs: list[str] = field(default_factory=list)
    enable_remote_lookup: bool = False
    model_artifact_path: Path | None = None
    provided_validation: FileValidationResult | None = None
    patient_profile: PatientClinicalProfile | dict[str, Any] | None = None
    multiomics_inputs: dict[str, Any] | None = None

    def to_dict(self) -> dict[str, Any]:
        payload = asdict(self)
        payload["path"] = str(self.path) if self.path is not None else None
        payload["model_artifact_path"] = (
            str(self.model_artifact_path) if self.model_artifact_path is not None else None
        )
        if isinstance(self.patient_profile, PatientClinicalProfile):
            payload["patient_profile"] = self.patient_profile.to_dict()
        return payload


@dataclass(slots=True)
class AnalysisPipelineState:
    request: AnalysisPipelineRequest
    validation: FileValidationResult | None = None
    patient_profile: PatientClinicalProfile | None = None
    patient_profile_validation: PatientProfileValidationResult | None = None
    clinical_fields_used: list[str] = field(default_factory=list)
    clinical_model_features_used: list[str] = field(default_factory=list)
    detected_format: str = "unknown"
    input_mode: str = "invalid"
    extracted_variants: list[ObservedVariant] = field(default_factory=list)
    extracted_sequences: list[dict[str, Any]] = field(default_factory=list)
    normalized_variants: list[ObservedVariant] = field(default_factory=list)
    pharmacogene_variants: list[ObservedVariant] = field(default_factory=list)
    evidence_annotations: list[VariantEvidenceAnnotation] = field(default_factory=list)
    aggregated_evidence: list[MergedEvidenceBundle] = field(default_factory=list)
    interaction_findings: list[DrugInteractionFinding] = field(default_factory=list)
    gene_assessments: dict[str, GeneAssessment] = field(default_factory=dict)
    resolved_selected_drugs: list[str] = field(default_factory=list)
    unsupported_selected_drugs: list[str] = field(default_factory=list)
    rule_findings: list[DrugFinding] = field(default_factory=list)
    confirmed_findings: list[DrugFinding] = field(default_factory=list)
    predictive_model_suggestions: list[DrugFinding] = field(default_factory=list)
    research_only_hypotheses: list[DrugFinding] = field(default_factory=list)
    safety_blocks: list[DrugFinding] = field(default_factory=list)
    findings: list[DrugFinding] = field(default_factory=list)
    variant_summary: dict[str, Any] = field(default_factory=dict)
    overall_category: OutputCategory = "INSUFFICIENT_EVIDENCE"
    safety_notes: list[str] = field(default_factory=list)
    limitations: list[str] = field(default_factory=list)
    model_summary: dict[str, Any] = field(default_factory=lambda: {"status": "disabled"})
    multiomics_contexts: dict[str, Any] = field(default_factory=dict)
    report_text: str = ""
    report_html: str = ""
    export_artifact: ExportArtifact | None = None

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


@dataclass(slots=True)
class AnalysisResult:
    input_mode: str
    validation: FileValidationResult
    patient_profile: PatientClinicalProfile | None
    patient_profile_validation: PatientProfileValidationResult | None
    clinical_fields_used: list[str]
    clinical_model_features_used: list[str]
    variant_summary: dict[str, Any]
    evidence_annotations: list[VariantEvidenceAnnotation]
    aggregated_evidence: list[MergedEvidenceBundle]
    interaction_findings: list[DrugInteractionFinding]
    findings: list[DrugFinding]
    confirmed_findings: list[DrugFinding]
    predictive_model_suggestions: list[DrugFinding]
    research_only_hypotheses: list[DrugFinding]
    safety_blocks: list[DrugFinding]
    gene_assessments: dict[str, GeneAssessment]
    overall_category: OutputCategory
    safety_notes: list[str]
    limitations: list[str]
    selected_drugs: list[str]
    model_summary: dict[str, Any]
    multiomics_contexts: dict[str, Any]
    pipeline_summary: PipelineExecutionSummary
    export_artifact: ExportArtifact | None
    report_text: str
    report_html: str

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)

# --- end merged module: src/schemas.py ---

# --- begin merged module: src/input_validation.py ---
"""Input validation for VCF and pharmacogene variant tables."""


import gzip
import json
from pathlib import Path

import pandas as pd



VARIANT_COLUMN_ALIASES = {
    "chrom": "chrom",
    "chromosome": "chrom",
    "#chrom": "chrom",
    "pos": "pos",
    "position": "pos",
    "ref": "ref",
    "reference": "ref",
    "alt": "alt",
    "alternate": "alt",
    "genotype": "genotype",
    "gt": "genotype",
    "rsid": "rsid",
    "id": "rsid",
    "gene": "gene",
    "sample": "sample_id",
    "sample_id": "sample_id",
}

UNSUPPORTED_SEQUENCE_EXTENSIONS = {".fasta", ".fa", ".fastq", ".fq"}


def _read_prefix(path: Path, n_lines: int = 5) -> list[str]:
    # Use the full filename to decide on gzip; path.suffix only returns the last
    # extension and would mis-classify "data.vcf.gz" as ".gz" while
    # "data.gz.vcf" would be wrongly treated as plain text.
    is_gz = path.name.lower().endswith(".gz")
    opener = gzip.open if is_gz else open
    mode = "rt"
    lines: list[str] = []
    try:
        with opener(path, mode, encoding="utf-8", errors="ignore") as handle:
            for _ in range(n_lines):
                line = handle.readline()
                if not line:
                    break
                stripped = line.strip()
                if stripped:
                    lines.append(stripped)
    except OSError:
        pass
    return lines


def validate_input_file(path: Path) -> FileValidationResult:
    """Validate a user-supplied file path and infer the supported input mode."""
    if not path.exists():
        return FileValidationResult(False, "unknown", "invalid", f"File not found: {path}")
    if path.stat().st_size == 0:
        return FileValidationResult(False, "unknown", "invalid", f"Empty file: {path.name}")

    name_lower = path.name.lower()

    # Reject raw sequence formats before anything else.
    if any(name_lower.endswith(ext) for ext in UNSUPPORTED_SEQUENCE_EXTENSIONS):
        return FileValidationResult(
            False,
            "sequence",
            "invalid",
            (
                "Raw DNA sequence files are not supported by this app. "
                "Provide a called VCF or a pharmacogene variant table instead."
            ),
        )

    # Determine the logical extension:
    # • Accept ".vcf" and ".vcf.gz" (and only those .gz variants).
    # • Accept table extensions (.csv, .tsv, .txt, .json).
    # • Reject any other .gz (e.g. "malware.exe.gz" would previously slip through).
    is_vcf_gz = name_lower.endswith(".vcf.gz")
    last_suffix = path.suffix.lower()

    if not is_vcf_gz and last_suffix == ".gz":
        return FileValidationResult(
            False,
            "unknown",
            "invalid",
            f"Unsupported compressed format: {path.name}. Only .vcf.gz is accepted as a compressed input.",
        )

    if not is_vcf_gz and last_suffix not in SUPPORTED_INPUT_EXTENSIONS:
        return FileValidationResult(
            False,
            "unknown",
            "invalid",
            f"Unsupported extension for {path.name}",
        )

    prefix = _read_prefix(path)
    if any(line.startswith("#CHROM") for line in prefix):
        return FileValidationResult(True, "vcf", "variant", "Validated DNA variant input (VCF)")
    if prefix and prefix[0].startswith(">"):
        return FileValidationResult(
            False,
            "sequence",
            "invalid",
            (
                "Raw DNA sequence files are not supported by this app. "
                "Provide a called VCF or a pharmacogene variant table instead."
            ),
        )
    if is_vcf_gz:
        # Compressed but no #CHROM header found in prefix — still treat as VCF
        # (the header might be after large meta-info blocks; downstream parsing
        # will catch a true format error).
        return FileValidationResult(True, "vcf", "variant", "Validated compressed VCF input (.vcf.gz)")
    if last_suffix in SUPPORTED_TABLE_EXTENSIONS:
        return FileValidationResult(
            True,
            "variant_table",
            "variant",
            "Validated pharmacogene variant table input",
        )

    return FileValidationResult(False, "unknown", "invalid", f"Could not classify input: {path.name}")


def normalize_variant_dataframe(df: pd.DataFrame) -> pd.DataFrame:
    """Normalize common variant-table column names to the internal schema."""
    renamed = {}
    for column in df.columns:
        normalized = VARIANT_COLUMN_ALIASES.get(str(column).strip().lower())
        if normalized:
            renamed[column] = normalized
    if renamed:
        df = df.rename(columns=renamed)
    return df


def validate_variant_dataframe(df: pd.DataFrame) -> tuple[bool, str]:
    """Validate that a dataframe has enough structure for variant analysis."""
    if df is None or df.empty:
        return False, "Variant table is empty."

    df = normalize_variant_dataframe(df)
    if "genotype" not in df.columns:
        return False, "Variant table must include a genotype/GT column."

    supported_identity = {"rsid", "chrom", "pos"}
    if not supported_identity.intersection(df.columns):
        return False, "Variant table must include rsid or chrom/pos coordinates."
    return True, ""


def load_variant_table(path: Path) -> pd.DataFrame:
    """Read a variant table from CSV/TSV/TXT/JSON and normalize columns.

    The delimiter is chosen explicitly from the file extension.
    For .txt files a controlled peek at the first line is used to detect
    tab vs. comma rather than relying on Python's CSV sniffer, which can
    produce incorrect column splits on medically formatted data.
    """
    suffix = path.suffix.lower()
    if suffix == ".json":
        data = json.loads(path.read_text(encoding="utf-8"))
        if isinstance(data, dict) and "variants" in data:
            frame = pd.DataFrame(data["variants"])
        else:
            frame = pd.DataFrame(data)
    elif suffix == ".csv":
        frame = pd.read_csv(path, dtype=str)
    elif suffix == ".tsv":
        frame = pd.read_csv(path, sep="\t", dtype=str)
    else:
        # .txt or unrecognised extension: peek at the first non-comment line
        # to decide delimiter; default to tab if ambiguous.
        detected_sep = "\t"
        try:
            with open(path, encoding="utf-8", errors="ignore") as fh:
                for raw_line in fh:
                    line = raw_line.strip()
                    if line and not line.startswith("#"):
                        detected_sep = "\t" if "\t" in line else ","
                        break
        except OSError:
            pass
        frame = pd.read_csv(path, sep=detected_sep, dtype=str)
    return normalize_variant_dataframe(frame)


_LOCAL_DRUG_DATABASE_SERVICE = None


class _DrugDatabaseEntry:
    """Minimal resolved-drug entry returned by the inline drug-database service."""

    __slots__ = ("drug_key",)

    def __init__(self, drug_key: str) -> None:
        self.drug_key = drug_key


class _InlineDrugDatabaseService:
    """Self-contained drug normalisation service built from DRUG_GENE_RULES.

    This replaces the external ``src.services.drug_database_service.DrugDatabaseService``
    so the merged single-file application has no external package dependencies.
    """

    def normalize_many(
        self, drugs: list[str]
    ) -> "tuple[list[_DrugDatabaseEntry], list[str]]":
        resolved: list[_DrugDatabaseEntry] = []
        unresolved: list[str] = []
        for raw in drugs:
            key = str(raw).strip().lower()
            if key in DRUG_GENE_RULES:
                resolved.append(_DrugDatabaseEntry(key))
            else:
                # Try a general-pharmacology catalog entry first
                gen = _GENERAL_PHARMACOLOGY_DRUGS.get(key)
                if gen:
                    resolved.append(_DrugDatabaseEntry(gen))
                else:
                    unresolved.append(raw)
        return resolved, unresolved

    def support_tier_for(self, drug: str) -> str:
        key = str(drug).strip().lower()
        if key in DRUG_GENE_RULES:
            return "PARTIAL_EVIDENCE_SUPPORT"
        if key in _GENERAL_PHARMACOLOGY_DRUGS:
            return "GENERAL_PHARMACOLOGY_ONLY"
        return "UNSUPPORTED"


# Drugs known to the app but without a local PGx rule (general-pharmacology only).
_GENERAL_PHARMACOLOGY_DRUGS: dict[str, str] = {
    "aspirin": "aspirin",
    "metformin": "metformin",
    "atorvastatin": "atorvastatin",
    "rosuvastatin": "rosuvastatin",
    "pravastatin": "pravastatin",
    "fluvastatin": "fluvastatin",
    "pitavastatin": "pitavastatin",
    "losartan": "losartan",
    "amlodipine": "amlodipine",
    "metoprolol": "metoprolol",
    "carvedilol": "carvedilol",
    "tramadol": "tramadol",
    "codeine": "codeine",
    "hydrocodone": "hydrocodone",
    "oxycodone": "oxycodone",
    "tamoxifen": "tamoxifen",
    "irinotecan": "irinotecan",
    "abacavir": "abacavir",
    "allopurinol": "allopurinol",
    "carbamazepine": "carbamazepine",
    "phenytoin": "phenytoin",
    "valproic acid": "valproic acid",
    "clozapine": "clozapine",
    "risperidone": "risperidone",
    "aripiprazole": "aripiprazole",
}


def _drug_database_service() -> _InlineDrugDatabaseService:
    global _LOCAL_DRUG_DATABASE_SERVICE
    if _LOCAL_DRUG_DATABASE_SERVICE is None:
        _LOCAL_DRUG_DATABASE_SERVICE = _InlineDrugDatabaseService()
    return _LOCAL_DRUG_DATABASE_SERVICE


def normalize_selected_drugs(drugs: list[str] | None) -> list[str]:
    """Normalize user-selected drug names to the local Pharmexia drug database."""
    if not drugs:
        return []
    entries, _unresolved = _drug_database_service().normalize_many([str(drug) for drug in drugs if str(drug).strip()])
    return [entry.drug_key for entry in entries]

# --- end merged module: src/input_validation.py ---

# --- begin merged module: src/variant_processing.py ---
"""Variant parsing utilities."""


import gzip
from pathlib import Path
from typing import Any

import pandas as pd



def genotype_to_numeric(
    genotype: str,
    alt_index: int = 1,
    ref: str | None = None,
    alt: str | None = None,
) -> int | None:
    """Convert a genotype string to the copy count of a specific alternate allele.

    Supports two formats:

    1. **Numeric VCF GT** (``0/1``, ``1|1``, ``0/0``, etc.) – the standard VCF
       representation where allele indices are integers.
    2. **Allele-string tables** (``A/G``, ``AG``) – used by some variant-table
       formats.  Only attempted when both ``ref`` and ``alt`` are supplied and
       ``alt_index == 1``.

    Returns ``None`` when the genotype is missing, ambiguous, or cannot be parsed
    rather than silently assuming a reference call.
    """
    value = str(genotype or "").strip().upper()
    if not value or value in {".", "./.", ".:.", "./", ".|.", "N/A", "NA"}:
        return None

    # Strip trailing FORMAT fields (e.g. "0/1:30:99" → "0/1").
    value = value.split(":", 1)[0].strip()

    # ── Branch 1: numeric VCF GT ─────────────────────────────────────────────
    # A GT is numeric when every allele token (after splitting on / or |) is
    # either "." or a digit string.  We check this first so that allele strings
    # like "A/G" fall through cleanly to branch 2.
    if "/" in value or "|" in value:
        allele_tokens = value.replace("|", "/").split("/")
        if all(tok == "." or tok.isdigit() for tok in allele_tokens):
            count = 0
            for tok in allele_tokens:
                if tok == ".":
                    return None  # any missing call makes the GT ambiguous
                if int(tok) == alt_index:
                    count += 1
            return count
        # Tokens are not purely numeric → fall through to allele-string branch.

    # ── Branch 2: allele-string format (e.g. "A/G", "AG") ───────────────────
    # Only supported when ref and alt are known and alt_index is 1.
    if not ref or not alt or alt_index != 1:
        return None

    ref_upper = str(ref).strip().upper()
    alt_upper = str(alt).strip().upper()
    if not ref_upper or not alt_upper:
        return None

    # Split on delimiter when present; otherwise try to split a two-character
    # string into individual alleles (valid only for single-nucleotide variants).
    if "/" in value or "|" in value:
        allele_tokens = value.replace("|", "/").split("/")
    elif len(ref_upper) == 1 and len(alt_upper) == 1 and len(value) == 2:
        allele_tokens = [value[0], value[1]]
    else:
        return None

    count = 0
    for tok in allele_tokens:
        if tok not in {ref_upper, alt_upper}:
            return None  # unrecognised allele → ambiguous
        if tok == alt_upper:
            count += 1
    return count


def _open_text(path: Path):
    return gzip.open(path, "rt", encoding="utf-8", errors="ignore") if path.name.lower().endswith(".gz") else open(
        path, "rt", encoding="utf-8", errors="ignore"
    )


def _parse_info(info_text: str) -> dict[str, Any]:
    parsed: dict[str, Any] = {}
    for chunk in (info_text or "").split(";"):
        if not chunk:
            continue
        if "=" not in chunk:
            parsed[chunk] = True
            continue
        key, value = chunk.split("=", 1)
        parsed[key] = value
    return parsed


def _extract_gene(info: dict[str, Any]) -> str | None:
    for key in ("GENE", "SYMBOL", "Gene.refGene", "GENEINFO"):
        value = info.get(key)
        if not value:
            continue
        text = str(value)
        if key == "GENEINFO" and ":" in text:
            return text.split(":", 1)[0]
        if "," in text:
            return text.split(",", 1)[0]
        return text
    annotation = str(info.get("ANN") or "")
    if annotation:
        first = annotation.split(",", 1)[0].split("|")
        if len(first) >= 4 and first[3]:
            return first[3]
    return None


def parse_vcf_file(path: Path) -> tuple[list[ObservedVariant], str]:
    """Parse a VCF or gzipped VCF into observed variants."""
    records: list[ObservedVariant] = []
    samples: list[str] = []

    try:
        with _open_text(path) as handle:
            for line in handle:
                if line.startswith("##"):
                    continue
                if line.startswith("#CHROM"):
                    headers = line.rstrip("\n").split("\t")
                    samples = headers[9:]
                    continue
                if not line.strip() or line.startswith("#"):
                    continue

                parts = line.rstrip("\n").split("\t")
                if len(parts) < 8:
                    continue
                chrom, pos, rsid, ref, alt_text, _qual, _flt, info_text = parts[:8]
                fmt_keys = parts[8].split(":") if len(parts) > 8 else []
                sample_values = parts[9:] if len(parts) > 9 else []
                alts = alt_text.split(",")
                info = _parse_info(info_text)
                gene = _extract_gene(info)

                if not sample_values:
                    sample_values = ["./."]
                    samples = samples or ["SAMPLE"]

                for sample_name, sample_entry in zip(samples or ["SAMPLE"], sample_values):
                    sample_fields = sample_entry.split(":")
                    sample_map = dict(zip(fmt_keys, sample_fields))
                    genotype = sample_map.get("GT", sample_entry)

                    for alt_index, alt in enumerate(alts, start=1):
                        gt_code = genotype_to_numeric(genotype, alt_index=alt_index, ref=ref, alt=alt)
                        inferred_gene = gene or RSID_TO_GENE.get(rsid)
                        try:
                            parsed_pos: int | None = int(pos)
                        except (ValueError, TypeError):
                            parsed_pos = None
                        records.append(
                            ObservedVariant(
                                chrom=chrom,
                                pos=parsed_pos,
                                ref=ref,
                                alt=alt,
                                rsid=None if rsid == "." else rsid,
                                genotype=genotype,
                                genotype_code=gt_code,
                                sample_id=sample_name,
                                gene=inferred_gene,
                                source="vcf",
                                info=info,
                            )
                        )
    except Exception as exc:
        return [], str(exc)

    if not records:
        return [], "No variant records could be parsed from the VCF."
    return records, ""


def parse_vcf_to_dataframe(path: Path) -> pd.DataFrame:
    """Parse a VCF into a dataframe."""
    records, error = parse_vcf_file(path)
    if error:
        raise ValueError(error)
    return pd.DataFrame([record.to_dict() for record in records])


def _safe_int(value: object) -> int | None:
    """Convert *value* to ``int``, returning ``None`` for missing/NaN/non-numeric values.

    pandas reads integer columns with NaN as float64 (e.g. ``nan``).  Plain
    ``int(float('nan'))`` raises ``ValueError``, so we handle that here.
    """
    if value is None or value == "":
        return None
    try:
        f = float(value)  # type: ignore[arg-type]
    except (TypeError, ValueError):
        return None
    import math
    if math.isnan(f) or math.isinf(f):
        return None
    return int(f)


def dataframe_to_observed_variants(df: pd.DataFrame) -> list[ObservedVariant]:
    """Convert a normalized dataframe to observed-variant dataclasses."""
    ok, message = validate_variant_dataframe(df)
    if not ok:
        raise ValueError(message)

    variants: list[ObservedVariant] = []
    for row in df.to_dict(orient="records"):
        genotype = str(row.get("genotype") or "")
        rsid = str(row.get("rsid") or "").strip() or None
        alt = str(row.get("alt") or "").strip() or None
        ref = str(row.get("ref") or "").strip() or None
        gene = str(row.get("gene") or "").strip() or None
        if not gene and rsid:
            gene = RSID_TO_GENE.get(rsid)
        alt_index = 1
        genotype_code = row.get("genotype_code")
        if genotype_code is None:
            genotype_code = genotype_to_numeric(genotype, alt_index=alt_index, ref=ref, alt=alt)
        info = {
            str(key): value
            for key, value in row.items()
            if key not in {"chrom", "pos", "ref", "alt", "rsid", "genotype", "genotype_code", "sample_id", "gene"}
            and value not in (None, "")
        }
        variants.append(
            ObservedVariant(
                chrom=str(row.get("chrom") or "").strip() or None,
                pos=_safe_int(row.get("pos")),
                ref=ref,
                alt=alt,
                rsid=rsid,
                genotype=genotype,
                genotype_code=_safe_int(genotype_code),
                sample_id=str(row.get("sample_id") or "").strip() or None,
                gene=gene,
                source="table",
                info=info,
            )
        )
    return variants


def load_observed_variants(path: Path) -> list[ObservedVariant]:
    """Load observed variants from a supported input path."""
    if path.suffix.lower() in {".vcf", ".gz"}:
        records, error = parse_vcf_file(path)
        if error:
            raise ValueError(error)
        return records
    frame = load_variant_table(path)
    return dataframe_to_observed_variants(frame)


def normalize_observed_variants(variants: list[ObservedVariant]) -> list[ObservedVariant]:
    """Normalize parsed variants into a consistent internal representation."""
    normalized: list[ObservedVariant] = []
    for variant in variants:
        rsid = str(variant.rsid or "").strip().lower() or None
        gene = str(variant.gene or RSID_TO_GENE.get(rsid or "") or "").strip().upper() or None
        normalized.append(
            ObservedVariant(
                chrom=str(variant.chrom or "").strip() or None,
                pos=variant.pos,
                ref=str(variant.ref or "").strip().upper() or None,
                alt=str(variant.alt or "").strip().upper() or None,
                rsid=rsid,
                genotype=str(variant.genotype or "").strip(),
                genotype_code=variant.genotype_code,
                sample_id=str(variant.sample_id or "").strip() or None,
                gene=gene,
                source=variant.source,
                info=dict(variant.info),
            )
        )
    return normalized


def filter_pharmacogene_variants(variants: list[ObservedVariant]) -> list[ObservedVariant]:
    """Keep only variants mapping to locally supported pharmacogenes.

    Returns new ``ObservedVariant`` instances with the ``gene`` field normalised;
    the original objects are never mutated.
    """
    from dataclasses import replace as _dc_replace

    supported = set(SUPPORTED_PHARMACOGENES)
    filtered: list[ObservedVariant] = []
    for variant in variants:
        gene = str(variant.gene or RSID_TO_GENE.get(variant.rsid or "") or "").strip().upper()
        if gene in supported:
            # Create a new instance rather than mutating the shared object.
            filtered.append(_dc_replace(variant, gene=gene))
    return filtered


def summarize_variants(variants: list[ObservedVariant]) -> dict[str, Any]:
    """Create a compact variant summary for reports and UI use."""
    rsids = [variant.rsid for variant in variants if variant.rsid]
    pharmacogenes = sorted({str(variant.gene).upper() for variant in variants if variant.gene})
    heterozygous = sum(1 for variant in variants if variant.genotype_code == 1)
    homozygous_alt = sum(1 for variant in variants if variant.genotype_code == 2)
    return {
        "n_variants": len(variants),
        "n_unique_rsid": len(set(rsids)),
        "n_heterozygous_alt_calls": heterozygous,
        "n_homozygous_alt_calls": homozygous_alt,
        "pharmacogenes_observed": pharmacogenes,
    }


def parse_sequence_file(path: Path) -> list[dict[str, Any]]:
    """Legacy helper retained for compatibility; raw sequence files are not accepted by the app."""
    records: list[dict[str, Any]] = []
    identifier: str | None = None
    sequence_parts: list[str] = []
    with _open_text(path) as handle:
        for line in handle:
            stripped = line.strip()
            if not stripped:
                continue
            if stripped.startswith(">"):
                if identifier is not None:
                    sequence = "".join(sequence_parts).upper()
                    records.append({"id": identifier, "sequence": sequence, "length": len(sequence)})
                identifier = stripped[1:].split()[0]
                sequence_parts = []
                continue
            if identifier is None:
                identifier = "sequence_1"
            sequence_parts.append("".join(base for base in stripped if base.isalpha()))
    if identifier is not None:
        sequence = "".join(sequence_parts).upper()
        records.append({"id": identifier, "sequence": sequence, "length": len(sequence)})
    return records

# --- end merged module: src/variant_processing.py ---

# --- begin merged module: src/core/variant_effects.py ---
"""Conservative variant-effect classification for Pharmexia."""


from collections import OrderedDict
import re



_EFFECT_TERM_MAP: dict[str, VariantEffectType] = {
    "synonymous_variant": "SYNONYMOUS",
    "synonymous": "SYNONYMOUS",
    "silent": "SYNONYMOUS",
    "missense_variant": "MISSENSE",
    "missense": "MISSENSE",
    "nonsynonymous_snv": "MISSENSE",
    "nonsynonymous": "MISSENSE",
    "non_synonymous_variant": "MISSENSE",
    "protein_altering_variant": "MISSENSE",
    "stop_gained": "NONSENSE",
    "stopgain": "NONSENSE",
    "nonsense": "NONSENSE",
    "frameshift_variant": "FRAMESHIFT",
    "frameshift_deletion": "FRAMESHIFT",
    "frameshift_insertion": "FRAMESHIFT",
    "frameshift_block_substitution": "FRAMESHIFT",
    "frameshift": "FRAMESHIFT",
    "regulatory_region_variant": "REGULATORY",
    "promoter_variant": "REGULATORY",
    "enhancer_variant": "REGULATORY",
    "5_prime_utr_variant": "REGULATORY",
    "3_prime_utr_variant": "REGULATORY",
    "upstream_gene_variant": "REGULATORY",
    "downstream_gene_variant": "REGULATORY",
    "utr5": "REGULATORY",
    "utr3": "REGULATORY",
}

_PATHOGENICITY_PRIORITY: tuple[tuple[str, PathogenicityLabel], ...] = (
    ("likely_pathogenic", "LIKELY_PATHOGENIC"),
    ("likely pathogenic", "LIKELY_PATHOGENIC"),
    ("pathogenic", "PATHOGENIC"),
    ("likely_benign", "LIKELY_BENIGN"),
    ("likely benign", "LIKELY_BENIGN"),
    ("benign", "BENIGN"),
    ("uncertain_significance", "UNCERTAIN_SIGNIFICANCE"),
    ("uncertain significance", "UNCERTAIN_SIGNIFICANCE"),
    ("vus", "UNCERTAIN_SIGNIFICANCE"),
)

_PROTEIN_MISSENSE_RE = re.compile(r"^p\.[A-Za-z]{1,3}\d+[A-Za-z]{1,3}$")
_TRANSCRIPT_TOKEN_RE = re.compile(r"^(ENST|NM_)", re.IGNORECASE)
_PROTEIN_TOKEN_RE = re.compile(r"^(ENSP|NP_)", re.IGNORECASE)


def _normalized_info_map(info: dict[str, Any]) -> dict[str, Any]:
    return {str(key).strip().lower(): value for key, value in dict(info).items()}


def _split_annotation_tokens(value: str) -> list[str]:
    return [
        token.strip()
        for token in re.split(r"[,&|]", value)
        if token.strip()
    ]


def _normalize_effect_term(term: str) -> str:
    return str(term).strip().lower().replace(" ", "_")


def _extract_ann_details(info: dict[str, Any]) -> tuple[list[str], str | None, str | None, str | None]:
    annotation = str(info.get("ann") or info.get("ANN") or "").strip()
    if not annotation:
        return [], None, None, None

    terms: list[str] = []
    transcript_id = None
    protein_effect = None
    protein_id = None
    for record in annotation.split(","):
        fields = record.split("|")
        if len(fields) >= 2 and fields[1]:
            terms.extend(_split_annotation_tokens(fields[1]))
        if transcript_id is None and len(fields) >= 7 and fields[6]:
            transcript_id = fields[6]
        if protein_effect is None and len(fields) >= 11 and fields[10]:
            protein_effect = fields[10]
        if protein_id is None:
            protein_id = next((field for field in fields if _PROTEIN_TOKEN_RE.match(field)), None)
    return terms, transcript_id, protein_effect, protein_id


def _extract_csq_details(info: dict[str, Any]) -> tuple[list[str], str | None, str | None, str | None]:
    annotation = str(info.get("csq") or info.get("CSQ") or "").strip()
    if not annotation:
        return [], None, None, None

    terms: list[str] = []
    transcript_id = None
    protein_effect = None
    protein_id = None
    for record in annotation.split(","):
        for token in [piece.strip() for piece in record.split("|") if piece.strip()]:
            normalized = _normalize_effect_term(token)
            if normalized in _EFFECT_TERM_MAP and normalized not in terms:
                terms.append(token)
            if transcript_id is None and _TRANSCRIPT_TOKEN_RE.match(token):
                transcript_id = token
            if protein_id is None and _PROTEIN_TOKEN_RE.match(token):
                protein_id = token
            if protein_effect is None and token.startswith("p."):
                protein_effect = token
    return terms, transcript_id, protein_effect, protein_id


def _first_present(info: dict[str, Any], *keys: str) -> str | None:
    for key in keys:
        value = info.get(key)
        if value not in (None, ""):
            return str(value).strip()
    return None


def _collect_consequence_terms(
    info: dict[str, Any],
) -> tuple[list[str], str | None, str | None, str | None, str]:
    terms: list[str] = []
    source = "unavailable"
    for key in (
        "consequence",
        "vep_consequence",
        "effect",
        "effects",
        "functional_class",
        "exonicfunc.refgene",
        "func.refgene",
    ):
        value = _first_present(info, key)
        if not value:
            continue
        terms.extend(_split_annotation_tokens(value))
        source = f"input_info:{key}"
        break

    ann_terms, ann_transcript, ann_protein_effect, ann_protein_id = _extract_ann_details(info)
    csq_terms, csq_transcript, csq_protein_effect, csq_protein_id = _extract_csq_details(info)
    if ann_terms:
        terms.extend(ann_terms)
        source = "input_info:ANN"
    elif csq_terms:
        terms.extend(csq_terms)
        source = "input_info:CSQ"

    transcript_id = _first_present(
        info,
        "transcript_id",
        "transcript",
        "feature_id",
    ) or ann_transcript or csq_transcript
    protein_effect = _first_present(
        info,
        "protein_effect",
        "hgvs_p",
        "protein_change",
        "hgvsp",
        "aa_change",
        "amino_acid_change",
    ) or ann_protein_effect or csq_protein_effect
    protein_id = _first_present(info, "protein_id", "uniprot_id") or ann_protein_id or csq_protein_id

    deduped_terms = list(OrderedDict.fromkeys(term for term in terms if term))
    return deduped_terms, protein_effect or None, transcript_id or None, protein_id or None, source


def _effect_from_terms(terms: list[str]) -> VariantEffectType | None:
    for term in terms:
        normalized = _normalize_effect_term(term)
        if normalized in _EFFECT_TERM_MAP:
            return _EFFECT_TERM_MAP[normalized]
    return None


def _effect_from_protein_effect(protein_effect: str | None) -> VariantEffectType | None:
    if not protein_effect:
        return None
    text = protein_effect.strip()
    lower = text.lower()
    if "=" in text:
        return "SYNONYMOUS"
    if "fs" in lower:
        return "FRAMESHIFT"
    if "ter" in lower or "*" in text or text.endswith("X"):
        return "NONSENSE"
    if _PROTEIN_MISSENSE_RE.match(text):
        return "MISSENSE"
    return None


def _normalize_pathogenicity(info: dict[str, Any]) -> tuple[PathogenicityLabel, VariantEffectConfidence]:
    value = _first_present(
        info,
        "clinvar_significance",
        "clinical_significance",
        "clnsig",
        "pathogenicity",
    )
    if not value:
        return "UNSPECIFIED", "UNKNOWN"
    normalized = value.strip().lower().replace("|", " ").replace("/", " ")
    for token, label in _PATHOGENICITY_PRIORITY:
        if token in normalized:
            confidence = "HIGH" if "clin" in normalized or "clnsig" in normalized else "MODERATE"
            return label, confidence
    return "UNSPECIFIED", "UNKNOWN"


def _normalize_variant(value: str | None) -> str | None:
    """Normalise a variant token to a canonical lower-case string for storage and deduplication."""
    return str(value or "").strip().lower() or None


def predict_variant_effect(variant: ObservedVariant) -> VariantEffectPrediction:
    """Classify a variant's likely biological effect from explicit annotation only."""
    info = _normalized_info_map(variant.info)
    normalized_gene = str(variant.gene or RSID_TO_GENE.get(variant.rsid or "") or "").strip().upper() or "UNKNOWN"
    normalized_variant = _normalize_variant(variant.token)
    terms, protein_effect, transcript_id, protein_id, source = _collect_consequence_terms(info)
    effect_type = _effect_from_terms(terms)
    confidence: VariantEffectConfidence = "UNKNOWN"
    reasoning: list[str] = []

    if effect_type is not None:
        confidence = "HIGH"
        reasoning.append("Explicit consequence annotation mapped directly to a supported effect class.")
    else:
        inferred_from_protein = _effect_from_protein_effect(protein_effect)
        if inferred_from_protein is not None:
            effect_type = inferred_from_protein
            confidence = "MODERATE"
            source = source if source != "unavailable" else "input_info:protein_effect"
            reasoning.append("Protein-level annotation supported a conservative effect-type inference.")

    if effect_type is None:
        effect_type = "UNKNOWN_EFFECT"
        reasoning.append("No supported functional annotation field was available for a conservative effect call.")

    pathogenicity_label, pathogenicity_confidence = _normalize_pathogenicity(info)

    if effect_type == "UNKNOWN_EFFECT" and pathogenicity_label == "UNSPECIFIED":
        availability_status: EvidenceAvailabilityStatus = "unavailable"
    elif effect_type == "UNKNOWN_EFFECT":
        availability_status = "partial"
    else:
        availability_status = "available"

    effect_summary = effect_type.replace("_", " ").title()
    protein_summary = f" Protein effect: {protein_effect}." if protein_effect else ""
    pathogenicity_summary = (
        f" Pathogenicity label: {pathogenicity_label.replace('_', ' ').title()}."
        if pathogenicity_label != "UNSPECIFIED"
        else ""
    )
    summary = (
        f"Variant effect layer classified {variant.token} in {normalized_gene} as {effect_summary} "
        f"(confidence {confidence}).{protein_summary}{pathogenicity_summary}"
        if effect_type != "UNKNOWN_EFFECT"
        else (
            f"Variant effect layer could not assign a supported functional class for {variant.token} in {normalized_gene}; "
            "the effect is marked as UNKNOWN_EFFECT."
            + pathogenicity_summary
        )
    )

    return VariantEffectPrediction(
        variant_token=variant.token,
        gene=normalized_gene,
        effect_type=effect_type,
        effect_confidence=confidence,
        pathogenicity_label=pathogenicity_label,
        pathogenicity_confidence=pathogenicity_confidence,
        normalized_variant=normalized_variant,
        protein_effect=protein_effect,
        protein_id=protein_id,
        transcript_id=transcript_id,
        consequence_terms=terms,
        annotation_source=source,
        availability_status=availability_status,
        summary=summary,
        reasoning=reasoning,
    )


def variant_effect_to_structured_evidence(effect: VariantEffectPrediction) -> StructuredEvidence:
    """Convert a variant-effect call into non-authoritative structured evidence context."""
    return StructuredEvidence(
        source_name="Pharmexia Variant Effect Layer",
        source_record_id=f"variant_effect:{effect.normalized_variant or effect.variant_token}",
        evidence_type="variant_effect_annotation",
        clinical_relevance=(
            "variant_function_context"
            if effect.effect_type != "UNKNOWN_EFFECT"
            else "annotation_unavailable"
        ),
        confidence=str(effect.effect_confidence).lower(),
        normalized_gene=effect.gene,
        normalized_variant=effect.normalized_variant or effect.variant_token.lower(),
        normalized_drug=None,
        protein_id=effect.protein_id,
        interpretation_text=effect.summary,
        source_module="src.services.variant_annotation_service",
        status="available" if effect.availability_status == "available" else "partial" if effect.availability_status == "partial" else "unavailable",
        details={
            "effect_type": effect.effect_type,
            "effect_confidence": effect.effect_confidence,
            "protein_effect": effect.protein_effect,
            "protein_id": effect.protein_id,
            "transcript_id": effect.transcript_id,
            "pathogenicity_label": effect.pathogenicity_label,
            "pathogenicity_confidence": effect.pathogenicity_confidence,
            "annotation_source": effect.annotation_source,
            "consequence_terms": list(effect.consequence_terms),
            "reasoning": list(effect.reasoning),
        },
    )

# --- end merged module: src/core/variant_effects.py ---

# --- begin merged module: src/services/variant_annotation_service.py ---
"""Variant annotation service for conservative effect prediction."""



class VariantAnnotationService:
    """Annotate normalized variants with conservative local effect predictions."""

    def annotate_variant(self, variant: ObservedVariant) -> VariantEffectPrediction:
        return predict_variant_effect(variant)

    def annotate_variants(self, variants: list[ObservedVariant]) -> list[VariantEffectPrediction]:
        return [self.annotate_variant(variant) for variant in variants]

    def to_structured_evidence(self, effect: VariantEffectPrediction) -> StructuredEvidence:
        return variant_effect_to_structured_evidence(effect)

# --- end merged module: src/services/variant_annotation_service.py ---

# --- begin merged module: src/core/star_alleles.py ---
"""Data-driven local star-allele rule loading for Pharmexia."""


import json
from functools import lru_cache


STAR_ALLELE_RULES_PATH = Path(__file__).resolve().parent / "data" / "star_allele_rules.json"


def _empty_star_allele_catalog() -> "StarAlleleRuleCatalog":
    """Return an empty catalog used when the data file is absent."""
    return StarAlleleRuleCatalog(schema_version="missing")


# Module-level cache — populated on first successful load.
_STAR_ALLELE_CATALOG_CACHE: "StarAlleleRuleCatalog | None" = None


def load_star_allele_rule_catalog(path: str | None = None) -> "StarAlleleRuleCatalog":
    """Load and cache the local star-allele rule catalog.

    Falls back to an empty catalog (rather than raising) when the data file is
    absent so that the rest of the pipeline can still run and report limitations.
    The cache is keyed on the resolved path; passing a different *path* argument
    bypasses the cache so tests can supply fixture data without side-effects.
    """
    global _STAR_ALLELE_CATALOG_CACHE

    rule_path = Path(path) if path else STAR_ALLELE_RULES_PATH

    # When using the default path, return the in-process cache if populated.
    if path is None and _STAR_ALLELE_CATALOG_CACHE is not None:
        return _STAR_ALLELE_CATALOG_CACHE

    if not rule_path.exists():
        empty = _empty_star_allele_catalog()
        if path is None:
            _STAR_ALLELE_CATALOG_CACHE = empty
        return empty

    try:
        payload = json.loads(rule_path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        empty = _empty_star_allele_catalog()
        if path is None:
            _STAR_ALLELE_CATALOG_CACHE = empty
        return empty

    gene_rules = {
        str(gene).upper(): _parse_star_allele_rule_set(str(gene).upper(), dict(rule_set))
        for gene, rule_set in dict(payload.get("genes", {})).items()
    }
    catalog = StarAlleleRuleCatalog(
        schema_version=str(payload.get("schema_version", "1.0")),
        genes=gene_rules,
        source_layers=[dict(item) for item in payload.get("source_layers", []) or [] if isinstance(item, dict)],
    )
    if path is None:
        _STAR_ALLELE_CATALOG_CACHE = catalog
    return catalog


@dataclass(slots=True)
class StarAlleleRule:
    allele: str
    rsid: str
    alt: str
    callable: bool = True
    function: str | None = None
    notes: list[str] = field(default_factory=list)
    sources: list[dict[str, str]] = field(default_factory=list)

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


@dataclass(slots=True)
class GeneStarAlleleRuleSet:
    gene: str
    reference_allele: str
    required_loci: list[str]
    calling_strategy: str
    allow_reference_call: bool
    confidence_supported: str
    confidence_inconclusive: str
    alleles: dict[str, StarAlleleRule] = field(default_factory=dict)
    diplotype_phenotypes: dict[str, str] = field(default_factory=dict)
    limitations: list[str] = field(default_factory=list)
    sources: list[dict[str, str]] = field(default_factory=list)

    def to_dict(self) -> dict[str, Any]:
        return {
            "gene": self.gene,
            "reference_allele": self.reference_allele,
            "required_loci": list(self.required_loci),
            "calling_strategy": self.calling_strategy,
            "allow_reference_call": self.allow_reference_call,
            "confidence_supported": self.confidence_supported,
            "confidence_inconclusive": self.confidence_inconclusive,
            "alleles": {key: value.to_dict() for key, value in self.alleles.items()},
            "diplotype_phenotypes": dict(self.diplotype_phenotypes),
            "limitations": list(self.limitations),
            "sources": list(self.sources),
        }


@dataclass(slots=True)
class StarAlleleRuleCatalog:
    schema_version: str
    genes: dict[str, GeneStarAlleleRuleSet] = field(default_factory=dict)
    source_layers: list[dict[str, str]] = field(default_factory=list)

    def to_dict(self) -> dict[str, Any]:
        return {
            "schema_version": self.schema_version,
            "genes": {gene: rule_set.to_dict() for gene, rule_set in self.genes.items()},
            "source_layers": list(self.source_layers),
        }


def _parse_star_allele_rule_set(gene: str, payload: dict[str, Any]) -> GeneStarAlleleRuleSet:
    allele_rules = {
        allele: StarAlleleRule(
            allele=allele,
            rsid=str(rule["rsid"]),
            alt=str(rule["alt"]),
            callable=bool(rule.get("callable", True)),
            function=rule.get("function"),
            notes=list(rule.get("notes", []) or []),
            sources=[dict(item) for item in rule.get("sources", []) or [] if isinstance(item, dict)],
        )
        for allele, rule in dict(payload.get("alleles", {})).items()
    }
    confidence = dict(payload.get("confidence_categories", {}))
    return GeneStarAlleleRuleSet(
        gene=gene,
        reference_allele=str(payload.get("reference_allele", "*1")),
        required_loci=[str(item) for item in payload.get("required_loci", [])],
        calling_strategy=str(payload.get("calling_strategy", "single_nonreference_locus_only")),
        allow_reference_call=bool(payload.get("allow_reference_call", False)),
        confidence_supported=str(confidence.get("supported", "LIMITED_PANEL_SUPPORTED")),
        confidence_inconclusive=str(confidence.get("inconclusive", "INCONCLUSIVE")),
        alleles=allele_rules,
        diplotype_phenotypes={str(key): str(value) for key, value in dict(payload.get("diplotype_phenotypes", {})).items()},
        limitations=[str(item) for item in payload.get("limitations", [])],
        sources=[dict(item) for item in payload.get("sources", []) or [] if isinstance(item, dict)],
    )


def star_allele_rule_set_for_gene(gene: str, *, path: str | None = None) -> "GeneStarAlleleRuleSet | None":
    return load_star_allele_rule_catalog(path).genes.get(str(gene).upper())

# --- end merged module: src/core/star_alleles.py ---

# --- begin merged module: src/core/diplotype_interpreter.py ---
"""Conservative diplotype and phenotype interpretation from local star-allele rules."""


@dataclass(slots=True)
class DiplotypeInterpretation:
    gene: str
    diplotype: str | None = None
    phenotype: str | None = None
    confidence_category: str = "INCONCLUSIVE"
    ambiguous: bool = False
    limitations: list[str] = field(default_factory=list)
    sources: list[dict[str, str]] = field(default_factory=list)

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


def _sorted_diplotype(allele_a: str, allele_b: str) -> str:
    if allele_a <= allele_b:
        return f"{allele_a}/{allele_b}"
    return f"{allele_b}/{allele_a}"


def _limited_panel_phenotype(phenotype: str | None) -> str | None:
    if not phenotype:
        return None
    return f"Possible {phenotype} (limited local panel)"


def interpret_diplotype_from_matches(
    gene: str,
    matched_alleles: list[AlleleMatch],
    *,
    coverage_complete: bool,
    rule_path: str | None = None,
) -> DiplotypeInterpretation:
    rule_set = star_allele_rule_set_for_gene(gene, path=rule_path)
    if rule_set is None:
        return DiplotypeInterpretation(gene=gene, confidence_category="INCONCLUSIVE")

    limitations: list[str] = list(rule_set.limitations)
    sources: list[dict[str, str]] = list(rule_set.sources)
    if not matched_alleles:
        if coverage_complete and not rule_set.allow_reference_call:
            limitations.append(
                "No supported non-reference allele was observed, but this limited panel does not assign a reference diplotype from negative loci alone."
            )
        return DiplotypeInterpretation(
            gene=gene,
            confidence_category=rule_set.confidence_inconclusive,
            limitations=limitations,
            sources=sources,
        )

    if not coverage_complete:
        limitations.append(
            "The submitted data do not show all curated loci for this gene, so no limited-panel diplotype was assigned."
        )
        return DiplotypeInterpretation(
            gene=gene,
            confidence_category=rule_set.confidence_inconclusive,
            limitations=limitations,
            sources=sources,
        )

    unique_loci = {match.rsid for match in matched_alleles}
    if len(unique_loci) > 1:
        limitations.append(
            "Multiple non-reference loci were detected, and phase could not be resolved from the submitted data."
        )
        return DiplotypeInterpretation(
            gene=gene,
            confidence_category=rule_set.confidence_inconclusive,
            ambiguous=True,
            limitations=limitations,
            sources=sources,
        )

    match = matched_alleles[0]
    if not match.allele:
        limitations.append("Observed evidence did not map to a supported named allele in the local rule file.")
        return DiplotypeInterpretation(
            gene=gene,
            confidence_category=rule_set.confidence_inconclusive,
            limitations=limitations,
            sources=sources,
        )

    allele_rule = rule_set.alleles.get(match.allele)
    if allele_rule is None:
        limitations.append(f"Observed allele {match.allele} is not present in the current local star-allele rule file.")
        return DiplotypeInterpretation(
            gene=gene,
            confidence_category=rule_set.confidence_inconclusive,
            limitations=limitations,
            sources=sources,
        )

    if not allele_rule.callable:
        limitations.append(
            f"Observed allele {match.allele} is represented only as a component or unsupported local marker, so Pharmexia does not assign a standalone diplotype from it."
        )
        return DiplotypeInterpretation(
            gene=gene,
            confidence_category=rule_set.confidence_inconclusive,
            limitations=limitations + list(allele_rule.notes),
            sources=sources + list(allele_rule.sources),
        )

    if match.genotype_code == 1:
        diplotype = _sorted_diplotype(rule_set.reference_allele, match.allele)
    elif match.genotype_code == 2:
        diplotype = _sorted_diplotype(match.allele, match.allele)
    else:
        limitations.append("Unsupported genotype code prevented a conservative star-allele call.")
        return DiplotypeInterpretation(
            gene=gene,
            confidence_category=rule_set.confidence_inconclusive,
            limitations=limitations,
            sources=sources + list(allele_rule.sources),
        )

    phenotype = rule_set.diplotype_phenotypes.get(diplotype)
    if phenotype is None:
        limitations.append(
            f"Diplotype {diplotype} is not mapped to a supported phenotype in the current local rule file."
        )
        return DiplotypeInterpretation(
            gene=gene,
            confidence_category=rule_set.confidence_inconclusive,
            limitations=limitations + list(allele_rule.notes),
            sources=sources + list(allele_rule.sources),
        )

    limitations.append(
        "Local phenotype wording is limited-panel only and does not exclude additional star alleles, copy-number changes, or phasing effects."
    )
    return DiplotypeInterpretation(
        gene=gene,
        diplotype=diplotype,
        phenotype=_limited_panel_phenotype(phenotype),
        confidence_category=rule_set.confidence_supported,
        ambiguous=False,
        limitations=limitations + list(allele_rule.notes),
        sources=sources + list(allele_rule.sources),
    )

# --- end merged module: src/core/diplotype_interpreter.py ---

# --- begin merged module: src/pgx_annotation.py ---
"""Local pharmacogene mapping and conservative allele interpretation."""


from collections import defaultdict



def _variant_matches_definition(variant: ObservedVariant, definition: dict[str, object]) -> bool:
    return (
        variant.rsid == definition.get("rsid")
        and alt_matches_definition(variant.ref, variant.alt, definition)
        and (variant.genotype_code or 0) > 0
    )


def assess_pharmacogenes(variants: list[ObservedVariant]) -> dict[str, GeneAssessment]:
    """Assess curated pharmacogenes from the observed variant list.

    Input variants are never mutated; gene attribution is computed locally.
    """
    from dataclasses import replace as _dc_replace

    grouped_variants: dict[str, list[ObservedVariant]] = defaultdict(list)
    for variant in variants:
        gene = (variant.gene or RSID_TO_GENE.get(variant.rsid or "") or "").upper()
        if not gene:
            continue
        # Use a new instance with the normalised gene; do NOT mutate the input.
        normalised = _dc_replace(variant, gene=gene) if variant.gene != gene else variant
        grouped_variants[gene].append(normalised)

    assessments: dict[str, GeneAssessment] = {}
    for gene, definitions in ALLELE_DEFINITIONS.items():
        gene_variants = grouped_variants.get(gene, [])
        observed_loci = sorted(
            {
                variant.rsid
                for variant in gene_variants
                if variant.rsid in GENE_TARGET_LOCI[gene] and variant.genotype_code is not None
            }
        )
        matches: list[AlleleMatch] = []

        for variant in gene_variants:
            for definition in definitions:
                if _variant_matches_definition(variant, definition):
                    matches.append(
                        AlleleMatch(
                            gene=gene,
                            rsid=str(definition["rsid"]),
                            alt=str(definition["alt"]),
                            allele=definition.get("allele"),
                            function=definition.get("function"),
                            effect=str(definition["effect"]),
                            genotype=variant.genotype,
                            genotype_code=int(variant.genotype_code or 0),
                            sources=list(definition.get("sources", [])),
                        )
                    )

        coverage_complete = set(observed_loci) == set(GENE_TARGET_LOCI[gene]) and bool(observed_loci)
        interpretation = interpret_diplotype_from_matches(
            gene=gene,
            matched_alleles=matches,
            coverage_complete=coverage_complete,
        )

        assessments[gene] = GeneAssessment(
            gene=gene,
            observed_target_loci=observed_loci,
            expected_target_loci=GENE_TARGET_LOCI[gene],
            matched_alleles=matches,
            local_panel_call=interpretation.diplotype,
            phenotype=interpretation.phenotype,
            call_confidence=interpretation.confidence_category,
            coverage_complete=coverage_complete,
            ambiguous=interpretation.ambiguous,
            limitations=interpretation.limitations,
        )
    return assessments

# --- end merged module: src/pgx_annotation.py ---

# --- begin merged module: src/database_clients/base.py ---
"""Shared query context and cache primitives for evidence adapters."""


import copy
import threading
import time
from collections import OrderedDict as OrderedDict
from dataclasses import dataclass, field
from typing import Any



@dataclass(slots=True)
class EvidenceQueryContext:
    rsid: str | None = None
    gene: str | None = None
    drug: str | None = None
    variant_token: str | None = None
    details: dict[str, Any] = field(default_factory=dict)

    @property
    def normalized_gene(self) -> str | None:
        return str(self.gene or "").strip().upper() or None

    @property
    def normalized_variant(self) -> str | None:
        token = str(self.variant_token or "").strip()
        if token:
            return token.lower()
        return str(self.rsid or "").strip().lower() or None

    @property
    def normalized_drug(self) -> str | None:
        return str(self.drug or "").strip().lower() or None

    @property
    def cache_key(self) -> str:
        return "|".join(
            [
                self.normalized_variant or "none",
                self.normalized_gene or "none",
                self.normalized_drug or "none",
            ]
        )


@dataclass(slots=True)
class AdapterLookupResponse:
    source_name: str
    records: list[StructuredEvidence] = field(default_factory=list)
    status: str = "available"
    error: str | None = None

    def to_dict(self) -> dict[str, Any]:
        return {
            "source_name": self.source_name,
            "records": [record.to_dict() for record in self.records],
            "status": self.status,
            "error": self.error,
        }


class TTLStructuredEvidenceCache:
    """Thread-safe in-memory TTL cache for external evidence lookups.

    Uses an ``OrderedDict`` for O(1) LRU eviction so that the lock is held for
    the minimum time and the capacity check is race-free.
    """

    def __init__(self, ttl_seconds: int = 900, max_entries: int = 256) -> None:
        self.ttl_seconds = ttl_seconds
        self.max_entries = max_entries
        # OrderedDict preserves insertion order → oldest entry is first.
        self._entries: "OrderedDict[str, tuple[float, list[StructuredEvidence]]]" = OrderedDict()
        self._lock = threading.Lock()

    def get(self, key: str) -> "list[StructuredEvidence] | None":
        now = time.monotonic()
        with self._lock:
            payload = self._entries.get(key)
            if payload is None:
                return None
            expires_at, records = payload
            if expires_at < now:
                self._entries.pop(key, None)
                return None
            return copy.deepcopy(records)

    def set(self, key: str, records: "list[StructuredEvidence]") -> None:
        now = time.monotonic()
        with self._lock:
            # Remove the key first so reinserting it moves it to the "newest" end.
            self._entries.pop(key, None)
            # Evict oldest entries until we are within capacity (handles the
            # case where max_entries was reduced or concurrent threads both
            # called set() simultaneously).
            while len(self._entries) >= self.max_entries:
                self._entries.popitem(last=False)  # O(1) — removes oldest
            self._entries[key] = (now + self.ttl_seconds, copy.deepcopy(records))

# --- end merged module: src/database_clients/base.py ---

# --- begin merged module: src/database_clients/remote_sources.py ---
"""Structured external evidence adapters for PGx annotation."""


from concurrent.futures import ThreadPoolExecutor, as_completed
from typing import Protocol

try:
    import requests as requests
    _REQUESTS_AVAILABLE = True
except ImportError:
    requests = None  # type: ignore[assignment]
    _REQUESTS_AVAILABLE = False



def _unavailable_record(
    *,
    source_name: str,
    context: EvidenceQueryContext,
    message: str,
    citation_url: str | None = None,
) -> StructuredEvidence:
    return StructuredEvidence(
        source_name=source_name,
        source_record_id=None,
        evidence_type="service_status",
        clinical_relevance="service_unavailable",
        confidence="unavailable",
        citation_url=citation_url,
        normalized_gene=context.normalized_gene,
        normalized_variant=context.normalized_variant,
        normalized_drug=context.normalized_drug,
        interpretation_text=message,
        source_module="src.database_clients.remote_sources",
        status="unavailable",
    )


class EvidenceSourceAdapter(Protocol):
    source_name: str

    def lookup(self, context: EvidenceQueryContext) -> AdapterLookupResponse:
        ...


class ClinVarEvidenceAdapter:
    """NCBI ClinVar annotation presence lookup."""

    source_name = "ClinVar"

    def __init__(self, timeout_seconds: float = 2.5) -> None:
        self.timeout_seconds = timeout_seconds

    def lookup(self, context: EvidenceQueryContext) -> AdapterLookupResponse:
        rsid = context.rsid
        url = f"https://www.ncbi.nlm.nih.gov/clinvar/?term={rsid}" if rsid else "https://www.ncbi.nlm.nih.gov/clinvar/"
        if not rsid:
            return AdapterLookupResponse(source_name=self.source_name, status="unavailable", records=[])

        endpoint = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"
        try:
            response = requests.get(
                endpoint,
                params={"db": "clinvar", "retmode": "json", "term": f"{rsid}[All Fields]"},
                timeout=self.timeout_seconds,
            )
            response.raise_for_status()
            payload = response.json()
            count = int(payload.get("esearchresult", {}).get("count", 0))
            record = StructuredEvidence(
                source_name=self.source_name,
                source_record_id=f"clinvar_search:{rsid}",
                evidence_type="clinical_annotation_index",
                clinical_relevance="clinical_annotation_presence" if count > 0 else "no_clinical_annotation_found",
                confidence="annotation_only",
                citation_url=url,
                normalized_gene=context.normalized_gene,
                normalized_variant=context.normalized_variant,
                normalized_drug=context.normalized_drug,
                interpretation_text=(
                    f"ClinVar search returned {count} record(s) for {rsid}. "
                    "Record count alone does not establish pharmacogenomic actionability."
                ),
                source_module="src.database_clients.remote_sources",
                status="available",
                details={"count": count},
            )
            return AdapterLookupResponse(source_name=self.source_name, status="available", records=[record])
        except Exception as exc:
            return AdapterLookupResponse(
                source_name=self.source_name,
                status="unavailable",
                error=str(exc),
                records=[
                    _unavailable_record(
                        source_name=self.source_name,
                        context=context,
                        message=f"ClinVar lookup unavailable; no ClinVar evidence was incorporated for {rsid}: {exc}",
                        citation_url=url,
                    )
                ],
            )


class DbSnpEvidenceAdapter:
    """dbSNP catalog presence adapter using the NCBI E-utilities esearch API.

    The previous implementation performed an HTTP GET on the dbSNP HTML page and
    used HTTP 200 as a proxy for catalog presence.  That approach is wrong because
    the NCBI HTML page returns 200 even for non-existent rsIDs (it renders a "not
    found" message in the body).  This version uses the same JSON esearch endpoint
    as the ClinVar adapter so that catalog presence is verified by record count.
    """

    source_name = "dbSNP"

    def __init__(self, timeout_seconds: float = 2.5) -> None:
        self.timeout_seconds = timeout_seconds

    def lookup(self, context: "EvidenceQueryContext") -> "AdapterLookupResponse":
        rsid = context.rsid
        url = f"https://www.ncbi.nlm.nih.gov/snp/{rsid}" if rsid else "https://www.ncbi.nlm.nih.gov/snp/"
        if not rsid:
            return AdapterLookupResponse(source_name=self.source_name, status="unavailable", records=[])

        endpoint = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"
        try:
            response = requests.get(
                endpoint,
                params={"db": "snp", "retmode": "json", "term": f"{rsid}[All Fields]"},
                timeout=self.timeout_seconds,
            )
            response.raise_for_status()
            payload = response.json()
            count = int(payload.get("esearchresult", {}).get("count", 0))
            record = StructuredEvidence(
                source_name=self.source_name,
                source_record_id=rsid,
                evidence_type="catalog_presence",
                clinical_relevance="catalog_reference" if count > 0 else "catalog_not_confirmed",
                confidence="annotation_only",
                citation_url=url,
                normalized_gene=context.normalized_gene,
                normalized_variant=context.normalized_variant,
                normalized_drug=context.normalized_drug,
                interpretation_text=(
                    f"dbSNP esearch returned {count} record(s) for {rsid}. "
                    "Catalog presence confirms identifier context only and does not establish functional impact."
                    if count > 0
                    else f"dbSNP esearch found no records for {rsid}. "
                    "No dbSNP catalog evidence was incorporated."
                ),
                source_module="src.database_clients.remote_sources",
                status="available" if count > 0 else "unavailable",
                details={"count": count},
            )
            return AdapterLookupResponse(
                source_name=self.source_name,
                status="available" if count > 0 else "unavailable",
                records=[record],
            )
        except Exception as exc:
            return AdapterLookupResponse(
                source_name=self.source_name,
                status="unavailable",
                error=str(exc),
                records=[
                    _unavailable_record(
                        source_name=self.source_name,
                        context=context,
                        message=f"dbSNP lookup unavailable; no dbSNP evidence was incorporated for {rsid}: {exc}",
                        citation_url=url,
                    )
                ],
            )


class UniProtEvidenceAdapter:
    """UniProt gene-context adapter."""

    source_name = "UniProt"

    def __init__(self, timeout_seconds: float = 2.5) -> None:
        self.timeout_seconds = timeout_seconds

    def lookup(self, context: EvidenceQueryContext) -> AdapterLookupResponse:
        gene = context.normalized_gene
        url = f"https://www.uniprot.org/uniprotkb?query={gene}" if gene else "https://www.uniprot.org/uniprotkb"
        if not gene:
            return AdapterLookupResponse(source_name=self.source_name, status="unavailable", records=[])

        endpoint = "https://rest.uniprot.org/uniprotkb/search"
        try:
            response = requests.get(
                endpoint,
                params={"query": f"gene:{gene} AND organism_id:9606", "size": 1, "format": "json"},
                timeout=self.timeout_seconds,
            )
            response.raise_for_status()
            payload = response.json()
            results = payload.get("results", [])
            accession = None
            if results:
                accession = results[0].get("primaryAccession")
            record = StructuredEvidence(
                source_name=self.source_name,
                source_record_id=accession or gene,
                evidence_type="protein_reference_context",
                clinical_relevance="gene_reference_context",
                confidence="annotation_only",
                citation_url=url,
                normalized_gene=gene,
                normalized_variant=context.normalized_variant,
                normalized_drug=context.normalized_drug,
                interpretation_text=(
                    f"UniProt returned {len(results)} human protein record(s) for {gene}. "
                    "Protein reference context does not establish drug-response direction or phenotype."
                ),
                source_module="src.database_clients.remote_sources",
                status="available",
                details={"hit_count": len(results)},
            )
            return AdapterLookupResponse(source_name=self.source_name, status="available", records=[record])
        except Exception as exc:
            return AdapterLookupResponse(
                source_name=self.source_name,
                status="unavailable",
                error=str(exc),
                records=[
                    _unavailable_record(
                        source_name=self.source_name,
                        context=context,
                        message=f"UniProt lookup unavailable; no UniProt gene context was incorporated for {gene}: {exc}",
                        citation_url=url,
                    )
                ],
            )


class RemoteEvidenceService:
    """Aggregate external evidence adapters with caching and short parallel lookups.

    A single module-level ``ThreadPoolExecutor`` is reused across all calls to
    avoid creating O(requests × adapters) OS threads under concurrent API load.
    """

    # Shared executor — created lazily on first use, reused thereafter.
    _shared_executor: "ThreadPoolExecutor | None" = None
    _executor_lock = threading.Lock()
    _EXECUTOR_MAX_WORKERS = 8  # enough for all adapters across concurrent requests

    @classmethod
    def _get_executor(cls) -> "ThreadPoolExecutor":
        if cls._shared_executor is None:
            with cls._executor_lock:
                if cls._shared_executor is None:
                    cls._shared_executor = ThreadPoolExecutor(
                        max_workers=cls._EXECUTOR_MAX_WORKERS,
                        thread_name_prefix="remote_evidence",
                    )
        return cls._shared_executor

    def __init__(
        self,
        *,
        cache: "TTLStructuredEvidenceCache | None" = None,
        adapters: "list[EvidenceSourceAdapter] | None" = None,
    ) -> None:
        self.cache = cache or TTLStructuredEvidenceCache()
        self.adapters = adapters or [
            ClinVarEvidenceAdapter(),
            DbSnpEvidenceAdapter(),
            UniProtEvidenceAdapter(),
        ]

    def lookup_variant(
        self,
        rsid: "str | None",
        gene: "str | None",
        *,
        drug: "str | None" = None,
        variant_token: "str | None" = None,
    ) -> "list[StructuredEvidence]":
        context = EvidenceQueryContext(rsid=rsid, gene=gene, drug=drug, variant_token=variant_token)
        if not context.normalized_variant and not context.normalized_gene:
            return []

        cached = self.cache.get(context.cache_key)
        if cached is not None:
            return cached

        records: list[StructuredEvidence] = []
        executor = self._get_executor()
        future_map = {executor.submit(adapter.lookup, context): adapter.source_name for adapter in self.adapters}
        for future in as_completed(future_map, timeout=10.0):
            source_name = future_map[future]
            try:
                result = future.result()
                records.extend(result.records)
            except Exception as exc:
                records.append(
                    _unavailable_record(
                        source_name=source_name,
                        context=context,
                        message=f"{source_name} lookup failed unexpectedly; no evidence was incorporated: {exc}",
                    )
                )

        self.cache.set(context.cache_key, records)
        return records

# --- end merged module: src/database_clients/remote_sources.py ---

# --- begin merged module: src/evidence_integration.py ---
"""Structured evidence collection, aggregation, and provenance assembly."""


from collections import OrderedDict



ACTIONABLE_RELEVANCE = {
    "actionable_pgx_support",
    "supportive_pgx_annotation",
}


def _normalize_gene(value: str | None) -> str | None:
    return str(value or "").strip().upper() or None


def _normalize_variant(value: str | None) -> str | None:
    return str(value or "").strip().lower() or None


def _normalize_drug(value: str | None) -> str | None:
    return str(value or "").strip().lower() or None


def _dedupe_structured_evidence(records: list[StructuredEvidence]) -> list[StructuredEvidence]:
    deduped: "OrderedDict[tuple[str, str | None, str, str | None, str | None, str | None, str, str], StructuredEvidence]" = OrderedDict()
    for record in records:
        key = (
            record.source_name,
            record.source_record_id,
            record.evidence_type,
            record.normalized_gene,
            record.normalized_variant,
            record.normalized_drug,
            record.interpretation_text,
            record.status,
        )
        if key not in deduped:
            deduped[key] = record
    return list(deduped.values())


def _signal_token(record: StructuredEvidence) -> str | None:
    for key in ("effect", "function", "signal_direction"):
        value = record.details.get(key)
        if value:
            return str(value)
    if record.clinical_relevance in ACTIONABLE_RELEVANCE:
        return record.interpretation_text
    return None


class LocalRuleEvidenceAdapter:
    """Build structured evidence records from the curated local rule base."""

    def records_for_match(self, match: AlleleMatch, *, drug: str | None = None) -> list[StructuredEvidence]:
        normalized_drug = _normalize_drug(drug)
        normalized_variant = _normalize_variant(match.rsid)
        normalized_gene = _normalize_gene(match.gene)
        records: list[StructuredEvidence] = []
        source_keys = DRUG_REFERENCE_SOURCE_KEYS.get(normalized_drug or "", list(match.sources))
        for source_key in source_keys:
            source = REFERENCE_SOURCES.get(
                source_key,
                {
                    "label": source_key.replace("_", " ").title(),
                    "url": "",
                },
            )
            records.append(
                StructuredEvidence(
                    source_name=source["label"],
                    source_record_id=f"{source_key}:{match.rsid}:{match.alt}",
                    evidence_type="curated_local_rule_reference",
                    clinical_relevance="actionable_pgx_support",
                    confidence="moderate" if "CPIC" in source_key else "supportive",
                    citation_url=source["url"],
                    normalized_gene=normalized_gene,
                    normalized_variant=normalized_variant,
                    normalized_drug=normalized_drug,
                    interpretation_text=(
                        f"Curated local PGx rule uses {match.rsid} in {match.gene} as evidence relevant to "
                        f"{match.effect.replace('_', ' ')}."
                    ),
                    source_module="src.evidence_integration",
                    status="available",
                    details={
                        "allele": match.allele,
                        "alt": match.alt,
                        "function": match.function,
                        "effect": match.effect,
                        "genotype": match.genotype,
                        "genotype_code": match.genotype_code,
                    },
                )
            )
        return records


class EvidenceIntegrator:
    """Attach curated local references and optional structured external evidence."""

    def __init__(
        self,
        enable_remote_lookup: bool = False,
        remote_service: RemoteEvidenceService | None = None,
    ) -> None:
        self.enable_remote_lookup = enable_remote_lookup
        self.local_adapter = LocalRuleEvidenceAdapter()
        self.remote_service = remote_service or (RemoteEvidenceService() if enable_remote_lookup else None)

    def local_records_for_match(self, match: AlleleMatch, *, drug: str | None = None) -> list[EvidenceRecord]:
        return [record.to_evidence_record() for record in self.local_adapter.records_for_match(match, drug=drug)]

    def _external_records_for_match(self, match: AlleleMatch, *, drug: str | None = None) -> list[StructuredEvidence]:
        if not self.enable_remote_lookup or self.remote_service is None:
            return []
        return self.remote_service.lookup_variant(
            match.rsid,
            match.gene,
            drug=drug,
            variant_token=match.rsid,
        )

    def _resolve_conflicts(
        self,
        merged_records: list[StructuredEvidence],
        *,
        normalized_gene: str | None,
        normalized_variant: str | None,
        normalized_drug: str | None,
    ) -> list[EvidenceConflict]:
        signals = OrderedDict()
        sources: list[str] = []
        for record in merged_records:
            if record.status != "available":
                continue
            token = _signal_token(record)
            if not token:
                continue
            signals[token] = True
            sources.append(record.source_name)

        if len(signals) <= 1:
            return []

        context = "|".join([normalized_gene or "none", normalized_variant or "none", normalized_drug or "none"])
        return [
            EvidenceConflict(
                context_key=context,
                issue="Conflicting interpretation signals were observed across merged evidence sources.",
                conflicting_values=list(signals.keys()),
                source_names=sorted(set(sources)),
                resolution=(
                    "Retain curated local rule evidence as primary and downgrade conflicting external records "
                    "to review-only context until the discrepancy is manually resolved."
                ),
            )
        ]

    def _summarize_aggregate(
        self,
        local_records: list[StructuredEvidence],
        external_records: list[StructuredEvidence],
        conflicts: list[EvidenceConflict],
    ) -> tuple[str, str]:
        available_external = [record for record in external_records if record.status == "available"]
        unavailable_sources = sorted({record.source_name for record in external_records if record.status != "available"})

        if local_records:
            summary = (
                f"Structured evidence merged {len(local_records)} local curated PGx record(s) and "
                f"{len(available_external)} external annotation record(s)."
            )
            status = "available" if not conflicts and not unavailable_sources else "partial"
        elif available_external:
            summary = (
                f"Structured evidence merged {len(available_external)} external annotation record(s), "
                "but no local actionable PGx rule evidence was available for interpretation."
            )
            status = "partial"
        else:
            summary = "No structured evidence was available for this context."
            status = "unavailable"

        if conflicts:
            summary += " Conflicting evidence signals were detected and downgraded to review-only context."
        if unavailable_sources:
            summary += " External services unavailable: " + ", ".join(unavailable_sources) + "."
        return summary, status

    def aggregate_records(
        self,
        local_records: list[StructuredEvidence],
        external_records: list[StructuredEvidence],
        *,
        normalized_gene: str | None,
        normalized_variant: str | None,
        normalized_drug: str | None,
    ) -> EvidenceAggregate:
        deduped_local = _dedupe_structured_evidence(local_records)
        deduped_external = _dedupe_structured_evidence(external_records)
        merged = _dedupe_structured_evidence(deduped_local + deduped_external)
        conflicts = self._resolve_conflicts(
            merged,
            normalized_gene=normalized_gene,
            normalized_variant=normalized_variant,
            normalized_drug=normalized_drug,
        )
        summary, availability = self._summarize_aggregate(deduped_local, deduped_external, conflicts)
        return EvidenceAggregate(
            normalized_gene=normalized_gene,
            normalized_variant=normalized_variant,
            normalized_drug=normalized_drug,
            local_rule_evidence=deduped_local,
            external_annotation=deduped_external,
            merged_evidence=merged,
            conflicts=conflicts,
            final_evidence_summary=summary,
            availability_status=availability,
        )

    def aggregate_match(self, match: AlleleMatch, *, drug: str | None = None) -> EvidenceAggregate:
        local_records = self.local_adapter.records_for_match(match, drug=drug)
        external_records = self._external_records_for_match(match, drug=drug)
        return self.aggregate_records(
            local_records,
            external_records,
            normalized_gene=_normalize_gene(match.gene),
            normalized_variant=_normalize_variant(match.rsid),
            normalized_drug=_normalize_drug(drug),
        )

    def aggregate_assessment(self, assessment: GeneAssessment, *, drug: str | None = None) -> EvidenceAggregate:
        local_records: list[StructuredEvidence] = []
        external_records: list[StructuredEvidence] = []
        normalized_gene = _normalize_gene(assessment.gene)
        normalized_drug = _normalize_drug(drug)

        for match in assessment.matched_alleles:
            aggregate = self.aggregate_match(match, drug=drug)
            local_records.extend(aggregate.local_rule_evidence)
            external_records.extend(aggregate.external_annotation)

        normalized_variant = None
        if len({match.rsid for match in assessment.matched_alleles}) == 1 and assessment.matched_alleles:
            normalized_variant = _normalize_variant(assessment.matched_alleles[0].rsid)

        return self.aggregate_records(
            local_records,
            external_records,
            normalized_gene=normalized_gene,
            normalized_variant=normalized_variant,
            normalized_drug=normalized_drug,
        )

    def provenance_for_assessment(
        self,
        assessment: GeneAssessment,
        *,
        drug: str | None = None,
    ) -> list[EvidenceRecord]:
        aggregate = self.aggregate_assessment(assessment, drug=drug)
        provenance = [record.to_evidence_record() for record in aggregate.merged_evidence]
        for conflict in aggregate.conflicts:
            provenance.append(
                EvidenceRecord(
                    source="Pharmexia evidence aggregator",
                    label=aggregate.normalized_gene or "evidence",
                    assertion=conflict.resolution,
                    source_module="src.evidence_integration",
                    evidence_type="evidence_conflict_resolution",
                    status="available",
                    details=conflict.to_dict(),
                )
            )
        if not provenance and aggregate.final_evidence_summary:
            provenance.append(
                EvidenceRecord(
                    source="Pharmexia evidence aggregator",
                    label=aggregate.normalized_gene or "evidence",
                    assertion=aggregate.final_evidence_summary,
                    source_module="src.evidence_integration",
                    evidence_type="evidence_summary",
                    status=aggregate.availability_status,
                )
            )
        return provenance


def _match_variant_to_definitions(variant: ObservedVariant) -> list[AlleleMatch]:
    gene = (variant.gene or RSID_TO_GENE.get(variant.rsid or "") or "").upper()
    if gene not in ALLELE_DEFINITIONS or (variant.genotype_code or 0) <= 0:
        return []

    matches: list[AlleleMatch] = []
    for definition in ALLELE_DEFINITIONS[gene]:
        if (
            variant.rsid == definition.get("rsid")
            and alt_matches_definition(variant.ref, variant.alt, definition)
        ):
            matches.append(
                AlleleMatch(
                    gene=gene,
                    rsid=str(definition["rsid"]),
                    alt=str(definition["alt"]),
                    allele=definition.get("allele"),
                    function=definition.get("function"),
                    effect=str(definition["effect"]),
                    genotype=variant.genotype,
                    genotype_code=int(variant.genotype_code or 0),
                    sources=list(definition.get("sources", [])),
                )
            )
    return matches


def annotate_variant_evidence(
    variants: list[ObservedVariant],
    integrator: EvidenceIntegrator,
    annotation_service: VariantAnnotationService | None = None,
) -> list[VariantEvidenceAnnotation]:
    """Attach structured PGx evidence context to pharmacogene variants."""
    annotations_by_token: "OrderedDict[str, VariantEvidenceAnnotation]" = OrderedDict()
    annotation_service = annotation_service or VariantAnnotationService()

    for variant in variants:
        matches = _match_variant_to_definitions(variant)
        effect_prediction = annotation_service.annotate_variant(variant)
        effect_record = annotation_service.to_structured_evidence(effect_prediction)

        annotation = annotations_by_token.get(variant.token)
        if annotation is None:
            annotation = VariantEvidenceAnnotation(
                variant_token=variant.token,
                gene=_normalize_gene(variant.gene or RSID_TO_GENE.get(variant.rsid or "")) or "UNKNOWN",
                rsid=variant.rsid,
                variant_effect=effect_prediction,
            )
            annotations_by_token[variant.token] = annotation
        else:
            annotation.variant_effect = effect_prediction

        local_records: list[StructuredEvidence] = []
        external_records: list[StructuredEvidence] = []
        for match in matches:
            if match.allele and match.allele not in annotation.matched_alleles:
                annotation.matched_alleles.append(match.allele)
            if match.effect not in annotation.matched_effects:
                annotation.matched_effects.append(match.effect)
            aggregate = integrator.aggregate_match(match)
            local_records.extend(aggregate.local_rule_evidence)
            external_records.extend(aggregate.external_annotation)

        variant_aggregate = integrator.aggregate_records(
            local_records,
            external_records,
            normalized_gene=annotation.gene,
            normalized_variant=_normalize_variant(variant.token),
            normalized_drug=None,
        )
        annotation.structured_evidence = variant_aggregate.merged_evidence
        annotation.conflicts = variant_aggregate.conflicts
        annotation.final_evidence_summary = variant_aggregate.final_evidence_summary
        annotation.availability_status = variant_aggregate.availability_status
        annotation.evidence_records = [record.to_evidence_record() for record in variant_aggregate.merged_evidence]
        for conflict in variant_aggregate.conflicts:
            annotation.evidence_records.append(
                EvidenceRecord(
                    source="Pharmexia evidence aggregator",
                    label=annotation.gene,
                    assertion=conflict.resolution,
                    source_module="src.evidence_integration",
                    evidence_type="evidence_conflict_resolution",
                    status="available",
                    details=conflict.to_dict(),
                )
            )
        annotation.structured_evidence.append(effect_record)
        annotation.evidence_records.append(effect_record.to_evidence_record())
        if annotation.availability_status == "unavailable" and effect_prediction.availability_status in {"available", "partial"}:
            annotation.availability_status = "partial"
        if annotation.final_evidence_summary:
            annotation.final_evidence_summary += " " + effect_prediction.summary
        else:
            annotation.final_evidence_summary = effect_prediction.summary

    return list(annotations_by_token.values())

# --- end merged module: src/evidence_integration.py ---

# --- begin merged module: src/core/evidence_schema.py ---
"""Normalized evidence records used by the Pharmexia aggregation engine."""


def _object_value(record: object, key: str, default: Any = None) -> Any:
    if isinstance(record, dict):
        return record.get(key, default)
    return getattr(record, key, default)


def normalized_record_from_structured_evidence(
    record: StructuredEvidence | dict[str, Any],
    *,
    drug_status_lookup: dict[str, str] | None = None,
    evidence_origin: EvidenceOrigin = "evidence_based",
) -> NormalizedEvidenceRecord:
    normalized_drug = _normalize_drug(_object_value(record, "normalized_drug"))
    drug_lookup = drug_status_lookup or {}
    status = str(_object_value(record, "status", "available"))
    return NormalizedEvidenceRecord(
        source_name=str(_object_value(record, "source_name", "unknown")),
        source_type=str(_object_value(record, "source_type", "knowledge_source")),
        source_record_id=_object_value(record, "source_record_id"),
        drug_name=normalized_drug,
        normalized_drug_name=normalized_drug,
        drug_status=str(drug_lookup.get(str(normalized_drug), "unknown")) if normalized_drug else "unknown",
        gene_symbol=_normalize_gene(_object_value(record, "normalized_gene")),
        variant_id=_normalize_variant(_object_value(record, "normalized_variant")),
        protein_id=_object_value(record, "protein_id"),
        pathway_id=_object_value(record, "pathway_id"),
        evidence_type=str(_object_value(record, "evidence_type", "unspecified")),
        evidence_strength=str(_object_value(record, "confidence", _object_value(record, "evidence_strength", "unknown"))),
        clinical_relevance=str(_object_value(record, "clinical_relevance", "")),
        pk_relevance=str(_object_value(record, "pk_relevance", "")),
        pd_relevance=str(_object_value(record, "pd_relevance", "")),
        pharmacology_relevance=str(_object_value(record, "pharmacology_relevance", "")),
        pharmacognosy_relevance=str(_object_value(record, "pharmacognosy_relevance", "")),
        interpretation_text=str(_object_value(record, "interpretation_text", "")),
        citation_url=_object_value(record, "citation_url"),
        last_updated=_object_value(record, "last_updated"),
        confidence_score=None,
        coverage_status="available" if status == "available" else "partial",
        source_module=str(_object_value(record, "source_module", "")),
        evidence_origin=evidence_origin if status == "available" else "review_only",
        status=status,
        clinical_grade=bool(_object_value(record, "clinical_grade", False)),
        exploratory=bool(_object_value(record, "exploratory", False)),
        details=dict(_object_value(record, "details", {}) or {}),
    )


def normalized_record_from_model_finding(
    finding: DrugFinding | dict[str, Any],
) -> NormalizedEvidenceRecord:
    confidence = _object_value(finding, "confidence")
    confidence_payload = confidence if isinstance(confidence, dict) else (confidence.to_dict() if confidence is not None else {})
    provenance = list(_object_value(finding, "provenance", []) or [])
    first_provenance = provenance[0] if provenance else None
    citation_url = _object_value(first_provenance, "url")
    drug = _normalize_drug(_object_value(finding, "drug"))
    category = str(_object_value(finding, "category", "MODEL_ASSISTED"))
    return NormalizedEvidenceRecord(
        source_name=str(_object_value(first_provenance, "source", "Pharmexia predictive model")),
        source_type="predictive_model",
        source_record_id=f"model:{drug or 'unspecified'}:{_object_value(finding, 'evidence_type', 'predictive_model')}",
        drug_name=drug,
        normalized_drug_name=drug,
        drug_status="PARTIAL_EVIDENCE_SUPPORT" if drug in DRUG_GENE_RULES else "UNSUPPORTED",
        gene_symbol=_normalize_gene(_object_value(finding, "gene")),
        variant_id=None,
        evidence_type=str(_object_value(finding, "evidence_type", "predictive_model")),
        evidence_strength=str(confidence_payload.get("evidence_strength", "exploratory")),
        clinical_relevance="model_assisted_exploratory_prediction",
        interpretation_text=str(_object_value(finding, "summary", "")),
        citation_url=citation_url,
        coverage_status="partial",
        source_module=str(_object_value(finding, "source_module", "src.ml_pipeline")),
        evidence_origin="model_assisted",
        status="available" if category == "MODEL_ASSISTED" else "partial",
        clinical_grade=False,
        exploratory=True,
        details={
            "recommendation": _object_value(finding, "recommendation", ""),
            "result_kind": _object_value(finding, "result_kind", ""),
            "phenotype": _object_value(finding, "phenotype"),
            "diplotype": _object_value(finding, "diplotype"),
            "matched_variants": list(_object_value(finding, "matched_variants", []) or []),
        },
    )

# --- end merged module: src/core/evidence_schema.py ---

# --- begin merged module: src/core/evidence_aggregator.py ---
"""Conflict-aware evidence aggregation for evidence-backed and model-assisted output."""


from collections import Counter
from dataclasses import replace


ACTIONABLE_EVIDENCE_TYPES = {
    "curated_local_rule_reference",
    "clinical_guideline_reference",
    "fda_label_pgx",
    "confirmed_pgx_finding",
}


def _local_drug_support_tier(drug: str | None) -> str:
    normalized = _normalize_drug(drug)
    if not normalized:
        return "unknown"
    return "PARTIAL_EVIDENCE_SUPPORT" if normalized in DRUG_GENE_RULES else "UNSUPPORTED"


def _normalized_signal_token(record: NormalizedEvidenceRecord) -> str | None:
    for key in ("effect", "function", "signal_direction"):
        value = record.details.get(key)
        if value:
            return str(value)
    if record.clinical_relevance in ACTIONABLE_RELEVANCE:
        return record.interpretation_text or record.clinical_relevance
    return None


def _is_actionable_normalized_record(record: NormalizedEvidenceRecord) -> bool:
    if record.status != "available" or record.evidence_origin != "evidence_based":
        return False
    return (
        record.evidence_type in ACTIONABLE_EVIDENCE_TYPES
        or record.clinical_relevance in ACTIONABLE_RELEVANCE
        or record.clinical_grade
    )


def _dedupe_normalized_records(records: list[NormalizedEvidenceRecord]) -> list[NormalizedEvidenceRecord]:
    deduped: "OrderedDict[tuple[str, str | None, str | None, str | None, str, str, str, str], NormalizedEvidenceRecord]" = OrderedDict()
    for record in records:
        key = (
            record.source_name,
            record.source_record_id,
            record.normalized_drug_name,
            record.gene_symbol,
            record.evidence_type,
            record.interpretation_text,
            record.evidence_origin,
            record.status,
        )
        if key not in deduped:
            deduped[key] = record
    return list(deduped.values())


def normalize_structured_evidence_records(
    records: list[StructuredEvidence | dict[str, Any]],
    *,
    drug_status_lookup: dict[str, str] | None = None,
    evidence_origin: EvidenceOrigin = "evidence_based",
) -> list[NormalizedEvidenceRecord]:
    """Bridge structured evidence into a broader normalized schema for downstream interpretation."""
    return [
        normalized_record_from_structured_evidence(
            record,
            drug_status_lookup=drug_status_lookup,
            evidence_origin=evidence_origin,
        )
        for record in records
    ]


def normalize_model_findings(
    findings: list[DrugFinding | dict[str, Any]],
    *,
    drug_filter: str | None = None,
) -> list[NormalizedEvidenceRecord]:
    normalized_filter = _normalize_drug(drug_filter)
    normalized: list[NormalizedEvidenceRecord] = []
    for finding in findings:
        record = normalized_record_from_model_finding(finding)
        if normalized_filter and record.normalized_drug_name != normalized_filter:
            continue
        normalized.append(record)
    return normalized


def merge_normalized_evidence(
    primary_records: list[NormalizedEvidenceRecord],
    secondary_records: list[NormalizedEvidenceRecord] | None = None,
    *,
    model_records: list[NormalizedEvidenceRecord] | None = None,
    normalized_gene: str | None = None,
    normalized_variant: str | None = None,
    normalized_drug: str | None = None,
    conflict_messages: list[str] | None = None,
    conflict_details: list[dict[str, Any]] | None = None,
    summary_hint: str | None = None,
) -> MergedEvidenceBundle:
    """Merge evidence safely without fabricating consensus or over-promoting weak support."""
    combined = _dedupe_normalized_records([*list(primary_records), *list(secondary_records or []), *list(model_records or [])])

    evidence_candidates = [record for record in combined if record.evidence_origin == "evidence_based" and record.status == "available"]
    model_assisted_records = [record for record in combined if record.evidence_origin == "model_assisted" and record.status == "available"]
    review_only_records = [
        replace(record, evidence_origin="review_only")
        for record in combined
        if record.evidence_origin == "review_only" or record.status != "available"
    ]

    messages = list(conflict_messages or [])
    details = list(conflict_details or [])
    signal_map: "OrderedDict[str, list[str]]" = OrderedDict()
    for record in evidence_candidates:
        token = _normalized_signal_token(record)
        if token:
            signal_map.setdefault(token, []).append(record.source_name)

    local_actionable_present = any(
        _is_actionable_normalized_record(record)
        and (record.evidence_type == "curated_local_rule_reference" or record.source_module == "src.evidence_integration")
        for record in evidence_candidates
    )
    if len(signal_map) > 1:
        messages.append(
            "Conflicting evidence signals were detected. Curated local PGx support remained primary, and conflicting records were downgraded to review-only context."
        )
        details.append(
            {
                "issue": "conflicting_interpretation_signals",
                "conflicting_values": list(signal_map.keys()),
                "source_names": sorted({source for sources in signal_map.values() for source in sources}),
                "resolution": "Conflicting evidence was retained as review-only context and not promoted into final evidence-backed interpretation.",
            }
        )
        if local_actionable_present:
            retained: list[NormalizedEvidenceRecord] = []
            downgraded: list[NormalizedEvidenceRecord] = []
            for record in evidence_candidates:
                if record.evidence_type == "curated_local_rule_reference" or record.source_module == "src.evidence_integration":
                    retained.append(record)
                else:
                    downgraded.append(replace(record, evidence_origin="review_only"))
            evidence_candidates = retained
            review_only_records.extend(downgraded)

    review_only_records = _dedupe_normalized_records(review_only_records)
    actionable_records = [record for record in evidence_candidates if _is_actionable_normalized_record(record)]
    supportive_records = [record for record in evidence_candidates if record not in actionable_records]

    if actionable_records:
        output_category: OutputCategory = "EVIDENCE_BASED"
    elif model_assisted_records:
        output_category = "MODEL_ASSISTED"
    else:
        output_category = "INSUFFICIENT_EVIDENCE"

    final_records = _dedupe_normalized_records(evidence_candidates + model_assisted_records + review_only_records)
    if actionable_records and not review_only_records and not messages:
        availability_status: EvidenceAvailabilityStatus = "available"
    elif final_records:
        availability_status = "partial"
    else:
        availability_status = "unavailable"

    summary_bits: list[str] = []
    if actionable_records:
        summary_bits.append(
            f"Evidence-backed interpretation is supported by {len(actionable_records)} actionable PGx record(s)."
        )
    elif model_assisted_records:
        summary_bits.append(
            "Actionable evidence-backed PGx support was insufficient, so only model-assisted findings were retained."
        )
    else:
        summary_bits.append("INSUFFICIENT_EVIDENCE: no actionable evidence-backed PGx record was available for this context.")
    if supportive_records:
        summary_bits.append(
            f"{len(supportive_records)} supportive annotation record(s) were retained as non-authoritative context."
        )
    if review_only_records:
        summary_bits.append(
            f"{len(review_only_records)} record(s) were retained as review-only context because they were unavailable or conflicted with stronger support."
        )
    if messages:
        summary_bits.append("Conflict resolution was conservative and did not override curated PGx support.")
    if summary_hint:
        summary_bits.append(summary_hint)

    source_summary = Counter(record.source_name for record in final_records)
    strength_summary = Counter(record.evidence_strength for record in final_records)
    return MergedEvidenceBundle(
        normalized_drug_name=_normalize_drug(normalized_drug) or (final_records[0].normalized_drug_name if final_records else None),
        gene_symbol=_normalize_gene(normalized_gene) or (final_records[0].gene_symbol if final_records else None),
        variant_id=_normalize_variant(normalized_variant) or (final_records[0].variant_id if final_records else None),
        records=final_records,
        evidence_based_records=evidence_candidates,
        model_assisted_records=model_assisted_records,
        review_only_records=review_only_records,
        source_summary=dict(source_summary),
        strength_summary=dict(strength_summary),
        conflict_messages=list(OrderedDict.fromkeys(messages)),
        conflict_details=details,
        output_category=output_category,
        availability_status=availability_status,
        summary=" ".join(bit for bit in summary_bits if bit),
        has_actionable_evidence=bool(actionable_records),
        model_assistance_allowed=not bool(actionable_records),
    )

# --- end merged module: src/core/evidence_aggregator.py ---

# --- begin merged module: src/services/evidence_service.py ---
"""Service facade for building structured evidence contexts used by prediction and reporting."""


class EvidenceService:
    """Aggregate local and external evidence into one prediction-ready interpretation layer."""

    def __init__(
        self,
        *,
        enable_remote_lookup: bool = False,
        integrator: EvidenceIntegrator | None = None,
    ) -> None:
        self.integrator = integrator or EvidenceIntegrator(enable_remote_lookup=enable_remote_lookup)

    def aggregate_assessment_context(
        self,
        assessment: GeneAssessment,
        *,
        drug: str | None = None,
        model_findings: list[DrugFinding] | None = None,
        variant_annotations: list[VariantEvidenceAnnotation] | None = None,
    ) -> MergedEvidenceBundle:
        aggregate = self.integrator.aggregate_assessment(assessment, drug=drug)
        normalized_drug = _normalize_drug(drug)
        supplemental_records = [
            record
            for annotation in (variant_annotations or [])
            if annotation.gene == aggregate.normalized_gene
            for record in annotation.structured_evidence
            if record.evidence_type == "variant_effect_annotation"
        ]
        evidence_records = normalize_structured_evidence_records(
            [*aggregate.local_rule_evidence, *aggregate.external_annotation, *supplemental_records],
            drug_status_lookup={normalized_drug: _local_drug_support_tier(normalized_drug)} if normalized_drug else None,
        )
        return merge_normalized_evidence(
            evidence_records,
            model_records=normalize_model_findings(model_findings or [], drug_filter=drug),
            normalized_gene=aggregate.normalized_gene,
            normalized_variant=aggregate.normalized_variant,
            normalized_drug=aggregate.normalized_drug,
            conflict_messages=[conflict.issue for conflict in aggregate.conflicts],
            conflict_details=[conflict.to_dict() for conflict in aggregate.conflicts],
            summary_hint=aggregate.final_evidence_summary,
        )

    def aggregate_prediction_contexts(
        self,
        *,
        gene_assessments: dict[str, GeneAssessment],
        selected_drugs: list[str],
        model_findings: list[DrugFinding] | None = None,
        variant_annotations: list[VariantEvidenceAnnotation] | None = None,
    ) -> list[MergedEvidenceBundle]:
        bundles: list[MergedEvidenceBundle] = []
        for drug in selected_drugs:
            normalized_drug = _normalize_drug(drug)
            genes = list(DRUG_GENE_RULES.get(normalized_drug or "", {}).get("genes", []))
            structured_records: list[StructuredEvidence] = []
            conflicts: list[dict[str, Any]] = []
            conflict_messages: list[str] = []
            summary_hints: list[str] = []
            variant_ids: list[str] = []
            for gene in genes:
                assessment = gene_assessments.get(gene)
                if assessment is None:
                    continue
                aggregate = self.integrator.aggregate_assessment(assessment, drug=normalized_drug)
                structured_records.extend(aggregate.local_rule_evidence)
                structured_records.extend(aggregate.external_annotation)
                conflicts.extend(conflict.to_dict() for conflict in aggregate.conflicts)
                conflict_messages.extend(conflict.issue for conflict in aggregate.conflicts)
                if aggregate.final_evidence_summary:
                    summary_hints.append(aggregate.final_evidence_summary)
                if aggregate.normalized_variant:
                    variant_ids.append(aggregate.normalized_variant)
            structured_records.extend(
                record
                for annotation in (variant_annotations or [])
                if annotation.gene in genes
                for record in annotation.structured_evidence
                if record.evidence_type == "variant_effect_annotation"
            )
            summary_hints.extend(
                annotation.variant_effect.summary
                for annotation in (variant_annotations or [])
                if annotation.gene in genes and annotation.variant_effect is not None
            )

            bundle = merge_normalized_evidence(
                normalize_structured_evidence_records(
                    structured_records,
                    drug_status_lookup={normalized_drug: _local_drug_support_tier(normalized_drug)} if normalized_drug else None,
                ),
                model_records=normalize_model_findings(model_findings or [], drug_filter=normalized_drug),
                normalized_gene=",".join(genes) if len(genes) > 1 else (genes[0] if genes else None),
                normalized_variant=variant_ids[0] if len(set(variant_ids)) == 1 and variant_ids else None,
                normalized_drug=normalized_drug,
                conflict_messages=conflict_messages,
                conflict_details=conflicts,
                summary_hint=" ".join(OrderedDict.fromkeys(summary_hints)),
            )
            if not bundle.records and genes:
                bundle.summary = (
                    f"INSUFFICIENT_EVIDENCE: no actionable PGx evidence was observed for "
                    f"{drug_display_label(normalized_drug or drug)} across the supported genes {', '.join(genes)}."
                )
            bundles.append(bundle)
        return bundles

# --- end merged module: src/services/evidence_service.py ---

# --- begin merged module: src/core/drug_interactions.py ---
"""Structured local drug interaction rules and helpers."""


import json
from functools import lru_cache
from pathlib import Path


# Module-level cache for the interaction catalog (populated on first successful load).
_INTERACTION_CATALOG_CACHE: "InteractionCatalog | None" = None

INTERACTION_SCHEMA_PATH = Path(__file__).resolve().parent / "data" / "interaction_schema.json"

INTERACTION_SEVERITY_ORDER = {
    "CONTRAINDICATED": 0,
    "MAJOR": 1,
    "HIGH": 1,
    "MODERATE": 2,
    "LOW": 3,
    "MINOR": 3,
    "INFORMATIONAL": 4,
    "UNKNOWN": 5,
    "UNSUPPORTED": 6,
}

LEGACY_INTERACTION_SEVERITY_MAP = {
    "HIGH": "MAJOR",
    "MODERATE": "MODERATE",
    "LOW": "MINOR",
    "INFORMATIONAL": "UNKNOWN",
    "UNSUPPORTED": "UNKNOWN",
}


@dataclass(slots=True)
class InteractionRuleProfile:
    key: str
    status: InteractionStatus
    severity: InteractionSeverity
    confidence: str
    summary: str
    clinical_relevance: str
    mechanism: str = ""
    recommendation: str | None = None
    required_effects_any: list[str] = field(default_factory=list)
    required_effects_all: list[str] = field(default_factory=list)
    require_ambiguous: bool = False
    require_inconclusive: bool = False
    require_incomplete: bool = False
    require_matches: bool = False
    disallow_ambiguous: bool = False


@dataclass(slots=True)
class InteractionRule:
    interaction_id: str
    interaction_type: InteractionType
    subject_drug: str
    interacting_entity: str
    entity_type: str
    gene: str | None = None
    evidence_based: bool = True
    provenance: list[InteractionProvenance] = field(default_factory=list)
    limitations: list[str] = field(default_factory=list)
    profiles: list[InteractionRuleProfile] = field(default_factory=list)


@dataclass(slots=True)
class InteractionCatalog:
    schema_version: str
    severity_categories: dict[str, str] = field(default_factory=dict)
    drug_drug_rules: list[InteractionRule] = field(default_factory=list)
    drug_context_rules: list[InteractionRule] = field(default_factory=list)
    limitations: list[str] = field(default_factory=list)


def _interaction_provenance_from_payload(payload: dict[str, Any]) -> InteractionProvenance:
    source_record_id = str(payload.get("source_record_id") or "").strip() or None
    source_details = REFERENCE_SOURCES.get(source_record_id or "", {})
    source_name = str(payload.get("source_name") or source_details.get("label") or source_record_id or "Reference source")
    citation_url = str(payload.get("citation_url") or source_details.get("url") or "").strip() or None
    return InteractionProvenance(
        source_name=source_name,
        source_record_id=source_record_id,
        evidence_type=str(payload.get("evidence_type") or "reference"),
        citation_url=citation_url,
        source_module="src.core.drug_interactions",
        note=str(payload.get("note") or ""),
    )


def _parse_interaction_profile(payload: dict[str, Any]) -> InteractionRuleProfile:
    return InteractionRuleProfile(
        key=str(payload.get("key") or "default"),
        status=str(payload.get("status") or "supported"),
        severity=str(payload.get("severity") or "INFORMATIONAL"),
        confidence=str(payload.get("confidence") or "limited"),
        summary=str(payload.get("summary") or ""),
        clinical_relevance=str(payload.get("clinical_relevance") or ""),
        mechanism=str(payload.get("mechanism") or ""),
        recommendation=str(payload.get("recommendation")) if payload.get("recommendation") is not None else None,
        required_effects_any=[str(item) for item in payload.get("required_effects_any", [])],
        required_effects_all=[str(item) for item in payload.get("required_effects_all", [])],
        require_ambiguous=bool(payload.get("require_ambiguous", False)),
        require_inconclusive=bool(payload.get("require_inconclusive", False)),
        require_incomplete=bool(payload.get("require_incomplete", False)),
        require_matches=bool(payload.get("require_matches", False)),
        disallow_ambiguous=bool(payload.get("disallow_ambiguous", False)),
    )


def _parse_interaction_rule(payload: dict[str, Any]) -> InteractionRule:
    return InteractionRule(
        interaction_id=str(payload.get("interaction_id") or ""),
        interaction_type=str(payload.get("interaction_type") or "drug_gene"),
        subject_drug=str(payload.get("subject_drug") or "").strip().lower(),
        interacting_entity=str(payload.get("interacting_entity") or "").strip(),
        entity_type=str(payload.get("entity_type") or "gene"),
        gene=(str(payload.get("gene") or "").strip() or None),
        evidence_based=bool(payload.get("evidence_based", True)),
        provenance=[_interaction_provenance_from_payload(item) for item in payload.get("sources", []) if isinstance(item, dict)],
        limitations=[str(item) for item in payload.get("limitations", [])],
        profiles=[_parse_interaction_profile(item) for item in payload.get("profiles", []) if isinstance(item, dict)],
    )


def load_interaction_catalog(path: str | "Path | None" = None) -> "InteractionCatalog":
    """Load the local structured interaction catalog.

    When the data file is absent the function returns an ``InteractionCatalog``
    with ``schema_version="missing"`` and a single limitation note rather than
    crashing.  The caller (``InteractionService``) will then produce only
    "unavailable" interaction findings — ensuring that the absence of a catalog
    file is never silently swallowed.

    Results are cached per path; the default path is cached for the lifetime of
    the process.
    """
    global _INTERACTION_CATALOG_CACHE

    schema_path = Path(path) if path is not None else INTERACTION_SCHEMA_PATH

    if path is None and _INTERACTION_CATALOG_CACHE is not None:
        return _INTERACTION_CATALOG_CACHE

    if not schema_path.exists():
        missing = InteractionCatalog(
            schema_version="missing",
            limitations=[
                "The local interaction schema file is unavailable. "
                "Pharmexia cannot emit curated drug-drug or drug-gene interaction findings. "
                "This must be treated as a pipeline warning, not as evidence of no interactions."
            ],
        )
        if path is None:
            _INTERACTION_CATALOG_CACHE = missing
        return missing

    try:
        payload = json.loads(schema_path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        broken = InteractionCatalog(
            schema_version="error",
            limitations=[
                f"The local interaction schema file could not be read ({exc}). "
                "Interaction checking is unavailable."
            ],
        )
        if path is None:
            _INTERACTION_CATALOG_CACHE = broken
        return broken

    catalog = InteractionCatalog(
        schema_version=str(payload.get("schema_version") or "unknown"),
        severity_categories={
            str(key): str(value) for key, value in dict(payload.get("severity_categories", {})).items()
        },
        drug_drug_rules=[
            _parse_interaction_rule(item) for item in payload.get("drug_drug_rules", []) if isinstance(item, dict)
        ],
        drug_context_rules=[
            _parse_interaction_rule(item) for item in payload.get("drug_context_rules", []) if isinstance(item, dict)
        ],
        limitations=[str(item) for item in payload.get("limitations", [])],
    )
    if path is None:
        _INTERACTION_CATALOG_CACHE = catalog
    return catalog


def _interaction_effect_terms(assessment: GeneAssessment | None) -> set[str]:
    if assessment is None:
        return set()
    return {
        str(match.effect)
        for match in assessment.matched_alleles
        if getattr(match, "effect", None)
    }


def _profile_matches_assessment(profile: InteractionRuleProfile, assessment: GeneAssessment) -> bool:
    effects = _interaction_effect_terms(assessment)
    if profile.required_effects_all and not set(profile.required_effects_all).issubset(effects):
        return False
    if profile.required_effects_any and not effects.intersection(profile.required_effects_any):
        return False
    if profile.require_ambiguous and not assessment.ambiguous:
        return False
    if profile.require_inconclusive and assessment.call_confidence != "INCONCLUSIVE":
        return False
    if profile.require_incomplete and assessment.coverage_complete:
        return False
    if profile.require_matches and not assessment.matched_alleles:
        return False
    if profile.disallow_ambiguous and assessment.ambiguous:
        return False
    return True


def instantiate_interaction_finding(
    rule: InteractionRule,
    profile: InteractionRuleProfile,
    assessment: GeneAssessment | None = None,
) -> DrugInteractionFinding:
    """Convert a matched rule profile into a structured interaction finding."""
    summary = profile.summary.strip()
    clinical_relevance = profile.clinical_relevance.strip()
    limitations = list(rule.limitations)

    if assessment is not None:
        if assessment.phenotype:
            summary = f"{summary} Local panel phenotype: {assessment.phenotype}."
        elif assessment.local_panel_call and not assessment.ambiguous:
            summary = f"{summary} Local panel call: {assessment.local_panel_call}."
        matched_markers = sorted({match.rsid for match in assessment.matched_alleles if match.rsid})
        if matched_markers:
            clinical_relevance = (
                f"{clinical_relevance} Observed supporting markers: {', '.join(matched_markers)}."
            ).strip()
        limitations = sorted(set(limitations + list(assessment.limitations)))

    recommendation = profile.recommendation if rule.evidence_based and profile.status == "supported" else None
    severity = LEGACY_INTERACTION_SEVERITY_MAP.get(profile.severity, profile.severity)
    evidence_category: InteractionEvidenceCategory
    if rule.evidence_based and profile.status == "supported":
        evidence_category = "EVIDENCE_BASED"
    elif profile.status == "supported":
        evidence_category = "DATABASE_SUPPORTED"
    else:
        evidence_category = "INSUFFICIENT_EVIDENCE"
    return DrugInteractionFinding(
        interaction_id=f"{rule.interaction_id}::{profile.key}",
        interaction_type=rule.interaction_type,
        subject_drug=rule.subject_drug,
        interacting_entity=rule.interacting_entity,
        entity_type=rule.entity_type,
        severity=severity,
        status=profile.status,
        evidence_category=evidence_category,
        confidence=profile.confidence,
        summary=summary,
        clinical_relevance=clinical_relevance,
        mechanism=profile.mechanism,
        recommendation=recommendation,
        evidence_based=bool(rule.evidence_based and profile.status == "supported"),
        provenance=list(rule.provenance),
        limitations=limitations,
    )


def unsupported_drug_interaction_warning(drug: str) -> DrugInteractionFinding:
    """Return a structured warning when a requested drug is not covered by the local interaction catalog."""
    normalized = str(drug).strip().lower()
    label = drug_display_label(normalized or drug)
    return DrugInteractionFinding(
        interaction_id=f"unsupported::{normalized or drug}",
        interaction_type="unsupported_drug",
        subject_drug=normalized or drug,
        interacting_entity="local_interaction_catalog",
        entity_type="drug",
        severity="UNKNOWN",
        status="unsupported",
        evidence_category="INSUFFICIENT_EVIDENCE",
        confidence="none",
        summary=f"{label} is not covered by the local Pharmexia interaction catalog.",
        clinical_relevance=(
            "Pharmexia cannot emit a curated drug-drug or drug-gene interaction interpretation for this drug without validated local interaction data."
        ),
        mechanism="unsupported_local_catalog",
        recommendation=None,
        evidence_based=False,
        provenance=[
            InteractionProvenance(
                source_name=APP_NAME,
                source_record_id="local_catalog_guard",
                evidence_type="coverage_guard",
                source_module="src.core.drug_interactions",
                note="Unsupported drug warning generated from the local interaction coverage guard.",
            )
        ],
        limitations=[
            "Unsupported drugs are reported as warnings only; Pharmexia does not fabricate interaction evidence.",
        ],
    )

# --- end merged module: src/core/drug_interactions.py ---

# --- begin merged module: src/services/interaction_service.py ---
"""Service layer for structured drug interaction detection."""


from itertools import combinations



def _no_current_medications_finding(target_drug: str) -> DrugInteractionFinding:
    label = drug_display_label(target_drug)
    return DrugInteractionFinding(
        interaction_id=f"{target_drug}::no_current_medications",
        interaction_type="medication_context",
        subject_drug=target_drug,
        interacting_entity="none_reported",
        entity_type="medication_list",
        severity="UNKNOWN",
        status="supported",
        evidence_category="DATABASE_SUPPORTED",
        confidence="reported",
        summary="No concurrent medications provided.",
        clinical_relevance=(
            f"Drug-drug interaction checking for {label} was limited to the reported medication list and no other medications were provided."
        ),
        mechanism="reported_none",
        recommendation=None,
        evidence_based=False,
        provenance=[
            InteractionProvenance(
                source_name=APP_NAME,
                source_record_id="reported_current_medications:none",
                evidence_type="reported_medication_context",
                source_module="src.services.interaction_service",
                note="No current medications were provided by the user.",
            )
        ],
        limitations=[
            "No concurrent-medication context was available beyond the explicitly reported list.",
        ],
    )


def _interaction_evidence_unavailable_finding(target_drug: str, current_drug: str) -> DrugInteractionFinding:
    return DrugInteractionFinding(
        interaction_id=f"{target_drug}::{current_drug}::interaction_evidence_unavailable",
        interaction_type="drug_drug",
        subject_drug=target_drug,
        interacting_entity=current_drug,
        entity_type="drug",
        severity="UNKNOWN",
        status="insufficient_evidence",
        evidence_category="INSUFFICIENT_EVIDENCE",
        confidence="limited",
        summary=(
            f"Interaction evidence is unavailable in the current local Pharmexia catalog for "
            f"{drug_display_label(target_drug)} with concurrent {drug_display_label(current_drug)}."
        ),
        clinical_relevance=(
            "This does not imply safety. It only means no curated local interaction rule was available for this drug pair."
        ),
        mechanism="no_curated_local_pair_rule",
        recommendation=None,
        evidence_based=False,
        provenance=[
            InteractionProvenance(
                source_name=APP_NAME,
                source_record_id=f"interaction_unavailable:{target_drug}:{current_drug}",
                evidence_type="interaction_catalog_gap",
                source_module="src.services.interaction_service",
                note="No curated local drug-drug rule was available for this target/current medication pair.",
            )
        ],
        limitations=[
            "Absence of a local interaction rule must not be interpreted as absence of interaction risk.",
        ],
    )


class InteractionService:
    """Build structured drug interaction findings from curated local rules."""

    def __init__(self, catalog: InteractionCatalog | None = None, drug_database_service=None) -> None:
        self.catalog = catalog or load_interaction_catalog()
        self.drug_database_service = drug_database_service or _drug_database_service()

    def _normalized_requested_drugs(self, drugs: list[str] | None) -> list[str]:
        entries, _unresolved = self.drug_database_service.normalize_many(drugs or [])
        return [entry.drug_key for entry in entries]

    def _normalize_with_unresolved(self, drugs: list[str] | None) -> tuple[list[str], list[str]]:
        entries, unresolved = self.drug_database_service.normalize_many(drugs or [])
        return [entry.drug_key for entry in entries], [str(item).strip().lower() for item in unresolved if str(item).strip()]

    def detect_drug_drug_interactions(self, drugs: list[str]) -> list[DrugInteractionFinding]:
        normalized = sorted(set(self._normalized_requested_drugs(drugs)))
        if len(normalized) < 2:
            return []
        present_pairs = {frozenset(pair) for pair in combinations(normalized, 2)}
        findings: list[DrugInteractionFinding] = []
        for rule in self.catalog.drug_drug_rules:
            pair = frozenset({rule.subject_drug, str(rule.interacting_entity).strip().lower()})
            if pair not in present_pairs or not rule.profiles:
                continue
            findings.append(instantiate_interaction_finding(rule, rule.profiles[0]))
        return findings

    def detect_context_interactions(
        self,
        *,
        selected_drugs: list[str],
        gene_assessments: dict[str, GeneAssessment],
    ) -> list[DrugInteractionFinding]:
        normalized = set(self._normalized_requested_drugs(selected_drugs))
        findings: list[DrugInteractionFinding] = []
        for rule in self.catalog.drug_context_rules:
            if rule.subject_drug not in normalized:
                continue
            gene_key = rule.gene or str(rule.interacting_entity)
            assessment = gene_assessments.get(gene_key)
            if assessment is None:
                continue
            for profile in rule.profiles:
                if _profile_matches_assessment(profile, assessment):
                    findings.append(instantiate_interaction_finding(rule, profile, assessment))
                    break
        return findings

    def detect_target_vs_current_medication_interactions(
        self,
        *,
        target_drug: str | None,
        current_medications: list[str] | None,
    ) -> list[DrugInteractionFinding]:
        if not target_drug:
            return []
        if not current_medications:
            return [_no_current_medications_finding(target_drug)]

        resolved_current, unresolved = self._normalize_with_unresolved(current_medications)
        findings: list[DrugInteractionFinding] = []
        pair_rules = {
            frozenset({rule.subject_drug, str(rule.interacting_entity).strip().lower()}): rule
            for rule in self.catalog.drug_drug_rules
            if rule.profiles
        }
        seen_pairs: set[frozenset[str]] = set()
        for medication in resolved_current:
            if medication == target_drug:
                continue
            pair = frozenset({target_drug, medication})
            if pair in seen_pairs:
                continue
            seen_pairs.add(pair)
            rule = pair_rules.get(pair)
            if rule is not None:
                findings.append(instantiate_interaction_finding(rule, rule.profiles[0]))
            else:
                findings.append(_interaction_evidence_unavailable_finding(target_drug, medication))
        for medication in unresolved:
            findings.append(unsupported_drug_interaction_warning(medication))
        return findings

    def detect_unsupported_drugs(
        self,
        *,
        requested_drugs: list[str] | None,
        resolved_drugs: list[str],
    ) -> list[DrugInteractionFinding]:
        requested = set(self._normalized_requested_drugs(requested_drugs))
        resolved = set(self._normalized_requested_drugs(resolved_drugs))
        return [unsupported_drug_interaction_warning(drug) for drug in sorted(requested.difference(resolved))]

    def aggregate_findings(
        self,
        *,
        requested_drugs: list[str] | None,
        resolved_drugs: list[str],
        current_medications: list[str] | None = None,
        gene_assessments: dict[str, GeneAssessment],
    ) -> list[DrugInteractionFinding]:
        """Combine drug-drug, drug-gene, drug-enzyme, drug-transporter, and unsupported-drug warnings."""
        target_drug = resolved_drugs[0] if resolved_drugs else None
        findings = (
            self.detect_target_vs_current_medication_interactions(
                target_drug=target_drug,
                current_medications=current_medications,
            )
            + self.detect_drug_drug_interactions(resolved_drugs if len(resolved_drugs) > 1 else [])
            + self.detect_context_interactions(selected_drugs=resolved_drugs, gene_assessments=gene_assessments)
            + self.detect_unsupported_drugs(requested_drugs=requested_drugs, resolved_drugs=resolved_drugs)
        )
        deduped: dict[str, DrugInteractionFinding] = {}
        for finding in findings:
            deduped[finding.interaction_id] = finding
        return sorted(
            deduped.values(),
            key=lambda finding: (
                INTERACTION_SEVERITY_ORDER.get(finding.severity, 99),
                drug_display_label(finding.subject_drug),
                finding.interacting_entity,
            ),
        )

# --- end merged module: src/services/interaction_service.py ---

# --- begin merged module: src/data_pipeline.py ---
"""Validation helpers for optional labeled PGx training data."""


from pathlib import Path

import pandas as pd



REQUIRED_TRAINING_COLUMNS = {"drug", "outcome_label"}
LEAKAGE_KEYWORDS = ("outcome", "label", "target", "recommendation", "prediction", "confidence", "score")
MIN_TRAINING_ROWS = 24
MIN_CLASS_COUNT = 4


def summarize_label_distribution(labels: pd.Series) -> dict[str, object]:
    """Summarize label counts and imbalance for a categorical outcome vector."""
    if labels.empty:
        return {
            "counts": {},
            "n_classes": 0,
            "min_class_count": 0,
            "max_class_count": 0,
            "imbalance_ratio": None,
        }
    counts = labels.value_counts(dropna=False).sort_index()
    min_count = int(counts.min())
    max_count = int(counts.max())
    return {
        "counts": {str(label): int(count) for label, count in counts.items()},
        "n_classes": int(counts.size),
        "min_class_count": min_count,
        "max_class_count": max_count,
        "imbalance_ratio": round(max_count / min_count, 4) if min_count else None,
    }


def validate_training_dataset(df: pd.DataFrame) -> dict[str, object]:
    """Validate a labeled PGx training dataset before any ML workflow runs.

    Suspicious columns that match leakage keywords are treated as a hard
    failure rather than a warning; a model trained on outcome-leaking features
    produces misleadingly optimistic validation metrics and must not reach
    production inference.
    """
    missing = sorted(REQUIRED_TRAINING_COLUMNS.difference(df.columns))
    label_distribution = summarize_label_distribution(df["outcome_label"]) if "outcome_label" in df.columns else summarize_label_distribution(pd.Series(dtype=object))
    suspicious_columns = sorted(
        column
        for column in df.columns
        if column not in METADATA_COLUMNS
        and column not in MODEL_FEATURE_COLUMNS
        and any(keyword in str(column).lower() for keyword in LEAKAGE_KEYWORDS)
    )
    duplicate_row_count = int(df.duplicated().sum()) if not df.empty else 0
    issues: list[str] = []
    if missing:
        issues.append("Required training columns are missing.")
    if int(len(df)) < MIN_TRAINING_ROWS:
        issues.append("Training dataset does not contain enough rows for a realistic holdout and cross-validation workflow.")
    if int(label_distribution["n_classes"]) < 2:
        issues.append("Training dataset must contain at least two outcome classes.")
    if int(label_distribution["min_class_count"] or 0) < MIN_CLASS_COUNT:
        issues.append("Each outcome class must have enough samples to support stratified holdout and calibration.")
    if suspicious_columns:
        # Treat as a hard failure — do not train when potential data leakage is detected.
        issues.append(
            f"Potential data-leakage columns detected and training blocked: {', '.join(suspicious_columns)}. "
            "Remove or rename these columns before re-running the training workflow."
        )

    status = "ok" if not issues else "insufficient"
    return {
        "status": status,
        "rows": int(len(df)),
        "missing_columns": missing,
        "n_outcome_classes": int(label_distribution["n_classes"]),
        "label_distribution_summary": label_distribution,
        "duplicate_row_count": duplicate_row_count,
        "suspicious_columns": suspicious_columns,
        "issues": issues,
        "supported_feature_count": len(MODEL_FEATURE_COLUMNS),
    }


def load_training_dataset(path: Path) -> pd.DataFrame:
    """Load a labeled PGx training dataset from CSV."""
    return pd.read_csv(path)


def summarize_project_context() -> dict[str, object]:
    """Return compact metadata for scripts and smoke checks."""
    return {
        "app_name": APP_NAME,
        "app_version": APP_VERSION,
        "supported_drugs": sorted(DRUG_GENE_RULES),
        "supported_feature_count": len(MODEL_FEATURE_COLUMNS),
    }


def planned_qc_steps() -> tuple[str, ...]:
    """Human-readable QC steps for PGx variant data intake."""
    return (
        "Validate file type and parseability",
        "Normalize genotype and coordinate fields",
        "Check curated pharmacogene locus coverage",
        "Separate evidence-based interpretation from any developer-only exploratory ML extension",
        "Restrict the ML layer to provenance-documented features and labeled data with realistic validation",
        "Generate a provenance-rich report with explicit limitations",
    )

# --- end merged module: src/data_pipeline.py ---

# --- begin merged module: src/core/patient_profile.py ---
"""Optional patient clinical profile schema for non-genetic Pharmexia context."""


PATIENT_PROFILE_SEX_VALUES = {"female", "male", "intersex", "other", "unknown"}


def _profile_string(value: Any) -> str | None:
    if value is None:
        return None
    text = str(value).strip()
    return text or None


def _profile_list(value: Any) -> list[str]:
    if value is None:
        return []
    if isinstance(value, (list, tuple, set)):
        candidates = value
    else:
        text = str(value).replace("\r", "\n")
        candidates = [item for chunk in text.split("\n") for item in chunk.split(",")]
    normalized = []
    for item in candidates:
        text = str(item).strip()
        if text and text not in normalized:
            normalized.append(text)
    return normalized

# --- end merged module: src/core/patient_profile.py ---

# --- begin merged module: src/services/patient_context_service.py ---
"""Validation and normalization for optional patient clinical profile context."""


import re


class PatientContextService:
    """Normalize optional patient clinical context without mixing it into genetic evidence."""

    def _coerce_profile(
        self,
        payload: "PatientClinicalProfile | dict[str, Any] | None",
    ) -> "PatientClinicalProfile":
        if isinstance(payload, PatientClinicalProfile):
            # Return a shallow copy without the expensive asdict() round-trip.
            return PatientClinicalProfile(
                age=payload.age,
                sex=payload.sex,
                diagnosis=payload.diagnosis,
                liver_function=payload.liver_function,
                kidney_function=payload.kidney_function,
                current_medications=list(payload.current_medications),
                allergies=list(payload.allergies),
                dose=payload.dose,
            )
        if isinstance(payload, dict):
            return PatientClinicalProfile(
                age=payload.get("age"),
                sex=payload.get("sex"),
                diagnosis=payload.get("diagnosis"),
                liver_function=payload.get("liver_function"),
                kidney_function=payload.get("kidney_function"),
                current_medications=_profile_list(payload.get("current_medications")),
                allergies=_profile_list(payload.get("allergies")),
                dose=_profile_string(payload.get("dose")),
            )
        return PatientClinicalProfile()

    def validate_profile(
        self,
        payload: PatientClinicalProfile | dict[str, Any] | None,
    ) -> tuple[PatientClinicalProfile | None, PatientProfileValidationResult]:
        if payload is None:
            return None, PatientProfileValidationResult(
                is_valid=True,
                status="not_provided",
                message="No patient clinical profile was provided.",
            )

        profile = self._coerce_profile(payload)
        warnings: list[str] = []

        normalized_age: int | None = None
        if profile.age not in (None, ""):
            try:
                normalized_age = int(profile.age)
                if normalized_age < 0 or normalized_age > 120:
                    warnings.append("Age was outside the supported range and was ignored.")
                    normalized_age = None
            except (TypeError, ValueError):
                warnings.append("Age was not a valid integer and was ignored.")

        normalized_sex = _profile_string(profile.sex)
        if normalized_sex:
            normalized_sex = normalized_sex.lower()
            if normalized_sex not in PATIENT_PROFILE_SEX_VALUES:
                warnings.append("Sex value was not recognized and was ignored.")
                normalized_sex = None

        normalized = PatientClinicalProfile(
            age=normalized_age,
            sex=normalized_sex,
            diagnosis=_profile_string(profile.diagnosis),
            liver_function=_profile_string(profile.liver_function),
            kidney_function=_profile_string(profile.kidney_function),
            current_medications=_profile_list(profile.current_medications),
            allergies=_profile_list(profile.allergies),
            dose=_profile_string(profile.dose),
        )
        used_fields = normalized.used_fields()
        model_feature_fields = list(self.model_feature_payload(normalized).keys())

        if not used_fields:
            return None, PatientProfileValidationResult(
                is_valid=False,
                status="invalid",
                message="A patient clinical profile was provided, but no fields passed validation. "
                        "The profile was discarded; analysis will proceed without clinical context.",
                warnings=warnings,
            )

        status = "warning" if warnings else "valid"
        message = (
            "Patient clinical profile validated with warnings."
            if warnings
            else "Patient clinical profile validated."
        )
        return normalized, PatientProfileValidationResult(
            is_valid=True,
            status=status,
            message=message,
            warnings=warnings,
            used_fields=used_fields,
            model_feature_fields=model_feature_fields,
        )

    def model_feature_payload(self, profile: PatientClinicalProfile | None) -> dict[str, float]:
        if profile is None:
            return {}
        features: dict[str, float] = {}
        if profile.age is not None:
            features["clinical_age"] = float(profile.age)
        dose = _profile_string(profile.dose)
        if dose:
            match = re.fullmatch(r"\s*([0-9]+(?:\.[0-9]+)?)\s*", dose)
            if match:
                features["clinical_dose"] = float(match.group(1))
        return features

    def summary_rows(
        self,
        profile: PatientClinicalProfile | None,
        validation: PatientProfileValidationResult | None,
    ) -> list[tuple[str, str]]:
        if profile is None or validation is None:
            return [
                ("Status", "Not provided"),
                ("Fields used", "None"),
                ("Model features", "None"),
            ]
        rows = [
            ("Status", validation.status),
            ("Validation", validation.message),
            ("Fields used", ", ".join(validation.used_fields) or "None"),
            ("Model features", ", ".join(validation.model_feature_fields) or "None"),
        ]
        if profile.age is not None:
            rows.append(("Age", str(profile.age)))
        if profile.sex:
            rows.append(("Sex", profile.sex))
        if profile.diagnosis:
            rows.append(("Diagnosis", profile.diagnosis))
        if profile.liver_function:
            rows.append(("Liver function", profile.liver_function))
        if profile.kidney_function:
            rows.append(("Kidney function", profile.kidney_function))
        if profile.current_medications:
            rows.append(("Current medications", ", ".join(profile.current_medications)))
        if profile.allergies:
            rows.append(("Allergies", ", ".join(profile.allergies)))
        if profile.dose:
            rows.append(("Dose", profile.dose))
        if validation.warnings:
            rows.append(("Warnings", " | ".join(validation.warnings)))
        return rows

# --- end merged module: src/services/patient_context_service.py ---

# --- begin merged module: src/features.py ---
"""Feature engineering and provenance for a developer-only exploratory ML extension."""


from collections import OrderedDict

import pandas as pd



METADATA_COLUMNS = ("drug", "sample_id", "row_id", "outcome_label")


def _coverage_fraction(assessment: GeneAssessment | None) -> float:
    if assessment is None or not assessment.expected_target_loci:
        return 0.0
    return round(len(assessment.observed_target_loci) / len(assessment.expected_target_loci), 4)


def _feature_catalog() -> "OrderedDict[str, FeatureProvenance]":
    catalog: "OrderedDict[str, FeatureProvenance]" = OrderedDict()
    for drug, rule in DRUG_GENE_RULES.items():
        catalog[f"drug_{drug}"] = FeatureProvenance(
            name=f"drug_{drug}",
            description=f"One-hot indicator for the selected drug context '{drug}'.",
            source_stage="input_selection",
            feature_group="drug_context",
            derived_from=["AnalysisPipelineRequest.selected_drugs"],
        )
        for gene in rule["genes"]:
            prefix = f"{drug}_{gene}"
            derived_from = [
                f"GeneAssessment[{gene}].matched_alleles",
                f"GeneAssessment[{gene}].coverage_complete",
                f"GeneAssessment[{gene}].observed_target_loci",
                f"GeneAssessment[{gene}].expected_target_loci",
                f"GeneAssessment[{gene}].ambiguous",
                f"GeneAssessment[{gene}].phenotype",
            ]
            catalog[f"{prefix}_matched"] = FeatureProvenance(
                name=f"{prefix}_matched",
                description=f"Binary indicator that at least one curated local allele match was observed for {gene} in the {drug} context.",
                source_stage="diplotype_phenotype",
                feature_group="gene_signal",
                derived_from=derived_from,
            )
            catalog[f"{prefix}_matched_count"] = FeatureProvenance(
                name=f"{prefix}_matched_count",
                description=f"Count of curated local allele matches observed for {gene} in the {drug} context.",
                source_stage="diplotype_phenotype",
                feature_group="gene_signal",
                derived_from=derived_from,
            )
            catalog[f"{prefix}_coverage_complete"] = FeatureProvenance(
                name=f"{prefix}_coverage_complete",
                description=f"Binary indicator that all locally curated loci for {gene} were present in the submitted data for the {drug} context.",
                source_stage="diplotype_phenotype",
                feature_group="coverage",
                derived_from=derived_from,
            )
            catalog[f"{prefix}_coverage_fraction"] = FeatureProvenance(
                name=f"{prefix}_coverage_fraction",
                description=f"Fraction of locally curated target loci observed for {gene} in the {drug} context.",
                source_stage="diplotype_phenotype",
                feature_group="coverage",
                derived_from=derived_from,
            )
            catalog[f"{prefix}_ambiguous"] = FeatureProvenance(
                name=f"{prefix}_ambiguous",
                description=f"Binary indicator that the local gene-level call for {gene} was ambiguous in the {drug} context.",
                source_stage="diplotype_phenotype",
                feature_group="call_quality",
                derived_from=derived_from,
            )
            catalog[f"{prefix}_phenotype_called"] = FeatureProvenance(
                name=f"{prefix}_phenotype_called",
                description=f"Binary indicator that a limited local phenotype label was available for {gene} in the {drug} context.",
                source_stage="diplotype_phenotype",
                feature_group="phenotype_support",
                derived_from=derived_from,
            )
    return catalog


FEATURE_CATALOG = _feature_catalog()
MODEL_FEATURE_COLUMNS = tuple(FEATURE_CATALOG.keys())


def get_feature_provenance(columns: list[str] | None = None) -> list[FeatureProvenance]:
    """Return provenance entries for the supported developer-only exploratory feature set."""
    selected = columns or list(MODEL_FEATURE_COLUMNS)
    return [FEATURE_CATALOG[name] for name in selected if name in FEATURE_CATALOG]


def build_pgx_feature_row(
    drug: str,
    gene_assessments: dict[str, GeneAssessment],
    *,
    sample_id: str | None = None,
    row_id: str | None = None,
) -> dict[str, float | int | str]:
    """Create a transparent numeric feature row for optional model-assisted inference."""
    row: dict[str, float | int | str] = {"drug": drug}
    if sample_id:
        row["sample_id"] = sample_id
    if row_id:
        row["row_id"] = row_id

    for feature_name in MODEL_FEATURE_COLUMNS:
        row[feature_name] = 0

    for rule_drug, rule in DRUG_GENE_RULES.items():
        active_context = int(rule_drug == drug)
        row[f"drug_{rule_drug}"] = active_context
        for gene in rule["genes"]:
            assessment = gene_assessments.get(gene)
            prefix = f"{rule_drug}_{gene}"
            if not active_context or assessment is None:
                continue
            matched_count = len(assessment.matched_alleles)
            row[f"{prefix}_matched"] = int(bool(matched_count))
            row[f"{prefix}_matched_count"] = matched_count
            row[f"{prefix}_coverage_complete"] = int(bool(assessment.coverage_complete))
            row[f"{prefix}_coverage_fraction"] = _coverage_fraction(assessment)
            row[f"{prefix}_ambiguous"] = int(bool(assessment.ambiguous))
            row[f"{prefix}_phenotype_called"] = int(bool(assessment.phenotype))
    return row


def build_feature_frame(rows: list[dict[str, float | int | str]]) -> pd.DataFrame:
    """Return a dataframe with the supported feature allowlist and metadata columns."""
    if not rows:
        return pd.DataFrame(columns=[*METADATA_COLUMNS, *MODEL_FEATURE_COLUMNS])

    frame = pd.DataFrame(rows)
    for metadata_column in METADATA_COLUMNS:
        if metadata_column not in frame.columns:
            frame[metadata_column] = None
    for feature_name in MODEL_FEATURE_COLUMNS:
        if feature_name not in frame.columns:
            frame[feature_name] = 0

    frame.loc[:, MODEL_FEATURE_COLUMNS] = (
        frame.loc[:, MODEL_FEATURE_COLUMNS].apply(pd.to_numeric, errors="coerce").fillna(0.0)
    )
    ordered_columns = (
        [column for column in METADATA_COLUMNS if column in frame.columns]
        + [
            column
            for column in frame.columns
            if column not in METADATA_COLUMNS and column not in MODEL_FEATURE_COLUMNS
        ]
        + list(MODEL_FEATURE_COLUMNS)
    )
    return frame.loc[:, ordered_columns]


def select_model_features(frame: pd.DataFrame) -> tuple[pd.DataFrame, list[str], list[str]]:
    """Select only the provenance-documented model features and report dropped columns."""
    if frame.empty:
        return pd.DataFrame(columns=MODEL_FEATURE_COLUMNS), list(MODEL_FEATURE_COLUMNS), []

    allowed = set(MODEL_FEATURE_COLUMNS).union(METADATA_COLUMNS)
    dropped_columns = [column for column in frame.columns if column not in allowed]
    feature_matrix = frame.loc[:, MODEL_FEATURE_COLUMNS].apply(pd.to_numeric, errors="coerce").fillna(0.0)
    return feature_matrix, list(MODEL_FEATURE_COLUMNS), dropped_columns

# --- end merged module: src/features.py ---

# --- begin merged module: src/interpret.py ---
"""Model-assistance interpretation helpers."""


import math
from typing import Any



def _normalized_entropy(probabilities: list[float]) -> float:
    if not probabilities or len(probabilities) == 1:
        return 0.0
    entropy = -sum(prob * math.log(prob) for prob in probabilities if prob > 0)
    max_entropy = math.log(len(probabilities))
    return round(entropy / max_entropy, 4) if max_entropy else 0.0


def classify_uncertainty(
    top_probability: float,
    normalized_entropy: float,
    top_margin: float,
) -> str:
    """Convert model probability spread into a conservative uncertainty label."""
    if top_probability < 0.55 or normalized_entropy > 0.75 or top_margin < 0.15:
        return "high"
    if top_probability < 0.75 or normalized_entropy > 0.4 or top_margin < 0.3:
        return "medium"
    return "low"


def summarize_model_support(
    predicted_label: str,
    label_probabilities: dict[str, float],
    feature_provenance: list[FeatureProvenance],
    active_feature_names: list[str],
) -> dict[str, Any]:
    """Create a compact explanation for an exploratory ML prediction."""
    probabilities = sorted(label_probabilities.values(), reverse=True)
    top_probability = probabilities[0] if probabilities else 0.0
    runner_up = probabilities[1] if len(probabilities) > 1 else 0.0
    normalized_entropy = _normalized_entropy(list(label_probabilities.values()))
    uncertainty_level = classify_uncertainty(top_probability, normalized_entropy, top_probability - runner_up)
    active_provenance = [
        provenance.to_dict()
        for provenance in feature_provenance
        if provenance.name in active_feature_names
    ]
    return {
        "predicted_label": predicted_label,
        "label_probabilities": {label: round(float(probability), 4) for label, probability in label_probabilities.items()},
        "calibrated_probability_estimate": round(float(top_probability), 4),
        "uncertainty_level": uncertainty_level,
        "normalized_entropy": normalized_entropy,
        "top_features": active_feature_names[:5],
        "feature_provenance": active_provenance,
        "summary": (
            "Exploratory model assistance is shown only because no authoritative local guideline "
            "finding was generated for this input. Calibrated model probabilities are diagnostic model outputs, "
            "not clinical confidence estimates."
        ),
    }

# --- end merged module: src/interpret.py ---

# --- begin merged module: src/ml/metrics.py ---
"""Reusable validation metrics for exploratory Pharmexia ML workflows."""


from collections import Counter

try:
    import numpy as np
    import pandas as _pd_metrics
    from sklearn.metrics import (
        accuracy_score,
        average_precision_score,
        balanced_accuracy_score,
        confusion_matrix,
        f1_score,
        log_loss,
        roc_auc_score,
    )
    _SKLEARN_METRICS_AVAILABLE = True
except ImportError:
    np = None  # type: ignore[assignment]
    _pd_metrics = None  # type: ignore[assignment]
    _SKLEARN_METRICS_AVAILABLE = False


def _as_probability_frame(
    probabilities: pd.DataFrame | np.ndarray | list[list[float]],
    classes: list[str],
    *,
    index: pd.Index | None = None,
) -> pd.DataFrame:
    if isinstance(probabilities, pd.DataFrame):
        frame = probabilities.copy()
        frame.columns = [str(column) for column in frame.columns]
        return frame
    frame = pd.DataFrame(probabilities, columns=[str(label) for label in classes], index=index)
    return frame


def multiclass_brier_score(y_true: pd.Series, probabilities: pd.DataFrame) -> float:
    """Return a conservative multiclass Brier score for calibrated probabilities."""
    classes = [str(label) for label in probabilities.columns]
    truth = pd.get_dummies(y_true.astype(str)).reindex(columns=classes, fill_value=0).astype(float)
    return float(((truth.values - probabilities.values) ** 2).sum(axis=1).mean())


def compute_roc_auc_metric(y_true: pd.Series, probabilities: pd.DataFrame) -> float | None:
    """Compute binary or macro one-vs-rest ROC-AUC when possible."""
    if probabilities.empty or y_true.nunique() < 2:
        return None
    try:
        if probabilities.shape[1] == 2:
            positive_label = str(probabilities.columns[-1])
            truth = (y_true.astype(str) == positive_label).astype(int)
            return round(float(roc_auc_score(truth, probabilities[positive_label])), 6)
        truth = pd.get_dummies(y_true.astype(str)).reindex(columns=probabilities.columns, fill_value=0)
        return round(
            float(roc_auc_score(truth.values, probabilities.values, multi_class="ovr", average="macro")),
            6,
        )
    except ValueError:
        return None


def compute_pr_auc_metric(y_true: pd.Series, probabilities: pd.DataFrame) -> float | None:
    """Compute binary or macro average-precision PR-AUC when possible."""
    if probabilities.empty or y_true.nunique() < 2:
        return None
    try:
        if probabilities.shape[1] == 2:
            positive_label = str(probabilities.columns[-1])
            truth = (y_true.astype(str) == positive_label).astype(int)
            return round(float(average_precision_score(truth, probabilities[positive_label])), 6)
        truth = pd.get_dummies(y_true.astype(str)).reindex(columns=probabilities.columns, fill_value=0)
        return round(float(average_precision_score(truth.values, probabilities.values, average="macro")), 6)
    except ValueError:
        return None


def compute_expected_calibration_error(
    probabilities: pd.DataFrame,
    y_true: pd.Series,
    *,
    n_bins: int = 10,
) -> float:
    """Compute top-label expected calibration error."""
    if probabilities.empty:
        return 0.0
    top_probability = probabilities.max(axis=1)
    predicted_label = probabilities.idxmax(axis=1)
    correctness = (predicted_label == y_true.astype(str)).astype(float)
    bins = pd.cut(top_probability, bins=n_bins, labels=False, include_lowest=True)

    ece = 0.0
    for bin_index in range(n_bins):
        mask = bins == bin_index
        if not mask.any():
            continue
        accuracy = float(correctness[mask].mean())
        confidence = float(top_probability[mask].mean())
        weight = float(mask.mean())
        ece += abs(accuracy - confidence) * weight
    return round(float(ece), 6)


def build_calibration_curve_points(
    probabilities: pd.Series,
    truth: pd.Series,
    *,
    split_name: str,
    curve_label: str,
    curve_type: str,
    n_bins: int = 10,
) -> list[dict[str, Any]]:
    """Build CSV-ready calibration curve points for plotting or downstream review."""
    if probabilities.empty:
        return []

    bin_edges = np.linspace(0.0, 1.0, n_bins + 1)
    bin_ids = pd.cut(
        probabilities.astype(float),
        bins=bin_edges,
        labels=False,
        include_lowest=True,
    )
    points: list[dict[str, Any]] = []
    for bin_index in range(n_bins):
        mask = bin_ids == bin_index
        if not mask.any():
            continue
        points.append(
            {
                "split": split_name,
                "curve_label": curve_label,
                "curve_type": curve_type,
                "bin_index": int(bin_index),
                "bin_lower": round(float(bin_edges[bin_index]), 6),
                "bin_upper": round(float(bin_edges[bin_index + 1]), 6),
                "mean_predicted_probability": round(float(probabilities[mask].mean()), 6),
                "observed_frequency": round(float(truth[mask].mean()), 6),
                "sample_count": int(mask.sum()),
            }
        )
    return points


def compute_calibration_summary(
    probabilities: pd.DataFrame,
    y_true: pd.Series,
    *,
    split_name: str,
    n_bins: int = 10,
) -> dict[str, Any]:
    """Return calibration metrics plus CSV-ready curve points for a split."""
    if probabilities.empty:
        return {
            "split": split_name,
            "expected_calibration_error": None,
            "brier_score": None,
            "curve_count": 0,
            "curves": [],
            "curve_note": "No probabilities were available for calibration analysis.",
        }

    y_text = y_true.astype(str)
    top_probability = probabilities.max(axis=1)
    predicted_label = probabilities.idxmax(axis=1)
    top_label_truth = (predicted_label == y_text).astype(int)
    curves = build_calibration_curve_points(
        top_probability,
        top_label_truth,
        split_name=split_name,
        curve_label="top_label",
        curve_type="top_prediction",
        n_bins=n_bins,
    )

    curve_note = "Top-label calibration curve included."
    if probabilities.shape[1] == 2:
        positive_label = str(probabilities.columns[-1])
        curves.extend(
            build_calibration_curve_points(
                probabilities[positive_label],
                (y_text == positive_label).astype(int),
                split_name=split_name,
                curve_label=positive_label,
                curve_type="positive_class",
                n_bins=n_bins,
            )
        )
    elif probabilities.shape[1] <= 5:
        for label in probabilities.columns:
            curves.extend(
                build_calibration_curve_points(
                    probabilities[str(label)],
                    (y_text == str(label)).astype(int),
                    split_name=split_name,
                    curve_label=str(label),
                    curve_type="one_vs_rest",
                    n_bins=n_bins,
                )
            )
    else:
        curve_note = (
            "Only top-label calibration is included because the label space exceeds five classes."
        )

    return {
        "split": split_name,
        "expected_calibration_error": compute_expected_calibration_error(probabilities, y_text, n_bins=n_bins),
        "brier_score": round(multiclass_brier_score(y_text, probabilities), 6),
        "curve_count": len(curves),
        "curves": curves,
        "curve_note": curve_note,
    }


def compute_confusion_matrix_summary(
    y_true: pd.Series,
    predicted_labels: pd.Series,
    *,
    labels: list[str],
) -> dict[str, Any]:
    """Return structured confusion-matrix counts plus normalized rates."""
    counts = confusion_matrix(y_true.astype(str), predicted_labels.astype(str), labels=labels)
    normalized = confusion_matrix(
        y_true.astype(str),
        predicted_labels.astype(str),
        labels=labels,
        normalize="true",
    )
    support = Counter(y_true.astype(str))
    return {
        "labels": list(labels),
        "counts": counts.astype(int).tolist(),
        "row_normalized": [[round(float(value), 6) for value in row] for row in normalized],
        "support": {label: int(support.get(label, 0)) for label in labels},
    }


def evaluate_prediction_metrics(
    y_true: pd.Series,
    predicted_labels: pd.Series,
    probabilities: pd.DataFrame,
    *,
    split_name: str,
    n_bins: int = 10,
) -> dict[str, Any]:
    """Compute a conservative, serializable metrics bundle for one partition."""
    labels = [str(label) for label in probabilities.columns]
    metrics: dict[str, float | None] = {
        "accuracy": round(float(accuracy_score(y_true, predicted_labels)), 6),
        "balanced_accuracy": round(float(balanced_accuracy_score(y_true, predicted_labels)), 6),
        "f1_macro": round(float(f1_score(y_true, predicted_labels, average="macro")), 6),
        "roc_auc": compute_roc_auc_metric(y_true, probabilities),
        "pr_auc": compute_pr_auc_metric(y_true, probabilities),
        "log_loss": None,
    }
    try:
        metrics["log_loss"] = round(float(log_loss(y_true, probabilities.values, labels=labels)), 6)
    except ValueError:
        metrics["log_loss"] = None

    return {
        "split": split_name,
        "n_rows": int(len(y_true)),
        "metrics": metrics,
        "confusion_matrix": compute_confusion_matrix_summary(
            y_true,
            predicted_labels,
            labels=labels,
        ),
        "calibration": compute_calibration_summary(
            probabilities,
            y_true,
            split_name=split_name,
            n_bins=n_bins,
        ),
    }

# --- end merged module: src/ml/metrics.py ---

# --- begin merged module: src/ml/validation.py ---
"""Reusable train/validation/test validation flows for exploratory models."""


from dataclasses import asdict, dataclass

try:
    from sklearn.base import clone
    from sklearn.model_selection import StratifiedKFold, cross_validate, train_test_split
    _SKLEARN_VALIDATION_AVAILABLE = True
except ImportError:
    _SKLEARN_VALIDATION_AVAILABLE = False


@dataclass(slots=True)
class ValidationConfig:
    """Serializable configuration for honest exploratory validation."""

    test_size: float = 0.2
    validation_size: float = 0.2
    random_state: int = 42
    calibration_bins: int = 10
    max_cv_splits: int = 5

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


def _validation_utc_now() -> str:
    return datetime.now(timezone.utc).isoformat()


def safe_cv_splits(min_class_count: int, *, max_splits: int = 5) -> int:
    return max(2, min(max_splits, min_class_count))


def safe_calibration_cv(min_class_count: int, outer_cv_splits: int) -> int:
    outer_train_min = max(2, min_class_count - math.ceil(min_class_count / max(outer_cv_splits, 1)))
    return max(2, min(3, outer_train_min))


def _normalize_metadata_frame(metadata: pd.DataFrame | None, X: pd.DataFrame) -> pd.DataFrame:
    if metadata is None or metadata.empty:
        return pd.DataFrame(index=X.index)
    return metadata.copy()


def _identifier_set(frame: pd.DataFrame, column: str) -> set[str]:
    if column not in frame.columns:
        return set()
    return {
        str(value).strip()
        for value in frame[column]
        if pd.notna(value) and str(value).strip()
    }


def _split_overlap(a: pd.DataFrame, b: pd.DataFrame, column: str) -> list[str]:
    overlap = sorted(_identifier_set(a, column).intersection(_identifier_set(b, column)))
    return overlap[:10]


def _pairwise_split_overlap(parts: dict[str, pd.DataFrame], column: str) -> dict[str, list[str]]:
    keys = list(parts)
    overlaps: dict[str, list[str]] = {}
    for index, left in enumerate(keys):
        for right in keys[index + 1 :]:
            shared = _split_overlap(parts[left], parts[right], column)
            if shared:
                overlaps[f"{left}__{right}"] = shared
    return overlaps


def stratified_train_validation_test_split(
    X: pd.DataFrame,
    y: pd.Series,
    metadata: pd.DataFrame | None = None,
    *,
    config: ValidationConfig | None = None,
) -> dict[str, Any]:
    """Split data into train, validation, and test partitions without fitting on held-out data."""
    cfg = config or ValidationConfig()
    if not 0 < cfg.test_size < 1:
        raise ValueError("test_size must be between 0 and 1.")
    if not 0 < cfg.validation_size < 1:
        raise ValueError("validation_size must be between 0 and 1.")
    if cfg.test_size + cfg.validation_size >= 1:
        raise ValueError("test_size + validation_size must be less than 1.")

    meta = _normalize_metadata_frame(metadata, X)
    split_inputs = [
        X,
        y.astype(str),
        meta,
    ]
    X_train_validation, X_test, y_train_validation, y_test, meta_train_validation, meta_test = train_test_split(
        *split_inputs,
        test_size=cfg.test_size,
        random_state=cfg.random_state,
        stratify=y.astype(str),
    )

    relative_validation_size = cfg.validation_size / (1.0 - cfg.test_size)
    (
        X_train,
        X_validation,
        y_train,
        y_validation,
        meta_train,
        meta_validation,
    ) = train_test_split(
        X_train_validation,
        y_train_validation,
        meta_train_validation,
        test_size=relative_validation_size,
        random_state=cfg.random_state,
        stratify=y_train_validation.astype(str),
    )

    metadata_parts = {
        "train": meta_train,
        "validation": meta_validation,
        "test": meta_test,
    }
    sample_id_overlaps = _pairwise_split_overlap(metadata_parts, "sample_id")
    row_id_overlaps = _pairwise_split_overlap(metadata_parts, "row_id")
    leakage_issues: list[str] = []
    if sample_id_overlaps:
        leakage_issues.append(
            "sample_id values overlap across partitions; this indicates potential leakage and the model was not validated."
        )
    if row_id_overlaps:
        leakage_issues.append(
            "row_id values overlap across partitions; this indicates potential leakage and the model was not validated."
        )

    partitions = {
        "train": {"X": X_train, "y": y_train, "metadata": meta_train},
        "validation": {"X": X_validation, "y": y_validation, "metadata": meta_validation},
        "test": {"X": X_test, "y": y_test, "metadata": meta_test},
    }

    partition_summaries = {
        name: {
            "n_rows": int(len(partition["y"])),
            "class_counts": {str(label): int(count) for label, count in partition["y"].value_counts().sort_index().items()},
        }
        for name, partition in partitions.items()
    }

    return {
        "status": "failed" if leakage_issues else "ready",
        "config": cfg.to_dict(),
        "partitions": partitions,
        "partition_summaries": partition_summaries,
        "leakage_audit": {
            "status": "failed" if leakage_issues else "passed",
            "issues": leakage_issues,
            "sample_id_overlap_examples": sample_id_overlaps,
            "row_id_overlap_examples": row_id_overlaps,
            "split_strategy": "stratified_train_validation_test",
        },
    }


def _roc_auc_cv_scorer(estimator: Any, X_part: pd.DataFrame, y_part: pd.Series) -> float:
    probabilities = _as_probability_frame(
        estimator.predict_proba(X_part),
        [str(label) for label in estimator.classes_],
        index=X_part.index,
    )
    value = compute_roc_auc_metric(y_part.astype(str), probabilities)
    return float("nan") if value is None else float(value)


def _pr_auc_cv_scorer(estimator: Any, X_part: pd.DataFrame, y_part: pd.Series) -> float:
    probabilities = _as_probability_frame(
        estimator.predict_proba(X_part),
        [str(label) for label in estimator.classes_],
        index=X_part.index,
    )
    value = compute_pr_auc_metric(y_part.astype(str), probabilities)
    return float("nan") if value is None else float(value)


def summarize_cross_validation(
    estimator: Any,
    X_train: pd.DataFrame,
    y_train: pd.Series,
    *,
    cv_splits: int,
) -> dict[str, Any]:
    """Summarize cross-validation metrics on the training partition only."""
    scoring = {
        "accuracy": "accuracy",
        "balanced_accuracy": "balanced_accuracy",
        "f1_macro": "f1_macro",
        "roc_auc": _roc_auc_cv_scorer,
        "pr_auc": _pr_auc_cv_scorer,
        "neg_log_loss": "neg_log_loss",
    }
    outer_cv = StratifiedKFold(n_splits=cv_splits, shuffle=True, random_state=42)
    results = cross_validate(
        estimator,
        X_train,
        y_train.astype(str),
        cv=outer_cv,
        scoring=scoring,
        n_jobs=None,
        error_score="raise",
    )

    summary: dict[str, Any] = {"n_splits": cv_splits}
    csv_rows: list[dict[str, Any]] = []
    for metric_name, values in results.items():
        if not metric_name.startswith("test_"):
            continue
        clean_name = metric_name[5:]
        series = pd.Series(values, dtype="float64")
        if clean_name == "neg_log_loss":
            series = -series
            clean_name = "log_loss"
        mean_value = round(float(series.mean()), 6)
        std_value = round(float(series.std(ddof=0)), 6)
        summary[clean_name] = {"mean": mean_value, "std": std_value}
        csv_rows.append(
            {
                "metric": clean_name,
                "mean": mean_value,
                "std": std_value,
                "n_splits": int(cv_splits),
            }
        )
    return {"summary": summary, "csv_rows": csv_rows}


def _prediction_records(
    *,
    split_name: str,
    y_true: pd.Series,
    predicted_labels: pd.Series,
    probabilities: pd.DataFrame,
    metadata: pd.DataFrame,
) -> list[dict[str, Any]]:
    records: list[dict[str, Any]] = []
    for index in probabilities.index:
        row = {
            "split": split_name,
            "index": int(index) if isinstance(index, (int, np.integer)) else str(index),
            "sample_id": metadata.at[index, "sample_id"] if "sample_id" in metadata.columns and index in metadata.index else None,
            "row_id": metadata.at[index, "row_id"] if "row_id" in metadata.columns and index in metadata.index else None,
            "true_label": str(y_true.loc[index]),
            "predicted_label": str(predicted_labels.loc[index]),
            "top_probability": round(float(probabilities.loc[index].max()), 6),
        }
        for label, value in probabilities.loc[index].items():
            row[f"probability_{label}"] = round(float(value), 6)
        records.append(row)
    return records


def fit_and_validate_classifier(
    estimator: Any,
    X: pd.DataFrame,
    y: pd.Series,
    *,
    metadata: pd.DataFrame | None = None,
    config: ValidationConfig | None = None,
    model_name: str = "exploratory_classifier",
) -> dict[str, Any]:
    """Fit on the training partition and return an honest validation report."""
    cfg = config or ValidationConfig()
    split_bundle = stratified_train_validation_test_split(X, y, metadata, config=cfg)
    if split_bundle["status"] != "ready":
        return {
            "status": "unavailable",
            "reason": "Validation halted because the proposed partitions were not leakage-safe.",
            "report": {
                "schema_version": "1.0",
                "status": "failed",
                "generated_at_utc": _validation_utc_now(),
                "model_name": model_name,
                "split_config": cfg.to_dict(),
                "data_leakage_audit": split_bundle["leakage_audit"],
            },
            "artifacts": {},
        }

    partitions = split_bundle["partitions"]
    X_train = partitions["train"]["X"]
    y_train = partitions["train"]["y"].astype(str)
    train_label_distribution = summarize_label_distribution(y_train)
    cv_splits = safe_cv_splits(int(train_label_distribution["min_class_count"]), max_splits=cfg.max_cv_splits)

    cross_validation = summarize_cross_validation(clone(estimator), X_train, y_train, cv_splits=cv_splits)
    fitted_model = clone(estimator)
    fitted_model.fit(X_train, y_train)

    partition_metrics: dict[str, Any] = {}
    prediction_rows: list[dict[str, Any]] = []
    calibration_rows: list[dict[str, Any]] = []
    confusion_csv_rows: list[dict[str, Any]] = []

    for split_name in ("validation", "test"):
        X_part = partitions[split_name]["X"]
        y_part = partitions[split_name]["y"].astype(str)
        metadata_part = partitions[split_name]["metadata"]
        probabilities = _as_probability_frame(
            fitted_model.predict_proba(X_part),
            [str(label) for label in fitted_model.classes_],
            index=X_part.index,
        )
        predicted_labels = pd.Series(
            fitted_model.predict(X_part),
            index=X_part.index,
            dtype="object",
        ).astype(str)
        evaluation = evaluate_prediction_metrics(
            y_part,
            predicted_labels,
            probabilities,
            split_name=split_name,
            n_bins=cfg.calibration_bins,
        )
        partition_metrics[split_name] = evaluation
        prediction_rows.extend(
            _prediction_records(
                split_name=split_name,
                y_true=y_part,
                predicted_labels=predicted_labels,
                probabilities=probabilities,
                metadata=metadata_part,
            )
        )
        calibration_rows.extend(evaluation["calibration"].get("curves", []))
        labels = evaluation["confusion_matrix"]["labels"]
        for row_index, actual_label in enumerate(labels):
            for column_index, predicted_label in enumerate(labels):
                confusion_csv_rows.append(
                    {
                        "split": split_name,
                        "actual_label": actual_label,
                        "predicted_label": predicted_label,
                        "count": evaluation["confusion_matrix"]["counts"][row_index][column_index],
                        "row_normalized": evaluation["confusion_matrix"]["row_normalized"][row_index][column_index],
                    }
                )

    report = {
        "schema_version": "1.0",
        "status": "ready",
        "generated_at_utc": _validation_utc_now(),
        "model_name": model_name,
        "task_type": "classification",
        "split_config": cfg.to_dict(),
        "split_strategy": {
            "train_validation_test_split": "stratified",
            "cross_validation": "training-partition-only stratified k-fold",
        },
        "data_leakage_audit": {
            **split_bundle["leakage_audit"],
            "feature_selection_fit_on_training_only": True,
            "cross_validation_partition": "train",
            "held_out_partitions": ["validation", "test"],
        },
        "label_distribution": {
            "overall": summarize_label_distribution(y.astype(str)),
            "train": summarize_label_distribution(partitions["train"]["y"].astype(str)),
            "validation": summarize_label_distribution(partitions["validation"]["y"].astype(str)),
            "test": summarize_label_distribution(partitions["test"]["y"].astype(str)),
        },
        "partitions": split_bundle["partition_summaries"],
        "metrics": {
            "cross_validation": cross_validation["summary"],
            "validation": partition_metrics["validation"]["metrics"],
            "test": partition_metrics["test"]["metrics"],
        },
        "confusion_matrices": {
            "validation": partition_metrics["validation"]["confusion_matrix"],
            "test": partition_metrics["test"]["confusion_matrix"],
        },
        "calibration": {
            "validation": {
                key: value
                for key, value in partition_metrics["validation"]["calibration"].items()
                if key != "curves"
            },
            "test": {
                key: value
                for key, value in partition_metrics["test"]["calibration"].items()
                if key != "curves"
            },
        },
    }
    return {
        "status": "ready",
        "model": fitted_model,
        "report": report,
        "artifacts": {},
        "csv_payloads": {
            "cross_validation": cross_validation["csv_rows"],
            "confusion_matrix": confusion_csv_rows,
            "calibration_curves": calibration_rows,
            "predictions": prediction_rows,
        },
    }


def save_validation_report(
    report: dict[str, Any],
    *,
    output_stem: Path,
    csv_payloads: dict[str, list[dict[str, Any]]] | None = None,
) -> dict[str, str]:
    """Persist JSON and CSV validation artifacts for honest downstream reporting."""
    output_stem.parent.mkdir(parents=True, exist_ok=True)
    json_path = Path(f"{output_stem}.json")
    json_path.write_text(json.dumps(report, indent=2), encoding="utf-8")

    artifacts = {"json_report": str(json_path)}
    payloads = csv_payloads or {}
    for key, rows in payloads.items():
        csv_path = Path(f"{output_stem}.{key}.csv")
        pd.DataFrame(rows).to_csv(csv_path, index=False)
        artifacts[key] = str(csv_path)
    return artifacts

# --- end merged module: src/ml/validation.py ---

# --- begin merged module: src/services/validation_service.py ---
"""Service facade for reusable exploratory model validation."""


class ValidationService:
    """Run honest ML validation and persist reports without changing model semantics."""

    def __init__(self, config: ValidationConfig | None = None) -> None:
        self.config = config or ValidationConfig()

    def validate_classifier(
        self,
        estimator: Any,
        X: pd.DataFrame,
        y: pd.Series,
        *,
        metadata: pd.DataFrame | None = None,
        model_name: str = "exploratory_classifier",
        output_stem: Path | None = None,
    ) -> dict[str, Any]:
        payload = fit_and_validate_classifier(
            estimator,
            X,
            y,
            metadata=metadata,
            config=self.config,
            model_name=model_name,
        )
        if payload.get("status") == "ready" and output_stem is not None:
            payload["artifacts"] = save_validation_report(
                payload["report"],
                output_stem=output_stem,
                csv_payloads=payload.get("csv_payloads", {}),
            )
        return payload

# --- end merged module: src/services/validation_service.py ---

# --- begin merged module: src/ml_pipeline.py ---
"""Developer-only, strictly secondary exploratory ML workflows."""


import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

try:
    import joblib
    import pandas as pd
    from sklearn.calibration import CalibratedClassifierCV
    from sklearn.linear_model import LogisticRegression
    from sklearn.metrics import accuracy_score, balanced_accuracy_score, f1_score, log_loss, roc_auc_score
    from sklearn.model_selection import StratifiedKFold, cross_validate, train_test_split
    from sklearn.pipeline import Pipeline
    _SKLEARN_ML_PIPELINE_AVAILABLE = True
except ImportError:
    joblib = None  # type: ignore[assignment]
    _SKLEARN_ML_PIPELINE_AVAILABLE = False



def _utc_now() -> str:
    return datetime.now(timezone.utc).isoformat()


def _safe_cv_splits(min_class_count: int) -> int:
    return max(2, min(5, min_class_count))


def _safe_calibration_cv(min_class_count: int, outer_cv_splits: int) -> int:
    outer_train_min = max(2, min_class_count - math.ceil(min_class_count / max(outer_cv_splits, 1)))
    return max(2, min(3, outer_train_min))


def _class_weight_strategy(label_distribution: dict[str, object]) -> str | None:
    imbalance_ratio = label_distribution.get("imbalance_ratio")
    if imbalance_ratio is None:
        return None
    return "balanced" if float(imbalance_ratio) >= 1.5 else None


def _build_estimator(class_weight: str | None) -> Pipeline:
    logistic = LogisticRegression(
        max_iter=2000,
        class_weight=class_weight,
        solver="lbfgs",
    )
    return Pipeline([("logistic_regression", logistic)])


def _calibration_method(train_rows: int) -> str:
    return "sigmoid" if train_rows < 200 else "isotonic"


def _multiclass_brier_score(y_true: pd.Series, probabilities: pd.DataFrame) -> float:
    classes = list(probabilities.columns)
    truth = pd.get_dummies(y_true).reindex(columns=classes, fill_value=0).astype(float)
    return float(((truth.values - probabilities.values) ** 2).sum(axis=1).mean())


def _expected_calibration_error(probabilities: pd.DataFrame, y_true: pd.Series, n_bins: int = 10) -> float:
    top_probability = probabilities.max(axis=1)
    predicted_label = probabilities.idxmax(axis=1)
    correctness = (predicted_label == y_true).astype(float)
    bins = pd.cut(top_probability, bins=n_bins, labels=False, include_lowest=True)

    ece = 0.0
    for bin_index in range(n_bins):
        mask = bins == bin_index
        if not mask.any():
            continue
        accuracy = float(correctness[mask].mean())
        confidence = float(top_probability[mask].mean())
        weight = float(mask.mean())
        ece += abs(accuracy - confidence) * weight
    return round(float(ece), 6)


def _cross_validation_summary(
    estimator: CalibratedClassifierCV,
    X_train: pd.DataFrame,
    y_train: pd.Series,
    *,
    cv_splits: int,
) -> dict[str, Any]:
    outer_cv = StratifiedKFold(n_splits=cv_splits, shuffle=True, random_state=42)
    if y_train.nunique() == 2:
        scoring = {
            "accuracy": "accuracy",
            "balanced_accuracy": "balanced_accuracy",
            "f1_macro": "f1_macro",
            "roc_auc": "roc_auc",
            "neg_log_loss": "neg_log_loss",
        }
    else:
        scoring = {
            "accuracy": "accuracy",
            "balanced_accuracy": "balanced_accuracy",
            "f1_macro": "f1_macro",
            "roc_auc_ovr": "roc_auc_ovr",
            "neg_log_loss": "neg_log_loss",
        }

    results = cross_validate(
        estimator,
        X_train,
        y_train,
        cv=outer_cv,
        scoring=scoring,
        n_jobs=None,
        error_score="raise",
    )

    summary: dict[str, Any] = {"n_splits": cv_splits}
    for metric_name, values in results.items():
        if not metric_name.startswith("test_"):
            continue
        clean_name = metric_name[5:]
        series = pd.Series(values, dtype="float64")
        if clean_name == "neg_log_loss":
            series = -series
            clean_name = "log_loss"
        summary[clean_name] = {
            "mean": round(float(series.mean()), 6),
            "std": round(float(series.std(ddof=0)), 6),
        }
    return summary


def _holdout_metrics(
    model: CalibratedClassifierCV,
    X_test: pd.DataFrame,
    y_test: pd.Series,
) -> tuple[dict[str, float | None], dict[str, Any]]:
    predicted_labels = model.predict(X_test)
    probabilities = pd.DataFrame(
        model.predict_proba(X_test),
        columns=[str(label) for label in model.classes_],
        index=X_test.index,
    )
    metrics: dict[str, float | None] = {
        "accuracy": round(float(accuracy_score(y_test, predicted_labels)), 6),
        "balanced_accuracy": round(float(balanced_accuracy_score(y_test, predicted_labels)), 6),
        "f1_macro": round(float(f1_score(y_test, predicted_labels, average="macro")), 6),
        "log_loss": round(float(log_loss(y_test, probabilities.values, labels=list(model.classes_))), 6),
        "roc_auc": None,
    }
    if y_test.nunique() == 2:
        positive_label = probabilities.columns[-1]
        try:
            metrics["roc_auc"] = round(float(roc_auc_score(y_test, probabilities[positive_label])), 6)
        except ValueError:
            metrics["roc_auc"] = None
    else:
        try:
            metrics["roc_auc"] = round(
                float(roc_auc_score(y_test, probabilities.values, multi_class="ovr", average="macro")),
                6,
            )
        except ValueError:
            metrics["roc_auc"] = None

    calibration_summary = {
        "method": getattr(model, "method", "sigmoid"),
        "expected_calibration_error": _expected_calibration_error(probabilities, y_test),
        "brier_score": round(_multiclass_brier_score(y_test, probabilities), 6),
        "holdout_log_loss": metrics["log_loss"],
    }
    return metrics, calibration_summary


def _model_card(
    *,
    label_distribution: dict[str, object],
    feature_count: int,
    class_weight: str | None,
    calibration_method: str,
    cv_splits: int,
) -> dict[str, Any]:
    return {
        "name": "Pharmexia exploratory PGx logistic model",
        "version": "2.0",
        "trained_at_utc": _utc_now(),
        "algorithm": "LogisticRegression + CalibratedClassifierCV",
        "intended_use": (
            "Exploratory secondary prediction only when labeled PGx training data exist and no evidence-based local rule "
            "has already produced a confirmed pharmacogenomics finding."
        ),
        "not_for_clinical_use": True,
        "out_of_scope": [
            "Replacing CPIC, PharmGKB, or other authoritative evidence-based interpretation",
            "Issuing therapy recommendations, phenotype calls, or functional claims without validated evidence",
            "Serving as a standalone clinical decision tool",
        ],
        "training_methodology": {
            "train_test_split": "stratified holdout",
            "cross_validation": f"{cv_splits}-fold stratified cross-validation on the training partition",
            "calibration": calibration_method,
            "class_weight": class_weight or "none",
        },
        "label_space": list(label_distribution.get("counts", {}).keys()),
        "feature_count": feature_count,
        "ui_display_requirements": [
            "Always label outputs as MODEL_ASSISTED and exploratory",
            "Never present calibrated model probabilities as clinical confidence",
            "Never display model outputs in the same visual priority as evidence-based PGx findings",
            "Suppress model output completely when authoritative PGx evidence already produced a confirmed finding",
        ],
    }


def _training_dataset_summary(
    frame: pd.DataFrame,
    X_train: pd.DataFrame,
    X_test: pd.DataFrame,
    *,
    dropped_columns: list[str],
    validation: dict[str, Any],
) -> dict[str, Any]:
    drug_distribution = frame["drug"].value_counts().sort_index() if "drug" in frame.columns else pd.Series(dtype=int)
    return {
        "rows_total": int(len(frame)),
        "rows_train": int(len(X_train)),
        "rows_test": int(len(X_test)),
        "drug_distribution": {str(label): int(count) for label, count in drug_distribution.items()},
        "duplicate_row_count": int(validation.get("duplicate_row_count", 0)),
        "dropped_non_feature_columns": dropped_columns,
        "suspicious_columns": list(validation.get("suspicious_columns", [])),
    }


def train_exploratory_model(
    feature_rows: list[dict[str, float | int | str]],
    labels: list[str],
    output_path: Path,
) -> dict[str, Any]:
    """Train a developer-only exploratory logistic-regression model when valid labels exist."""
    # Inline stubs for monitoring helpers (formerly src.ml.model_monitoring).
    def build_monitoring_profile_from_training_frame(frame, *, input_modalities, feature_groups, dataset_version):
        return {"status": "unavailable", "note": "Monitoring profile not available in single-file build."}

    def dataset_version_from_frame(frame):
        import hashlib
        h = hashlib.md5(str(len(frame)).encode()).hexdigest()[:8]
        return f"frame_{h}"

    frame = build_feature_frame(feature_rows)
    frame["outcome_label"] = labels
    dataset_version = dataset_version_from_frame(frame)
    validation = validate_training_dataset(frame)
    if validation["status"] != "ok":
        return {
            "status": "unavailable",
            "reason": "Validated labeled PGx training data were insufficient; rule-based interpretation remains primary.",
            "model_card": _model_card(
                label_distribution=validation.get("label_distribution_summary", {}),
                feature_count=len(get_feature_provenance()),
                class_weight=None,
                calibration_method="not_applicable",
                cv_splits=0,
            ),
            "training_dataset_summary": {
                "rows_total": int(len(frame)),
                "rows_train": 0,
                "rows_test": 0,
                "drug_distribution": (
                    {str(label): int(count) for label, count in frame["drug"].value_counts().items()}
                    if "drug" in frame.columns
                    else {}
                ),
                "duplicate_row_count": int(validation.get("duplicate_row_count", 0)),
                "dropped_non_feature_columns": [],
                "suspicious_columns": list(validation.get("suspicious_columns", [])),
                "dataset_version": dataset_version,
            },
            "label_distribution_summary": validation.get("label_distribution_summary", {}),
            "validation": validation,
        }

    X, feature_columns, dropped_columns = select_model_features(frame)
    y = frame["outcome_label"].astype(str)

    # ── Remove exact duplicate rows before splitting to avoid leakage ────────
    combined = X.copy()
    combined["_outcome_label_"] = y.values
    before = len(combined)
    combined = combined.drop_duplicates()
    if len(combined) < before:
        import warnings as _warnings
        _warnings.warn(
            f"train_exploratory_model: {before - len(combined)} duplicate rows removed before splitting.",
            stacklevel=2,
        )
    X = combined.drop(columns=["_outcome_label_"])
    y = combined["_outcome_label_"].reset_index(drop=True)
    X = X.reset_index(drop=True)

    label_distribution = summarize_label_distribution(y)
    class_weight = _class_weight_strategy(label_distribution)
    test_size = 0.25

    # ── Use the leakage-audited split helper ─────────────────────────────────
    split_result = stratified_train_validation_test_split(
        X,
        y,
        config=ValidationConfig(test_size=test_size, validation_size=0.0),
    )
    if split_result["status"] != "ready":
        return {
            "status": "unavailable",
            "reason": "Training halted: data-leakage audit failed on the proposed train/test split. "
                      + "; ".join(split_result["leakage_audit"].get("issues", [])),
            "model_card": _model_card(
                label_distribution=label_distribution,
                feature_count=len(feature_columns),
                class_weight=None,
                calibration_method="not_applicable",
                cv_splits=0,
            ),
        }

    X_train = split_result["partitions"]["train"]["X"]
    y_train = split_result["partitions"]["train"]["y"].astype(str)
    # For test: merge validation + test since we used validation_size=0.0
    X_test = split_result["partitions"]["test"]["X"]
    y_test = split_result["partitions"]["test"]["y"].astype(str)

    train_label_distribution = summarize_label_distribution(y_train)
    test_label_distribution = summarize_label_distribution(y_test)
    cv_splits = _safe_cv_splits(int(train_label_distribution["min_class_count"]))
    calibration_cv = _safe_calibration_cv(int(train_label_distribution["min_class_count"]), cv_splits)
    calibration_method = _calibration_method(len(X_train))

    base_estimator = _build_estimator(class_weight)
    calibrated_model = CalibratedClassifierCV(
        estimator=base_estimator,
        method=calibration_method,
        cv=calibration_cv,
    )

    cross_validation = _cross_validation_summary(
        calibrated_model,
        X_train,
        y_train,
        cv_splits=cv_splits,
    )
    calibrated_model.fit(X_train, y_train)
    holdout_metrics, calibration_summary = _holdout_metrics(calibrated_model, X_test, y_test)

    feature_provenance = [item.to_dict() for item in get_feature_provenance(feature_columns)]
    monitoring_profile = build_monitoring_profile_from_training_frame(
        X_train,
        input_modalities=["tabular_variant_features"],
        feature_groups={"tabular": list(feature_columns)},
        dataset_version=dataset_version,
    )
    artifact = {
        "artifact_version": "2.0",
        "status": "ready",
        "model": calibrated_model,
        "feature_columns": feature_columns,
        "feature_provenance": feature_provenance,
        "model_card": _model_card(
            label_distribution=label_distribution,
            feature_count=len(feature_columns),
                class_weight=class_weight,
                calibration_method=calibration_method,
                cv_splits=cv_splits,
            ),
        "training_dataset_summary": _training_dataset_summary(
            frame,
            X_train,
            X_test,
            dropped_columns=dropped_columns,
            validation=validation,
        ),
        "label_distribution_summary": {
            "overall": label_distribution,
            "train": train_label_distribution,
            "test": test_label_distribution,
        },
        "validation_metrics": {
            "cross_validation": cross_validation,
            "holdout": holdout_metrics,
        },
        "calibration_summary": {
            **calibration_summary,
            "cv_folds": calibration_cv,
        },
        "training_validation": validation,
        "monitoring_profile": monitoring_profile,
    }
    artifact["training_dataset_summary"]["dataset_version"] = dataset_version

    output_path.parent.mkdir(parents=True, exist_ok=True)
    joblib.dump(artifact, output_path)
    return {
        "status": "ready",
        "artifact_path": str(output_path),
        "model_card": artifact["model_card"],
        "training_dataset_summary": artifact["training_dataset_summary"],
        "label_distribution_summary": artifact["label_distribution_summary"],
        "validation_metrics": artifact["validation_metrics"],
        "calibration_summary": artifact["calibration_summary"],
    }


def _legacy_artifact_summary(artifact: dict[str, Any]) -> dict[str, Any]:
    return {
        "status": "legacy_ready",
        "artifact_family": "classical_ml",
        "artifact_kind": str(artifact.get("artifact_kind") or "legacy_or_unknown"),
        "model_card": {
            "name": "Legacy exploratory PGx model artifact",
            "version": "legacy",
            "not_for_clinical_use": True,
            "ui_display_requirements": [
                "Display as MODEL_ASSISTED only",
                "Do not present as evidence-based or clinical-grade",
            ],
        },
        "training_dataset_summary": {},
        "label_distribution_summary": {},
        "validation_metrics": {},
        "calibration_summary": {},
        "feature_provenance": [item.to_dict() for item in get_feature_provenance(artifact.get("feature_columns", []))],
        "monitoring_profile_status": "unavailable",
    }


def summarize_model_artifact(artifact: dict[str, Any] | None) -> dict[str, Any]:
    """Return the serializable public metadata from a model artifact."""
    if artifact is None:
        return {"status": "disabled"}
    if "model_card" not in artifact:
        return _legacy_artifact_summary(artifact)
    return {
        "status": artifact.get("status", "ready"),
        "artifact_family": "classical_ml",
        "artifact_kind": artifact.get("artifact_kind") or artifact.get("model_card", {}).get("artifact_kind", "unknown"),
        "model_card": artifact.get("model_card", {}),
        "training_dataset_summary": artifact.get("training_dataset_summary", {}),
        "label_distribution_summary": artifact.get("label_distribution_summary", {}),
        "validation_metrics": artifact.get("validation_metrics", {}),
        "benchmark_dashboard": artifact.get("benchmark_dashboard", {}),
        "calibration_summary": artifact.get("calibration_summary", {}),
        "feature_provenance": artifact.get("feature_provenance", []),
        "training_validation": artifact.get("training_validation", {}),
        "monitoring_profile_status": artifact.get("monitoring_profile", {}).get("status", "unavailable"),
    }


def load_model_artifact(path: Path) -> dict[str, Any] | None:
    """Load a developer-only exploratory model artifact if one exists."""
    if not path.exists():
        return None
    return joblib.load(path)


def predict_with_model(
    drug: str,
    gene_assessments: dict[str, Any],
    artifact: dict[str, Any],
    *,
    feature_values: dict[str, Any] | None = None,
) -> dict[str, Any]:
    """Return a model-assisted prediction only for validated patient-response artifacts."""
    # Inline stub for PredictiveModelService readiness gate.
    class _ReadinessResult:
        can_run_inference = True
        reason = ""
        limitations: list[str] = []

        def to_dict(self) -> dict[str, Any]:
            return {"can_run_inference": self.can_run_inference, "reason": self.reason, "limitations": self.limitations}

    readiness = _ReadinessResult()
    artifact_status = artifact.get("status")
    if artifact_status not in {None, "ready"} and "model" not in artifact:
        readiness.can_run_inference = False
        readiness.reason = "Model artifact is not ready for inference."

    if not readiness.can_run_inference:
        return {
            "status": "unavailable",
            "reason": readiness.reason,
            "predictive_model_readiness": readiness.to_dict(),
        }

    feature_row = build_pgx_feature_row(drug, gene_assessments)
    if feature_values:
        feature_row.update(feature_values)
    frame = build_feature_frame([feature_row])
    X, feature_columns, _dropped_columns = select_model_features(frame)
    compatible_features = [column for column in artifact["feature_columns"] if column in X.columns]
    if not compatible_features:
        return {
            "status": "unavailable",
            "reason": (
                "The attached patient-response model artifact was trained on feature columns that do not align with the "
                "current live PGx inference feature set."
            ),
            "predictive_model_readiness": readiness.to_dict(),
        }
    frame = X.reindex(columns=artifact["feature_columns"], fill_value=0.0)
    model = artifact["model"]
    probabilities = model.predict_proba(frame)[0]
    labels = [str(label) for label in artifact.get("class_labels", model.classes_)]
    label_probabilities = {label: float(probability) for label, probability in zip(labels, probabilities)}
    best_label = max(label_probabilities, key=label_probabilities.get)
    active_feature_names = [
        column
        for column in feature_columns
        if column in frame.columns and float(frame.iloc[0][column]) > 0
    ]
    feature_provenance = get_feature_provenance(artifact.get("feature_columns", feature_columns))
    summary = summarize_model_support(best_label, label_probabilities, feature_provenance, active_feature_names)
    summary["explanation"] = {"status": "unavailable", "message": "Explainability service not available in single-file build."}
    summary["artifact_family"] = "classical_ml"
    summary["model_name"] = str(artifact.get("model_card", {}).get("name") or "exploratory_model")
    summary["source_module"] = "src.ml_pipeline"
    summary["predictive_model_readiness"] = readiness.to_dict()
    input_modalities = ["tabular_variant_features"]
    observed_keys = set(feature_row)
    if any(key.startswith("rna__") for key in observed_keys):
        input_modalities.append("rna_expression")
    if any(key.startswith("epigenetic__") for key in observed_keys):
        input_modalities.append("epigenetic")
    if any(key.startswith("proteomics__") for key in observed_keys):
        input_modalities.append("proteomics")
    summary["input_modalities"] = input_modalities
    summary["observed_feature_values"] = {
        str(column): round(float(frame.iloc[0][column]), 6)
        for column in frame.columns
    }
    summary["status"] = "ready"
    return summary


def write_model_status(path: Path, payload: dict[str, Any]) -> None:
    """Persist model availability metadata for scripts and CI."""
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2), encoding="utf-8")

# --- end merged module: src/ml_pipeline.py ---

# --- begin merged module: src/risk_logic.py ---
"""Rule-based PGx interpretation and conservative confidence categorization."""




def _confidence(
    category: str,
    evidence_strength: str,
    data_completeness: str,
    rationale: list[str],
) -> ConfidenceAssessment:
    return ConfidenceAssessment(
        category=category,
        evidence_strength=evidence_strength,
        data_completeness=data_completeness,
        rationale=rationale,
    )


def _safety_provenance(
    label: str,
    assertion: str,
    evidence_type: str,
) -> list[EvidenceRecord]:
    return [
        EvidenceRecord(
                source="Pharmexia local safety guard",
            label=label,
            assertion=assertion,
            source_module="src.risk_logic",
            evidence_type=evidence_type,
        )
    ]


def _make_finding(
    *,
    drug: str,
    gene: str,
    category: str,
    result_kind: str,
    summary: str,
    recommendation: str,
    confidence: ConfidenceAssessment,
    source_module: str,
    evidence_type: str,
    provenance: list[EvidenceRecord],
    clinical_grade: bool = False,
    exploratory: bool = False,
    phenotype: str | None = None,
    diplotype: str | None = None,
    matched_variants: list[str] | None = None,
    safety_notes: list[str] | None = None,
    limitations: list[str] | None = None,
) -> DrugFinding:
    return DrugFinding(
        drug=drug,
        gene=gene,
        category=category,
        result_kind=result_kind,
        summary=summary,
        recommendation=recommendation,
        confidence=confidence,
        source_module=source_module,
        evidence_type=evidence_type,
        clinical_grade=clinical_grade,
        exploratory=exploratory,
        provenance=provenance,
        phenotype=phenotype,
        diplotype=diplotype,
        matched_variants=matched_variants or [],
        safety_notes=safety_notes or [],
        limitations=limitations or [],
    )


def _insufficient_finding(drug: str, reasons: list[str]) -> DrugFinding:
    summary = "No supported, clinically actionable local PGx finding could be made for this drug from the submitted data."
    return _make_finding(
        drug=drug,
        gene=",".join(DRUG_GENE_RULES[drug]["genes"]),
        category="INSUFFICIENT_EVIDENCE",
        result_kind="SAFETY_BLOCK",
        summary=summary,
        recommendation=(
            "Do not generate a clinical claim. Consider confirmatory PGx testing with a validated assay "
            "if this drug is clinically relevant."
        ),
        confidence=_confidence(
            "INSUFFICIENT_EVIDENCE",
            "none",
            "partial",
            reasons,
        ),
        source_module="src.risk_logic",
        evidence_type="insufficient_evidence_guard",
        provenance=_safety_provenance(drug, summary, "insufficient_evidence_guard"),
        safety_notes=["Unsupported claims are intentionally suppressed when evidence is incomplete."],
        limitations=DRUG_GENE_RULES[drug]["limitations"],
    )


def _make_warfarin_finding(
    assessments: dict[str, GeneAssessment],
    evidence: EvidenceIntegrator,
) -> DrugFinding:
    cyp2c9 = assessments.get("CYP2C9")
    vkorc1 = assessments.get("VKORC1")
    summary_bits: list[str] = []
    safety_notes = [
        "Do not calculate or suggest a warfarin dose from this application alone.",
        "Manual clinical review, INR monitoring, and a validated dosing algorithm are required before action.",
    ]
    limitations = list(DRUG_GENE_RULES["warfarin"]["limitations"])
    provenance: list[EvidenceRecord] = []
    matched_variants: list[str] = []

    if cyp2c9 and cyp2c9.matched_alleles:
        allele_names = ", ".join(match.allele or match.rsid for match in cyp2c9.matched_alleles)
        summary_bits.append(
            f"Curated CYP2C9 decreased-function allele evidence was observed in the local rule set ({allele_names})."
        )
        if cyp2c9.phenotype:
            summary_bits.append(f"CYP2C9 limited-panel phenotype: {cyp2c9.phenotype}.")
        provenance.extend(evidence.provenance_for_assessment(cyp2c9, drug="warfarin"))
        matched_variants.extend(match.rsid for match in cyp2c9.matched_alleles)
        limitations.extend(cyp2c9.limitations)

    if vkorc1 and vkorc1.matched_alleles:
        summary_bits.append(
            "Curated VKORC1 rs9923231 A-allele evidence was observed, which is associated with higher warfarin sensitivity in authoritative references."
        )
        provenance.extend(evidence.provenance_for_assessment(vkorc1, drug="warfarin"))
        matched_variants.extend(match.rsid for match in vkorc1.matched_alleles)
        limitations.extend(vkorc1.limitations)

    if not summary_bits:
        return _insufficient_finding(
            "warfarin",
            ["No curated CYP2C9 or VKORC1 evidence-bearing allele was observed in the submitted data."],
        )

    both_gene_signals = bool(cyp2c9 and cyp2c9.matched_alleles) and bool(vkorc1 and vkorc1.matched_alleles)
    local_targets_complete = bool(cyp2c9 and cyp2c9.coverage_complete) and bool(vkorc1 and vkorc1.coverage_complete)
    return _make_finding(
        drug="warfarin",
        gene="CYP2C9,VKORC1",
        category="EVIDENCE_BASED",
        result_kind="CONFIRMED_PGX_FINDING",
        summary=" ".join(summary_bits),
        recommendation=(
            "Manual review only: consult current CPIC/FDA-aligned warfarin guidance together with clinical covariates "
            "and INR. This application does not provide a dose or therapy instruction."
        ),
        confidence=_confidence(
            "EVIDENCE_BASED",
            "moderate" if both_gene_signals else "limited",
            "complete" if local_targets_complete else "partial",
            [
                "The result is anchored to curated CYP2C9 and VKORC1 references relevant to warfarin response.",
                "Numeric dosing is deliberately suppressed because clinical covariates and INR are required.",
                "The local desktop workflow is not a full validated clinical warfarin dosing engine.",
            ],
        ),
        source_module="src.risk_logic",
        evidence_type="curated_local_rule",
        provenance=provenance or _safety_provenance("warfarin", "Curated local evidence records were not available.", "provenance_gap"),
        phenotype=cyp2c9.phenotype if cyp2c9 else None,
        diplotype=cyp2c9.local_panel_call if cyp2c9 and not cyp2c9.ambiguous else None,
        matched_variants=sorted(set(matched_variants)),
        safety_notes=safety_notes,
        limitations=sorted(set(limitations)),
    )


def _make_clopidogrel_finding(
    assessment: GeneAssessment,
    evidence: EvidenceIntegrator,
) -> DrugFinding:
    if not assessment.matched_alleles:
        return _insufficient_finding(
            "clopidogrel",
            ["No curated CYP2C19 allele affecting the local clopidogrel rule set was observed."],
        )

    effect_terms = {match.effect for match in assessment.matched_alleles}
    reduced = "reduced_cyp2c19_activity" in effect_terms
    increased = "increased_cyp2c19_activity" in effect_terms
    mixed_signal = reduced and increased

    summary_bits: list[str] = []
    if reduced:
        summary_bits.append(
            "Curated CYP2C19 loss-of-function allele evidence was observed, which can reduce clopidogrel bioactivation in authoritative PGx references."
        )
    if increased:
        summary_bits.append("Curated CYP2C19 increased-function allele evidence was observed.")
    if mixed_signal:
        summary_bits.append(
            "Both reduced-function and increased-function CYP2C19 evidence were present, so this local panel does not assign a definitive net phenotype or treatment implication."
        )
    elif assessment.phenotype:
        summary_bits.append(f"CYP2C19 limited-panel phenotype: {assessment.phenotype}.")
    elif assessment.ambiguous:
        summary_bits.append("A definitive CYP2C19 diplotype was not assigned because phase or haplotype structure is unresolved.")
    else:
        summary_bits.append("No definitive CYP2C19 phenotype was assigned from the submitted data.")

    return _make_finding(
        drug="clopidogrel",
        gene="CYP2C19",
        category="EVIDENCE_BASED",
        result_kind="CONFIRMED_PGX_FINDING",
        summary=" ".join(summary_bits),
        recommendation=(
            "Manual review only: consult current CPIC clopidogrel guidance for the treated indication before any therapy change. "
            "This application does not auto-select an alternative antiplatelet agent."
        ),
        confidence=_confidence(
            "EVIDENCE_BASED",
            "moderate" if assessment.coverage_complete and not mixed_signal and not assessment.ambiguous else "limited",
            "complete" if assessment.coverage_complete else "partial",
            [
                "The local rule is limited to curated CYP2C19 alleles with established clopidogrel relevance.",
                "Mixed-function or unresolved haplotype evidence is not converted into a definitive therapy call.",
                "Clinical action still depends on indication, urgency, and bleeding or thrombosis context.",
            ],
        ),
        source_module="src.risk_logic",
        evidence_type="curated_local_rule",
        provenance=evidence.provenance_for_assessment(assessment, drug="clopidogrel"),
        phenotype=None if mixed_signal else assessment.phenotype,
        diplotype=None if mixed_signal or assessment.ambiguous else assessment.local_panel_call,
        matched_variants=sorted({match.rsid for match in assessment.matched_alleles}),
        safety_notes=[
            "Do not auto-switch antiplatelet therapy without clinician review.",
            "Mixed-function CYP2C19 evidence must not be simplified into a definitive phenotype by this app.",
        ],
        limitations=sorted(set(DRUG_GENE_RULES["clopidogrel"]["limitations"] + assessment.limitations)),
    )


def _make_cyp2c19_exposure_finding(
    drug: str,
    assessment: GeneAssessment,
    evidence: EvidenceIntegrator,
    *,
    reduced_summary: str,
    increased_summary: str,
    recommendation: str,
    confidence_notes: list[str],
    safety_notes: list[str],
) -> DrugFinding:
    if not assessment.matched_alleles:
        return _insufficient_finding(
            drug,
            [f"No curated CYP2C19 allele affecting the local {drug_display_label(drug)} rule set was observed."],
        )

    effect_terms = {match.effect for match in assessment.matched_alleles}
    reduced = "reduced_cyp2c19_activity" in effect_terms
    increased = "increased_cyp2c19_activity" in effect_terms
    mixed_signal = reduced and increased

    summary_bits: list[str] = []
    if reduced:
        summary_bits.append(reduced_summary)
    if increased:
        summary_bits.append(increased_summary)
    if mixed_signal:
        summary_bits.append(
            f"Both reduced-function and increased-function CYP2C19 evidence were present, so this local panel does not assign a definitive net phenotype or treatment implication for {drug_display_label(drug)}."
        )
    elif assessment.phenotype:
        summary_bits.append(f"CYP2C19 limited-panel phenotype: {assessment.phenotype}.")
    elif assessment.ambiguous:
        summary_bits.append("A definitive CYP2C19 diplotype was not assigned because phase or haplotype structure is unresolved.")
    else:
        summary_bits.append("No definitive CYP2C19 phenotype was assigned from the submitted data.")

    return _make_finding(
        drug=drug,
        gene="CYP2C19",
        category="EVIDENCE_BASED",
        result_kind="CONFIRMED_PGX_FINDING",
        summary=" ".join(summary_bits),
        recommendation=recommendation,
        confidence=_confidence(
            "EVIDENCE_BASED",
            "moderate" if assessment.coverage_complete and not mixed_signal and not assessment.ambiguous else "limited",
            "complete" if assessment.coverage_complete else "partial",
            confidence_notes,
        ),
        source_module="src.risk_logic",
        evidence_type="curated_local_rule",
        provenance=evidence.provenance_for_assessment(assessment, drug=drug),
        phenotype=None if mixed_signal else assessment.phenotype,
        diplotype=None if mixed_signal or assessment.ambiguous else assessment.local_panel_call,
        matched_variants=sorted({match.rsid for match in assessment.matched_alleles}),
        safety_notes=safety_notes,
        limitations=sorted(set(DRUG_GENE_RULES[drug]["limitations"] + assessment.limitations)),
    )


def _make_ssri_finding(
    drug: str,
    assessment: GeneAssessment,
    evidence: EvidenceIntegrator,
) -> DrugFinding:
    return _make_cyp2c19_exposure_finding(
        drug,
        assessment,
        evidence,
        reduced_summary=(
            f"Curated CYP2C19 loss-of-function allele evidence was observed, which can increase {drug_display_label(drug)} exposure in authoritative PGx references."
        ),
        increased_summary=(
            f"Curated CYP2C19 increased-function allele evidence was observed, which can lower {drug_display_label(drug)} exposure in authoritative PGx references."
        ),
        recommendation=(
            f"Manual review only: consult current antidepressant PGx guidance and the active {drug_display_label(drug)} label before any dose or therapy change. "
            "This application does not auto-select an antidepressant or dose."
        ),
        confidence_notes=[
            f"The local rule is limited to curated CYP2C19 alleles with established {drug_display_label(drug)} relevance.",
            "This local workflow does not model the full antidepressant selection context or non-genetic tolerability factors.",
            "Mixed-function or unresolved haplotype evidence is not converted into a definitive therapy call.",
        ],
        safety_notes=[
            "Do not auto-switch antidepressant therapy without clinician review.",
            "Antidepressant selection still depends on diagnosis, adverse-effect profile, comorbidities, and concurrent medications.",
        ],
    )


def _make_ppi_finding(
    drug: str,
    assessment: GeneAssessment,
    evidence: EvidenceIntegrator,
) -> DrugFinding:
    return _make_cyp2c19_exposure_finding(
        drug,
        assessment,
        evidence,
        reduced_summary=(
            f"Curated CYP2C19 loss-of-function allele evidence was observed, which can increase {drug_display_label(drug)} exposure and acid suppression in authoritative PGx references."
        ),
        increased_summary=(
            f"Curated CYP2C19 increased-function allele evidence was observed, which can lower {drug_display_label(drug)} exposure and reduce acid suppression in authoritative PGx references."
        ),
        recommendation=(
            f"Manual review only: consult current proton pump inhibitor PGx guidance and the active {drug_display_label(drug)} label before any dose or regimen change. "
            "This application does not auto-adjust treatment duration or regimen."
        ),
        confidence_notes=[
            f"The local rule is limited to curated CYP2C19 alleles with established {drug_display_label(drug)} relevance.",
            "Clinical action still depends on indication, treatment goals, and interacting medications.",
            "Mixed-function or unresolved haplotype evidence is not converted into a definitive therapy call.",
        ],
        safety_notes=[
            "Do not infer a proton pump inhibitor regimen or duration from this application alone.",
            "Treatment still depends on indication, ulcer risk, and concomitant therapies.",
        ],
    )


def _make_voriconazole_finding(
    assessment: GeneAssessment,
    evidence: EvidenceIntegrator,
) -> DrugFinding:
    return _make_cyp2c19_exposure_finding(
        "voriconazole",
        assessment,
        evidence,
        reduced_summary=(
            "Curated CYP2C19 loss-of-function allele evidence was observed, which can increase voriconazole exposure in authoritative PGx references."
        ),
        increased_summary=(
            "Curated CYP2C19 increased-function allele evidence was observed, which can lower voriconazole exposure and reduce the likelihood of achieving target concentrations in authoritative PGx references."
        ),
        recommendation=(
            "Manual review only: consult current voriconazole PGx guidance, indication-specific antifungal management, and therapeutic drug monitoring practice before any dose or therapy change. "
            "This application does not assign an antifungal regimen."
        ),
        confidence_notes=[
            "The local rule is limited to curated CYP2C19 alleles with established voriconazole relevance.",
            "Voriconazole interpretation depends on indication, co-medications, and therapeutic drug monitoring context.",
            "Mixed-function or unresolved haplotype evidence is not converted into a definitive therapy call.",
        ],
        safety_notes=[
            "Do not auto-select an antifungal strategy from this application.",
            "Therapeutic drug monitoring and clinician review remain important for voriconazole use.",
        ],
    )


def _make_simvastatin_finding(
    assessment: GeneAssessment,
    evidence: EvidenceIntegrator,
) -> DrugFinding:
    if not assessment.matched_alleles:
        return _insufficient_finding(
            "simvastatin",
            ["No SLCO1B1 rs4149056 evidence-bearing allele was observed."],
        )

    zygosity = "heterozygous" if any(match.genotype_code == 1 for match in assessment.matched_alleles) else "homozygous"
    summary = (
        f"Curated SLCO1B1 rs4149056 C-allele evidence was observed ({zygosity}), which is associated with higher simvastatin-associated "
        "muscle toxicity risk in authoritative PGx references."
    )
    return _make_finding(
        drug="simvastatin",
        gene="SLCO1B1",
        category="EVIDENCE_BASED",
        result_kind="CONFIRMED_PGX_FINDING",
        summary=summary,
        recommendation=(
            "Manual review only: consult current statin PGx guidance before changing therapy. "
            "This application does not recommend a specific replacement statin or dose."
        ),
        confidence=_confidence(
            "EVIDENCE_BASED",
            "limited",
            "partial",
            [
                "The local interpretation uses rs4149056 as a clinically relevant proxy but does not reconstruct full SLCO1B1 haplotypes.",
                "A negative local result must not be used to claim absence of simvastatin risk.",
            ],
        ),
        source_module="src.risk_logic",
        evidence_type="curated_local_rule",
        provenance=evidence.provenance_for_assessment(assessment, drug="simvastatin"),
        matched_variants=sorted({match.rsid for match in assessment.matched_alleles}),
        safety_notes=[
            "Do not claim absence of simvastatin risk from a negative local result.",
            "Do not auto-select an alternative statin or fixed dose from this application.",
        ],
        limitations=sorted(set(DRUG_GENE_RULES["simvastatin"]["limitations"] + assessment.limitations)),
    )


def _make_thiopurine_finding(
    drug: str,
    tpmt: GeneAssessment,
    nudt15: GeneAssessment,
    evidence: EvidenceIntegrator,
) -> DrugFinding:
    provenance: list[EvidenceRecord] = []
    matched_variants: list[str] = []
    summary_bits: list[str] = []
    limitations = list(DRUG_GENE_RULES[drug]["limitations"])

    if tpmt.matched_alleles:
        summary_bits.append("Curated TPMT reduced-function or no-function allele evidence was observed.")
        if tpmt.phenotype:
            summary_bits.append(f"TPMT limited-panel phenotype: {tpmt.phenotype}.")
        elif tpmt.ambiguous:
            summary_bits.append("TPMT phase or haplotype structure was unresolved, so no definitive TPMT diplotype was assigned.")
        provenance.extend(evidence.provenance_for_assessment(tpmt, drug=drug))
        matched_variants.extend(match.rsid for match in tpmt.matched_alleles)
        limitations.extend(tpmt.limitations)

    if nudt15.matched_alleles:
        summary_bits.append("Curated NUDT15 no-function allele evidence was observed.")
        if nudt15.phenotype:
            summary_bits.append(f"NUDT15 limited-panel phenotype: {nudt15.phenotype}.")
        provenance.extend(evidence.provenance_for_assessment(nudt15, drug=drug))
        matched_variants.extend(match.rsid for match in nudt15.matched_alleles)
        limitations.extend(nudt15.limitations)

    if not summary_bits:
        return _insufficient_finding(
            drug,
            ["No curated TPMT or NUDT15 evidence-bearing allele was observed."],
        )

    if tpmt.matched_alleles and nudt15.matched_alleles:
        summary_bits.append(
            "A combined TPMT/NUDT15 phenotype was not assigned because this local workflow does not validate a unified combined-gene call."
        )

    return _make_finding(
        drug=drug,
        gene="TPMT,NUDT15",
        category="EVIDENCE_BASED",
        result_kind="CONFIRMED_PGX_FINDING",
        summary=" ".join(summary_bits),
        recommendation=(
            "Manual review only: consult current thiopurine PGx guidance and validated TPMT/NUDT15 testing before any dose or therapy change. "
            "This application does not provide a starting dose."
        ),
        confidence=_confidence(
            "EVIDENCE_BASED",
            "limited",
            "partial",
            [
                "TPMT and NUDT15 evidence is authoritative for thiopurine toxicity risk, but phenotype assignment can require broader allele coverage or phasing.",
                "This local workflow does not issue a combined-gene clinical phenotype or numeric dosing instruction.",
            ],
        ),
        source_module="src.risk_logic",
        evidence_type="curated_local_rule",
        provenance=provenance,
        matched_variants=sorted(set(matched_variants)),
        safety_notes=[
            "Do not infer a thiopurine starting dose from this application.",
            "Combined TPMT and NUDT15 findings require clinician review and validated PGx testing.",
        ],
        limitations=sorted(set(limitations)),
    )


def interpret_drug_rules(
    gene_assessments: dict[str, GeneAssessment],
    selected_drugs: list[str],
    evidence: EvidenceIntegrator,
) -> list[DrugFinding]:
    """Generate safe drug-response findings from curated local PGx rules.

    Every gene assessment lookup uses ``.get()`` so that a drug can be
    selected even when the patient VCF contains no variants for the
    corresponding pharmacogene(s) — the result is an INSUFFICIENT_EVIDENCE
    finding rather than a KeyError crash.
    """
    drugs = list(selected_drugs)
    if not drugs:
        return []
    findings: list[DrugFinding] = []

    for drug in drugs:
        if drug == "warfarin":
            findings.append(_make_warfarin_finding(gene_assessments, evidence))

        elif drug == "clopidogrel":
            assessment = gene_assessments.get("CYP2C19")
            if assessment is None:
                findings.append(_insufficient_finding(drug, ["CYP2C19 assessment not available for the submitted data."]))
            else:
                findings.append(_make_clopidogrel_finding(assessment, evidence))

        elif drug in {"citalopram", "escitalopram", "sertraline"}:
            assessment = gene_assessments.get("CYP2C19")
            if assessment is None:
                findings.append(_insufficient_finding(drug, ["CYP2C19 assessment not available for the submitted data."]))
            else:
                findings.append(_make_ssri_finding(drug, assessment, evidence))

        elif drug in {"omeprazole", "lansoprazole", "pantoprazole"}:
            assessment = gene_assessments.get("CYP2C19")
            if assessment is None:
                findings.append(_insufficient_finding(drug, ["CYP2C19 assessment not available for the submitted data."]))
            else:
                findings.append(_make_ppi_finding(drug, assessment, evidence))

        elif drug == "voriconazole":
            assessment = gene_assessments.get("CYP2C19")
            if assessment is None:
                findings.append(_insufficient_finding(drug, ["CYP2C19 assessment not available for the submitted data."]))
            else:
                findings.append(_make_voriconazole_finding(assessment, evidence))

        elif drug == "simvastatin":
            assessment = gene_assessments.get("SLCO1B1")
            if assessment is None:
                findings.append(_insufficient_finding(drug, ["SLCO1B1 assessment not available for the submitted data."]))
            else:
                findings.append(_make_simvastatin_finding(assessment, evidence))

        elif drug in {"azathioprine", "mercaptopurine", "thioguanine"}:
            tpmt = gene_assessments.get("TPMT")
            nudt15 = gene_assessments.get("NUDT15")
            if tpmt is None and nudt15 is None:
                findings.append(_insufficient_finding(drug, ["Neither TPMT nor NUDT15 assessment available for the submitted data."]))
            elif tpmt is None:
                findings.append(_insufficient_finding(drug, ["TPMT assessment not available; combined thiopurine call requires both TPMT and NUDT15."]))
            elif nudt15 is None:
                findings.append(_insufficient_finding(drug, ["NUDT15 assessment not available; combined thiopurine call requires both TPMT and NUDT15."]))
            else:
                findings.append(_make_thiopurine_finding(drug, tpmt, nudt15, evidence))

    return findings

# --- end merged module: src/risk_logic.py ---

# --- begin merged module: src/models/view_models.py ---
"""View-model dataclasses for the PySide6 desktop interface."""


from dataclasses import asdict, dataclass, field
from typing import Any


@dataclass(slots=True)
class FindingTableRow:
    drug: str
    category: str
    gene: str
    phenotype: str
    summary: str
    recommendation: str

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


@dataclass(slots=True)
class AnalysisViewModel:
    input_label: str
    summary_line: str
    findings_rows: list[FindingTableRow] = field(default_factory=list)
    report_html: str = ""
    report_text: str = ""
    pipeline_status: str = "warning"
    can_export: bool = False

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)

# --- end merged module: src/models/view_models.py ---

# --- begin merged module: src/reporting.py ---
"""Structured and HTML report generation."""


from html import escape
from typing import Any



def _input_type_label(input_mode: str) -> str:
    if input_mode == "variant":
        return "DNA variant input"
    return "invalid input"


def _bool_label(value: bool) -> str:
    return "yes" if value else "no"


def _interaction_entity_label(finding: DrugInteractionFinding) -> str:
    if finding.entity_type == "drug":
        return drug_display_label(finding.interacting_entity)
    return finding.interacting_entity


def _explanation_line_items(explanation: dict[str, Any] | None) -> list[str]:
    if not explanation:
        return ["Explanation: unavailable"]
    status = str(explanation.get("status") or "unavailable")
    explanation_type = str(explanation.get("explanation_type") or "unavailable")
    items = [f"Explanation: {status} ({explanation_type})"]
    if status != "available":
        message = str(explanation.get("message") or "No explanation payload was available.")
        items.append(f"Explanation note: {message}")
        return items

    top_features = ", ".join(item.get("label", "") for item in explanation.get("top_features", [])[:3] if item.get("label"))
    top_genes = ", ".join(item.get("label", "") for item in explanation.get("top_genes", [])[:3] if item.get("label"))
    top_tokens = ", ".join(item.get("label", "") for item in explanation.get("top_sequence_tokens", [])[:3] if item.get("label"))
    if top_features:
        items.append(f"Top features: {top_features}")
    if top_genes:
        items.append(f"Top genes: {top_genes}")
    if top_tokens:
        items.append(f"Top sequence tokens: {top_tokens}")
    return items


def _finding_text_block(finding: DrugFinding) -> list[str]:
    lines = [
        f"- {finding.drug}: {finding.summary}",
        f"  Result kind: {finding.result_kind}",
        f"  Output category: {finding.category}",
        f"  Source module: {finding.source_module}",
        f"  Evidence type: {finding.evidence_type}",
        f"  Confidence category: {finding.confidence.category}",
        f"  Clinical-grade: {_bool_label(finding.clinical_grade)}",
        f"  Exploratory: {_bool_label(finding.exploratory)}",
    ]
    if finding.phenotype:
        lines.append(f"  Phenotype: {finding.phenotype}")
    if finding.diplotype:
        lines.append(f"  Local panel call: {finding.diplotype}")
    lines.append(f"  Recommended next step: {finding.recommendation}")
    lines.append(f"  Matched variant evidence: {', '.join(finding.matched_variants) or 'None'}")
    if finding.category == "MODEL_ASSISTED" or finding.explanation:
        for item in _explanation_line_items(finding.explanation):
            lines.append(f"  {item}")
    if finding.provenance:
        for record in finding.provenance:
            lines.append(
                f"  Provenance: {record.source} | {record.source_module} | {record.evidence_type} | {record.assertion}"
            )
    else:
        lines.append("  Provenance: None attached")
    return lines


def _finding_html(finding: DrugFinding) -> str:
    sources = "".join(
        (
            "<li>"
            f"<a href='{escape(record.url or '#')}'>{escape(record.source)}</a> | "
            f"{escape(record.source_module)} | {escape(record.evidence_type)} | "
            f"{escape(record.assertion)}"
            "</li>"
        )
        for record in finding.provenance
    )
    safety = "".join(f"<li>{escape(note)}</li>" for note in finding.safety_notes)
    limits = "".join(f"<li>{escape(note)}</li>" for note in finding.limitations)
    phenotype = f"<p><b>Phenotype:</b> {escape(finding.phenotype)}</p>" if finding.phenotype else ""
    diplotype = f"<p><b>Local panel call:</b> {escape(finding.diplotype)}</p>" if finding.diplotype else ""
    explanation_lines = "".join(f"<li>{escape(item)}</li>" for item in _explanation_line_items(finding.explanation))
    explanation_section = (
        f"<h4>Explanation</h4><ul>{explanation_lines or '<li>Explanation unavailable</li>'}</ul>"
        if finding.category == "MODEL_ASSISTED" or finding.explanation
        else ""
    )
    return f"""
    <section>
      <h3>{escape(finding.drug.title())}</h3>
      <p>{escape(finding.summary)}</p>
      <p><b>Result kind:</b> {escape(finding.result_kind)}</p>
      <p><b>Output category:</b> {escape(finding.category)}</p>
      <p><b>Source module:</b> {escape(finding.source_module)}</p>
      <p><b>Evidence type:</b> {escape(finding.evidence_type)}</p>
      <p><b>Confidence:</b> {escape(finding.confidence.category)} | {escape(finding.confidence.evidence_strength)} | {escape(finding.confidence.data_completeness)}</p>
      <p><b>Clinical-grade:</b> {escape(_bool_label(finding.clinical_grade))}</p>
      <p><b>Exploratory:</b> {escape(_bool_label(finding.exploratory))}</p>
      {phenotype}
      {diplotype}
      <p><b>Recommendation:</b> {escape(finding.recommendation)}</p>
      <p><b>Matched variant evidence:</b> {escape(', '.join(finding.matched_variants) or 'None')}</p>
      {explanation_section}
      <h4>Safety Notes</h4>
      <ul>{safety or '<li>None</li>'}</ul>
      <h4>Limitations</h4>
      <ul>{limits or '<li>None</li>'}</ul>
      <h4>Provenance</h4>
      <ul>{sources or '<li>No provenance records attached.</li>'}</ul>
    </section>
    """


def _render_text_section(title: str, findings: list[DrugFinding]) -> list[str]:
    lines = ["", f"{title}:"]
    for finding in findings:
        lines.extend(_finding_text_block(finding))
    return lines


def _render_html_section(title: str, findings: list[DrugFinding]) -> str:
    if not findings:
        return ""
    body = "".join(_finding_html(finding) for finding in findings)
    return f"""
    <section>
      <h2>{escape(title)}</h2>
      {body}
    </section>
    """


def _render_patient_profile_text(result: AnalysisResult) -> list[str]:
    validation = result.patient_profile_validation
    if validation is None or validation.status == "not_provided":
        return ["", "Patient clinical profile:", "- Not provided"]

    rows = PatientContextService().summary_rows(result.patient_profile, validation)
    lines = ["", "Patient clinical profile:"]
    for label, value in rows:
        lines.append(f"- {label}: {value}")
    if result.clinical_model_features_used:
        lines.append(
            "- Clinical model features applied only to exploratory model contexts: "
            + ", ".join(result.clinical_model_features_used)
        )
    else:
        lines.append("- Clinical modifiers were retained separately from genetic evidence.")
    return lines


def _render_patient_profile_html(result: AnalysisResult) -> str:
    validation = result.patient_profile_validation
    if validation is None or validation.status == "not_provided":
        body = "<li>Status: Not provided</li>"
    else:
        rows = PatientContextService().summary_rows(result.patient_profile, validation)
        body = "".join(f"<li><b>{escape(label)}:</b> {escape(value)}</li>" for label, value in rows)
        if result.clinical_model_features_used:
            body += (
                "<li><b>Model feature use:</b> "
                + escape(", ".join(result.clinical_model_features_used))
                + " (exploratory model context only)</li>"
            )
        else:
            body += "<li><b>Model feature use:</b> None; clinical modifiers remained separate from genetic evidence.</li>"
    return f"""
    <section>
      <h2>Patient Clinical Profile</h2>
      <ul>{body}</ul>
    </section>
    """


def _evidence_annotation_text(annotation: VariantEvidenceAnnotation) -> list[str]:
    effect = annotation.variant_effect
    effect_text = (
        f" | effect={effect.effect_type} ({effect.effect_confidence})"
        + (f" | protein={effect.protein_effect}" if effect and effect.protein_effect else "")
        + (
            f" | pathogenicity={effect.pathogenicity_label}"
            if effect and effect.pathogenicity_label != "UNSPECIFIED"
            else ""
        )
        if effect is not None
        else ""
    )
    return [
        (
            f"- {annotation.variant_token}: gene={annotation.gene} | status={annotation.availability_status} | "
            f"matched_alleles={', '.join(annotation.matched_alleles) or 'None'}{effect_text} | summary={annotation.final_evidence_summary}"
        )
    ]


def _render_evidence_annotations_text(annotations: list[VariantEvidenceAnnotation]) -> list[str]:
    if not annotations:
        return []
    lines = ["", "Structured evidence annotations:"]
    for annotation in annotations:
        lines.extend(_evidence_annotation_text(annotation))
    return lines


def _render_evidence_annotations_html(annotations: list[VariantEvidenceAnnotation]) -> str:
    if not annotations:
        return ""
    items: list[str] = []
    for annotation in annotations:
        parts = [
            f"<b>{escape(annotation.variant_token)}</b>: gene={escape(annotation.gene)}",
            f"status={escape(annotation.availability_status)}",
            f"matched_alleles={escape(', '.join(annotation.matched_alleles) or 'None')}",
        ]
        if annotation.variant_effect is not None:
            parts.append(
                f"effect={escape(annotation.variant_effect.effect_type)} ({escape(annotation.variant_effect.effect_confidence)})"
            )
            if annotation.variant_effect.protein_effect:
                parts.append(f"protein={escape(annotation.variant_effect.protein_effect)}")
            if annotation.variant_effect.pathogenicity_label != "UNSPECIFIED":
                parts.append(f"pathogenicity={escape(annotation.variant_effect.pathogenicity_label)}")
        parts.append(f"summary={escape(annotation.final_evidence_summary)}")
        items.append("<li>" + " | ".join(parts) + "</li>")
    body = "".join(items)
    return f"""
    <section>
      <h2>Structured Evidence Annotations</h2>
      <ul>{body}</ul>
    </section>
    """


def _render_aggregated_evidence_text(bundles: list[MergedEvidenceBundle]) -> list[str]:
    if not bundles:
        return []
    lines = ["", "Evidence aggregation engine summary:"]
    for bundle in bundles:
        drug = drug_display_label(bundle.normalized_drug_name or "unspecified")
        lines.append(
            f"- {drug}: category={bundle.output_category} | status={bundle.availability_status} | summary={bundle.summary}"
        )
        lines.append(
            "  "
            + f"evidence_based={len(bundle.evidence_based_records)} | "
            + f"model_assisted={len(bundle.model_assisted_records)} | "
            + f"review_only={len(bundle.review_only_records)}"
        )
        if bundle.conflict_messages:
            lines.append("  conflicts=" + "; ".join(bundle.conflict_messages))
    return lines


def _render_aggregated_evidence_html(bundles: list[MergedEvidenceBundle]) -> str:
    if not bundles:
        return ""
    body = "".join(
        (
            "<li>"
            f"<b>{escape(drug_display_label(bundle.normalized_drug_name or 'unspecified'))}</b>: "
            f"category={escape(bundle.output_category)} | "
            f"status={escape(bundle.availability_status)} | "
            f"evidence_based={len(bundle.evidence_based_records)} | "
            f"model_assisted={len(bundle.model_assisted_records)} | "
            f"review_only={len(bundle.review_only_records)} | "
            f"summary={escape(bundle.summary)}"
            + (
                f" | conflicts={escape('; '.join(bundle.conflict_messages))}"
                if bundle.conflict_messages
                else ""
            )
            + "</li>"
        )
        for bundle in bundles
    )
    return f"""
    <section>
      <h2>Evidence Aggregation Engine Summary</h2>
      <ul>{body}</ul>
    </section>
    """


def _interaction_text_block(finding: DrugInteractionFinding) -> list[str]:
    lines = [
        (
            f"- {drug_display_label(finding.subject_drug)} -> {_interaction_entity_label(finding)}: "
            f"{finding.summary}"
        ),
        f"  Interaction type: {finding.interaction_type}",
        f"  Entity type: {finding.entity_type}",
        f"  Severity: {finding.severity}",
        f"  Status: {finding.status}",
        f"  Evidence category: {finding.evidence_category}",
        f"  Confidence: {finding.confidence}",
        f"  Evidence-based: {_bool_label(finding.evidence_based)}",
        f"  Clinical relevance: {finding.clinical_relevance}",
    ]
    if finding.mechanism:
        lines.append(f"  Mechanism: {finding.mechanism}")
    lines.append(
        "  Recommended next step: "
        + (finding.recommendation or "No automated recommendation is emitted for this interaction context.")
    )
    if finding.provenance:
        for record in finding.provenance:
            citation = f" | {record.citation_url}" if record.citation_url else ""
            note = f" | {record.note}" if record.note else ""
            lines.append(
                f"  Provenance: {record.source_name} | {record.source_module} | {record.evidence_type}{citation}{note}"
            )
    else:
        lines.append("  Provenance: None attached")
    return lines


def _interaction_html(finding: DrugInteractionFinding) -> str:
    sources = "".join(
        (
            "<li>"
            f"<a href='{escape(record.citation_url or '#')}'>{escape(record.source_name)}</a> | "
            f"{escape(record.source_module)} | {escape(record.evidence_type)}"
            + (f" | {escape(record.note)}" if record.note else "")
            + "</li>"
        )
        for record in finding.provenance
    )
    limits = "".join(f"<li>{escape(note)}</li>" for note in finding.limitations)
    return f"""
    <section>
      <h3>{escape(drug_display_label(finding.subject_drug))} -> {escape(_interaction_entity_label(finding))}</h3>
      <p>{escape(finding.summary)}</p>
      <p><b>Interaction type:</b> {escape(finding.interaction_type)}</p>
      <p><b>Entity type:</b> {escape(finding.entity_type)}</p>
      <p><b>Severity:</b> {escape(finding.severity)}</p>
      <p><b>Status:</b> {escape(finding.status)}</p>
      <p><b>Evidence category:</b> {escape(finding.evidence_category)}</p>
      <p><b>Confidence:</b> {escape(finding.confidence)}</p>
      <p><b>Evidence-based:</b> {escape(_bool_label(finding.evidence_based))}</p>
      <p><b>Clinical relevance:</b> {escape(finding.clinical_relevance)}</p>
      <p><b>Mechanism:</b> {escape(finding.mechanism or 'None')}</p>
      <p><b>Recommendation:</b> {escape(finding.recommendation or 'No automated recommendation is emitted for this interaction context.')}</p>
      <h4>Limitations</h4>
      <ul>{limits or '<li>None</li>'}</ul>
      <h4>Provenance</h4>
      <ul>{sources or '<li>No provenance records attached.</li>'}</ul>
    </section>
    """


def _render_interactions_text(findings: list[DrugInteractionFinding]) -> list[str]:
    if not findings:
        return []
    lines = ["", "Drug interaction engine summary:"]
    drug_drug = [finding for finding in findings if finding.interaction_type in {"drug_drug", "medication_context", "unsupported_drug"}]
    drug_gene = [finding for finding in findings if finding.interaction_type not in {"drug_drug", "medication_context", "unsupported_drug"}]
    if drug_drug:
        lines.append("- Drug-drug and medication-list context:")
        for finding in drug_drug:
            lines.extend(_interaction_text_block(finding))
    if drug_gene:
        lines.append("- Drug-gene / drug-enzyme / drug-transporter context:")
        for finding in drug_gene:
            lines.extend(_interaction_text_block(finding))
    return lines


def _render_interactions_html(findings: list[DrugInteractionFinding]) -> str:
    if not findings:
        return ""
    drug_drug = "".join(
        _interaction_html(finding)
        for finding in findings
        if finding.interaction_type in {"drug_drug", "medication_context", "unsupported_drug"}
    )
    drug_gene = "".join(
        _interaction_html(finding)
        for finding in findings
        if finding.interaction_type not in {"drug_drug", "medication_context", "unsupported_drug"}
    )
    return f"""
    <section>
      <h2>Drug Interaction Engine Summary</h2>
      {f"<h3>Drug-Drug and Medication Context</h3>{drug_drug}" if drug_drug else ""}
      {f"<h3>Drug-Gene and Drug-Enzyme Context</h3>{drug_gene}" if drug_gene else ""}
    </section>
    """


def _format_mapping(mapping: dict[str, Any]) -> str:
    if not mapping:
        return "None"
    return ", ".join(f"{key}={value}" for key, value in mapping.items())


def _model_summary_text(model_summary: dict[str, Any]) -> list[str]:
    status = str(model_summary.get("status") or "disabled")
    if status == "disabled":
        return []

    artifact_family = str(model_summary.get("artifact_family") or "classical_ml")
    readiness = model_summary.get("predictive_model_readiness", {})
    if not isinstance(readiness, dict):
        readiness = {}
    model_card = model_summary.get("model_card", {})
    dataset = model_summary.get("training_dataset_summary", {})
    label_distribution = model_summary.get("label_distribution_summary", {})
    validation_metrics = model_summary.get("validation_metrics", {})
    calibration_summary = model_summary.get("calibration_summary", {})
    training_validation = model_summary.get("training_validation", {})
    monitoring = model_summary.get("monitoring", {}) if isinstance(model_summary.get("monitoring"), dict) else {}
    monitoring_artifacts = (
        model_summary.get("monitoring_artifacts", {}) if isinstance(model_summary.get("monitoring_artifacts"), dict) else {}
    )
    multiomics_contexts = (
        model_summary.get("multiomics_contexts", {}) if isinstance(model_summary.get("multiomics_contexts"), dict) else {}
    )

    overall_labels = label_distribution.get("overall", label_distribution)
    overall_counts = overall_labels.get("counts", {}) if isinstance(overall_labels, dict) else {}
    holdout = validation_metrics.get("holdout", {}) if isinstance(validation_metrics, dict) else {}
    cross_validation = validation_metrics.get("cross_validation", {}) if isinstance(validation_metrics, dict) else {}
    lines = [
        "",
        "Predictive model layer summary:",
        f"- Status: {status}",
        f"- Artifact family: {artifact_family}",
        f"- Predictive readiness: {readiness.get('status', 'not_evaluated')}",
        f"- Artifact kind: {readiness.get('artifact_kind') or model_summary.get('artifact_kind', 'unknown')}",
        f"- Can run supervised drug-response inference: {_bool_label(bool(readiness.get('can_run_inference', False)))}",
        f"- Summary: {model_summary.get('summary') or model_summary.get('reason') or 'None'}",
        f"- Model card: {model_card.get('name', 'Unknown')} | version {model_card.get('version', 'unknown')} | {model_card.get('algorithm', 'unspecified')}",
        f"- Architecture: {model_card.get('architecture', 'unspecified')}",
        f"- Input modalities: {', '.join(model_card.get('input_modalities', [])) or 'None'}",
        f"- Intended use: {model_card.get('intended_use', 'Exploratory secondary model assistance only')}",
        f"- Not for clinical use: {_bool_label(bool(model_card.get('not_for_clinical_use', True)))}",
        (
            f"- Training dataset: rows_total={dataset.get('rows_total', 0)}, rows_train={dataset.get('rows_train', 0)}, "
            f"rows_validation={dataset.get('rows_validation', 0)}, rows_test={dataset.get('rows_test', 0)}, "
            f"drugs={_format_mapping(dataset.get('drug_distribution', {}))}"
        ),
        f"- Label distribution: {_format_mapping(overall_counts)}",
        f"- Holdout metrics: {_format_mapping(holdout)}",
        (
            "- Cross-validation means: "
            + _format_mapping(
                {
                    key: value.get('mean')
                    for key, value in cross_validation.items()
                    if key != "n_splits" and isinstance(value, dict)
                }
            )
        ),
        f"- Calibration summary: {_format_mapping(calibration_summary)}",
        f"- Explainability artifacts: {', '.join(model_summary.get('explainability_artifacts', [])) or 'None'}",
        f"- Monitoring profile status: {model_summary.get('monitoring_profile_status', 'unknown')}",
    ]
    issues = list(training_validation.get("issues", [])) if isinstance(training_validation, dict) else []
    suspicious_columns = list(training_validation.get("suspicious_columns", [])) if isinstance(training_validation, dict) else []
    if suspicious_columns:
        lines.append(f"- Suspicious non-feature columns detected and excluded from modeling: {', '.join(suspicious_columns)}")
    if issues:
        lines.append(f"- Training validation issues: {'; '.join(issues)}")
    if monitoring:
        lines.append(f"- Monitoring status: {monitoring.get('status', 'unavailable')}")
        lines.append(
            "- Monitoring summary: "
            + _format_mapping(
                {
                    "total_predictions": monitoring.get("total_predictions", 0),
                    "modalities": _format_mapping(monitoring.get("modality_summary", {})),
                    "avg_confidence": monitoring.get("confidence_summary", {}).get("average_prediction_confidence"),
                    "high_uncertainty": monitoring.get("confidence_summary", {}).get("high_uncertainty_predictions"),
                }
            )
        )
        lines.append(f"- Monitoring drift summary: {_format_mapping(monitoring.get('drift_summary', {}))}")
        lines.append(
            f"- Monitoring dataset-quality summary: {_format_mapping(monitoring.get('dataset_quality_summary', {}))}"
        )
        monitoring_warnings = list(monitoring.get("warnings", []))
        if monitoring_warnings:
            lines.append(f"- Monitoring warnings: {'; '.join(monitoring_warnings)}")
        if monitoring_artifacts:
            lines.append(f"- Monitoring artifacts: {_format_mapping(monitoring_artifacts)}")
    if multiomics_contexts:
        lines.append("- Multi-omics contexts:")
        for drug, context in multiomics_contexts.items():
            if not isinstance(context, dict):
                continue
            lines.append(
                f"  {drug}: present={', '.join(context.get('present_modalities', [])) or 'None'} | "
                f"used={', '.join(context.get('prediction_enabled_modalities', [])) or 'None'} | "
                f"disabled={', '.join(context.get('disabled_modalities', [])) or 'None'} | "
                f"fusion_ready={context.get('fusion_ready', False)}"
            )
    lines.append("- UI handling: Evidence-backed PGx findings outrank model outputs; unvalidated or knowledge-support artifacts are blocked from predictive display.")
    return lines


def _model_summary_html(model_summary: dict[str, Any]) -> str:
    status = str(model_summary.get("status") or "disabled")
    if status == "disabled":
        return ""

    artifact_family = str(model_summary.get("artifact_family") or "classical_ml")
    readiness = model_summary.get("predictive_model_readiness", {})
    if not isinstance(readiness, dict):
        readiness = {}
    model_card = model_summary.get("model_card", {})
    dataset = model_summary.get("training_dataset_summary", {})
    label_distribution = model_summary.get("label_distribution_summary", {})
    validation_metrics = model_summary.get("validation_metrics", {})
    calibration_summary = model_summary.get("calibration_summary", {})
    training_validation = model_summary.get("training_validation", {})
    monitoring = model_summary.get("monitoring", {}) if isinstance(model_summary.get("monitoring"), dict) else {}
    monitoring_artifacts = (
        model_summary.get("monitoring_artifacts", {}) if isinstance(model_summary.get("monitoring_artifacts"), dict) else {}
    )
    multiomics_contexts = (
        model_summary.get("multiomics_contexts", {}) if isinstance(model_summary.get("multiomics_contexts"), dict) else {}
    )

    overall_labels = label_distribution.get("overall", label_distribution)
    overall_counts = overall_labels.get("counts", {}) if isinstance(overall_labels, dict) else {}
    holdout = validation_metrics.get("holdout", {}) if isinstance(validation_metrics, dict) else {}
    cross_validation = validation_metrics.get("cross_validation", {}) if isinstance(validation_metrics, dict) else {}
    cross_validation_means = {
        key: value.get("mean")
        for key, value in cross_validation.items()
        if key != "n_splits" and isinstance(value, dict)
    }
    suspicious_columns = (
        list(training_validation.get("suspicious_columns", [])) if isinstance(training_validation, dict) else []
    )
    issues = list(training_validation.get("issues", [])) if isinstance(training_validation, dict) else []
    monitoring_warnings = "".join(
        f"<li>{escape(str(item))}</li>" for item in monitoring.get("warnings", [])
    )
    multiomics_html = "".join(
        (
            f"<li><b>{escape(str(drug))}:</b> "
            f"present={escape(', '.join(context.get('present_modalities', [])) or 'None')} | "
            f"used={escape(', '.join(context.get('prediction_enabled_modalities', [])) or 'None')} | "
            f"disabled={escape(', '.join(context.get('disabled_modalities', [])) or 'None')} | "
            f"fusion_ready={escape(str(context.get('fusion_ready', False)))}</li>"
        )
        for drug, context in multiomics_contexts.items()
        if isinstance(context, dict)
    )
    display_requirements = "".join(
        f"<li>{escape(str(item))}</li>" for item in model_card.get("ui_display_requirements", [])
    )

    return f"""
    <section>
      <h2>Predictive Model Layer Summary</h2>
      <p><b>Status:</b> {escape(status)}</p>
      <p><b>Artifact family:</b> {escape(artifact_family)}</p>
      <p><b>Predictive readiness:</b> {escape(str(readiness.get('status', 'not_evaluated')))}</p>
      <p><b>Artifact kind:</b> {escape(str(readiness.get('artifact_kind') or model_summary.get('artifact_kind', 'unknown')))}</p>
      <p><b>Can run supervised drug-response inference:</b> {escape(_bool_label(bool(readiness.get('can_run_inference', False))))}</p>
      <p><b>Summary:</b> {escape(str(model_summary.get('summary') or model_summary.get('reason') or 'None'))}</p>
      <p><b>Model card:</b> {escape(str(model_card.get('name', 'Unknown')))} | version {escape(str(model_card.get('version', 'unknown')))} | {escape(str(model_card.get('algorithm', 'unspecified')))}</p>
      <p><b>Architecture:</b> {escape(str(model_card.get('architecture', 'unspecified')))}</p>
      <p><b>Input modalities:</b> {escape(', '.join(model_card.get('input_modalities', [])) or 'None')}</p>
      <p><b>Intended use:</b> {escape(str(model_card.get('intended_use', 'Exploratory secondary model assistance only')))}</p>
      <p><b>Not for clinical use:</b> {escape(_bool_label(bool(model_card.get('not_for_clinical_use', True))))}</p>
      <p><b>Training dataset:</b> rows_total={escape(str(dataset.get('rows_total', 0)))}, rows_train={escape(str(dataset.get('rows_train', 0)))}, rows_validation={escape(str(dataset.get('rows_validation', 0)))}, rows_test={escape(str(dataset.get('rows_test', 0)))}, drugs={escape(_format_mapping(dataset.get('drug_distribution', {})))}</p>
      <p><b>Label distribution:</b> {escape(_format_mapping(overall_counts))}</p>
      <p><b>Holdout metrics:</b> {escape(_format_mapping(holdout))}</p>
      <p><b>Cross-validation means:</b> {escape(_format_mapping(cross_validation_means))}</p>
      <p><b>Calibration summary:</b> {escape(_format_mapping(calibration_summary))}</p>
      <p><b>Explainability artifacts:</b> {escape(', '.join(model_summary.get('explainability_artifacts', [])) or 'None')}</p>
      <p><b>Monitoring profile status:</b> {escape(str(model_summary.get('monitoring_profile_status', 'unknown')))}</p>
      <p><b>Monitoring status:</b> {escape(str(monitoring.get('status', 'unavailable')))}</p>
      <p><b>Monitoring summary:</b> total_predictions={escape(str(monitoring.get('total_predictions', 0)))}, modalities={escape(_format_mapping(monitoring.get('modality_summary', {})))}, confidence={escape(_format_mapping(monitoring.get('confidence_summary', {})))}</p>
      <p><b>Monitoring drift summary:</b> {escape(_format_mapping(monitoring.get('drift_summary', {})))}</p>
      <p><b>Monitoring dataset-quality summary:</b> {escape(_format_mapping(monitoring.get('dataset_quality_summary', {})))}</p>
      {f"<p><b>Monitoring artifacts:</b> {escape(_format_mapping(monitoring_artifacts))}</p>" if monitoring_artifacts else ""}
      <p><b>Suspicious non-feature columns excluded:</b> {escape(', '.join(suspicious_columns) or 'None')}</p>
      <p><b>Training validation issues:</b> {escape('; '.join(issues) or 'None')}</p>
      {'<h4>Monitoring Warnings</h4><ul>' + monitoring_warnings + '</ul>' if monitoring_warnings else ''}
      {'<h4>Multi-Omics Contexts</h4><ul>' + multiomics_html + '</ul>' if multiomics_html else ''}
      <h4>UI Display Requirements</h4>
      <ul>{display_requirements or '<li>Evidence-backed PGx findings outrank model outputs; unvalidated artifacts are blocked from predictive display.</li>'}</ul>
    </section>
    """


def _visible_pipeline_steps(result: AnalysisResult) -> list[Any]:
    steps = list(result.pipeline_summary.step_results)
    if result.model_summary.get("status") == "disabled":
        steps = [step for step in steps if step.key != "optional_ml_assistance"]
    return steps


def _response_efficiency_text(model_summary: dict[str, Any]) -> list[str]:
    summary = model_summary.get("response_efficiency")
    if not isinstance(summary, dict):
        return []
    lines = ["", "Response Efficiency / Probability Summary:"]
    lines.append(f"- Label type: {summary.get('label_type', 'insufficient labeled data')}")
    lines.append(f"- Evidence level: {summary.get('evidence_level', 'INSUFFICIENT_EVIDENCE')}")
    if summary.get("known_response_rate") is not None:
        lines.append(f"- Validated response rate from dataset: {summary['known_response_rate']}")
    if summary.get("predicted_response_probability") is not None:
        lines.append(f"- Model-predicted response probability: {summary['predicted_response_probability']}")
    if summary.get("predicted_toxicity_risk") is not None:
        lines.append(f"- Predicted toxicity risk: {summary['predicted_toxicity_risk']}")
    lines.append(f"- Explanation: {summary.get('explanation', 'No validated response estimate available.')}")
    for limitation in summary.get("limitations", []) or []:
        lines.append(f"- Limitation: {limitation}")
    return lines


def _response_efficiency_html(model_summary: dict[str, Any]) -> str:
    summary = model_summary.get("response_efficiency")
    if not isinstance(summary, dict):
        return ""
    rows = [
        ("Label type", summary.get("label_type", "insufficient labeled data")),
        ("Evidence level", summary.get("evidence_level", "INSUFFICIENT_EVIDENCE")),
        ("Validated response rate from dataset", summary.get("known_response_rate", "Not available")),
        ("Model-predicted response probability", summary.get("predicted_response_probability", "Not available")),
        ("Predicted toxicity risk", summary.get("predicted_toxicity_risk", "Not available")),
        ("Explanation", summary.get("explanation", "No validated response estimate available.")),
    ]
    limitations = "".join(f"<li>{escape(str(item))}</li>" for item in summary.get("limitations", []) or [])
    return (
        "<section><h2>Response Efficiency / Probability Summary</h2><ul>"
        + "".join(f"<li><b>{escape(str(label))}:</b> {escape(str(value))}</li>" for label, value in rows)
        + f"</ul><h4>Limitations</h4><ul>{limitations or '<li>None</li>'}</ul></section>"
    )


def render_text_report(result: AnalysisResult) -> str:
    """Render a human-readable DNA pharmacogenomics report."""
    if result.input_mode == "variant":
        input_heading = "Variant input summary:"
    else:
        input_heading = "Input summary:"
    input_label = _input_type_label(result.input_mode)
    target_drug_text = ", ".join(drug_display_label(drug) for drug in result.selected_drugs) or "not selected"
    target_support_tier = _selected_drug_support_tier(result.selected_drugs[0] if result.selected_drugs else None)
    current_medications = (
        ", ".join(result.patient_profile.current_medications)
        if result.patient_profile is not None and result.patient_profile.current_medications
        else "No concurrent medications provided"
    )
    lines = [
        f"{APP_NAME} {APP_VERSION}",
        f"Overall category: {result.overall_category}",
        f"Input type: {input_label}",
        f"Target drug context: {target_drug_text}",
        f"Target drug support tier: {target_support_tier}",
        f"Current medications: {current_medications}",
        f"Validated input: {result.validation.message}",
        (
            "Pipeline status: "
            f"{result.pipeline_summary.overall_status} | "
            f"{result.pipeline_summary.completed_steps} success | "
            f"{result.pipeline_summary.warning_steps} warning | "
            f"{result.pipeline_summary.failed_steps} failed | "
            f"{result.pipeline_summary.skipped_steps} skipped"
        ),
        "",
        input_heading,
        f"- {result.variant_summary}",
    ]
    lines.extend(_render_patient_profile_text(result))
    if result.confirmed_findings:
        lines.extend(_render_text_section("Confirmed Evidence-Backed PGx Findings", result.confirmed_findings))
    if result.predictive_model_suggestions:
        lines.extend(_render_text_section("Optional Exploratory Model Output", result.predictive_model_suggestions))
    if result.research_only_hypotheses:
        lines.extend(_render_text_section("Exploratory Research-Only Output", result.research_only_hypotheses))
    if result.safety_blocks:
        lines.extend(_render_text_section("Safety Blocks / Validation Messages", result.safety_blocks))
    lines.extend(_render_evidence_annotations_text(result.evidence_annotations))
    lines.extend(_render_aggregated_evidence_text(result.aggregated_evidence))
    lines.extend(_render_interactions_text(result.interaction_findings))
    lines.extend(_response_efficiency_text(result.model_summary))
    lines.extend(["", "Safety notes:"])
    for note in result.safety_notes:
        lines.append(f"- {note}")
    lines.extend(["", "Global limitations:"])
    for note in result.limitations:
        lines.append(f"- {note}")
    lines.extend(["", "Pipeline execution summary:"])
    for step in _visible_pipeline_steps(result):
        lines.append(f"- {step.order}. {step.label}: {step.status} | {step.message}")
    lines.extend(_model_summary_text(result.model_summary))
    lines.extend(["", REPORT_DISCLAIMER])
    return "\n".join(lines)


def render_html_report(result: AnalysisResult) -> str:
    """Render a clean HTML report for the UI."""
    validation_warnings = "".join(f"<li>{escape(item)}</li>" for item in result.validation.warnings)
    safety_html = "".join(f"<li>{escape(item)}</li>" for item in result.safety_notes)
    limitation_html = "".join(f"<li>{escape(item)}</li>" for item in result.limitations)
    if result.input_mode == "variant":
        input_summary_title = "Variant Input Summary"
    else:
        input_summary_title = "Input Summary"
    input_label = _input_type_label(result.input_mode)
    target_drug_text = ", ".join(drug_display_label(drug) for drug in result.selected_drugs) or "Not selected"
    target_support_tier = _selected_drug_support_tier(result.selected_drugs[0] if result.selected_drugs else None)
    current_medications = (
        ", ".join(result.patient_profile.current_medications)
        if result.patient_profile is not None and result.patient_profile.current_medications
        else "No concurrent medications provided"
    )
    return f"""
    <html>
      <head>
        <meta charset="utf-8" />
        <title>{escape(APP_NAME)} Report</title>
        <style>
          body {{ font-family: Segoe UI, sans-serif; margin: 24px; color: #0f172a; }}
          h1, h2, h3, h4 {{ color: #0b3d62; }}
          section {{ border: 1px solid #dbe5ef; border-radius: 10px; padding: 14px; margin: 16px 0; }}
          .panel {{ background: #f8fbff; border-left: 5px solid #0b3d62; padding: 12px; }}
        </style>
      </head>
      <body>
        <h1>{escape(APP_NAME)} Drug-Response Report</h1>
        <div class="panel">
          <p><b>Version:</b> {escape(APP_VERSION)}</p>
            <p><b>Overall category:</b> {escape(result.overall_category)}</p>
            <p><b>Input type:</b> {escape(input_label)}</p>
            <p><b>Target drug context:</b> {escape(target_drug_text)}</p>
            <p><b>Target drug support tier:</b> {escape(target_support_tier)}</p>
            <p><b>Current medications:</b> {escape(current_medications)}</p>
            <p><b>Validation:</b> {escape(result.validation.message)}</p>
            <p><b>Pipeline status:</b> {escape(result.pipeline_summary.overall_status)}</p>
          <p><b>Pipeline step counts:</b> success {result.pipeline_summary.completed_steps} | warning {result.pipeline_summary.warning_steps} | failed {result.pipeline_summary.failed_steps} | skipped {result.pipeline_summary.skipped_steps}</p>
        </div>
        <section>
          <h2>{escape(input_summary_title)}</h2>
          <pre>{escape(str(result.variant_summary))}</pre>
        </section>
        {_render_patient_profile_html(result)}
        <section>
          <h2>Input Validation Notes</h2>
          <ul>{validation_warnings or '<li>None</li>'}</ul>
        </section>
        {_render_html_section("Confirmed Evidence-Backed PGx Findings", result.confirmed_findings)}
        {_render_html_section("Optional Exploratory Model Output", result.predictive_model_suggestions)}
        {_render_html_section("Exploratory Research-Only Output", result.research_only_hypotheses)}
        {_render_html_section("Safety Blocks / Validation Messages", result.safety_blocks)}
        {_render_evidence_annotations_html(result.evidence_annotations)}
        {_render_aggregated_evidence_html(result.aggregated_evidence)}
        {_render_interactions_html(result.interaction_findings)}
        {_response_efficiency_html(result.model_summary)}
        <section>
          <h2>Safety Notes</h2>
          <ul>{safety_html or '<li>None</li>'}</ul>
        </section>
        <section>
          <h2>Global Limitations</h2>
          <ul>{limitation_html or '<li>None</li>'}</ul>
        </section>
        <section>
          <h2>Pipeline Execution Summary</h2>
          <ul>
            {''.join(f"<li>{escape(str(step.order))}. {escape(step.label)}: {escape(step.status)} | {escape(step.message)}</li>" for step in _visible_pipeline_steps(result)) or '<li>None</li>'}
          </ul>
        </section>
        {_model_summary_html(result.model_summary)}
        <section>
          <h2>Disclaimer</h2>
          <p>{escape(REPORT_DISCLAIMER)}</p>
        </section>
      </body>
    </html>
    """

# --- end merged module: src/reporting.py ---

# --- begin merged module: src/services/export_service.py ---
"""Export helpers for report payloads."""


import json
from pathlib import Path
from typing import Any



class ExportService:
    """Write prepared analysis payloads to disk in export-friendly formats."""

    default_filename = f"{EXPORT_BASENAME}.json"

    def build_payload(self, result: AnalysisResult) -> dict[str, Any]:
        if result.export_artifact is not None and result.export_artifact.payload:
            return result.export_artifact.payload
        return result.to_dict()

    def export_json(self, destination: Path, result: AnalysisResult) -> Path:
        destination.write_text(json.dumps(self.build_payload(result), indent=2), encoding="utf-8")
        return destination

# --- end merged module: src/services/export_service.py ---

# --- begin merged module: src/services/report_service.py ---
"""Presentation-oriented report helpers for the desktop app."""




class ReportService:
    """Adapt analysis results into UI-friendly view models."""

    def _display_summary(self, finding: DrugFinding) -> str:
        if finding.category == "MODEL_ASSISTED":
            return f"Model-assisted only: {finding.summary}"
        if finding.exploratory:
            return f"Exploratory only: {finding.summary}"
        return finding.summary

    def _display_recommendation(self, finding: DrugFinding) -> str:
        if finding.category == "MODEL_ASSISTED":
            return f"Do not present as clinical fact. {finding.recommendation}"
        return finding.recommendation

    def input_label(self, result: AnalysisResult) -> str:
        if result.input_mode == "variant":
            return "DNA variant input"
        return "invalid input"

    def findings_rows(self, findings: list[DrugFinding]) -> list[FindingTableRow]:
        return [
            FindingTableRow(
                drug=finding.drug,
                category=finding.category,
                gene=finding.gene,
                phenotype=finding.phenotype or "",
                summary=self._display_summary(finding),
                recommendation=self._display_recommendation(finding),
            )
            for finding in findings
        ]

    def build_summary_line(self, result: AnalysisResult) -> str:
        pipeline = result.pipeline_summary
        target_drug_text = ", ".join(drug_display_label(drug) for drug in result.selected_drugs) or "Choose target drug"
        summary = (
            f"Overall output category: {result.overall_category} | "
            f"Target drug: {target_drug_text} | "
            f"Input type: {self.input_label(result)} | "
            f"Pipeline: {pipeline.overall_status} "
            f"({pipeline.completed_steps} success, {pipeline.warning_steps} warning, {pipeline.skipped_steps} skipped)"
        )
        if result.clinical_fields_used:
            summary += f" | Clinical context: {len(result.clinical_fields_used)} field(s)"
        if result.interaction_findings:
            summary += f" | Interaction findings: {len(result.interaction_findings)}"
        model_status = result.model_summary.get("status")
        if model_status == "exploratory_predictions_available":
            summary += " | Model output: supervised predictive layer available"
        elif model_status == "suppressed_due_to_evidence_precedence":
            summary += " | Model output: suppressed by evidence precedence"
        elif model_status == "not_predictive_drug_response_model":
            summary += " | Model output: blocked, not a patient-response model"
        return summary

    def build_view_model(self, result: AnalysisResult) -> AnalysisViewModel:
        return AnalysisViewModel(
            input_label=self.input_label(result),
            summary_line=self.build_summary_line(result),
            findings_rows=self.findings_rows(result.findings),
            report_html=result.report_html,
            report_text=result.report_text,
            pipeline_status=result.pipeline_summary.overall_status,
            can_export=result.pipeline_summary.can_export,
        )

# --- end merged module: src/services/report_service.py ---

# --- begin merged module: src/analysis_pipeline.py ---
"""Structured pharmacogenomics analysis pipeline with explicit step contracts."""


from typing import Any



class PipelineStep:
    """Base class for pipeline steps with a shared output contract."""

    order: int = 0
    key: str = ""
    label: str = ""

    def run(self, state: AnalysisPipelineState) -> PipelineStepResult:
        raise NotImplementedError

    def _result(
        self,
        status: str,
        message: str,
        *,
        metadata: dict[str, Any] | None = None,
        warnings: list[str] | None = None,
        errors: list[str] | None = None,
    ) -> PipelineStepResult:
        return PipelineStepResult(
            order=self.order,
            key=self.key,
            label=self.label,
            status=status,
            message=message,
            metadata=metadata or {},
            warnings=warnings or [],
            errors=errors or [],
        )


def _build_validation_guard_finding(message: str) -> DrugFinding:
    return DrugFinding(
        drug="Input validation",
        gene="N/A",
        category="INSUFFICIENT_EVIDENCE",
        result_kind="SAFETY_BLOCK",
        summary=message,
        recommendation="Provide a supported DNA VCF or pharmacogene variant table.",
        confidence=ConfidenceAssessment(
            category="INSUFFICIENT_EVIDENCE",
            evidence_strength="none",
            data_completeness="insufficient",
            rationale=[message],
        ),
        source_module="src.analysis_pipeline",
        evidence_type="input_validation_guard",
        clinical_grade=False,
        exploratory=False,
        provenance=[
            EvidenceRecord(
                source=f"{APP_NAME} pipeline",
                label="Input validation",
                assertion=message,
                source_module="src.analysis_pipeline",
                evidence_type="input_validation_guard",
            )
        ],
        safety_notes=["No downstream pharmacogenomics analysis was run because validation failed."],
        limitations=["The input did not meet the file validation requirements."],
    )
def _build_unsupported_drug_finding(unsupported_drugs: list[str]) -> DrugFinding:
    supported = ", ".join(drug_display_label(drug) for drug in sorted(DRUG_GENE_RULES))
    message = "Unsupported drug selection: " + ", ".join(sorted(unsupported_drugs))
    return DrugFinding(
        drug="Drug selection",
        gene="N/A",
        category="INSUFFICIENT_EVIDENCE",
        result_kind="SAFETY_BLOCK",
        summary=message,
        recommendation=f"Choose one or more supported drugs: {supported}.",
        confidence=ConfidenceAssessment(
            category="INSUFFICIENT_EVIDENCE",
            evidence_strength="none",
            data_completeness="partial",
            rationale=[message],
        ),
        source_module="src.analysis_pipeline",
        evidence_type="drug_selection_guard",
        clinical_grade=False,
        exploratory=False,
        provenance=[
            EvidenceRecord(
                source=f"{APP_NAME} pipeline",
                label="Drug selection",
                assertion=message,
                source_module="src.analysis_pipeline",
                evidence_type="drug_selection_guard",
            )
        ],
        safety_notes=["Analysis was limited because one or more requested drugs are unsupported by the local PGx rule set."],
        limitations=["Only a small curated set of drugs is interpreted by the local application."],
    )


def _build_missing_drug_selection_finding() -> DrugFinding:
    supported = ", ".join(drug_display_label(drug) for drug in sorted(DRUG_GENE_RULES))
    message = "No target drug was selected for pharmacogenomics interpretation."
    return DrugFinding(
        drug="Drug selection",
        gene="N/A",
        category="INSUFFICIENT_EVIDENCE",
        result_kind="SAFETY_BLOCK",
        summary=message,
        recommendation=(
            "Choose one supported drug context before analysis so the app can apply drug-specific PGx rules: "
            f"{supported}."
        ),
        confidence=ConfidenceAssessment(
            category="INSUFFICIENT_EVIDENCE",
            evidence_strength="none",
            data_completeness="partial",
            rationale=[
                message,
                "The app does not infer the clinically relevant drug context automatically from a variant file alone.",
            ],
        ),
        source_module="src.analysis_pipeline",
        evidence_type="drug_selection_required",
        clinical_grade=False,
        exploratory=False,
        provenance=[
            EvidenceRecord(
                source=APP_NAME,
                label="Drug selection guard",
                assertion=message,
                source_module="src.analysis_pipeline",
                evidence_type="drug_selection_required",
                details={"supported_drugs": sorted(DRUG_GENE_RULES)},
            )
        ],
        safety_notes=[
            "Drug-specific interpretation is intentionally blocked until a target drug is selected.",
        ],
        limitations=[
            "The local app interprets only a limited curated set of drugs and does not infer which medication is clinically relevant for a sample.",
        ],
    )


def _build_general_pharmacology_only_finding(selected_drugs: list[str]) -> DrugFinding:
    labels = ", ".join(drug_display_label(drug) for drug in selected_drugs)
    message = (
        f"Target drug context {labels} is available only as local general pharmacology metadata; "
        "no evidence-backed pharmacogenomics rule is shipped for this drug."
    )
    return DrugFinding(
        drug=labels or "Drug selection",
        gene="N/A",
        category="INSUFFICIENT_EVIDENCE",
        result_kind="SAFETY_BLOCK",
        summary=message,
        recommendation=(
            "General pharmacology context can still be preserved for reporting and interaction checks, "
            "but Pharmexia will not fabricate a drug-specific PGx interpretation."
        ),
        confidence=ConfidenceAssessment(
            category="INSUFFICIENT_EVIDENCE",
            evidence_strength="limited",
            data_completeness="partial",
            rationale=[
                message,
                "The selected target drug does not have a local evidence-backed PGx rule in this build.",
            ],
        ),
        source_module="src.analysis_pipeline",
        evidence_type="general_pharmacology_only_context",
        clinical_grade=False,
        exploratory=False,
        provenance=[
            EvidenceRecord(
                source=APP_NAME,
                label="General pharmacology target-drug context",
                assertion=message,
                source_module="src.analysis_pipeline",
                evidence_type="general_pharmacology_only_context",
                details={"selected_drugs": list(selected_drugs)},
            )
        ],
        safety_notes=[
            "General-pharmacology target-drug context is reported separately from evidence-backed PGx interpretation.",
        ],
        limitations=[
            "This build does not claim universal FDA-approved drug PGx coverage.",
            "Only the local curated PGx subset can produce evidence-backed drug-response findings.",
        ],
    )


def _build_model_finding(drug: str, prediction: dict[str, Any]) -> DrugFinding:
    predicted_label = str(prediction.get("predicted_label") or "unavailable")
    calibrated_probability_estimate = prediction.get("calibrated_probability_estimate")
    model_name = str(prediction.get("model_name") or "exploratory_model")
    source_module = str(prediction.get("source_module") or "src.ml_pipeline")
    artifact_family = str(prediction.get("artifact_family") or "classical_ml")
    model_descriptor = "deep-learning model" if artifact_family == "deep_learning" else "classical ML model"
    input_modalities = list(prediction.get("input_modalities") or [])
    monitoring = prediction.get("monitoring", {}) if isinstance(prediction.get("monitoring"), dict) else {}
    modality_text = f" Modalities used: {', '.join(input_modalities)}." if input_modalities else ""
    probability_text = (
        f" Calibrated model probability estimate for the predicted label: {calibrated_probability_estimate}."
        if calibrated_probability_estimate is not None
        else ""
    )
    uncertainty_level = str(prediction.get("uncertainty_level") or "unknown")
    monitoring_status = str(monitoring.get("status") or monitoring.get("reliability_status") or "")
    monitoring_warning = ""
    if monitoring_status == "warning":
        warning_items = list(monitoring.get("warnings", []))
        monitoring_warning = (
            f" Monitoring warning: {warning_items[0]}"
            if warning_items
            else " Monitoring warning: inference input differed from the training-time monitoring baseline."
        )
    summary = (
        f"Supervised model-assisted output from {model_name} for {drug} suggested '{predicted_label}', but no "
        f"authoritative local PGx rule confirmed an evidence-backed pharmacogenomics finding for this input.{probability_text}"
        f" Uncertainty level: {uncertainty_level}.{modality_text}{monitoring_warning} "
        f"{str(prediction.get('summary') or '').strip()}"
    ).strip()
    explanation = prediction.get("explanation")
    confidence_rationale = [
        "The artifact passed the patient-response readiness gate, so supervised model output can be shown as secondary prediction context.",
        "No evidence-based local PGx rule fired for this drug; evidence-based findings would override this model output.",
        "Calibrated model probabilities are model estimates, not clinical confidence measures.",
    ]
    if monitoring_status == "warning":
        confidence_rationale.append(
            "Monitoring detected input-distribution or dataset-quality warnings, so this exploratory output requires extra caution."
        )
    limitations = [
        "Model-assisted output is not authoritative PGx evidence.",
        "Model assistance cannot establish phenotype, functional impact, or therapy recommendations without authoritative evidence.",
        "Patient-response model artifacts require independent external validation before clinical use.",
        "Sequence-based model support requires explicit sequence-context input; the app does not infer raw-sequence clinical claims automatically.",
    ]
    if monitoring_status == "warning":
        limitations.append("Monitoring flagged inference-time drift or dataset-quality concerns relative to the stored training baseline.")
    return DrugFinding(
        drug=drug,
        gene="model",
        category="MODEL_ASSISTED",
        result_kind="PREDICTIVE_MODEL_SUGGESTION",
        summary=summary,
        recommendation=(
            "Model-assisted output only. Do not treat this as a clinical recommendation, phenotype call, or "
            "therapy directive. Review authoritative PGx evidence manually."
        ),
        confidence=ConfidenceAssessment(
            category="MODEL_ASSISTED",
            evidence_strength="exploratory",
            data_completeness="partial",
            rationale=confidence_rationale,
        ),
        source_module=source_module,
        evidence_type="supervised_deep_learning_support" if artifact_family == "deep_learning" else "supervised_model_support",
        clinical_grade=False,
        exploratory=True,
        explanation=explanation if isinstance(explanation, dict) else None,
        provenance=[
            EvidenceRecord(
                source=f"{APP_NAME} supervised {model_descriptor}",
                label=drug,
                assertion=f"Supervised {model_descriptor} output from {model_name}: {predicted_label}. Uncertainty: {uncertainty_level}.",
                source_module=source_module,
                evidence_type="supervised_deep_learning_support" if artifact_family == "deep_learning" else "supervised_model_support",
                details={
                    "model_name": model_name,
                    "artifact_family": artifact_family,
                    "input_modalities": input_modalities,
                    "top_features": prediction.get("top_features", []),
                    "top_tokens": prediction.get("top_tokens", []),
                    "label_probabilities": prediction.get("label_probabilities", {}),
                    "calibrated_probability_estimate": prediction.get("calibrated_probability_estimate"),
                    "uncertainty_level": uncertainty_level,
                    "feature_provenance": prediction.get("feature_provenance", []),
                    "explanation": explanation if isinstance(explanation, dict) else {},
                    "explanations": prediction.get("explanations", {}),
                    "monitoring": monitoring,
                },
            )
        ],
        safety_notes=["Model-assisted output must not be used as a standalone clinical claim."],
        limitations=limitations,
    )


def _build_non_predictive_model_finding(drug: str, readiness: dict[str, Any]) -> DrugFinding:
    artifact_kind = str(readiness.get("artifact_kind") or "unknown")
    model_name = str(readiness.get("model_name") or "attached_model")
    reason = str(readiness.get("reason") or "The attached model was not validated for patient drug-response prediction.")
    limitations = list(readiness.get("limitations") or [])
    if not limitations:
        limitations = ["No supervised patient-response prediction was generated from this artifact."]
    summary = (
        f"Model artifact '{model_name}' was not used as a drug-response predictor for {drug}. "
        f"Artifact kind: {artifact_kind}. {reason}"
    )
    return DrugFinding(
        drug=drug,
        gene="model",
        category="EXPLORATORY_ONLY",
        result_kind="MODEL_NOT_PREDICTIVE_DRUG_RESPONSE",
        summary=summary,
        recommendation=(
            "Attach a validated, labeled patient/sample-level drug-response model artifact before presenting "
            "ML output as prediction. Evidence-based PGx rules remain the primary interpretation layer."
        ),
        confidence=ConfidenceAssessment(
            category="EXPLORATORY_ONLY",
            evidence_strength="not_predictive_response_model",
            data_completeness="insufficient",
            rationale=[
                "Knowledge-support, legacy, or unvalidated artifacts are not supervised patient drug-response models.",
                "Pharmexia blocked drug-response inference rather than fabricating a predictive result.",
            ],
        ),
        source_module="src.services.predictive_model_service",
        evidence_type="predictive_model_readiness_gate",
        clinical_grade=False,
        exploratory=True,
        provenance=[
            EvidenceRecord(
                source=f"{APP_NAME} predictive model readiness gate",
                label=drug,
                assertion=reason,
                source_module="src.services.predictive_model_service",
                evidence_type="predictive_model_readiness_gate",
                details=dict(readiness),
            )
        ],
        safety_notes=["No model-based drug-response prediction was generated from the attached artifact."],
        limitations=limitations,
    )


def _resolve_selected_drugs(selected_drugs: list[str]) -> tuple[list[str], list[str]]:
    if not selected_drugs or not any(str(drug).strip() for drug in selected_drugs):
        return [], []

    service = _drug_database_service()
    resolved_entries, unresolved = service.normalize_many(selected_drugs)
    normalized = [entry.drug_key for entry in resolved_entries]
    unsupported = sorted({str(drug).strip().lower() for drug in unresolved if str(drug).strip()})
    return normalized, unsupported


def _pgx_supported_selected_drugs(selected_drugs: list[str]) -> list[str]:
    return [drug for drug in selected_drugs if drug in DRUG_GENE_RULES]


def _general_only_selected_drugs(selected_drugs: list[str]) -> list[str]:
    service = _drug_database_service()
    return [
        drug
        for drug in selected_drugs
        if service.support_tier_for(drug) == "GENERAL_PHARMACOLOGY_ONLY"
    ]


def _selected_drug_support_tier(drug: str | None) -> str:
    if not drug:
        return "UNSUPPORTED"
    return _drug_database_service().support_tier_for(drug)


def _current_medications_from_state(state: AnalysisPipelineState) -> list[str]:
    if state.patient_profile is None or not state.patient_profile.current_medications:
        return []
    return list(state.patient_profile.current_medications)


def _choose_overall_category(findings: list[DrugFinding]) -> str:
    if any(finding.category == "EVIDENCE_BASED" for finding in findings):
        return "EVIDENCE_BASED"
    if any(finding.category == "MODEL_ASSISTED" for finding in findings):
        return "MODEL_ASSISTED"
    if any(finding.category == "EXPLORATORY_ONLY" for finding in findings):
        return "EXPLORATORY_ONLY"
    return "INSUFFICIENT_EVIDENCE"


def _collect_safety_notes(findings: list[DrugFinding]) -> list[str]:
    notes = {note for finding in findings for note in finding.safety_notes}
    notes.add("Authoritative guideline evidence is never overridden by exploratory ML output.")
    notes.add("Negative or incomplete local results must not be treated as proof of normal pharmacogenomics status.")
    return sorted(notes)


def _collect_limitations(
    findings: list[DrugFinding],
    gene_assessments: dict[str, Any],
) -> list[str]:
    limitations = {
        "Only a curated subset of actionable pharmacogene loci is interpreted locally.",
        "Negative local results must not be treated as proof of normal genotype or absence of PGx risk.",
    }
    for finding in findings:
        limitations.update(finding.limitations)
    for assessment in gene_assessments.values():
        limitations.update(getattr(assessment, "limitations", []))
    return sorted(limitations)


def _prediction_drugs(state: AnalysisPipelineState) -> list[str]:
    return list(_pgx_supported_selected_drugs(state.resolved_selected_drugs))


def _refresh_aggregated_evidence(state: AnalysisPipelineState) -> None:
    prediction_drugs = _prediction_drugs(state)
    if not prediction_drugs:
        state.aggregated_evidence = []
        return
    service = EvidenceService(enable_remote_lookup=state.request.enable_remote_lookup)
    state.aggregated_evidence = service.aggregate_prediction_contexts(
        gene_assessments=state.gene_assessments,
        selected_drugs=prediction_drugs,
        model_findings=state.predictive_model_suggestions,
        variant_annotations=state.evidence_annotations,
    )


def _refresh_interaction_findings(state: AnalysisPipelineState) -> None:
    service = InteractionService()
    state.interaction_findings = service.aggregate_findings(
        requested_drugs=state.request.selected_drugs,
        resolved_drugs=state.resolved_selected_drugs,
        current_medications=_current_medications_from_state(state),
        gene_assessments=state.gene_assessments,
    )


def _collect_interaction_safety_notes(findings: list[DrugInteractionFinding]) -> list[str]:
    notes = [
        finding.summary
        for finding in findings
        if finding.severity in {"CONTRAINDICATED", "MAJOR", "MODERATE", "UNSUPPORTED", "UNKNOWN", "HIGH"}
    ]
    return list(OrderedDict.fromkeys(note for note in notes if note))


def _collect_interaction_limitations(findings: list[DrugInteractionFinding]) -> list[str]:
    return sorted({note for finding in findings for note in finding.limitations})


def _collect_sequence_context_for_drug(drug: str, variants: list[ObservedVariant]) -> str | None:
    genes = set(DRUG_GENE_RULES.get(drug, {}).get("genes", []))
    if not genes:
        return None
    contexts: list[str] = []
    for variant in variants:
        if variant.gene not in genes:
            continue
        for key in ("sequence_context", "sequence", "sequence_window", "context_sequence", "dna_sequence"):
            value = variant.info.get(key)
            if value:
                contexts.append(str(value))
                break
    if not contexts:
        return None
    return "NNN".join(contexts)


def _collect_clinical_metadata(
    variants: list[ObservedVariant],
    patient_profile: PatientClinicalProfile | None = None,
) -> dict[str, float]:
    metadata: dict[str, float] = {}
    for variant in variants:
        for key, value in variant.info.items():
            normalized_key = str(key).strip().lower()
            if not normalized_key.startswith("clinical_"):
                continue
            try:
                metadata[normalized_key] = float(value)
            except (TypeError, ValueError):
                continue
    profile_features = PatientContextService().model_feature_payload(patient_profile)
    metadata.update(profile_features)
    return metadata


def _load_dl_inference_helpers() -> dict[str, Any]:
    """Return a dict of no-op DL inference helpers.

    The deep-learning inference service is an optional external component.
    When it is not installed the pipeline skips DL inference gracefully.
    """
    def _is_dl_path(path: Any) -> bool:
        return False

    def _load_dl_artifact(path: Any) -> None:
        return None

    def _predict_dl(artifact: Any, **kwargs: Any) -> dict[str, Any]:
        return {"status": "unavailable", "reason": "Deep-learning inference service not available."}

    def _summarize_dl(artifact: Any) -> dict[str, Any]:
        return {"status": "unavailable"}

    return {
        "is_deep_learning_artifact_path": _is_dl_path,
        "load_dl_model_artifact": _load_dl_artifact,
        "predict_with_dl_model": _predict_dl,
        "summarize_dl_model_artifact": _summarize_dl,
    }


def _load_monitoring_service() -> Any:
    """Return a no-op monitoring service stub."""

    class _NoopMonitoringService:
        def audit_prediction(self, **kwargs: Any) -> Any:
            class _Rec:
                def to_dict(self) -> dict[str, Any]:
                    return {}
            return _Rec()

        def finalize_report(self, **kwargs: Any) -> dict[str, Any]:
            return {"report": {"status": "unavailable", "warnings": []}, "artifacts": {}}

    return _NoopMonitoringService()


def _load_multimodal_feature_service() -> Any:
    """Return a no-op multimodal feature service stub."""

    class _NoopMultimodalFeatureService:
        def build_prediction_container(
            self,
            *,
            dna_variant_features: dict[str, Any],
            patient_profile: Any = None,
            multiomics_inputs: Any = None,
            compatible_tabular_columns: list[str] | None = None,
            compatible_clinical_columns: list[str] | None = None,
        ) -> Any:
            class _Container:
                model_tabular_features: dict[str, Any] = {}
                model_clinical_features: dict[str, Any] = {}
                present_modalities: list[str] = []
                prediction_enabled_modalities: list[str] = []
                disabled_modalities: list[str] = []
                fusion_ready: bool = False

                def to_dict(self) -> dict[str, Any]:
                    return {
                        "model_tabular_features": {},
                        "model_clinical_features": {},
                        "present_modalities": [],
                        "prediction_enabled_modalities": [],
                        "disabled_modalities": [],
                        "fusion_ready": False,
                    }

            c = _Container()
            c.model_tabular_features = dict(dna_variant_features)
            return c

    return _NoopMultimodalFeatureService()


class InputValidationStep(PipelineStep):
    order = 1
    key = "input_validation"
    label = "Input Validation"

    def run(self, state: AnalysisPipelineState) -> PipelineStepResult:
        request = state.request
        patient_service = PatientContextService()
        state.patient_profile, state.patient_profile_validation = patient_service.validate_profile(request.patient_profile)
        if state.patient_profile_validation is not None:
            state.clinical_fields_used = list(state.patient_profile_validation.used_fields)
            state.clinical_model_features_used = list(state.patient_profile_validation.model_feature_fields)
        patient_warnings = (
            list(state.patient_profile_validation.warnings)
            if state.patient_profile_validation is not None
            else []
        )
        if (
            state.patient_profile_validation is not None
            and not state.patient_profile_validation.is_valid
            and state.patient_profile_validation.status != "not_provided"
        ):
            # The profile failed validation — emit the message as a warning
            # so it is visible in the pipeline output, but do not halt the run.
            patient_warnings.append(state.patient_profile_validation.message)
        if request.path is None and not request.input_variants:
            message = "No input source was provided to the analysis pipeline."
            state.validation = FileValidationResult(False, "unknown", "invalid", message)
            state.safety_blocks = [_build_validation_guard_finding(message)]
            return self._result("failed", message, errors=[message])

        if request.path is None:
            state.validation = request.provided_validation or FileValidationResult(
                True,
                "payload",
                "variant",
                "In-memory variant payload accepted",
            )
            state.input_mode = state.validation.input_mode
            state.detected_format = state.validation.detected_format
            return self._result(
                "warning" if state.validation.warnings or patient_warnings else "success",
                state.validation.message,
                metadata={
                    "source": "in_memory_payload",
                    "n_variants": len(request.input_variants),
                    "clinical_fields_used": list(state.clinical_fields_used),
                    "clinical_model_features_used": list(state.clinical_model_features_used),
                },
                warnings=list(state.validation.warnings) + patient_warnings,
            )

        path = request.path
        if not path.exists():
            message = f"File not found: {path}"
            state.validation = FileValidationResult(False, "unknown", "invalid", message)
            state.safety_blocks = [_build_validation_guard_finding(message)]
            return self._result("failed", message, errors=[message])
        if path.stat().st_size == 0:
            message = f"Empty file: {path.name}"
            state.validation = FileValidationResult(False, "unknown", "invalid", message)
            state.safety_blocks = [_build_validation_guard_finding(message)]
            return self._result("failed", message, errors=[message])

        preliminary = validate_input_file(path)
        if not preliminary.is_valid:
            state.validation = preliminary
            state.safety_blocks = [_build_validation_guard_finding(preliminary.message)]
            return self._result("failed", preliminary.message, errors=[preliminary.message])

        state.validation = FileValidationResult(
            True,
            "pending_classification",
            "pending",
            f"Input file passed structural validation: {path.name}",
        )
        return self._result(
            "warning" if patient_warnings else "success",
            state.validation.message,
            metadata={
                "path": str(path),
                "size_bytes": path.stat().st_size,
                "clinical_fields_used": list(state.clinical_fields_used),
                "clinical_model_features_used": list(state.clinical_model_features_used),
            },
            warnings=patient_warnings,
        )


class FileTypeClassificationStep(PipelineStep):
    order = 2
    key = "file_type_classification"
    label = "File-Type Classification"

    def run(self, state: AnalysisPipelineState) -> PipelineStepResult:
        if state.request.path is None:
            state.detected_format = state.validation.detected_format if state.validation else "payload"
            state.input_mode = state.validation.input_mode if state.validation else "variant"
            return self._result(
                "warning" if state.validation and state.validation.warnings else "success",
                "Classified in-memory input as a variant payload.",
                metadata={"detected_format": state.detected_format, "input_mode": state.input_mode},
                warnings=list(state.validation.warnings if state.validation else []),
            )

        classified = validate_input_file(state.request.path)
        state.validation = classified
        state.detected_format = classified.detected_format
        state.input_mode = classified.input_mode
        if not classified.is_valid:
            state.safety_blocks = [_build_validation_guard_finding(classified.message)]
            return self._result("failed", classified.message, errors=[classified.message])
        return self._result(
            "warning" if classified.warnings else "success",
            classified.message,
            metadata={"detected_format": classified.detected_format, "input_mode": classified.input_mode},
            warnings=list(classified.warnings),
        )


class ExtractionStep(PipelineStep):
    order = 3
    key = "extraction"
    label = "Variant Extraction"

    def run(self, state: AnalysisPipelineState) -> PipelineStepResult:
        if state.request.path is None:
            state.extracted_variants = list(state.request.input_variants)
            state.variant_summary = summarize_variants(state.extracted_variants)
            return self._result(
                "success",
                "Loaded in-memory observed variants.",
                metadata={"n_variants": len(state.extracted_variants)},
            )

        try:
            state.extracted_variants = load_observed_variants(state.request.path)
        except Exception as exc:
            message = f"Variant extraction failed: {exc}"
            state.safety_blocks = [_build_validation_guard_finding(message)]
            return self._result("failed", message, errors=[str(exc)])

        state.variant_summary = summarize_variants(state.extracted_variants)
        return self._result(
            "success",
            "Extracted observed variants from the input.",
            metadata={"n_variants": len(state.extracted_variants)},
        )


class VariantNormalizationStep(PipelineStep):
    order = 4
    key = "variant_normalization"
    label = "Variant Normalization"

    def run(self, state: AnalysisPipelineState) -> PipelineStepResult:
        if state.input_mode != "variant":
            return self._result("skipped", "Variant normalization was skipped because the input is not variant-based.")

        state.normalized_variants = normalize_observed_variants(state.extracted_variants)
        state.variant_summary = summarize_variants(state.normalized_variants)
        return self._result(
            "success",
            "Normalized observed variants into the shared internal schema.",
            metadata={"n_variants": len(state.normalized_variants)},
        )


class PharmacogeneFilteringStep(PipelineStep):
    order = 5
    key = "pharmacogene_filtering"
    label = "Pharmacogene Filtering"

    def run(self, state: AnalysisPipelineState) -> PipelineStepResult:
        if state.input_mode != "variant":
            return self._result("skipped", "Pharmacogene filtering was skipped because the input is not variant-based.")

        state.pharmacogene_variants = filter_pharmacogene_variants(state.normalized_variants)
        state.variant_summary["n_pharmacogene_variants"] = len(state.pharmacogene_variants)
        status = "success" if state.pharmacogene_variants else "warning"
        message = (
            "Filtered normalized variants to the locally supported pharmacogene set."
            if state.pharmacogene_variants
            else "No locally supported pharmacogene variants were retained after filtering."
        )
        return self._result(
            status,
            message,
            metadata={"n_pharmacogene_variants": len(state.pharmacogene_variants)},
        )


class EvidenceAnnotationStep(PipelineStep):
    order = 6
    key = "evidence_annotation"
    label = "Evidence Annotation"

    def run(self, state: AnalysisPipelineState) -> PipelineStepResult:
        if state.input_mode != "variant":
            return self._result("skipped", "Evidence annotation was skipped because the input is not variant-based.")

        integrator = EvidenceIntegrator(enable_remote_lookup=state.request.enable_remote_lookup)
        state.evidence_annotations = annotate_variant_evidence(state.pharmacogene_variants, integrator)
        state.model_summary.setdefault("evidence_annotation", {})
        conflict_count = sum(len(annotation.conflicts) for annotation in state.evidence_annotations)
        available_count = sum(
            1 for annotation in state.evidence_annotations if annotation.availability_status == "available"
        )
        partial_count = sum(
            1 for annotation in state.evidence_annotations if annotation.availability_status == "partial"
        )
        effect_available_count = sum(
            1
            for annotation in state.evidence_annotations
            if annotation.variant_effect is not None and annotation.variant_effect.effect_type != "UNKNOWN_EFFECT"
        )
        status = "success" if state.evidence_annotations else "warning"
        message = (
            "Annotated retained pharmacogene variants against the local PGx evidence set."
            if state.evidence_annotations
            else "No retained variants matched the local PGx evidence annotation set."
        )
        return self._result(
            status,
            message,
            metadata={
                "n_evidence_annotations": len(state.evidence_annotations),
                "n_available_evidence_annotations": available_count,
                "n_partial_evidence_annotations": partial_count,
                "n_evidence_conflicts": conflict_count,
                "n_variant_effect_annotations": effect_available_count,
                "remote_lookup_enabled": state.request.enable_remote_lookup,
            },
        )


class DiplotypePhenotypeStep(PipelineStep):
    order = 7
    key = "diplotype_phenotype"
    label = "Diplotype / Star-Allele / Phenotype"

    def run(self, state: AnalysisPipelineState) -> PipelineStepResult:
        if state.input_mode != "variant":
            return self._result("skipped", "Diplotype and phenotype inference was skipped because the input is not variant-based.")

        state.gene_assessments = assess_pharmacogenes(state.pharmacogene_variants)
        matched_genes = [
            gene
            for gene, assessment in state.gene_assessments.items()
            if assessment.matched_alleles or assessment.observed_target_loci
        ]
        status = "success" if matched_genes else "warning"
        message = (
            "Assessed retained pharmacogene variants for limited local star-allele and phenotype support."
            if matched_genes
            else "No retained pharmacogene variants supported a local diplotype or phenotype stage output."
        )
        return self._result(
            status,
            message,
            metadata={"genes_with_signal": matched_genes, "n_gene_assessments": len(state.gene_assessments)},
        )


class RuleBasedClinicalInterpretationStep(PipelineStep):
    order = 8
    key = "rule_based_interpretation"
    label = "Rule-Based Clinical Interpretation"

    def run(self, state: AnalysisPipelineState) -> PipelineStepResult:
        state.resolved_selected_drugs, state.unsupported_selected_drugs = _resolve_selected_drugs(
            state.request.selected_drugs
        )
        state.interaction_findings = []
        pgx_selected_drugs = _pgx_supported_selected_drugs(state.resolved_selected_drugs)
        general_only_selected_drugs = _general_only_selected_drugs(state.resolved_selected_drugs)
        warnings: list[str] = []
        if state.unsupported_selected_drugs:
            warnings.append("Unsupported selected drugs were skipped: " + ", ".join(state.unsupported_selected_drugs))

        if not state.request.selected_drugs:
            state.safety_blocks = [_build_missing_drug_selection_finding()]
            return self._result(
                "warning",
                "Rule-based interpretation was blocked until a target drug was selected.",
                metadata={"selected_drugs": [], "requires_target_drug": True},
            )

        if state.request.selected_drugs and not state.resolved_selected_drugs:
            state.safety_blocks = [_build_unsupported_drug_finding(state.unsupported_selected_drugs)]
            _refresh_interaction_findings(state)
            return self._result(
                "warning",
                "Rule-based interpretation produced only a drug-selection safety block.",
                metadata={
                    "unsupported_selected_drugs": state.unsupported_selected_drugs,
                    "n_interaction_findings": len(state.interaction_findings),
                },
                warnings=warnings,
            )

        if state.resolved_selected_drugs and not pgx_selected_drugs:
            if general_only_selected_drugs:
                state.safety_blocks = [_build_general_pharmacology_only_finding(general_only_selected_drugs)]
            else:
                state.safety_blocks = [_build_unsupported_drug_finding(state.resolved_selected_drugs)]
            _refresh_interaction_findings(state)
            return self._result(
                "warning",
                "Target drug context was preserved for interaction/general-pharmacology reporting, but no evidence-backed PGx rule was available.",
                metadata={
                    "selected_drugs": state.resolved_selected_drugs,
                    "general_only_selected_drugs": general_only_selected_drugs,
                    "n_interaction_findings": len(state.interaction_findings),
                },
                warnings=warnings,
            )

        evidence = EvidenceIntegrator(enable_remote_lookup=state.request.enable_remote_lookup)
        state.rule_findings = interpret_drug_rules(
            state.gene_assessments,
            pgx_selected_drugs,
            evidence,
        )
        state.confirmed_findings = [
            finding for finding in state.rule_findings if finding.result_kind == "CONFIRMED_PGX_FINDING"
        ]
        state.safety_blocks.extend(
            finding for finding in state.rule_findings if finding.result_kind == "SAFETY_BLOCK"
        )
        _refresh_aggregated_evidence(state)
        _refresh_interaction_findings(state)

        # If the interaction catalog is missing, make that visible in the output
        # rather than silently returning zero interaction findings.
        catalog = load_interaction_catalog()
        if catalog.schema_version in {"missing", "error"}:
            from dataclasses import replace as _r
            state.interaction_findings.insert(
                0,
                DrugInteractionFinding(
                    interaction_id="catalog_missing::schema",
                    interaction_type="unsupported_drug",
                    subject_drug="interaction_catalog",
                    interacting_entity="local_catalog",
                    entity_type="catalog",
                    severity="UNKNOWN",
                    status="unsupported",
                    evidence_category="INSUFFICIENT_EVIDENCE",
                    confidence="none",
                    summary=(
                        "The local drug interaction schema file was not found or could not be loaded. "
                        "Drug-drug and drug-gene interaction checking is unavailable for this run."
                    ),
                    clinical_relevance=(
                        "Absence of interaction warnings must NOT be interpreted as absence of interaction risk."
                    ),
                    mechanism="missing_catalog_file",
                    evidence_based=False,
                    provenance=[
                        InteractionProvenance(
                            source_name=APP_NAME,
                            source_record_id="catalog_missing",
                            evidence_type="catalog_availability_guard",
                            source_module="src.analysis_pipeline",
                            note="Interaction schema was missing at runtime.",
                        )
                    ],
                    limitations=list(catalog.limitations),
                ),
            )

        status = "success" if state.confirmed_findings else "warning"
        message = (
            "Generated rule-based pharmacogenomics findings from curated local evidence."
            if state.confirmed_findings
            else "Rule-based interpretation did not produce a confirmed evidence-backed PGx finding."
        )
        return self._result(
            status,
            message,
            metadata={
                "n_confirmed_findings": len(state.confirmed_findings),
                "n_safety_blocks": len(state.safety_blocks),
                "selected_drugs": state.resolved_selected_drugs,
                "n_aggregated_evidence_contexts": len(state.aggregated_evidence),
                "n_interaction_findings": len(state.interaction_findings),
            },
            warnings=warnings,
        )


class OptionalMLAssistanceStep(PipelineStep):
    order = 9
    key = "optional_ml_assistance"
    label = "Optional Model Assistance"

    def run(self, state: AnalysisPipelineState) -> PipelineStepResult:
        if state.input_mode != "variant":
            state.model_summary = {
                "status": "disabled",
                "reason": "Exploratory model assistance is only available for variant-based input.",
            }
            return self._result("skipped", "Optional model assistance was skipped because the input is not variant-based.")

        if not _prediction_drugs(state):
            state.model_summary = {
                "status": "disabled",
                "reason": "Optional model assistance requires a target drug with local evidence-backed PGx support.",
            }
            return self._result("skipped", state.model_summary["reason"])

        if state.request.model_artifact_path is None:
            state.model_summary = {
                "status": "disabled",
                "reason": "No exploratory model artifact was configured for this analysis run.",
            }
            return self._result("skipped", "Optional model assistance was skipped because no model artifact was requested.")

        prediction_drugs = _prediction_drugs(state)
        if not prediction_drugs:
            state.model_summary = {
                "status": "disabled",
                "reason": "Optional model assistance was not run because no supported drug context remained after validation.",
            }
            return self._result("skipped", state.model_summary["reason"])

        artifact_path = state.request.model_artifact_path
        monitoring_service = _load_monitoring_service()
        multimodal_feature_service = _load_multimodal_feature_service()
        dl_helpers = _load_dl_inference_helpers()

        # Inline PredictiveModelService readiness gate.
        class _PredictiveModelService:
            def evaluate_artifact(self, artifact: Any, *, artifact_family: str = "classical_ml") -> Any:
                class _Readiness:
                    can_run_inference = True
                    reason = ""
                    limitations: list[str] = []
                    artifact_kind = artifact_family

                    def to_dict(self) -> dict[str, Any]:
                        return {
                            "can_run_inference": self.can_run_inference,
                            "reason": self.reason,
                            "limitations": self.limitations,
                            "artifact_kind": self.artifact_kind,
                        }

                r = _Readiness()
                if not isinstance(artifact, dict):
                    r.can_run_inference = False
                    r.reason = "Artifact is not a valid dictionary."
                elif artifact.get("status") not in {None, "ready", "legacy_ready"}:
                    r.can_run_inference = False
                    r.reason = f"Artifact status '{artifact.get('status')}' is not ready for inference."
                elif "model" not in artifact:
                    r.can_run_inference = False
                    r.reason = "Artifact does not contain a fitted model object."
                return r

        predictive_model_service = _PredictiveModelService()
        if dl_helpers["is_deep_learning_artifact_path"](artifact_path):
            artifact = dl_helpers["load_dl_model_artifact"](artifact_path)
            if artifact is None:
                state.model_summary = {
                    "status": "unavailable",
                    "artifact_family": "deep_learning",
                    "reason": "No exploratory deep-learning artifact was found; rule-based interpretation remained primary.",
                }
                return self._result("warning", state.model_summary["reason"])

            artifact_summary = dl_helpers["summarize_dl_model_artifact"](artifact)
            readiness = predictive_model_service.evaluate_artifact(artifact, artifact_family="deep_learning")
            state.model_summary = artifact_summary

            if any(bundle.output_category == "EVIDENCE_BASED" for bundle in state.aggregated_evidence):
                state.model_summary = {
                    **artifact_summary,
                    "status": "suppressed_due_to_evidence_precedence",
                    "summary": "Exploratory deep-learning output was suppressed because evidence-backed PGx findings were available.",
                    "predictive_model_readiness": readiness.to_dict(),
                }
                return self._result("skipped", state.model_summary["summary"])

            if not readiness.can_run_inference:
                readiness_payload = readiness.to_dict()
                state.research_only_hypotheses.extend(
                    _build_non_predictive_model_finding(drug, readiness_payload) for drug in prediction_drugs
                )
                state.model_summary = {
                    **artifact_summary,
                    "status": "not_predictive_drug_response_model",
                    "summary": readiness.reason,
                    "predictive_model_readiness": readiness_payload,
                    "predictions": [],
                }
                return self._result(
                    "warning",
                    "Attached deep-learning artifact was not used for drug-response prediction.",
                    metadata={
                        "predictive_model_readiness": readiness_payload,
                        "n_research_only_hypotheses": len(state.research_only_hypotheses),
                    },
                    warnings=list(readiness.limitations),
                )

            if artifact_summary.get("status") != "ready":
                state.model_summary = {
                    **artifact_summary,
                    "predictive_model_readiness": readiness.to_dict(),
                }
                return self._result(
                    "warning",
                    str(artifact_summary.get("reason") or "Exploratory deep-learning artifact was not ready for inference."),
                )

            predictions: list[dict[str, Any]] = []
            monitoring_records: list[Any] = []
            base_clinical_metadata = _collect_clinical_metadata(
                state.pharmacogene_variants,
                state.patient_profile,
            )
            multiomics_contexts: dict[str, Any] = {}
            for drug in prediction_drugs:
                container = multimodal_feature_service.build_prediction_container(
                    dna_variant_features=build_pgx_feature_row(drug, state.gene_assessments),
                    patient_profile=state.patient_profile,
                    multiomics_inputs=state.request.multiomics_inputs,
                    compatible_tabular_columns=list(artifact.get("tabular_preprocessor", {}).get("columns", [])),
                    compatible_clinical_columns=list(artifact.get("clinical_preprocessor", {}).get("columns", [])),
                )
                multiomics_contexts[drug] = container.to_dict()
                tabular_features = dict(container.model_tabular_features)
                clinical_features = {**base_clinical_metadata, **dict(container.model_clinical_features)}
                sequence_context = _collect_sequence_context_for_drug(drug, state.pharmacogene_variants)
                variant_tokens = [
                    variant.token
                    for variant in state.pharmacogene_variants
                    if variant.gene in DRUG_GENE_RULES.get(drug, {}).get("genes", [])
                ]
                prediction = dl_helpers["predict_with_dl_model"](
                    artifact=artifact,
                    drug=drug,
                    tabular_features=tabular_features,
                    sequence_context=sequence_context,
                    clinical_features=clinical_features,
                    variant_tokens=variant_tokens,
                )
                if prediction.get("status") != "ready":
                    continue
                prediction["multiomics_context"] = container.to_dict()
                monitoring_record = monitoring_service.audit_prediction(
                    artifact=artifact,
                    artifact_family="deep_learning",
                    artifact_path=artifact_path,
                    drug=drug,
                    prediction=prediction,
                    input_modalities=list(prediction.get("input_modalities") or []),
                    tabular_features=tabular_features,
                    clinical_features=clinical_features,
                    sequence_context=sequence_context,
                )
                prediction["monitoring"] = monitoring_record.to_dict()
                monitoring_records.append(monitoring_record)
                predictions.append({"drug": drug, **prediction})
                state.predictive_model_suggestions.append(_build_model_finding(drug, prediction))

            state.multiomics_contexts = multiomics_contexts
            _refresh_aggregated_evidence(state)
            monitoring_bundle = monitoring_service.finalize_report(
                artifact=artifact,
                artifact_family="deep_learning",
                records=monitoring_records,
                artifact_path=artifact_path,
            )
            state.model_summary = {
                **artifact_summary,
                "status": "exploratory_predictions_available" if predictions else artifact_summary.get("status", "ready"),
                "predictions": predictions,
                "predictive_model_readiness": readiness.to_dict(),
                "monitoring": monitoring_bundle["report"],
                "monitoring_artifacts": monitoring_bundle["artifacts"],
                "multiomics_contexts": state.multiomics_contexts,
            }
            monitoring_warnings = list(dict.fromkeys(monitoring_bundle["report"].get("warnings", [])))
            return self._result(
                "warning",
                (
                    "Generated exploratory deep-learning suggestions because no evidence-backed PGx finding was available."
                    if state.predictive_model_suggestions
                    else "Exploratory deep-learning metadata were available, but no DL suggestion passed inference readiness checks."
                ),
                metadata={
                    "n_model_suggestions": len(state.predictive_model_suggestions),
                    "model_card_name": artifact_summary.get("model_card", {}).get("name"),
                    "artifact_family": "deep_learning",
                    "monitoring_status": monitoring_bundle["report"].get("status"),
                    "monitoring_json_report": monitoring_bundle["artifacts"].get("json_report"),
                    "multiomics_enabled_modalities": {
                        drug: context.get("prediction_enabled_modalities", [])
                        for drug, context in state.multiomics_contexts.items()
                    },
                },
                warnings=monitoring_warnings,
            )

        artifact = load_model_artifact(artifact_path)
        if artifact is None:
            state.model_summary = {
                "status": "unavailable",
                "artifact_family": "classical_ml",
                "reason": "No exploratory model artifact was found; rule-based interpretation remained primary.",
            }
            return self._result("warning", state.model_summary["reason"])

        artifact_summary = summarize_model_artifact(artifact)
        readiness = predictive_model_service.evaluate_artifact(artifact, artifact_family="classical_ml")
        state.model_summary = artifact_summary

        if any(bundle.output_category == "EVIDENCE_BASED" for bundle in state.aggregated_evidence):
            state.model_summary = {
                **artifact_summary,
                "status": "suppressed_due_to_evidence_precedence",
                "summary": "Exploratory model output was suppressed because evidence-backed PGx findings were available.",
                "predictive_model_readiness": readiness.to_dict(),
            }
            return self._result("skipped", state.model_summary["summary"])

        if not readiness.can_run_inference:
            readiness_payload = readiness.to_dict()
            state.research_only_hypotheses.extend(
                _build_non_predictive_model_finding(drug, readiness_payload) for drug in prediction_drugs
            )
            state.model_summary = {
                **artifact_summary,
                "status": "not_predictive_drug_response_model",
                "summary": readiness.reason,
                "predictive_model_readiness": readiness_payload,
                "predictions": [],
            }
            return self._result(
                "warning",
                "Attached model artifact was not used for drug-response prediction.",
                metadata={
                    "predictive_model_readiness": readiness_payload,
                    "n_research_only_hypotheses": len(state.research_only_hypotheses),
                },
                warnings=list(readiness.limitations),
            )

        if artifact_summary.get("status") not in {"ready", "legacy_ready"}:
            state.model_summary = {
                **artifact_summary,
                "predictive_model_readiness": readiness.to_dict(),
            }
            return self._result(
                "warning",
                str(artifact_summary.get("reason") or "Exploratory model artifact was not ready for inference."),
            )

        predictions: list[dict[str, Any]] = []
        monitoring_records: list[Any] = []
        multiomics_contexts: dict[str, Any] = {}
        for drug in prediction_drugs:
            container = multimodal_feature_service.build_prediction_container(
                dna_variant_features=build_pgx_feature_row(drug, state.gene_assessments),
                patient_profile=state.patient_profile,
                multiomics_inputs=state.request.multiomics_inputs,
                compatible_tabular_columns=list(artifact.get("feature_columns", [])),
                compatible_clinical_columns=[],
            )
            multiomics_contexts[drug] = container.to_dict()
            prediction = predict_with_model(
                drug,
                state.gene_assessments,
                artifact,
                feature_values=container.model_tabular_features,
            )
            if prediction.get("status") != "ready":
                continue
            prediction["multiomics_context"] = container.to_dict()
            monitoring_record = monitoring_service.audit_prediction(
                artifact=artifact,
                artifact_family="classical_ml",
                artifact_path=artifact_path,
                drug=drug,
                prediction=prediction,
                input_modalities=list(prediction.get("input_modalities") or []),
                tabular_features=dict(prediction.get("observed_feature_values", {})),
            )
            prediction["monitoring"] = monitoring_record.to_dict()
            monitoring_records.append(monitoring_record)
            predictions.append({"drug": drug, **prediction})
            state.predictive_model_suggestions.append(_build_model_finding(drug, prediction))
        state.multiomics_contexts = multiomics_contexts
        _refresh_aggregated_evidence(state)
        monitoring_bundle = monitoring_service.finalize_report(
            artifact=artifact,
            artifact_family="classical_ml",
            records=monitoring_records,
            artifact_path=artifact_path,
        )
        state.model_summary = {
            **artifact_summary,
            "status": "exploratory_predictions_available" if predictions else artifact_summary.get("status", "ready"),
            "predictions": predictions,
            "predictive_model_readiness": readiness.to_dict(),
            "monitoring": monitoring_bundle["report"],
            "monitoring_artifacts": monitoring_bundle["artifacts"],
            "multiomics_contexts": state.multiomics_contexts,
        }
        monitoring_warnings = list(dict.fromkeys(monitoring_bundle["report"].get("warnings", [])))
        return self._result(
            "warning",
            (
                "Generated exploratory model-assisted suggestions because no evidence-backed PGx finding was available."
                if state.predictive_model_suggestions
                else "Exploratory model metadata were available, but no model suggestion passed inference readiness checks."
            ),
            metadata={
                "n_model_suggestions": len(state.predictive_model_suggestions),
                "model_card_name": artifact_summary.get("model_card", {}).get("name"),
                "monitoring_status": monitoring_bundle["report"].get("status"),
                "monitoring_json_report": monitoring_bundle["artifacts"].get("json_report"),
                "multiomics_enabled_modalities": {
                    drug: context.get("prediction_enabled_modalities", [])
                    for drug, context in state.multiomics_contexts.items()
                },
            },
            warnings=monitoring_warnings,
        )


class ConfidenceAssignmentStep(PipelineStep):
    order = 10
    key = "confidence_assignment"
    label = "Confidence Assignment"

    def run(self, state: AnalysisPipelineState) -> PipelineStepResult:
        if state.resolved_selected_drugs and not state.aggregated_evidence:
            _refresh_aggregated_evidence(state)
        if (state.resolved_selected_drugs or state.unsupported_selected_drugs) and not state.interaction_findings:
            _refresh_interaction_findings(state)
        state.model_summary.setdefault(
            "target_drug_support_tier",
            _selected_drug_support_tier(state.resolved_selected_drugs[0] if state.resolved_selected_drugs else None),
        )
        state.model_summary.setdefault("current_medications", _current_medications_from_state(state))
        try:
            # Inline stub for ResponseEfficiencyService (optional real-world module).
            class _ResponseEfficiencyStub:
                def summarize(self, *, target_drug, confirmed_findings, model_suggestions, model_summary, aggregated_evidence):
                    class _Summary:
                        def to_dict(self) -> dict[str, Any]:
                            return {
                                "label_type": "insufficient labeled data",
                                "evidence_level": "INSUFFICIENT_EVIDENCE",
                                "explanation": "Response-efficiency summary not available in this build.",
                                "limitations": ["No validated response dataset was available."],
                            }
                    return _Summary()

            state.model_summary["response_efficiency"] = _ResponseEfficiencyStub().summarize(
                target_drug=state.resolved_selected_drugs[0] if state.resolved_selected_drugs else None,
                confirmed_findings=state.confirmed_findings,
                model_suggestions=state.predictive_model_suggestions,
                model_summary=state.model_summary,
                aggregated_evidence=state.aggregated_evidence,
            ).to_dict()
        except Exception as exc:
            state.model_summary["response_efficiency"] = {
                "label_type": "insufficient labeled data",
                "evidence_level": "INSUFFICIENT_EVIDENCE",
                "explanation": f"Response-efficiency summary was unavailable: {exc}",
                "limitations": ["No response probability or acceptance rate was inferred."],
            }
        state.findings = (
            list(state.confirmed_findings)
            + list(state.predictive_model_suggestions)
            + list(state.research_only_hypotheses)
            + list(state.safety_blocks)
        )
        if not state.findings:
            state.safety_blocks = [_build_validation_guard_finding("No supported analysis output was generated.")]
            state.findings = list(state.safety_blocks)

        state.overall_category = _choose_overall_category(state.findings)
        state.safety_notes = sorted(
            set(_collect_safety_notes(state.findings)).union(_collect_interaction_safety_notes(state.interaction_findings))
        )
        state.limitations = sorted(
            set(_collect_limitations(state.findings, state.gene_assessments)).union(
                _collect_interaction_limitations(state.interaction_findings)
            )
        )
        prediction_layer = {
            "final_priority": "evidence_based_rules_override_models",
            "confirmed_evidence_backed_findings": len(state.confirmed_findings),
            "supervised_model_predictions": len(state.predictive_model_suggestions),
            "research_only_or_blocked_model_outputs": len(state.research_only_hypotheses),
            "predictive_model_status": state.model_summary.get("status", "disabled"),
            "predictive_model_readiness": state.model_summary.get("predictive_model_readiness", {}),
        }
        state.model_summary = {
            **state.model_summary,
            "prediction_layer": prediction_layer,
        }

        status = "success" if state.confirmed_findings else "warning"
        return self._result(
            status,
            "Assigned confidence categories and assembled the final result buckets.",
            metadata={
                "overall_category": state.overall_category,
                "n_findings": len(state.findings),
                "n_confirmed_findings": len(state.confirmed_findings),
                "n_model_suggestions": len(state.predictive_model_suggestions),
                "n_research_only_hypotheses": len(state.research_only_hypotheses),
                "n_safety_blocks": len(state.safety_blocks),
                "n_aggregated_evidence_contexts": len(state.aggregated_evidence),
                "n_interaction_findings": len(state.interaction_findings),
            },
        )


class ReportGenerationStep(PipelineStep):
    order = 11
    key = "report_generation"
    label = "Report Generation"

    def run(self, state: AnalysisPipelineState) -> PipelineStepResult:
        placeholder_summary = PipelineExecutionSummary(
            overall_status="success",
            message="Pipeline execution summary will be finalized after all steps complete.",
            total_steps=12,
            completed_steps=0,
            warning_steps=0,
            failed_steps=0,
            skipped_steps=0,
            can_export=False,
        )
        provisional = _build_result_from_state(state, placeholder_summary)
        state.report_text = render_text_report(provisional)
        state.report_html = render_html_report(provisional)
        return self._result(
            "success",
            "Generated text and HTML reports from the current pipeline state.",
            metadata={"report_text_length": len(state.report_text), "report_html_length": len(state.report_html)},
        )


class ExportPreparationStep(PipelineStep):
    order = 12
    key = "export_preparation"
    label = "Export"

    def run(self, state: AnalysisPipelineState) -> PipelineStepResult:
        default_filename = f"{EXPORT_BASENAME}.json"
        state.export_artifact = ExportArtifact(
            filename=default_filename,
            media_type="application/json",
            payload={},
        )
        return self._result(
            "success",
            "Prepared an export bundle for UI or API delivery.",
            metadata={"filename": default_filename, "media_type": state.export_artifact.media_type},
        )


def _build_result_from_state(
    state: AnalysisPipelineState,
    pipeline_summary: PipelineExecutionSummary,
) -> AnalysisResult:
    validation = state.validation or FileValidationResult(False, "unknown", "invalid", "No validation result available.")
    findings = state.findings or (
        list(state.confirmed_findings)
        + list(state.predictive_model_suggestions)
        + list(state.research_only_hypotheses)
        + list(state.safety_blocks)
    )
    overall_category = state.overall_category if findings else "INSUFFICIENT_EVIDENCE"
    safety_notes = state.safety_notes or (_collect_safety_notes(findings) if findings else [])
    limitations = state.limitations or (
        _collect_limitations(findings, state.gene_assessments) if findings else []
    )
    return AnalysisResult(
        input_mode=state.input_mode,
        validation=validation,
        patient_profile=state.patient_profile,
        patient_profile_validation=state.patient_profile_validation,
        clinical_fields_used=list(state.clinical_fields_used),
        clinical_model_features_used=list(state.clinical_model_features_used),
        variant_summary=state.variant_summary,
        evidence_annotations=state.evidence_annotations,
        aggregated_evidence=state.aggregated_evidence,
        interaction_findings=state.interaction_findings,
        findings=findings,
        confirmed_findings=state.confirmed_findings,
        predictive_model_suggestions=state.predictive_model_suggestions,
        research_only_hypotheses=state.research_only_hypotheses,
        safety_blocks=state.safety_blocks,
        gene_assessments=state.gene_assessments,
        overall_category=overall_category,
        safety_notes=safety_notes,
        limitations=limitations,
        selected_drugs=list(state.resolved_selected_drugs),
        model_summary=state.model_summary,
        multiomics_contexts=state.multiomics_contexts,
        pipeline_summary=pipeline_summary,
        export_artifact=state.export_artifact,
        report_text=state.report_text,
        report_html=state.report_html,
    )


def _build_export_payload(result: AnalysisResult) -> dict[str, Any]:
    target_drug = result.selected_drugs[0] if result.selected_drugs else None
    target_support_tier = _selected_drug_support_tier(target_drug)
    current_medications = (
        list(result.patient_profile.current_medications)
        if result.patient_profile is not None and result.patient_profile.current_medications
        else []
    )
    return {
        "app_name": APP_NAME,
        "app_version": APP_VERSION,
        "input_mode": result.input_mode,
        "validation": result.validation.to_dict(),
        "patient_profile": result.patient_profile.to_dict() if result.patient_profile is not None else None,
        "patient_profile_validation": (
            result.patient_profile_validation.to_dict() if result.patient_profile_validation is not None else None
        ),
        "clinical_fields_used": list(result.clinical_fields_used),
        "clinical_model_features_used": list(result.clinical_model_features_used),
        "variant_summary": result.variant_summary,
        "target_drug": target_drug,
        "normalized_target_drug": target_drug,
        "selected_drugs": list(result.selected_drugs),
        "current_medications": current_medications,
        "support_tier": target_support_tier,
        "evidence_sources": sorted(
            {
                record.source_name
                for bundle in result.aggregated_evidence
                for record in bundle.records
                if getattr(record, "source_name", None)
            }
        ),
        "evidence_annotations": [annotation.to_dict() for annotation in result.evidence_annotations],
        "aggregated_evidence": [bundle.to_dict() for bundle in result.aggregated_evidence],
        "interaction_findings": [finding.to_dict() for finding in result.interaction_findings],
        "findings": [finding.to_dict() for finding in result.findings],
        "confirmed_findings": [finding.to_dict() for finding in result.confirmed_findings],
        "predictive_model_suggestions": [finding.to_dict() for finding in result.predictive_model_suggestions],
        "research_only_hypotheses": [finding.to_dict() for finding in result.research_only_hypotheses],
        "safety_blocks": [finding.to_dict() for finding in result.safety_blocks],
        "gene_assessments": {gene: assessment.to_dict() for gene, assessment in result.gene_assessments.items()},
        "overall_category": result.overall_category,
        "safety_notes": list(result.safety_notes),
        "limitations": list(result.limitations),
        "model_summary": dict(result.model_summary),
        "prediction_layer": dict(result.model_summary.get("prediction_layer", {})),
        "response_efficiency": dict(result.model_summary.get("response_efficiency", {})),
        "multiomics_contexts": dict(result.multiomics_contexts),
        "pipeline_summary": result.pipeline_summary.to_dict(),
        "report_text": result.report_text,
        "report_html": result.report_html,
    }


class PharmacogenomicsPipeline:
    """Run the shared PGx workflow as a stepwise, inspectable pipeline."""

    def __init__(self) -> None:
        self.steps: list[PipelineStep] = [
            InputValidationStep(),
            FileTypeClassificationStep(),
            ExtractionStep(),
            VariantNormalizationStep(),
            PharmacogeneFilteringStep(),
            EvidenceAnnotationStep(),
            DiplotypePhenotypeStep(),
            RuleBasedClinicalInterpretationStep(),
            OptionalMLAssistanceStep(),
            ConfidenceAssignmentStep(),
            ReportGenerationStep(),
            ExportPreparationStep(),
        ]

    def run(self, request: AnalysisPipelineRequest) -> AnalysisResult:
        state = AnalysisPipelineState(request=request)
        step_results: list[PipelineStepResult] = []
        halted = False

        for step in self.steps:
            if halted:
                step_results.append(
                    PipelineStepResult(
                        order=step.order,
                        key=step.key,
                        label=step.label,
                        status="skipped",
                        message="Skipped because an upstream pipeline step failed.",
                    )
                )
                continue

            try:
                result = step.run(state)
            except Exception as exc:
                message = f"{step.label} failed unexpectedly."
                if not state.safety_blocks:
                    state.safety_blocks = [_build_validation_guard_finding(f"{message} {exc}")]
                result = PipelineStepResult(
                    order=step.order,
                    key=step.key,
                    label=step.label,
                    status="failed",
                    message=message,
                    errors=[str(exc)],
                )
            step_results.append(result)
            if result.status == "failed":
                halted = True

        pipeline_summary = self._summarize(step_results, export_ready=state.export_artifact is not None and not halted)
        result = _build_result_from_state(state, pipeline_summary)
        result.report_text = render_text_report(result)
        result.report_html = render_html_report(result)
        if result.export_artifact is not None:
            result.export_artifact.payload = _build_export_payload(result)
        return result

    def _summarize(
        self,
        step_results: list[PipelineStepResult],
        *,
        export_ready: bool,
    ) -> PipelineExecutionSummary:
        completed_steps = sum(1 for step in step_results if step.status == "success")
        warning_steps = sum(1 for step in step_results if step.status == "warning")
        failed_steps = sum(1 for step in step_results if step.status == "failed")
        skipped_steps = sum(1 for step in step_results if step.status == "skipped")

        if failed_steps:
            overall_status = "failed"
            message = "Pipeline execution stopped because at least one required step failed."
        elif warning_steps:
            overall_status = "warning"
            message = "Pipeline execution completed with warnings or downgraded outputs."
        else:
            overall_status = "success"
            message = "Pipeline execution completed successfully."

        return PipelineExecutionSummary(
            overall_status=overall_status,
            message=message,
            step_results=step_results,
            total_steps=len(self.steps),
            completed_steps=completed_steps,
            warning_steps=warning_steps,
            failed_steps=failed_steps,
            skipped_steps=skipped_steps,
            can_export=export_ready,
        )

# --- end merged module: src/analysis_pipeline.py ---

# --- begin merged module: src/services/analysis_service.py ---
"""Shared service facade over the structured PGx analysis pipeline."""


from pathlib import Path



class AnalysisService:
    """Backend PGx pipeline used by the desktop app, API, and tests."""

    def __init__(self, pipeline: PharmacogenomicsPipeline | None = None) -> None:
        self.pipeline = pipeline or PharmacogenomicsPipeline()

    def analyze_file(
        self,
        path: Path,
        selected_drugs: list[str] | None = None,
        enable_remote_lookup: bool = False,
        model_artifact_path: Path | None = None,
        patient_profile: PatientClinicalProfile | dict[str, Any] | None = None,
        multiomics_inputs: dict[str, Any] | None = None,
    ) -> AnalysisResult:
        request = AnalysisPipelineRequest(
            path=path,
            selected_drugs=selected_drugs or [],
            enable_remote_lookup=enable_remote_lookup,
            model_artifact_path=model_artifact_path,
            patient_profile=patient_profile,
            multiomics_inputs=multiomics_inputs,
        )
        return self.pipeline.run(request)

    def analyze_variants(
        self,
        variants: list[ObservedVariant],
        validation: FileValidationResult | None = None,
        selected_drugs: list[str] | None = None,
        enable_remote_lookup: bool = False,
        model_artifact_path: Path | None = None,
        patient_profile: PatientClinicalProfile | dict[str, Any] | None = None,
        multiomics_inputs: dict[str, Any] | None = None,
    ) -> AnalysisResult:
        """Run the full local PGx interpretation pipeline on parsed variants."""
        request = AnalysisPipelineRequest(
            input_variants=variants,
            selected_drugs=selected_drugs or [],
            enable_remote_lookup=enable_remote_lookup,
            model_artifact_path=model_artifact_path,
            provided_validation=validation,
            patient_profile=patient_profile,
            multiomics_inputs=multiomics_inputs,
        )
        return self.pipeline.run(request)

# --- end merged module: src/services/analysis_service.py ---

# --- begin merged module: src/ui/controller.py ---
"""Thin controller that connects the Qt window to backend services."""


from pathlib import Path



class MainWindowController:
    """Coordinate UI events without embedding scientific logic in widgets."""

    def __init__(
        self,
        analysis_service: AnalysisService | None = None,
        report_service: ReportService | None = None,
        export_service: ExportService | None = None,
    ) -> None:
        self.analysis_service = analysis_service or AnalysisService()
        self.report_service = report_service or ReportService()
        self.export_service = export_service or ExportService()
        self.current_result: AnalysisResult | None = None
        self.current_view_model: AnalysisViewModel | None = None

    def analyze_path(self, path: Path) -> AnalysisViewModel:
        result = self.analysis_service.analyze_file(path)
        self.current_result = result
        self.current_view_model = self.report_service.build_view_model(result)
        return self.current_view_model

    def can_export(self) -> bool:
        return self.current_result is not None and self.current_view_model is not None and self.current_view_model.can_export

    def export_current_result(self, destination: Path) -> Path:
        if self.current_result is None:
            raise ValueError("No analysis result is available for export.")
        return self.export_service.export_json(destination, self.current_result)

# --- end merged module: src/ui/controller.py ---

# --- begin merged module: src/ui/report_views.py ---
"""Reusable Qt widgets for presenting PGx results.

PySide6 is an optional dependency.  When it is not installed the desktop UI
classes are replaced with no-op stubs so the rest of the module (analysis
pipeline, API, CLI) still loads and works normally.
"""

try:
    from PySide6.QtWidgets import QTableWidget, QTableWidgetItem, QTextBrowser
    _PYSIDE6_AVAILABLE = True
except ImportError:
    _PYSIDE6_AVAILABLE = False

if _PYSIDE6_AVAILABLE:
    class FindingsTable(QTableWidget):  # type: ignore[misc]
        """Table view for analysis findings."""

        def __init__(self) -> None:
            super().__init__(0, 6)
            self.setHorizontalHeaderLabels(
                [
                    "Drug / Context",
                    "Output Category",
                    "Pharmacogene / Context",
                    "Phenotype",
                    "Evidence Summary",
                    "Recommended Next Step",
                ]
            )

        def set_rows(self, rows: "list[FindingTableRow]") -> None:
            self.setRowCount(0)
            for row_index, row in enumerate(rows):
                self.insertRow(row_index)
                self.setItem(row_index, 0, QTableWidgetItem(row.drug))
                self.setItem(row_index, 1, QTableWidgetItem(row.category))
                self.setItem(row_index, 2, QTableWidgetItem(row.gene))
                self.setItem(row_index, 3, QTableWidgetItem(row.phenotype))
                self.setItem(row_index, 4, QTableWidgetItem(row.summary))
                self.setItem(row_index, 5, QTableWidgetItem(row.recommendation))
            self.resizeColumnsToContents()

    class ReportBrowser(QTextBrowser):  # type: ignore[misc]
        """HTML report surface."""

        def set_report_html(self, html: str) -> None:
            self.setHtml(html)

else:
    class FindingsTable:  # type: ignore[no-redef]
        """No-op stub used when PySide6 is not installed."""
        def __init__(self) -> None: pass
        def set_rows(self, rows: "list[FindingTableRow]") -> None: pass

    class ReportBrowser:  # type: ignore[no-redef]
        """No-op stub used when PySide6 is not installed."""
        def __init__(self) -> None: pass
        def set_report_html(self, html: str) -> None: pass

# --- end merged module: src/ui/report_views.py ---

# --- begin merged module: src/ui/main_window.py ---
"""Main PySide6 window for the Pharmexia desktop application.

PySide6 is optional.  When not installed the window class and launcher are
replaced with stubs that print a clear installation message instead of
crashing with an ImportError.
"""

import sys
from pathlib import Path

if _PYSIDE6_AVAILABLE:
    from PySide6.QtWidgets import (
        QApplication,
        QFileDialog,
        QHBoxLayout,
        QLabel,
        QLineEdit,
        QMainWindow,
        QMessageBox,
        QPushButton,
        QVBoxLayout,
        QWidget,
    )

    class PharmexiaMainWindow(QMainWindow):  # type: ignore[misc]
        """Thin Qt shell around the desktop controller and report views."""

        def __init__(
            self,
            service: "AnalysisService | None" = None,
            report_service: "ReportService | None" = None,
            export_service: "ExportService | None" = None,
        ) -> None:
            super().__init__()
            self.controller = MainWindowController(
                analysis_service=service,
                report_service=report_service,
                export_service=export_service,
            )
            self.current_path: "Path | None" = None
            self.setWindowTitle(DESKTOP_WINDOW_TITLE)
            self.resize(1200, 800)
            self._build_ui()

        def _build_ui(self) -> None:
            central = QWidget()
            layout = QVBoxLayout(central)

            top_row = QHBoxLayout()
            self.path_edit = QLineEdit()
            self.path_edit.setPlaceholderText("Choose a DNA VCF or pharmacogene variant table")
            browse_button = QPushButton("Browse")
            browse_button.clicked.connect(self.choose_file)
            analyze_button = QPushButton("Analyze Drug Response")
            analyze_button.clicked.connect(self.run_analysis)
            export_button = QPushButton("Export Report JSON")
            export_button.clicked.connect(self.export_json)
            top_row.addWidget(QLabel("DNA / Variant Input"))
            top_row.addWidget(self.path_edit, 1)
            top_row.addWidget(browse_button)
            top_row.addWidget(analyze_button)
            top_row.addWidget(export_button)
            layout.addLayout(top_row)

            self.summary_label = QLabel(
                "Load a DNA VCF or pharmacogene variant file to start drug-response analysis."
            )
            layout.addWidget(self.summary_label)

            self.findings_table = FindingsTable()
            layout.addWidget(self.findings_table)

            self.report_browser = ReportBrowser()
            layout.addWidget(self.report_browser, 1)
            self.setCentralWidget(central)

        def choose_file(self) -> None:
            path, _ = QFileDialog.getOpenFileName(
                self,
                "Open DNA / VCF Pharmacogenomics Input",
                str(Path.cwd()),
                "Supported Files (*.vcf *.vcf.gz *.csv *.tsv *.txt *.json)",
            )
            if path:
                self.current_path = Path(path)
                self.path_edit.setText(path)

        def run_analysis(self) -> None:
            raw_path = self.path_edit.text().strip()
            if not raw_path:
                QMessageBox.information(self, "Missing input", "Choose a supported file first.")
                return
            self.current_path = Path(raw_path)
            view_model = self.controller.analyze_path(self.current_path)
            self.summary_label.setText(view_model.summary_line)
            self.findings_table.set_rows(view_model.findings_rows)
            self.report_browser.set_report_html(view_model.report_html)

        def export_json(self) -> None:
            if not self.controller.can_export():
                QMessageBox.information(self, "No analysis", "Run drug-response analysis before exporting.")
                return
            path, _ = QFileDialog.getSaveFileName(
                self,
                "Export Drug-Response Report JSON",
                ExportService.default_filename,
                "JSON (*.json)",
            )
            if not path:
                return
            destination = self.controller.export_current_result(Path(path))
            QMessageBox.information(self, "Exported", f"Saved DNA pharmacogenomics report to {destination}")

    def launch_app(
        service: "AnalysisService | None" = None,
        report_service: "ReportService | None" = None,
        export_service: "ExportService | None" = None,
    ) -> int:
        """Launch the Pharmexia desktop application."""
        qt_app = QApplication.instance() or QApplication(sys.argv)
        window = PharmexiaMainWindow(
            service=service,
            report_service=report_service,
            export_service=export_service,
        )
        window.show()
        return qt_app.exec()

else:
    class PharmexiaMainWindow:  # type: ignore[no-redef]
        """Stub used when PySide6 is not installed."""
        def __init__(self, **kwargs: object) -> None: pass
        def show(self) -> None: pass

    def launch_app(  # type: ignore[misc]
        service: "AnalysisService | None" = None,
        report_service: "ReportService | None" = None,
        export_service: "ExportService | None" = None,
    ) -> int:
        print(
            "\nPharmexia desktop UI requires PySide6.\n"
            "Install it with:  pip install PySide6\n"
            "\nThe analysis pipeline and API are available without the UI.\n"
        )
        return 1

# --- end merged module: src/ui/main_window.py ---

# --- begin merged module: src/api.py ---
"""FastAPI surface for the shared PGx analysis service.

fastapi and pydantic are optional runtime dependencies.  When they are not
installed the module still loads and the desktop UI / analysis pipeline work
normally.  Only the HTTP API surface is unavailable, and ``app`` is set to
``None`` so that ``uvicorn oncox:app`` will fail with a clear message rather
than an ImportError at module load time.
"""


from typing import Any

try:
    from fastapi import FastAPI, HTTPException as _HTTPException
    import pandas as _pd_api
    from pydantic import BaseModel, Field
    _FASTAPI_AVAILABLE = True
except ImportError:
    _FASTAPI_AVAILABLE = False


if _FASTAPI_AVAILABLE:
    class VariantPayload(BaseModel):  # type: ignore[misc]
        chrom: str | None = None
        pos: int | None = None
        ref: str | None = None
        alt: str | None = None
        rsid: str | None = None
        genotype: str
        gene: str | None = None
        sample_id: str | None = None

    class AnalysisRequest(BaseModel):  # type: ignore[misc]
        variants: list[VariantPayload]
        selected_drugs: list[str] = Field(default_factory=list)
        target_drug: str | None = None
        current_medications: list[str] = Field(default_factory=list)
        patient_profile: dict[str, Any] | None = None
        enable_remote_lookup: bool = False

    def create_fastapi_app(service: "AnalysisService | None" = None) -> "FastAPI":
        analysis_service = service or AnalysisService()
        api = FastAPI(title=API_TITLE, version=APP_VERSION)

        @api.get("/health")
        def health() -> dict[str, str]:
            return {"status": "ok", "app_name": APP_NAME, "version": APP_VERSION}

        @api.post("/analyze/variants")
        def analyze_variants(request: AnalysisRequest) -> dict[str, Any]:
            frame = request.model_dump()
            try:
                variants_frame = normalize_variant_dataframe(_pd_api.DataFrame(frame["variants"]))
                variants = dataframe_to_observed_variants(variants_frame)
            except Exception as exc:
                raise _HTTPException(
                    status_code=400,
                    detail=f"Variant payload could not be normalized: {exc}",
                ) from exc

            selected_drugs = list(frame.get("selected_drugs") or [])
            target_drug = str(frame.get("target_drug") or "").strip()
            if target_drug and target_drug not in selected_drugs:
                selected_drugs = [target_drug, *selected_drugs]

            patient_profile = dict(frame.get("patient_profile") or {})
            current_medications = list(frame.get("current_medications") or [])
            if current_medications and "current_medications" not in patient_profile:
                patient_profile["current_medications"] = current_medications

            result = analysis_service.analyze_variants(
                variants=variants,
                selected_drugs=selected_drugs,
                patient_profile=patient_profile or None,
                enable_remote_lookup=bool(frame.get("enable_remote_lookup")),
            )
            return _build_export_payload(result)

        return api

    _api_service = AnalysisService()
    app: "FastAPI | None" = create_fastapi_app(_api_service)

else:
    # fastapi / pydantic not installed — provide safe stubs so that
    # ``import oncox; oncox.app`` doesn't raise NameError.
    def create_fastapi_app(service: "AnalysisService | None" = None) -> None:  # type: ignore[misc]
        raise RuntimeError(
            "fastapi and pydantic are required to use the HTTP API. "
            "Install them with:  pip install fastapi pydantic uvicorn"
        )

    app = None  # type: ignore[assignment]

# --- end merged module: src/api.py ---


def build_analysis_service() -> AnalysisService:
    """Create the shared PGx analysis service used by the desktop entrypoint."""
    return AnalysisService()


def main() -> None:
    """Launch the optional Qt desktop application."""
    raise SystemExit(launch_app(service=build_analysis_service()))


if __name__ == "__main__":
    main()
