from main import read_data
from main import dual_prediction_schema
from main import scatter_plot

temperature_data, temperature_data_2day, temperature_data_3day = read_data("temperature_data")
humidity_data, humidity_data_2day, humidity_data_3day = read_data("humidity_data")

temperature_thresholds = [round(i, 1) for i in range(10)]
humidity_thresholds = [round(i, 1) for i in range(10)]


def plot(moving_average_factor, label):
    mse_errors, reduced_transmission = dual_prediction_schema(temperature_data,
                                                              humidity_data,
                                                              moving_average_factor,
                                                              temperature_thresholds,
                                                              humidity_thresholds)

    mse_errors_2day, reduced_transmission_2day = dual_prediction_schema(temperature_data_2day,
                                                                        humidity_data_2day,
                                                                        moving_average_factor,
                                                                        temperature_thresholds,
                                                                        humidity_thresholds)

    mse_errors_3day, reduced_transmission_3day = dual_prediction_schema(temperature_data_3day,
                                                                        humidity_data_3day,
                                                                        moving_average_factor,
                                                                        temperature_thresholds,
                                                                        humidity_thresholds)

    scatter_plot(mse_errors, f"MSE Errors Daily - {label}")
    scatter_plot(reduced_transmission, f"Reduced Transmission Daily - {label}")
    scatter_plot(mse_errors_2day, f"MSE Errors Every Second Day - {label}")
    scatter_plot(reduced_transmission_2day, f"Reduced Transmission Every Second Day - {label}")
    scatter_plot(mse_errors_3day, f"MSE Errors Every Third Day - {label}")
    scatter_plot(reduced_transmission_3day, f"Reduced Transmission Every Third Day - {label}")


plot(1, "Moving Average 1")
plot(2, "Moving Average 2")
plot(3, "Moving Average 3")
