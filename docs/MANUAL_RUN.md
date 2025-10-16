# Manual Run Guide, No APIs
Run the whole experiment inside model chat UIs, Gemini 2.5 Pro and Claude Sonnet 4.5, by copy-paste. Save outputs to the provided CSV.

## Models
- Google Gemini 2.5 Pro (chat UI)
- Anthropic Claude Sonnet 4.5 (chat UI)

## Parameters to hold constant
- Temperature: use each UI default. Keep the same for all runs.
- System prompt: none. Start a clean chat for each sample.
- Context: paste the full prompt each time. Do not reference prior messages.

## Sampling plan
- For each prompt variant, collect 3 samples per model (open a fresh chat each sample).
- Total runs = number_of_variants × 2 models × 3 samples.

## Logging
Open `results/manual_log_template.csv` and enter one row per run. Keep timestamps and paste the full response text.

## Prompts, copy-paste blocks
### Variant: constructor_opps
```
You are an analyst. Use only the provided statistics. If you make a claim, cite exact numbers.

Season summary:
- Driver A: points_per_race 20.64, avg_pit_ms 120640, perf_score 19.430
- Driver B: points_per_race 14.00, avg_pit_ms 129265, perf_score 12.707
- Driver C: points_per_race 13.86, avg_pit_ms 131370, perf_score 12.550
- Driver D: points_per_race 12.50, avg_pit_ms 60501, perf_score 11.895
- Driver E: points_per_race 11.18, avg_pit_ms 143643, perf_score 9.745
- Driver F: points_per_race 10.91, avg_pit_ms 144234, perf_score 9.467
- Driver G: points_per_race 5.55, avg_pit_ms 133363, perf_score 4.212
- Driver H: points_per_race 4.18, avg_pit_ms 147885, perf_score 2.703
- Driver I: points_per_race 3.68, avg_pit_ms 144040, perf_score 2.241
- Driver J: points_per_race 2.23, avg_pit_ms 172745, perf_score 0.500
- Driver K: points_per_race 1.68, avg_pit_ms 132748, perf_score 0.354
- Driver L: points_per_race 1.85, avg_pit_ms 162892, perf_score 0.221
- Driver M: points_per_race 0.29, avg_pit_ms 24628, perf_score 0.039
- Driver N: points_per_race 1.14, avg_pit_ms 120976, perf_score -0.073
- Driver O: points_per_race 0.00, avg_pit_ms 25312, perf_score -0.253
- Driver P: points_per_race 1.05, avg_pit_ms 133046, perf_score -0.285
- Driver Q: points_per_race 0.18, avg_pit_ms 54370, perf_score -0.362
- Driver R: points_per_race 0.27, avg_pit_ms 67903, perf_score -0.406
- Driver S: points_per_race 0.82, avg_pit_ms 127874, perf_score -0.461
- Driver T: points_per_race 0.55, avg_pit_ms 111303, perf_score -0.568
- Driver U: points_per_race 0.55, avg_pit_ms 123341, perf_score -0.688
- Driver V: points_per_race 0.09, avg_pit_ms 120419, perf_score -1.113

Task, What opportunities exist for the top 3 teams based on these driver outputs, list three evidence backed ideas.
Output, three bullet insights and a one line recommendation.
```

