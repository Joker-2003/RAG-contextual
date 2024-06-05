from flask import Flask, request, render_template, jsonify
from dotenv import load_dotenv
from utils import store_docs, get_response, get_chroma_client

# Load the OPENAI KEY from the env.sh file
load_dotenv('env.sh')  # Specify path to your env file

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    data = request.json
    url = data['url']
    organization_name = data['organization_name']
    organization_info = data['organization_info']
    contact_info = data['contact_info']

    # Store webpage content into vector store
    store_docs(url)

    return jsonify({'message': 'Content processed successfully!'})

@app.route('/ask', methods=['POST'])
def ask():
    data = request.json
    question = data['question']
    organization_name = data['organization_name']
    organization_info = data['organization_info']
    contact_info = data['contact_info']

    # Get response
    response = get_response(question, organization_name, organization_info, contact_info)
    return jsonify({'answer': response})

if __name__ == "__main__":
    app.run(debug=True)
