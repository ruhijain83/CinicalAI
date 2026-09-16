# Radiology Workflow Discovery

## Problem

Radiologists may spend time manually locating and reviewing
relevant prior imaging studies and radiology reports.

## Current Workflow

1. Open current imaging study.
2. Identify the patient.
3. Search historical imaging studies.
4. Filter relevant modalities.
5. Identify relevant body region/anatomy.
6. Exclude irrelevant or duplicate studies.
7. Order studies chronologically.
8. Select the most relevant prior study.
9. Retrieve the corresponding final report.
10. Review prior findings.
11. Compare prior findings with the current study.

## Candidate Bottleneck

Prior-study and report retrieval.

## Proposed Investigation

Determine whether an AI-assisted workflow can reduce the
time required to identify and review relevant prior imaging
while maintaining high retrieval accuracy and grounded responses.

## Design Principle

Deterministic clinical selection rules should remain outside
the LLM whenever possible.

The LLM should be used for language understanding,
relevance reasoning, summarization, and comparison.

## Initial Success Metrics

- Prior-study retrieval accuracy
- Correct modality selection
- Correct latest relevant study
- Correct report retrieval
- Grounded response rate
- Unsupported claim rate
- Retrieval latency
- End-to-end latency