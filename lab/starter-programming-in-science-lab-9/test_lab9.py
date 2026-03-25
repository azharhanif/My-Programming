import unittest
import numpy as np
import matplotlib.pyplot as plt
from Lab10 import plot_curve, plot_hr_diagram, plot_density

def test_plot_curve():
    """Test case for plot_curve function."""
    x_values = np.array([1, 2, 3, 4, 5])
    y_values = np.array([1, 4, 9, 16, 25])
    try:
        plot_curve(x_values, y_values)
        success = True
    except Exception:
        success = False
    assert success, "plot_curve failed to execute correctly"

def test_plot_hr_diagram():
    """Test case for plot_hr_diagram function."""
    temperature = np.array([3000, 5000, 7000, 9000, 11000])
    luminosity = np.array([0.1, 1, 10, 100, 1000])
    try:
        plot_hr_diagram(temperature, luminosity)
        success = True
    except Exception:
        success = False
    assert success, "plot_hr_diagram failed to execute correctly"

def test_plot_density():
    """Test case for plot_density function."""
    np.random.seed(0)
    data = np.random.randn(1000, 2)
    try:
        plot_density(data, 'hot')
        success = True
    except Exception:
        success = False
    assert success, "plot_density failed to execute correctly"

if __name__ == "__main__":
    test_plot_curve()
    test_plot_hr_diagram()
    test_plot_density()
    print("All tests passed.")