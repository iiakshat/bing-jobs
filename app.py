import Scraper as sc
from flask import Flask, render_template, request, send_file
import json

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/scrape', methods=['POST'])
def scrape():
    url = request.form.get('url')
    data = sc.find_jobs(url)
    json_file_path = 'Jobs/output.json'
    with open(json_file_path, 'w') as json_file:
        json.dump(data, json_file)

    return send_file(json_file_path, as_attachment=True, download_name='output.json')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)