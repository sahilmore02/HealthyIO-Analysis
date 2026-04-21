# HealthyIO Data Analysis

This analyzes how daily habits impact a user's health score using structured health-related data.

## Tools Used
- Python
- Pandas
- MySQL

## Note on Dataset

The data used in here is dummy data created as part of the other project(HealthyIO).  
It is intended for practice and analysis purposes only.

## What I Did
- Loaded data from multiple tables (profile, health_score, physical_exercise, food_intake)
- Merged datasets using common keys (user_id, log_id)
- Created meaningful groups (age groups, water intake ranges, calorie ranges)
- Performed grouped analysis using Pandas

## Key Analysis
- Sleep vs Health Score
- Exercise Type vs Health Score
- Calories Burn vs Health Score
- Water Intake vs Health Score
- Age Groups vs Health Score

## Key Findings

- Users with higher sleep hours tend to have better health scores  
- Higher water intake shows a positive relationship with health  
- High-intensity exercises result in better scores  
- Middle age group (30–60) shows relatively higher average health scores  

## How to Run
1. Make sure MySQL is running and the `healthyIO` database is available  
2. Update database credentials in the script:
   ```python
   host="localhost"
   user="your_username"
   password="your_password"
   database="healthyIO"