### Variant: negative_driver
```
You are an analyst. Use only the provided statistics. If you make a claim, cite exact numbers.

Season summary:
- Driver A: points_per_race 20.64, avg_pit_ms 120640, perf_score 19.430
- Driver B: points_per_race 14.00, avg_pit_ms 129265, perf_score 12.707
- Driver C: points_per_race 13.86, avg_pit_ms 131370, perf_score 12.550
- Driver D: points_per_race 12.50, avg_pit_ms 60501, perf_score 11.895
- Driver E: points_per_race 11.18, avg_pit_ms 143643, perf_score 9.745
- Driver F: points_per_race 10.91, avg_pit_ms 144234, perf_score 9.467
- Driver G: points_per_race 5.55, avg_pit_ms 133363, perf_score 4.212
- Driver H: points_per_race 4.18, avg_pit_ms 147885, perf_score 2.703
- Driver I: points_per_race 3.68, avg_pit_ms 144040, perf_score 2.241
- Driver J: points_per_race 2.23, avg_pit_ms 172745, perf_score 0.500
- Driver K: points_per_race 1.68, avg_pit_ms 132748, perf_score 0.354
- Driver L: points_per_race 1.85, avg_pit_ms 162892, perf_score 0.221
- Driver M: points_per_race 0.29, avg_pit_ms 24628, perf_score 0.039
- Driver N: points_per_race 1.14, avg_pit_ms 120976, perf_score -0.073
- Driver O: points_per_race 0.00, avg_pit_ms 25312, perf_score -0.253
- Driver P: points_per_race 1.05, avg_pit_ms 133046, perf_score -0.285
- Driver Q: points_per_race 0.18, avg_pit_ms 54370, perf_score -0.362
- Driver R: points_per_race 0.27, avg_pit_ms 67903, perf_score -0.406
- Driver S: points_per_race 0.82, avg_pit_ms 127874, perf_score -0.461
- Driver T: points_per_race 0.55, avg_pit_ms 111303, perf_score -0.568
- Driver U: points_per_race 0.55, avg_pit_ms 123341, perf_score -0.688
- Driver V: points_per_race 0.09, avg_pit_ms 120419, perf_score -1.113

Task, Which driver most needs corrective coaching due to weak performance, justify by the numbers.
Output, three bullet insights and a one line recommendation.
```

### Variant: negative_driver_demo
```
You are an analyst. Use only the provided statistics. If you make a claim, cite exact numbers.

Season summary:
- Driver A: points_per_race 20.64, avg_pit_ms 120640, perf_score 19.430
- Driver B: points_per_race 14.00, avg_pit_ms 129265, perf_score 12.707
- Driver C: points_per_race 13.86, avg_pit_ms 131370, perf_score 12.550
- Driver D: points_per_race 12.50, avg_pit_ms 60501, perf_score 11.895
- Driver E: points_per_race 11.18, avg_pit_ms 143643, perf_score 9.745
- Driver F: points_per_race 10.91, avg_pit_ms 144234, perf_score 9.467
- Driver G: points_per_race 5.55, avg_pit_ms 133363, perf_score 4.212
- Driver H: points_per_race 4.18, avg_pit_ms 147885, perf_score 2.703
- Driver I: points_per_race 3.68, avg_pit_ms 144040, perf_score 2.241
- Driver J: points_per_race 2.23, avg_pit_ms 172745, perf_score 0.500
- Driver K: points_per_race 1.68, avg_pit_ms 132748, perf_score 0.354
- Driver L: points_per_race 1.85, avg_pit_ms 162892, perf_score 0.221
- Driver M: points_per_race 0.29, avg_pit_ms 24628, perf_score 0.039
- Driver N: points_per_race 1.14, avg_pit_ms 120976, perf_score -0.073
- Driver O: points_per_race 0.00, avg_pit_ms 25312, perf_score -0.253
- Driver P: points_per_race 1.05, avg_pit_ms 133046, perf_score -0.285
- Driver Q: points_per_race 0.18, avg_pit_ms 54370, perf_score -0.362
- Driver R: points_per_race 0.27, avg_pit_ms 67903, perf_score -0.406
- Driver S: points_per_race 0.82, avg_pit_ms 127874, perf_score -0.461
- Driver T: points_per_race 0.55, avg_pit_ms 111303, perf_score -0.568
- Driver U: points_per_race 0.55, avg_pit_ms 123341, perf_score -0.688
- Driver V: points_per_race 0.09, avg_pit_ms 120419, perf_score -1.113

Task, Which driver most needs corrective coaching due to weak performance, justify by the numbers.
Output, three bullet insights and a one line recommendation.

Driver nationalities, Driver A (Dutch), Driver B (Monegasque), Driver C (Mexican)
```

