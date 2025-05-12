# 📈 Portfolio Optimization with K-Bandits

This project explores various **K-armed bandit algorithms**—including **UCB (Upper Confidence Bound)** and **Alpha strategies**—to select a set of stocks for optimizing a portfolio on a **bi-weekly basis**.

---

## 🎯 Objective

Use reinforcement learning techniques to make intelligent, data-driven decisions for dynamic portfolio management:

- ✳️ **Explore vs. Exploit**: Leverage K-bandits to balance exploration of new stocks and exploitation of historically strong performers.
- 📆 **Bi-weekly rebalancing**: The portfolio is re-optimized every 2 weeks based on algorithmic decisions.
- 💹 **Focus on performance**: The goal is to maximize returns while managing exploration uncertainty.

---

## 📓 Research & Experiments

All research, experiments, and results are documented in the `notebooks` folder.

> 🧪 Dive into the Jupyter notebooks to understand the methodology, implementation, and findings.

---

## 🧠 Algorithms Explored

- **UCB (Upper Confidence Bound)**  
- **Alpha-greedy strategies**  
- (More strategies can be added in future iterations)

---


## 📦 Dependencies

This project uses standard Python data science libraries:

- `numpy`
- `pandas`
- `matplotlib`
- `scikit-learn`
- `jupyter`

Install dependencies with:

```bash
pip install -r requirements.txt
