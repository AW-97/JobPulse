import requests
import json

API_URL = "https://remotive.com/api/remote-jobs"


def fetch_jobs():
    response = requests.get(API_URL)

    print("STATUS:", response.status_code)

    if response.status_code != 200:
        print("Błąd API")
        return []

    data = response.json()
    return data["jobs"]


def filter_jobs(jobs):
    keywords = ["devops", "aws", "cloud", "kubernetes"]
    filtered = []

    for job in jobs:
        title = job.get("title", "").lower()
        description = job.get("description", "").lower()
        tags = " ".join(job.get("tags", [])).lower()

        text = title + " " + description + " " + tags

        if any(k in text for k in keywords):
            filtered.append(job)

    return filtered


def save_jobs(jobs):
    with open("jobs.json", "w", encoding="utf-8") as f:
        json.dump(jobs, f, indent=2)


def main():
    jobs = fetch_jobs()

    print("Pobrano:", len(jobs))

    filtered = filter_jobs(jobs)

    print("Po filtrze:", len(filtered))

    save_jobs(filtered)

    print("Zapisano do jobs.json")


if __name__ == "__main__":
    main()
