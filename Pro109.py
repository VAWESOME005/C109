import pandas as pd
import statistics as stats

df = pd.read_csv("pro_data.csv")

math_scores = df["math score"].tolist()

scores_mean = stats.mean(math_scores)
scores_median = stats.median(math_scores)
scores_mode = stats.mode(math_scores)

print(scores_mean, scores_median, scores_mode)

scores_sd = stats.stdev(math_scores)

print(scores_sd)

sd1_start = scores_mean - scores_sd
sd1_end = scores_mean + scores_sd

sd2_start = scores_mean - (2*scores_sd)
sd2_end = scores_mean + (2*scores_sd)

sd3_start = scores_mean - (3*scores_sd)
sd3_end = scores_mean + (3*scores_sd)

data_within_sd1 = [result for result in math_scores if result > sd1_start and result < sd1_end]
data_within_sd2 = [result for result in math_scores if result > sd2_start and result < sd2_end]
data_within_sd3 = [result for result in math_scores if result > sd3_start and result < sd3_end]

percent_data_within_sd1 = (len(data_within_sd1) / len(math_scores)) * 100

percent_data_within_sd2 = (len(data_within_sd2) / len(math_scores)) * 100

percent_data_within_sd3 = (len(data_within_sd3) / len(math_scores)) * 100

print("1st standard deviation percentage is ", percent_data_within_sd1)

print("2nd standard deviation percentage is ", percent_data_within_sd2)

print("3rd standard deviation percentage is ", percent_data_within_sd3)