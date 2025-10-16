from flask import Flask, request, jsonify
import os
import psycopg2

app = Flask(__name__)

DB_HOST = os.environ.get("DB_HOST", "db")
DB_PORT = int(os.environ.get("DB_PORT", 5432))
DB_NAME = os.environ.get("DB_NAME", "main")
DB_USER = os.environ.get("DB_USER", "main")
DB_PASS = os.environ.get("DB_PASS", "main")

def get_conn():
    return psycopg2.connect(
        host=DB_HOST, port=DB_PORT, dbname=DB_NAME, user=DB_USER, password=DB_PASS
    )

@app.route("/user", methods=["GET"])
def get_user():
    """
    GET /user?username=alice
    Retourne l'utilisateur correspondant au username fourni.
    """
    username = request.args.get("username", "").strip()
    if not username:
        return jsonify({"error": "paramètre 'username' requis"}), 400

    sql = "SELECT * FROM users WHERE username = '" + username + "';"
    print(sql)
    with get_conn() as conn:
        with conn.cursor() as cur:
            cur.execute(sql)
            row = cur.fetchone()

    if row is None:
        return jsonify(None), 404

    return jsonify(row), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
