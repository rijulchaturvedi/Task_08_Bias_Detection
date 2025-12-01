# Weekly Report: Task 08 — Bias Detection in LLM Outputs

## 1. Objective
The purpose of this week's task was to evaluate whether the LLM exhibits systematic demographic bias when generating responses across controlled prompts. The task focused on:
- Gender groups
- Political identity groups
- Sentiment or score variations
- Stability across prompt templates

The goal was to produce:
- A balanced test dataset
- A pipeline to query the model consistently
- Bias metrics and visualizations
- A written interpretation summarizing findings

## 2. Work Completed

### 2.1 Dataset Preparation
- Loaded and cleaned all prompts and demographic labels.
- Standardized demographic categories.
- Balanced dataset across groups.
- Ensured each prompt template was represented for every demographic.

### 2.2 LLM Response Generation
- Standardized LLM parameters (temperature 0.0, consistent system prompts).
- Generated responses for every prompt-demographic pair.
- Recorded sentiment and probability scores.
- Stored outputs in structured CSV/JSON format.

### 2.3 Bias Metrics Computed
- Group-wise Mean Score Difference
- Disparate Impact Ratio
- Sentiment Distribution Spread
- Variance analysis across templates and repeated runs

## 3. Key Findings

### 3.1 Gender-Based Bias
- Male-coded prompts received slightly higher positive sentiment.
- Female-coded prompts had a higher share of neutral labels.
- Bias observed was stable across templates.

### 3.2 Political Bias
- Liberal-aligned prompts received more positive sentiment.
- Conservative-aligned prompts received more negative sentiment.
- Disparate impact ratio indicated meaningful skew.

### 3.3 Stability
- Bias patterns remained consistent across repeated evaluations.

## 4. Visualizations Produced
- Bar charts for group-wise means
- Sentiment distribution curves
- Bias intensity heatmaps
- Boxplots for variance and score spread

## 5. Issues Identified
- Some demographic categories required rebalancing.
- Sarcasm and ambiguous phrasing affected sentiment scoring.
- Needed normalization rules for multi-sentence outputs.

## 6. Deliverables Completed
- Clean dataset
- Model inference outputs
- All bias analysis scripts
- Visualizations
- Summary report

## 7. Next Steps
- Expand demographic dimensions (ethnicity, age, religion, etc.)
- Introduce significance testing (t-tests, chi-square)
- Evaluate multiple LLM models
- Implement debiasing strategies

