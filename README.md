# 🏥 Hospital Residency Matching — Gale–Shapley Algorithm

This project implements a simplified version of the **Stable Matching Algorithm** (Gale–Shapley) for matching medical students to hospitals based on mutual preferences and hospital capacity. It models the real-world logic behind systems like the **National Resident Matching Program (NRMP)**.

---

## 📦 Features

- Many-to-one matching: hospitals can accept multiple students.
- Preference-based selection: both students and hospitals rank each other.
- Guaranteed stability: no student-hospital pair would prefer each other over their current match.
- Easy to customize with real names, preferences, and capacities.

---

## 🧠 How It Works

Each student proposes to hospitals in order of preference. Hospitals accept students based on their own rankings and available slots. If a hospital prefers a new applicant over its current lowest-ranked match, it replaces them. This continues until all students are matched.

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/NisaEngineers/Hospital-Residency-Matching.git
cd Hospital-Residency-Matching
# Hospital-Residency-Matching
python main.py
```
