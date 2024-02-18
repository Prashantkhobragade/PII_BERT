from flask import Flask, request, jsonify
from src.anonymization import anonymize_text

app = Flask(__name__)

@app.route('/anonymize', methods=['POST'])
def anonymize_email():
    if request.method == 'POST':
        data = request.get_json()
        email_text = data.get('email_text', '')

        anonymized_text = anonymize_text(email_text)

        response = {
            'anonymized_text': anonymized_text
        }
        return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
