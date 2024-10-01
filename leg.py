import numpy as np
from numpy.polynomial.legendre import legfit, legval
import matplotlib.pyplot as plt


def legendre_fit(x, y, degree):
    # Perform Legendre polynomial fit
    coeffs = legfit(x, y, degree)
    # Evaluate the fitted polynomial
    fitted_curve = legval(x, coeffs)
    return coeffs, fitted_curve


# Example dataset
theta = np.array(
    [
        90,
        95,
        100,
        105,
        110,
        115,
        120,
        125,
        130,
        135,
        140,
        145,
        150,
        155,
        160,
        165,
        170,
        175,
        180,
    ]
)
amp = np.array(
    [
        0.129,
        0.224,
        0.346,
        0.324,
        0.129,
        0.132,
        0.359,
        0.448,
        0.369,
        0.153,
        0.15,
        0.407,
        0.477,
        0.363,
        0.023,
        0.114,
        0.751,
        0.98,
        1.012,
    ]
)

# Degree of the Legendre polynomial
degree = 10

# Perform Legendre polynomial fit
coeffs, fitted_curve = legendre_fit(theta, amp, degree)

# Plot the original data and the fitted curve
plt.scatter(theta, amp, label="Original Data")
plt.plot(theta, fitted_curve, color="red", label="Legendre Polynomial Fit")
plt.xlabel("theta")
plt.ylabel("Amplitude")
plt.title("Legendre Polynomial Fit")
plt.legend()
plt.show()

print("Coefficients of the Legendre polynomial fit:", coeffs)
