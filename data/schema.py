from pydantic import BaseModel
from typing import List
from datetime import date
class Candidate(BaseModel):
    id:int
    name:str
    email:str
    job_title:str
    years_of_experience: int
    skills:List[str]
    education:str
    summary:str
class JobPosting(BaseModel):
    id:int
    company:str
    job_title:str
    skills_required:List[str]
    years_required:int
    job_desc:str
    date_posted:date
