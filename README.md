# Pediatric Hemodynamic Shock Prediction
### Dataset Description

This dataset contains medical data from pediatric intensive care unit (PICU) patients, with clinical measurements and a binary target variable indicating whether a patient will develop shock within 6 hours.

**The dataset includes 500,000 records with the following features:**

- **patient_id:** A unique identifier for each patient in the format PICU_XXXXXX.
- **age_months:** The patient's age in months, ranging from 0 to 200 months (~0-16 years).
- **weight_kg:** The patient's weight in kilograms, ranging from 3 to 80 kg.
- **heart_rate:** The patient's heart rate (beats per minute), ranging from 60 to 220 bpm.
- **blood_pressure_sys:** The systolic blood pressure (mmHg), ranging from 60 to 140 mmHg.
- **blood_pressure_dia:** The diastolic blood pressure (mmHg), ranging from 30 to 90 mmHg.
- **respiratory_rate:** The respiratory rate (breaths per minute), ranging from 15 to 70 breaths per minute.
- **spo2:** The blood oxygen saturation percentage, ranging from 70% to 100%.
- **temperature_c:** The body temperature in Celsius, ranging from 34°C to 41°C.
- **lactate_level:** The lactate level (mmol/L), ranging from 0.5 to 10 mmol/L.
- **capillary_refill_sec:** The capillary refill time (seconds), ranging from 1 to 5 seconds.
- **gcs_score:** The Glasgow Coma Scale score, ranging from 3 to 15.
- **base_deficit:** The base deficit (mmol/L), ranging from -15 to 5 mmol/L.
- **urine_output_ml_hr:** The urine output (mL/hr), ranging from 0 to 3 mL/hr.
- **crt_level:** The creatinine level (mg/dL), ranging from 0.2 to 2.0 mg/dL.
- **bun_level:** The blood urea nitrogen (BUN) level (mg/dL), ranging from 5 to 30 mg/dL.
- **wbc_count:** The white blood cell (WBC) count (10^3/μL), ranging from 3 to 30 10^3/μL.
- **hemoglobin:** The hemoglobin level (g/dL), ranging from 6 to 18 g/dL.
- **platelet_count:** The platelet count (10^3/μL), ranging from 50 to 500 10^3/μL.
- **bilirubin:** The bilirubin level (mg/dL), ranging from 0.1 to 3.0 mg/dL.
- **pco2:** The partial pressure of carbon dioxide (PCO2) in mmHg, ranging from 20 to 70 mmHg.

**The target variable is:**
- **shock_within_6h:** A binary classification label indicating whether the patient will develop shock within 6 hours, based on the patient's clinical features.