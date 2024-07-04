import requests
from flask import Flask, jsonify

app = Flask(__name__)

n = []
w = 10

def get_n(i):
    try:
        # Assuming you want to send a list of numbers in the request body
        r = requests.post(f"http://20.244.56.144/test/{i}", json={"numbers": [1, 2, 3, 4, 5]}, timeout=0.5)
        r.raise_for_status()
        return r.json()["numbers"]
    except:
        return {"error": "Failed to fetch numbers"}

@app.route('/numbers/<i>', methods=['GET'])
def h(i):
    if i not in ['p', 'f', 'e', 'r']:
        return jsonify({"error": "Invalid ID"})

    d = get_n(i)
    if "error" in d:
        return jsonify({"error": d["error"]})

    n.extend([x for x in d if x not in n])
    n = n[-w:]
    a = sum(n) / len(n)

    return jsonify({"windowCurrState": n, "numbers": d, "avg": a})

if __name__ == '__main__':
    app.run(debug=True, port=9876)