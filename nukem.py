import math
from scipy.stats import poisson

def neukum_production_function(D, time_period_years):
    # Coefficients ak for the NPF (for m = 11)
    a = [-3.921, 0.8923, -0.2312, 0.0522, -0.0106, 0.0024, -0.0005, 0.0001, -2e-05, 4e-06, -7e-07, 1e-07]

    # Calculate log10(N) using the NPF equation
    log10_D = math.log10(D)
    log10_N = sum(a[k] * (log10_D ** k) for k in range(len(a)))

    # Convert log10(N) to N
    N = 10 ** log10_N

    # Production rate for craters larger than 4 km per km^2 per Gyr
    production_rate_per_km2_per_Gyr = 1.7e-5

    # Convert time period from years to Gyr
    time_period_Gyr = time_period_years / 1e9

    # Calculate expected number of craters in the given time period
    expected_craters = production_rate_per_km2_per_Gyr * time_period_Gyr

    # Probability of at least one crater larger than D appearing in the time period
    probability = 1 - poisson.cdf(0, expected_craters)

    return expected_craters, probability

if __name__ == '__main__':
    # Example usage (for the moon)
    D = 0.1  # Crater diameter in km
    time_period_years = 10 * 1e9  # Time period in years (1 Gyr)
    expected_craters, probability = neukum_production_function(D, time_period_years)

    print(f"Expected number of craters larger than {D} km in {time_period_years} years: {expected_craters}")
    print(f"Probability of at least one crater larger than {D} km appearing in {time_period_years} years: {probability}")
