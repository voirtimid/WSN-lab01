import matplotlib.pyplot as plt
import numpy as np

from main import read_data
from main import dual_prediction_schema
from main import scatter_plot
from main import plot

temperature_data, temperature_data_2day, temperature_data_3day = read_data("temperature_data")
humidity_data, humidity_data_2day, humidity_data_3day = read_data("humidity_data")

temperature_thresholds = [round(i * 0.5, 1) for i in range(20)]
humidity_thresholds = [round(i * 0.5, 1) for i in range(20)]

mse_errors, reduced_transmission = dual_prediction_schema(temperature_data,
                                                          humidity_data, 1,
                                                          temperature_thresholds,
                                                          humidity_thresholds)

print(mse_errors)
print(reduced_transmission)

