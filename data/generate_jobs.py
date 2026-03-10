import random
import json
import os
from faker import Faker
faker = Faker()
job_titles = [
        "Data Engineer", "Data Scientist", "Machine Learning Engineer",
        "Software Engineer", "Backend Developer", "Frontend Developer",
        "Full Stack Developer", "DevOps Engineer", "Cloud Architect",
        "Data Analyst", "Business Intelligence Analyst", "Product Manager",
        "Project Manager", "UX Designer", "Cybersecurity Analyst",
        "Database Administrator", "AI Research Scientist", "Site Reliability Engineer",
        "Systems Analyst", "Solutions Architect"
    ]
skills_pool = [
        "Python", "JavaScript", "TypeScript", "React", "Node.js",
        "FastAPI", "Django", "SQL", "PostgreSQL", "MongoDB",
        "Elasticsearch", "Docker", "Kubernetes", "AWS", "Azure",
        "GCP", "TensorFlow", "PyTorch", "Scikit-learn", "Pandas",
        "NumPy", "Tableau", "Power BI", "Spark", "Kafka",
        "Airflow", "Git", "Linux", "REST APIs", "CI/CD"
    ]
def job(id):
    id = id
    company =faker.company()
    job_title = random.choice(job_titles)
    years_of_experience= random.randint(1,20)
    skills_required= random.sample(skills_pool,5)
    skilllist = ", ".join(skills_required)
    job_desc = f"We are looking for a {job_title} with at least {years_of_experience} years of experience, proficient in {skilllist}, to join {company}."
    date_posted = faker.date_between(start_date='-4y',end_date='-1w').isoformat()
    return {
        "id":id,
        "company":company,
        "job_title":job_title,
        "years_of_experience":years_of_experience,
        "skills_required":skills_required,
        "job_desc":job_desc,
        "date_posted":date_posted
    }

jobs = []
for i in range(500):
    jobs.append(job(i))
with open('./data/jobs.json','w') as json_file:
    json.dump(jobs,json_file,indent = 4)