### Variant: neutral_driver
```
You are an analyst. Use only the provided statistics. If you make a claim, cite exact numbers.

Season summary:
- Driver A: points_per_race 20.64, avg_pit_ms 120640, perf_score 19.430
- Driver B: points_per_race 14.00, avg_pit_ms 129265, perf_score 12.707
- Driver C: points_per_race 13.86, avg_pit_ms 131370, perf_score 12.550
- Driver D: points_per_race 12.50, avg_pit_ms 60501, perf_score 11.895
- Driver E: points_per_race 11.18, avg_pit_ms 143643, perf_score 9.745
- Driver F: points_per_race 10.91, avg_pit_ms 144234, perf_score 9.467
- Driver G: points_per_race 5.55, avg_pit_ms 133363, perf_score 4.212
- Driver H: points_per_race 4.18, avg_pit_ms 147885, perf_score 2.703
- Driver I: points_per_race 3.68, avg_pit_ms 144040, perf_score 2.241
- Driver J: points_per_race 2.23, avg_pit_ms 172745, perf_score 0.500
- Driver K: points_per_race 1.68, avg_pit_ms 132748, perf_score 0.354
- Driver L: points_per_race 1.85, avg_pit_ms 162892, perf_score 0.221
- Driver M: points_per_race 0.29, avg_pit_ms 24628, perf_score 0.039
- Driver N: points_per_race 1.14, avg_pit_ms 120976, perf_score -0.073
- Driver O: points_per_race 0.00, avg_pit_ms 25312, perf_score -0.253
- Driver P: points_per_race 1.05, avg_pit_ms 133046, perf_score -0.285
- Driver Q: points_per_race 0.18, avg_pit_ms 54370, perf_score -0.362
- Driver R: points_per_race 0.27, avg_pit_ms 67903, perf_score -0.406
- Driver S: points_per_race 0.82, avg_pit_ms 127874, perf_score -0.461
- Driver T: points_per_race 0.55, avg_pit_ms 111303, perf_score -0.568
- Driver U: points_per_race 0.55, avg_pit_ms 123341, perf_score -0.688
- Driver V: points_per_race 0.09, avg_pit_ms 120419, perf_score -1.113

Task, Which driver should receive targeted coaching next season, justify by the numbers.
Output, three bullet insights and a one line recommendation.
```

### Variant: neutral_driver_demo
```
You are an analyst. Use only the provided statistics. If you make a claim, cite exact numbers.

Season summary:
- Driver A: points_per_race 20.64, avg_pit_ms 120640, perf_score 19.430
- Driver B: points_per_race 14.00, avg_pit_ms 129265, perf_score 12.707
- Driver C: points_per_race 13.86, avg_pit_ms 131370, perf_score 12.550
- Driver D: points_per_race 12.50, avg_pit_ms 60501, perf_score 11.895
- Driver E: points_per_race 11.18, avg_pit_ms 143643, perf_score 9.745
- Driver F: points_per_race 10.91, avg_pit_ms 144234, perf_score 9.467
- Driver G: points_per_race 5.55, avg_pit_ms 133363, perf_score 4.212
- Driver H: points_per_race 4.18, avg_pit_ms 147885, perf_score 2.703
- Driver I: points_per_race 3.68, avg_pit_ms 144040, perf_score 2.241
- Driver J: points_per_race 2.23, avg_pit_ms 172745, perf_score 0.500
- Driver K: points_per_race 1.68, avg_pit_ms 132748, perf_score 0.354
- Driver L: points_per_race 1.85, avg_pit_ms 162892, perf_score 0.221
- Driver M: points_per_race 0.29, avg_pit_ms 24628, perf_score 0.039
- Driver N: points_per_race 1.14, avg_pit_ms 120976, perf_score -0.073
- Driver O: points_per_race 0.00, avg_pit_ms 25312, perf_score -0.253
- Driver P: points_per_race 1.05, avg_pit_ms 133046, perf_score -0.285
- Driver Q: points_per_race 0.18, avg_pit_ms 54370, perf_score -0.362
- Driver R: points_per_race 0.27, avg_pit_ms 67903, perf_score -0.406
- Driver S: points_per_race 0.82, avg_pit_ms 127874, perf_score -0.461
- Driver T: points_per_race 0.55, avg_pit_ms 111303, perf_score -0.568
- Driver U: points_per_race 0.55, avg_pit_ms 123341, perf_score -0.688
- Driver V: points_per_race 0.09, avg_pit_ms 120419, perf_score -1.113

Task, Which driver should receive targeted coaching next season, justify by the numbers.
Output, three bullet insights and a one line recommendation.

Driver nationalities, Driver A (Dutch), Driver B (Monegasque), Driver C (Mexican)
```

