# Premier League 2^3 Factorial Experimental Design

**Course:** DSA 503 Data Collection and Design of Experiments
**Instructor:** Prof. Thistleton

## Research Question
How do pressing intensity (PPDA), home/away advantage, and possession percentage interact to affect goals scored in Premier League matches?

## Design
- Type: 2^3 full factorial design
- Factor A: Pressing intensity (high vs low PPDA)
- Factor B: Match venue (home vs away)
- Factor C: Possession (high vs low)
- Blocking variable: Season (RCBD to control year-to-year variation)
- Response: Goals scored per match

## Statistical Methods
- Two-way and three-way ANOVA
- By-hand SS calculations verified with aov() in R
- Interaction plots for all factor pairs
- Residual diagnostics: Shapiro-Wilk, Levene test
- Full model vs reduced main-effects comparison
- 6-step hypothesis testing framework throughout

## Files
| File | Description |
|------|-------------|
| `EPL_Factorial_Design.ipynb` | Full R notebook (Colab R-kernel) |

## Tech Stack
R, ggplot2, agricolae, dplyr, Google Colab R-kernel
