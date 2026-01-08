from sklearn.feature_extraction.text import CountVectorizer
import re

def calculate_ats_score(resume, jd):
    vectorizer = CountVectorizer().fit_transform([resume, jd])
    vectors = vectorizer.toarray()

    similarity = (vectors[0] @ vectors[1]) / (
        (vectors[0] @ vectors[0]) ** 0.5 * (vectors[1] @ vectors[1]) ** 0.5
    )

    return round(similarity * 100, 2)

def extract_skills(resume, skill_list):
    found = []
    for skill in skill_list:
        if re.search(rf"\b{skill.lower()}\b", resume.lower()):
            found.append(skill)
    return found

def extract_education(resume):
    keywords = ["b.tech", "bachelor", "master", "msc", "diploma", "phd", "SSC", "HSC"]
    return [k for k in keywords if k in resume.lower()]

def extract_experience(resume):
    return "Experience section detected" if "experience" in resume.lower() else "No experience section found"

