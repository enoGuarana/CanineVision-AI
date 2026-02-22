# CanineVision AI: Video-Based Behavioral Classifier for Service Dog Aptitude

**CanineVision AI** is a decision support tool designed to objectively assess the behavioral suitability of dogs in specialized training programs. By analyzing training footage through **3D CNNs** and **Pose Estimation**, the system predicts training success probability and flags critical behavioral risks early in the process.

> **The Philosophy:** The model does not decide if a dog is fit. It provides objective data; the instructor decides with the data.

## 🔍 The Problem

Service dog training programs face significant challenges regarding retention, cost, and consistency:

* **High Dropout Rate:** Approximately 30-50% of dogs are discharged due to behavioral unsuitability.
* **Subjectivity:** Assessment relies on human observation, leading to inconsistencies (e.g., different instructors reaching opposite conclusions).
* **High Costs:** Training a single dog costs **R$ 15k – 25k (~$3k–$5k USD)** over 18 months. Early failure leads to significant financial loss.
* **Animal Welfare:** Late detection of unsuitability prolongs stress for animals in environments where they cannot thrive.

### 💸 Cost of Consequences

| Consequence | Real Cost Impact |
| --- | --- |
| **Late Discharge** | R$ 15k–25k wasted per dog (18 months of training). |
| **False Positive** | Risk of accidents with users + psychological trauma to the dog. |
| **False Negative** | Loss of potential + unnecessary stress to the animal. |
| **Instructor Discrepancy** | Rework and delays required due to conflicting evaluations. |

## 💡 The Solution

CanineVision AI acts as a **Decision Support Tool** that standardizes subjective criteria into objective metrics.

Instead of a simple "Pass/Fail," the model provides granular insights:

> *"This dog ignored 7/10 distractions (class average: 8.2) and took 22s to recover focus after a disruptive event (critical limit: 15s)."*

### How It Works

1. **Input:** Video footage of dogs during standardized training modules.
2. **Processing:** AI analyzes behavior sequences and temporal pose estimation.
3. **Output:** Success probability score + Critical Behavioral Indicators (CBIs).
4. **Decision:** The instructor uses this data to confirm or review discharge decisions.

## 🛠 Technical Approach

| Component | Technology / Source |
| --- | --- |
| **Core Model** | 3D CNN (I3D) or TimeSformer |
| **Pose Estimation** | DeepLabCut (Synthetic Data Generation) |
| **Data Sources** | Public Training Videos (YouTube: Lobo Bravo, Guide Dogs UK) |
| **Labels** | Partnership with schools (e.g., "ignores distractions", "maintains posture") |
| **Stack** | Python, PyTorch / TensorFlow, OpenCV, Pandas |

## 📈 Impact Analysis

By implementing CanineVision AI, training organizations can achieve:

* **Cost Reduction:** Save resources by identifying unsuitable candidates early in the pipeline.
* **Optimized Resources:** Focus training efforts on dogs with the highest success probabilities.
* **Animal Welfare:** Reduce stress for unsuitable dogs by rehoming them sooner.
* **Standardization:** Minimize the discrepancy between different instructors' evaluations.

## 🚀 Installation & Usage

*(Instructions for environment setup and running the inference scripts will be placed here.)*

```bash
# Example setup
git clone https://github.com/your-repo/caninevision-ai.git
cd caninevision-ai
pip install -r requirements.txt

```

---

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a **Pull Request**.

For **partnerships** or **data collaboration** (especially with training schools), please open an issue or contact the maintainers directly.
