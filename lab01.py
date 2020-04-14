import matplotlib.pyplot as plt

f = open("dataset", "r")
measured_data = [float(line) for line in f]

measured_data_every_2day = [measured_data[i] for i in range(len(measured_data)) if i % 2 == 0]
measured_data_every_3day = [measured_data[i] for i in range(len(measured_data)) if i % 3 == 0]

print(f"Length of measured data is: {len(measured_data)}")
# print(measured_data)

plt.subplot(xlabel='Single measure',
            ylabel="Temperature",
            title='Data for temperature in Skopje for the last 15 days!')
plt.plot(measured_data)
plt.show()

thresholds = [round(i * 0.5, 1) for i in range(20)]
print(f"Thresholds: {thresholds}")


def dual_prediction_schema(data, moving_average_factor):
    mse_errors = {}
    reduced_transmission = {}

    for threshold in thresholds:
        counter = 0
        predicted_values = []
        mse_values = []

        for i in range(len(data)):
            if i < moving_average_factor:
                predicted_values.append(data[i])
                counter += 1
            else:
                extracted_data = predicted_values[i - moving_average_factor:i]
                prediction = round(sum(extracted_data) / moving_average_factor, 3)
                prediction_error = abs(prediction - data[i])
                if prediction_error >= threshold:
                    counter += 1
                    predicted_values.append(data[i])
                    mse_values.append(prediction_error)
                else:
                    predicted_values.append(prediction)

        mse_errors[threshold] = round(sum(mse_values) / len(mse_values), 3)
        reduced_transmission[threshold] = round(((counter * 1.0 / len(data)) * 100), 2)

    return mse_errors, reduced_transmission


mse_errors_1, reduced_transmission_1 = dual_prediction_schema(measured_data, 1)
# print(f"MSE errors: {mse_errors_1}")
# print(f"% reduced_transmissions: {reduced_transmission_1}")
mse_errors_1_2day, reduced_transmission_1_2day = dual_prediction_schema(measured_data_every_2day, 1)
mse_errors_1_3day, reduced_transmission_1_3day = dual_prediction_schema(measured_data_every_3day, 1)

mse_errors_2, reduced_transmission_2 = dual_prediction_schema(measured_data, 2)
mse_errors_2_2day, reduced_transmission_2_2day = dual_prediction_schema(measured_data_every_2day, 2)
mse_errors_2_3day, reduced_transmission_2_3day = dual_prediction_schema(measured_data_every_3day, 2)

mse_errors_3, reduced_transmission_3 = dual_prediction_schema(measured_data, 3)
mse_errors_3_2day, reduced_transmission_3_2day = dual_prediction_schema(measured_data_every_2day, 3)
mse_errors_3_3day, reduced_transmission_3_3day = dual_prediction_schema(measured_data_every_3day, 3)


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


def plot_reduced_transmissions_freq_1():
    plot(reduced_transmission_1,
         reduced_transmission_2,
         reduced_transmission_3,
         "% in reduced transmissions (freq 1)")


def plot_mse_errors_freq_1():
    plot(mse_errors_1,
         mse_errors_2,
         mse_errors_3,
         "Average MSE error (freq 1)")


def plot_reduced_transmissions_freq_2():
    plot(reduced_transmission_1_2day,
         reduced_transmission_2_2day,
         reduced_transmission_3_2day,
         "% in reduced transmissions (freq 2)")


def plot_mse_errors_freq_2():
    plot(mse_errors_1_2day,
         mse_errors_2_2day,
         mse_errors_3_2day,
         "Average MSE error (freq 2)")


def plot_reduced_transmissions_freq_3():
    plot(reduced_transmission_1_3day,
         reduced_transmission_2_3day,
         reduced_transmission_3_3day,
         "% in reduced transmissions (freq 3)")


def plot_mse_errors_freq_3():
    plot(mse_errors_1_3day,
         mse_errors_2_3day,
         mse_errors_3_3day,
         "Average MSE error (freq 3)")


# plot_reduced_transmissions_freq_1()
# plot_reduced_transmissions_freq_2()
# plot_reduced_transmissions_freq_3()
# plot_mse_errors_freq_1()
# plot_mse_errors_freq_2()
# plot_mse_errors_freq_3()
