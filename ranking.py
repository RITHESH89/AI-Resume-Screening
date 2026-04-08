from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
from resume_parser import extract_text

model = SentenceTransformer("all-MiniLM-L6-v2")

def rank_resumes(files, job_desc):
    job_embedding = model.encode([job_desc])

    scores = []

    for file in files:
        resume_text = extract_text(file)
        resume_embedding = model.encode([resume_text])

        score = cosine_similarity(job_embedding, resume_embedding)[0][0]
        scores.append((file.name, float(score)))

    scores.sort(key=lambda x: x[1], reverse=True)
    return scores
