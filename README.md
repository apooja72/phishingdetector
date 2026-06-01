![Python](https://img.shields.io/badge/Python-3.10-blue)
![XGBoost](https://img.shields.io/badge/XGBoost-Machine%20Learning-green)
![Cybersecurity](https://img.shields.io/badge/Cybersecurity-Phishing%20Detection-red)

# Multi-Vector Phishing Detection Using XGBoost

📄 **IEEE Published Research Project**

## Overview

Phishing attacks continue to be a major cybersecurity threat, using malicious URLs, deceptive emails, and infected attachments to compromise users and organizations. Traditional detection systems often focus on a single attack vector, limiting their effectiveness against sophisticated phishing campaigns.

This project introduces a **Multi-Vector Phishing Detection Framework** that independently analyzes URLs, emails, and file attachments using dedicated **XGBoost classifiers**. The outputs from each module are combined through a **weighted decision-level fusion mechanism** to generate a unified phishing risk score, enabling more reliable and accurate threat detection.

---

## Key Features

### URL Analysis

* Lexical feature extraction (URL length, digits, special characters, IP-based URLs)
* Character-level n-gram analysis
* TF-IDF feature representation
* Detection of URL obfuscation and domain spoofing

### Email Analysis

* NLP preprocessing and TF-IDF vectorization
* Suspicious keyword detection
* SPF, DKIM, and DMARC verification
* Embedded URL analysis

### Attachment Analysis

* Static file inspection
* Metadata and entropy analysis
* Macro and script detection
* Detection of suspicious strings and embedded URLs

### Decision-Level Fusion

* Independent phishing probability generation for each vector
* Weighted score aggregation
* Unified phishing risk assessment

---

## Technology Stack

* Python
* XGBoost
* Scikit-Learn
* Pandas
* NumPy
* NLTK
* TF-IDF Vectorization
* Machine Learning
* Natural Language Processing (NLP)

---

## Methodology

The framework follows a modular pipeline:

1. Extract features from URLs, emails, and attachments.
2. Process each vector using a dedicated XGBoost classifier.
3. Generate phishing probability scores:

   * URL Score (S_url)
   * Email Score (S_email)
   * Attachment Score (S_attach)
4. Combine scores using weighted decision-level fusion.
5. Classify the sample as **Phishing** or **Benign**.

---

## Results

The proposed framework achieved approximately **85% accuracy** on publicly sourced phishing and benign datasets while maintaining balanced precision, recall, and F1-score.

| Metric    | Performance |
| --------- | ----------- |
| Accuracy  | ~85%        |
| Precision | Balanced    |
| Recall    | Balanced    |
| F1-Score  | Balanced    |

---

## Publication

**Paper Title:** Multi-Vector Phishing Detection Using XGBoost-Based Decision Fusion

**Published In:** IEEE, 2026

---

## Contributors

- A POOJA
- ARCHANA C 
- RASHMI C 

This work is associated with an IEEE-published research project on multi-vector phishing detection using XGBoost-based decision fusion.
---

## License

This project is intended for educational, academic, and research purposes.
