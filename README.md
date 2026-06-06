# Evidence-Guided Multimodal Fake News Detection Using Text-Image Consistency and External Knowledge

## Overview

The rapid growth of social media has increased the spread of misinformation in the form of text, images, and multimodal content. Traditional fake news detection systems mainly focus on textual information and often fail to verify factual correctness using external evidence.

This project proposes an Evidence-Guided Multimodal Fake News Detection Framework that combines semantic text understanding, image-text consistency analysis, external knowledge retrieval, and evidence verification to improve the reliability of fake news detection.

The system utilizes SBERT for textual representation, CLIP for image-text consistency analysis, Retrieval-Augmented Generation (RAG) with FAISS for evidence retrieval, BART-Large-MNLI for evidence verification, and LightGBM for final classification. An LLM-based explanation layer provides human-readable reasoning for predictions. :contentReference[oaicite:1]{index=1}

---

## Problem Statement

Modern misinformation frequently combines misleading textual claims with unrelated or manipulated images. Existing systems often:

- Focus only on textual content
- Ignore image-text inconsistencies
- Lack external evidence verification
- Produce black-box predictions without explanations

This project addresses these limitations through a multimodal and evidence-based approach. :contentReference[oaicite:2]{index=2}

---

## Proposed Architecture

The framework consists of:

1. Text Processing using SBERT
2. Image Analysis using CLIP
3. Evidence Retrieval using RAG + FAISS
4. Evidence Verification using BART-Large-MNLI
5. Feature Fusion
6. LightGBM Classification
7. LLM-Based Explainability Layer

### Workflow

Input News Claim + Image

↓
SBERT Text Embeddings

↓
CLIP Image-Text Similarity

↓
RAG Evidence Retrieval (FAISS)

↓
NLI Verification

↓
Feature Fusion

↓
LightGBM Classifier

↓
Fake / Real Prediction

↓
LLM-Based Explanation

---

## Technologies Used

| Category | Tools |
|-----------|--------|
| Programming Language | Python |
| Deep Learning | PyTorch |
| NLP Models | SBERT, BERT, BART-MNLI |
| Multimodal Learning | CLIP |
| Retrieval System | RAG, FAISS |
| Machine Learning | LightGBM |
| Data Processing | Pandas, NumPy, Scikit-Learn |
| Explainability | Gemini API / LLM |
| Development Platform | Google Colab |
| User Interface | Streamlit |

---

## Key Features

- Multimodal fake news detection
- Text-image consistency verification
- External evidence retrieval
- Natural Language Inference validation
- Feature fusion architecture
- Explainable AI output
- Real-time claim verification support

---

## Dataset

The framework was trained and evaluated using multimodal fake news datasets containing:

- News headlines
- Associated images
- Binary labels (Fake / Real)

Dataset preprocessing includes:

- Missing value removal
- Feature extraction
- Embedding generation
- Evidence corpus construction

---

## Results

The proposed framework demonstrates improved performance compared to traditional text-only approaches by integrating:

- Semantic text understanding
- Visual consistency analysis
- Evidence-based verification
- Explainable reasoning

The system successfully provides:

- Prediction (Fake / Real)
- Retrieved supporting evidence
- Human-readable explanation

---

## Research Contributions

- Evidence-guided multimodal architecture
- Integration of SBERT, CLIP, RAG, and NLI
- External knowledge verification mechanism
- Explainable fake news detection framework
- Improved trust and interpretability

---

## Project Outcomes

- Developed an end-to-end multimodal fake news detection pipeline.
- Improved reliability through evidence-based verification.
- Reduced dependence on text-only classification.
- Enhanced transparency using LLM-generated explanations.

---

## Publication

This work was submitted to an international conference under the title:

**"Evidence-Guided Multimodal Fake News Detection Using Text-Image Consistency and External Knowledge"**

---

## Author

**Madakasira Hari Srinivas**
M.Tech – Computer Science and Engineering (Big Data Analytics)
Vellore Institute of Technology (VIT)
