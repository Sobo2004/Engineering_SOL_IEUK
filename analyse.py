import pandas as pd

# Load the CSV file
df = pd.read_csv("telemetry_data.csv")

summary = df.groupby("turbine_id").agg(
    average_temperature=("temperature_c", "mean"),
    max_vibration=("vibration_mm_s", "max"),
    average_rpm=("rpm", "mean")
).reset_index()

# Anomaly rules
failing = summary[
    (summary["average_temperature"] > 85) |
    (summary["max_vibration"] > 15)
]

# Display results
print("Turbine Summary:")
print(summary)

print("\nFailing Turbines:")
print(failing["turbine_id"].tolist())