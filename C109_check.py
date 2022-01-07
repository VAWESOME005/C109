import pandas as pd
import statistics

df = pd.read_csv("data.csv")

weight = df["Weight(Pounds)"].tolist()

weight_mean = statistics.mean(weight)
weight_median = statistics.median(weight)
weight_mode = statistics.mode(weight)

print("Mean:", weight_mean)

print("Median:", weight_median)

print("Mode:", weight_mode)

weight_sd = statistics.stdev(weight)

print("Standard Deviation:", weight_sd)

weight_sd1_start = weight_mean - weight_sd
weight_sd1_end = weight_mean + weight_sd

weight_sd2_start = weight_mean - (2*weight_sd)
weight_sd2_end = weight_mean + (2*weight_sd)

weight_sd3_start = weight_mean - (3*weight_sd)
weight_sd3_end = weight_mean + (3*weight_sd)

weight_data_within_1sd = [result for result in weight if result > weight_sd1_start and result < weight_sd1_end]

weight_data_within_2sd = [result for result in weight if result > weight_sd2_start and result < weight_sd2_end]

weight_data_within_3sd = [result for result in weight if result > weight_sd3_start and result < weight_sd3_end]

percent_weight_data_within_1sd = (len(weight_data_within_1sd) / len(weight)) * 100
print("The percent of the data within the 1st standard deviation is ", percent_weight_data_within_1sd)
percent_weight_data_within_2sd = (len(weight_data_within_2sd) / len(weight)) * 100
print("The percent of the data within the 2nd standard deviation is ", percent_weight_data_within_2sd)
percent_weight_data_within_3sd = (len(weight_data_within_3sd) / len(weight)) * 100
print("The percent of the data within the 3rd standard deviation is ", percent_weight_data_within_3sd)