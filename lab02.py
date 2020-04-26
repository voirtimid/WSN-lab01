from main import read_data
from main import dual_prediction_schema
from main import scatter_plot

temperature_data, temperature_data_2day, temperature_data_3day = read_data("temperature_data")
humidity_data, humidity_data_2day, humidity_data_3day = read_data("humidity_data")

temperature_thresholds = [round(i, 1) for i in range(10)]
humidity_thresholds = [round(i, 1) for i in range(10)]

mse_errors, reduced_transmission = dual_prediction_schema(temperature_data,
                                                          humidity_data, 1,
                                                          temperature_thresholds,
                                                          humidity_thresholds)

mse_errors_2day, reduced_transmission_2day = dual_prediction_schema(temperature_data_2day,
                                                                    humidity_data_2day, 1,
                                                                    temperature_thresholds,
                                                                    humidity_thresholds)

mse_errors_3day, reduced_transmission_3day = dual_prediction_schema(temperature_data_3day,
                                                                    humidity_data_3day, 1,
                                                                    temperature_thresholds,
                                                                    humidity_thresholds)

# alt shift e

scatter_plot(mse_errors, "MSE Errors Daily")
scatter_plot(reduced_transmission, "Reduced Transmission Daily")
scatter_plot(mse_errors_2day, "MSE Errors Every Second Day")
scatter_plot(reduced_transmission_2day, "Reduced Transmission Every Second Day")
scatter_plot(mse_errors_3day, "MSE Errors Every Third Day")
scatter_plot(reduced_transmission_3day, "Reduced Transmission Every Third Day")
