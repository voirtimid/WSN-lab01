import matplotlib.pyplot as plt


def read_data(filename):
    f = open(filename, "r")
    measured_data = [float(line) for line in f]

    measured_data_every_2day = [measured_data[i] for i in range(len(measured_data)) if i % 2 == 0]
    measured_data_every_3day = [measured_data[i] for i in range(len(measured_data)) if i % 3 == 0]

    return measured_data, measured_data_every_2day, measured_data_every_3day


def scatter_plot(data1, data2):
    plt.scatter(data1, data2, alpha=0.5)
    plt.title('Scatter plot pythonspot.com')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.show()


def plot(data1, data2, data3, ylabel):
    plt.subplot(xlabel='Threshold',
                ylabel=ylabel,
                title='Data for temperature in Skopje for the last 15 days!')
    sorted_list = sorted(data1.items())
    x, y = zip(*sorted_list)
    plt.plot(x, y,
             color='red',
             label='moving_average (1)',
             marker='o')

    sorted_list = sorted(data2.items())
    x, y = zip(*sorted_list)
    plt.plot(x, y,
             color='green',
             label='moving_average (2)',
             marker='o')

    sorted_list = sorted(data3.items())
    x, y = zip(*sorted_list)
    plt.plot(x, y,
             color='blue',
             label='moving_average (3)',
             marker='o')
    plt.legend(loc='best')

    plt.show()


def dual_prediction_schema(data1, data2, moving_average_factor, thresholds1, thresholds2):
    mse_errors = {}
    reduced_transmission = {}

    for threshold1 in thresholds1:
        for threshold2 in thresholds2:
            counter = 0
            predicted_values_1 = []
            predicted_values_2 = []
            mse_values = []

            for i in range(len(data1)):
                if i < moving_average_factor:
                    predicted_values_1.append(data1[i])
                    predicted_values_2.append(data2[i])
                    counter += 1
                else:
                    extracted_data_1 = predicted_values_1[i - moving_average_factor:i]
                    extracted_data_2 = predicted_values_2[i - moving_average_factor:i]
                    prediction_1 = round(sum(extracted_data_1) / moving_average_factor, 3)
                    prediction_2 = round(sum(extracted_data_2) / moving_average_factor, 3)
                    prediction_error_1 = abs(prediction_1 - data1[i])
                    prediction_error_2 = abs(prediction_2 - data2[i])
                    if prediction_error_1 >= threshold1 and prediction_error_2 >= threshold2:
                        counter += 1
                        predicted_values_1.append(data1[i])
                        predicted_values_2.append(data2[i])
                        mse_values.append(pow(prediction_error_1, 2) + pow(prediction_error_2, 2))
                    else:
                        predicted_values_1.append(prediction_1)
                        predicted_values_2.append(prediction_2)

            mse_errors[str(threshold1) + ":" + str(threshold2)] = round(sum(mse_values) / len(mse_values), 3)
            reduced_transmission[str(threshold1) + ":" + str(threshold2)] = round(((counter * 1.0 / len(data1)) * 100), 2)

    return mse_errors, reduced_transmission
