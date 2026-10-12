print("Merhaba Git!")
print("İlk Git projemi oluşturuyorum.")

jobs = [
    {"id": 1, "company": "Jotform", "position": "Backend Intern"},
    {"id": 2, "company": "Trendyol", "position": "Software Intern"}
]

for job in jobs:
    print(job["company"], "-", job["position"])