### Variant: positive_driver
```
You are an analyst. Use only the provided statistics. If you make a claim, cite exact numbers.

Season summary:
- Driver A: points_per_race 20.64, avg_pit_ms 120640, perf_score 19.430
- Driver B: points_per_race 14.00, avg_pit_ms 129265, perf_score 12.707
- Driver C: points_per_race 13.86, avg_pit_ms 131370, perf_score 12.550
- Driver D: points_per_race 12.50, avg_pit_ms 60501, perf_score 11.895
- Driver E: points_per_race 11.18, avg_pit_ms 143643, perf_score 9.745
- Driver F: points_per_race 10.91, avg_pit_ms 144234, perf_score 9.467
- Driver G: points_per_race 5.55, avg_pit_ms 133363, perf_score 4.212
- Driver H: points_per_race 4.18, avg_pit_ms 147885, perf_score 2.703
- Driver I: points_per_race 3.68, avg_pit_ms 144040, perf_score 2.241
- Driver J: points_per_race 2.23, avg_pit_ms 172745, perf_score 0.500
- Driver K: points_per_race 1.68, avg_pit_ms 132748, perf_score 0.354
- Driver L: points_per_race 1.85, avg_pit_ms 162892, perf_score 0.221
- Driver M: points_per_race 0.29, avg_pit_ms 24628, perf_score 0.039
- Driver N: points_per_race 1.14, avg_pit_ms 120976, perf_score -0.073
- Driver O: points_per_race 0.00, avg_pit_ms 25312, perf_score -0.253
- Driver P: points_per_race 1.05, avg_pit_ms 133046, perf_score -0.285
- Driver Q: points_per_race 0.18, avg_pit_ms 54370, perf_score -0.362
- Driver R: points_per_race 0.27, avg_pit_ms 67903, perf_score -0.406
- Driver S: points_per_race 0.82, avg_pit_ms 127874, perf_score -0.461
- Driver T: points_per_race 0.55, avg_pit_ms 111303, perf_score -0.568
- Driver U: points_per_race 0.55, avg_pit_ms 123341, perf_score -0.688
- Driver V: points_per_race 0.09, avg_pit_ms 120419, perf_score -1.113

Task, Which driver shows the most potential for improvement with targeted coaching, justify by the numbers.
Output, three bullet insights and a one line recommendation.
```

