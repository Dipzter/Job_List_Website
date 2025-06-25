from flask import Flask, request, render_template, redirect

jobs = []

app = Flask(__name__)

@app.route("/")
def home():
    return "Welcome to your Job Tracker! "

@app.route("/add_job")
def add_job():
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
    return render_template("jobs.html", jobs = jobs)

if __name__ == "__main__":
    app.run(debug = True)