import requests
import matplotlib.pyplot as plt

url = "https://api.slingacademy.com/v1/sample-data/files/student-scores.json"

try:
    response = requests.get(url, timeout=60)
    print("Status code:", response.status_code)

    response.raise_for_status()
    data = response.json()

    print("Data type:", type(data))
    print(data.keys() if isinstance(data, dict) else type(data))

except requests.exceptions.Timeout:
    print("The server took too long to respond. Please try again.")

except requests.exceptions.RequestException as error:
    print("Request failed:", error)

print("Number of records:", len(data))
print("First record:", data[0])
print("Fields:", data[0].keys())
student_names = []
averages = []

for student in data:
    average = (
        student["math_score"]
        + student["history_score"]
        + student["physics_score"]
        + student["chemistry_score"]
        + student["biology_score"]
        + student["english_score"]
    ) / 6

    print(student["first_name"], student["last_name"], average)
    student_names.append(student["first_name"])
    averages.append(average)


plt.bar(student_names, averages)
plt.title("Average Student Test Scores")
plt.xlabel("Student Names")
plt.ylabel("Average Scores")
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()