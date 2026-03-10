import json
from email_validator import validate_email,EmailNotValidError
from datetime import datetime
errors =[]
with open("./data/candidate.json", "r") as json_file:
    candidates = json.load(json_file)
def validate_candidate(candidates):
    seen_ids = set()
    emails = set()
    for candidate in candidates:
        required_fields = ["name", "job_title", "skills", "summary", "education"]
        for field in required_fields:
            if not candidate[field]:
                errors.append(f"{field} is empty")
        if candidate["id"] not in seen_ids:
            seen_ids.add(candidate["id"])
        else:
            error = "The ID already exists"
            errors.append(error)
        try:
            validate_email(candidate["email"],check_deliverability=False)
        except EmailNotValidError:
            error = "The email is not valid"
            errors.append(error)
        if candidate["email"] not in emails:
            emails.add(candidate["email"])
        else:
            error = "The Email already exists"
            errors.append(error)
validate_candidate(candidates)
if errors:
    for error in errors:
        print(error)
else:
    print("Validation passed")
with open("./data/jobs.json", "r") as json_file:
    jobs = json.load(json_file)
def validate_job(jobs):
    seen_ids = set()
    for job in jobs:
        required_fields = ["company", "job_title", "skills_required", "job_desc", "date_posted"]
        for field in required_fields:
            if not job[field]:
                errors.append(f"{field} is empty")
        if job["id"] not in seen_ids:
            seen_ids.add(job["id"])
        else:
            error = "The ID already exists"
            errors.append(error)
        try:
            datetime.strptime(job["date_posted"], "%Y-%m-%d")
        except ValueError:
            error = "The date format is wrong"
            errors.append(error)
validate_job(jobs)
if errors:
    for error in errors:
        print(error)
else:
    print("Validation passed")





       

            
    





