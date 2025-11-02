from flask import Flask, render_template, request, jsonify
import openai
import numpy as np
import json

app = Flask(__name__)
collected_keywords = []
# Set up OpenAI API credentials
openai.api_key = ''


# Define the default route to return the index.html file
@app.route("/")
def index():
    return render_template("index.html")

# Define a new route for the dashboard
@app.route("/dashboard")
def dashboard():
        # Generate sample data for the chart (replace this with your actual data)
    labels = list(range(1, 11))  # X-axis labels
    data = list(np.random.randint(1, 10, size=10))  # Y-axis data points

    return render_template("dashboard.html", labels=labels, data=data)


# Define the /api route to handle POST requests
@app.route("/api", methods=["POST"])
def api():
    # Get the message from the POST request
    message = request.json.get("message")
    # Send the message to OpenAI's API and receive the response
    
    
    completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "user", "content": message}
    ]
    )
    if completion.choices[0].message!=None:
        return completion.choices[0].message

    else :
        return 'Failed to Generate response!'
    
# Define a route to receive messages from the chatbot
@app.route("/api/chatbot", methods=["POST"])
def chatbot():
    message = request.json.get("message")

    # Add code to analyze the message and extract keywords
    keywords = extract_keywords(message)

    # Append the keywords to the collected_keywords list
    collected_keywords.extend(keywords)

    # Send a response to the chatbot
    response = generate_response(message)
    return jsonify({"response": response})

# Define a new route to provide the analyzed data as JSON
@app.route("/api/get_analyzed_data")
def get_analyzed_data():
    with open('analyzed_data.json', 'r') as infile:
        analyzed_data = json.load(infile)
    return jsonify(analyzed_data)



if __name__=='__main__':
    app.run()


