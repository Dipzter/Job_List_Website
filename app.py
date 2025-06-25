from flask import Flask
from flask import request

jobs = []

app = Flask(__name__)

@app.route("/")
def home():
    return "Welcome to your Job Tracker! "

@app.route("/add_job")
def add_job():
    # Get 'company' and 'title' from request.args
    # If both exist, append them as a dict to the 'jobs' list
    # Return a confirmation message
    # Else, return a "Missing data" error message
    company = request.args.get("company")
    title = request.args.get("title")
    if company and title:
        jobs.append({"company" : company,
                     "title" : title})
        return f"Job added: {company} -- {title}"
    else:
        return "Missing title or company name"
        
@app.route("/jobs")
def list_jobs():
    # If jobs is empty, return "No jobs yet."
    # Otherwise, loop through and return jobs formatted with <br>
    if not jobs:
        return "No jobs added or program run yet"
    else:
        job_list = "<br>".join(f"{j["company"]} - {j["title"]}" for j in jobs)
        return f"<h2>Tracked Jobs</h2>{job_list}"

if __name__ == "__main__":
    app.run(debug = True)