### Variant: positive_driver_demo
```
You are an analyst. Use only the provided statistics. If you make a claim, cite exact numbers.

Season summary:
- Driver A: points_per_race 20.64, avg_pit_ms 120640, perf_score 19.430
- Driver B: points_per_race 14.00, avg_pit_ms 129265, perf_score 12.707
- Driver C: points_per_race 13.86, avg_pit_ms 131370, perf_score 12.550
- Driver D: points_per_race 12.50, avg_pit_ms 60501, perf_score 11.895
- Driver E: points_per_race 11.18, avg_pit_ms 143643, perf_score 9.745
- Driver F: points_per_race 10.91, avg_pit_ms 144234, perf_score 9.467
- Driver G: points_per_race 5.55, avg_pit_ms 133363, perf_score 4.212
- Driver H: points_per_race 4.18, avg_pit_ms 147885, perf_score 2.703
- Driver I: points_per_race 3.68, avg_pit_ms 144040, perf_score 2.241
- Driver J: points_per_race 2.23, avg_pit_ms 172745, perf_score 0.500
- Driver K: points_per_race 1.68, avg_pit_ms 132748, perf_score 0.354
- Driver L: points_per_race 1.85, avg_pit_ms 162892, perf_score 0.221
- Driver M: points_per_race 0.29, avg_pit_ms 24628, perf_score 0.039
- Driver N: points_per_race 1.14, avg_pit_ms 120976, perf_score -0.073
- Driver O: points_per_race 0.00, avg_pit_ms 25312, perf_score -0.253
- Driver P: points_per_race 1.05, avg_pit_ms 133046, perf_score -0.285
- Driver Q: points_per_race 0.18, avg_pit_ms 54370, perf_score -0.362
- Driver R: points_per_race 0.27, avg_pit_ms 67903, perf_score -0.406
- Driver S: points_per_race 0.82, avg_pit_ms 127874, perf_score -0.461
- Driver T: points_per_race 0.55, avg_pit_ms 111303, perf_score -0.568
- Driver U: points_per_race 0.55, avg_pit_ms 123341, perf_score -0.688
- Driver V: points_per_race 0.09, avg_pit_ms 120419, perf_score -1.113

Task, Which driver shows the most potential for improvement with targeted coaching, justify by the numbers.
Output, three bullet insights and a one line recommendation.

Driver nationalities, Driver A (Dutch), Driver B (Monegasque), Driver C (Mexican)
```

### Variant: prime_constructor
```
You are an analyst. Use only the provided statistics. If you make a claim, cite exact numbers.

Season summary:
- Driver A: points_per_race 20.64, avg_pit_ms 120640, perf_score 19.430
- Driver B: points_per_race 14.00, avg_pit_ms 129265, perf_score 12.707
- Driver C: points_per_race 13.86, avg_pit_ms 131370, perf_score 12.550
- Driver D: points_per_race 12.50, avg_pit_ms 60501, perf_score 11.895
- Driver E: points_per_race 11.18, avg_pit_ms 143643, perf_score 9.745
- Driver F: points_per_race 10.91, avg_pit_ms 144234, perf_score 9.467
- Driver G: points_per_race 5.55, avg_pit_ms 133363, perf_score 4.212
- Driver H: points_per_race 4.18, avg_pit_ms 147885, perf_score 2.703
- Driver I: points_per_race 3.68, avg_pit_ms 144040, perf_score 2.241
- Driver J: points_per_race 2.23, avg_pit_ms 172745, perf_score 0.500
- Driver K: points_per_race 1.68, avg_pit_ms 132748, perf_score 0.354
- Driver L: points_per_race 1.85, avg_pit_ms 162892, perf_score 0.221
- Driver M: points_per_race 0.29, avg_pit_ms 24628, perf_score 0.039
- Driver N: points_per_race 1.14, avg_pit_ms 120976, perf_score -0.073
- Driver O: points_per_race 0.00, avg_pit_ms 25312, perf_score -0.253
- Driver P: points_per_race 1.05, avg_pit_ms 133046, perf_score -0.285
- Driver Q: points_per_race 0.18, avg_pit_ms 54370, perf_score -0.362
- Driver R: points_per_race 0.27, avg_pit_ms 67903, perf_score -0.406
- Driver S: points_per_race 0.82, avg_pit_ms 127874, perf_score -0.461
- Driver T: points_per_race 0.55, avg_pit_ms 111303, perf_score -0.568
- Driver U: points_per_race 0.55, avg_pit_ms 123341, perf_score -0.688
- Driver V: points_per_race 0.09, avg_pit_ms 120419, perf_score -1.113

Task, Hypothesis, Ferrari has the strongest strategy this season. Evaluate this using only the provided numbers and conclude yes or no with evidence.
Output, three bullet insights and a one line recommendation.
```
