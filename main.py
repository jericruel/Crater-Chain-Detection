from nukem import neukum_production_function

if __name__ == '__main__':
    # Example usage (for the moon)
    D = 0.1  # Crater diameter in km
    time_period_years = 10 * 1e9  # Time period in years (1 Gyr)
    expected_craters, probability = neukum_production_function(D, time_period_years)

    print(f"Expected number of craters larger than {D} km in {time_period_years} years: {expected_craters}")
    print(f"Probability of at least one crater larger than {D} km appearing in {time_period_years} years: {probability}")