from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <html>
    <head>
        <title>Anshika Gupta | AI Engineer</title>
        <style>
            body{
                font-family:Arial, sans-serif;
                background:#111827;
                color:white;
                margin:50px;
                line-height:1.6;
            }

            h1{
                color:#60a5fa;
            }

            h2{
                color:#93c5fd;
                margin-top:30px;
            }

            .card{
                background:#1f2937;
                padding:20px;
                border-radius:10px;
                margin-top:15px;
            }

            ul{
                margin-left:20px;
            }

            a{
                color:#60a5fa;
                text-decoration:none;
            }
        </style>
    </head>

    <body>

        <h1>Anshika Gupta</h1>
        <h3>AI Engineer | Full Stack Developer | AI & ML Student</h3>

        <div class="card">
            <h2>About Me</h2>
            <p>
                Third-year B.Tech Computer Science (AI & ML) student at
                ATLAS SkillTech University with experience building
                enterprise AI systems, full-stack applications,
                production backend services, and intelligent automation.
            </p>
        </div>

        <div class="card">
            <h2>Education</h2>
            <p>
                B.Tech Computer Science (AI & ML)<br>
                ATLAS SkillTech University<br>
                CGPA: 9.55
            </p>
        </div>

        <div class="card">
            <h2>Experience</h2>

            <h3>BWE Studio</h3>

            <ul>
                <li>Built enterprise AI platforms including Council and REGOS</li>
                <li>Worked with React, Next.js, Supabase and PostgreSQL</li>
                <li>Implemented authentication, backend APIs and AI integrations</li>
                <li>Integrated payment systems and deployed Android applications</li>
            </ul>

            <h3>Unicornis AI</h3>

            <ul>
                <li>Optimized Text-to-Speech inference latency</li>
                <li>Worked with ONNX Runtime, FastAPI and streaming pipelines</li>
            </ul>

        </div>

        <div class="card">

            <h2>Projects</h2>

            <ul>
                <li>Council – Enterprise Multi-Agent AI Platform</li>
                <li>REGOS – AI Regulatory Intelligence Platform</li>
                <li>TechMentor AI</li>
                <li>PullUp Ride Sharing App</li>
                <li>WHO Health Digital Twin</li>
                <li>ExoDetect</li>
            </ul>

        </div>

        <div class="card">

            <h2>Skills</h2>

            <p>

            Python • C++ • Java • React • Next.js • TypeScript •
            FastAPI • Flask • Django • PostgreSQL • Firebase •
            Supabase • Docker • AWS • OpenAI API • Claude • Gemini •
            RAG • AI Agents • Machine Learning • Computer Vision

            </p>

        </div>

        <div class="card">

            <h2>Achievements</h2>

            <ul>
                <li>Springer Research Publication</li>
                <li>IEEE YESIST12 Finalist</li>
                <li>Stanford CS231N Coursework</li>
                <li>Daniel Bourke Deep Learning (PyTorch)</li>
            </ul>

        </div>

        <div class="card">

            <h2>Contact</h2>

            <p>Email: anshikaa.akg19@gmail.com</p>
            <p>Location: Mumbai, India</p>

        </div>

    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(debug=True)
