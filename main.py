# 1
scores = [72, 85, 90, 68, 88]

print("Scores:", scores)

average = sum(scores) / len(scores)
print("Average score:", average)

print("Highest score:", max(scores))
print("Lowest score:", min(scores))


# 2
study_hours = [1, 2, 3, 4, 5]
exam_scores = [50, 55, 65, 70, 80]

for hours, score in zip(study_hours, exam_scores):
    print(f"Input: {hours} hours → Output: {score} marks")


# 3
def pass_fail(score):
    if score >= 60:
        return "Pass"
    else:
        return "Fail"

scores = [45, 67, 82, 59]

for s in scores:
    print(f"Score: {s} → Result: {pass_fail(s)}")


# 4
sizes = [500, 800, 1000, 1200]
prices = [50, 80, 100, 130]

for size, price in zip(sizes, prices):
    print(f"House size: {size} sq ft → Price: {price}")

positive_trend = True

for i in range(1, len(prices)):
    if prices[i] <= prices[i - 1]:
        positive_trend = False
        break

if positive_trend:
    print("Positive trend")


# 5
study_hours = [2, 4, 6, 8]
scores = [55, 65, 75, 85]

increases = []
for i in range(1, len(scores)):
    increases.append(scores[i] - scores[i - 1])

average_increase = sum(increases) / len(increases)
print("Average increase per 2 hours:", average_increase)

last_score = scores[-1]
predicted_score = last_score + average_increase

print("Predicted score for 10 hours of study:", predicted_score)


# 6
scores = [35, 58, 62, 74, 89, 45]

for score in scores:
    if score < 50:
        category = "Low"
    elif 50 <= score <= 70:
        category = "Medium"
    else:
        category = "High"

    print(f"Score: {score}, Category: {category}")


# 7
ages = [18, 20, 22, 24, 26]
heights = [160, 165, 170, 175, 180]

for age, height in zip(ages, heights):
    print(f"Age: {age}, Height: {height} cm")

average_age = sum(ages) / len(ages)
print(f"\nAverage Age: {average_age}")

average_height = sum(heights) / len(heights)
print(f"Average Height: {average_height} cm")

print("\nObservation: Height appears to increase as age increases in this dataset.")
