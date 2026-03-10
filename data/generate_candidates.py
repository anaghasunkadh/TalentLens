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
def candidate(id):
    id = random.randint(1,1000)
    name =faker.name()
    email = faker.email()
    job_title = random.choice(job_titles)
    years_of_experience= random.randint(1,20)
    skills= random.sample(skills_pool,5)
    education = random.choice(["bachelor","masters","Phd"])
    skilllist = ", ".join(skills)
    summary = f"A {job_title} with {years_of_experience} years of experience, skilled in {skilllist}, holding a {education} degree."
    return {
        "id":id,
        "name":name,
        "email":email,
        "job_title":job_title,
        "years_of_experience":years_of_experience,
        "skills":skills,
        "education":education,
        "summary":summary
    }

candidates = []
for i in range(500):
    candidates.append(candidate(i))
with open('./data/candidate.json','w') as json_file:
    json.dump(candidates,json_file,indent = 4)