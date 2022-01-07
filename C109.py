# import pandas as pd
# import statistics

# df = pd.read_csv("data.csv")

# height = df["Height(Inches)"].tolist()

# height_mean = statistics.mean(height)
# height_median = statistics.median(height)
# height_mode = statistics.mode(height)

# print("Mean:", height_mean)

# print("Median:", height_median)

# print("Mode:", height_mode)

# height_sd = statistics.stdev(height)

# print("Standard Deviation:", height_sd)

# height_sd1_start = height_mean - height_sd
# height_sd1_end = height_mean + height_sd

# height_sd2_start = height_mean - (2*height_sd)
# height_sd2_end = height_mean + (2*height_sd)

# height_sd3_start = height_mean - (3*height_sd)
# height_sd3_end = height_mean + (3*height_sd)

# height_data_within_1sd = [result for result in height if result > height_sd1_start and result < height_sd1_end]

# height_data_within_2sd = [result for result in height if result > height_sd2_start and result < height_sd2_end]

# height_data_within_3sd = [result for result in height if result > height_sd3_start and result < height_sd3_end]

# percent_height_data_within_1sd = (len(height_data_within_1sd) / len(height)) * 100
# print("The percent of the data within the 1st standard deviation is ", percent_height_data_within_1sd)
# percent_height_data_within_2sd = (len(height_data_within_2sd) / len(height)) * 100
# print("The percent of the data within the 2nd standard deviation is ", percent_height_data_within_2sd)
# percent_height_data_within_3sd = (len(height_data_within_3sd) / len(height)) * 100
# print("The percent of the data within the 3rd standard deviation is ", percent_height_data_within_3sd)

