# MeshMap FR — production entry point
import json
import sqlite3
from pathlib import Path
from flask import Flask, render_template, request, jsonify, abort

BASE_DIR = Path(__file__).resolve().parent
DB_PATH = BASE_DIR / "data" / "meshmap.db"

app = Flask(__name__)




def get_db():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    conn = get_db()
    conn.execute("""
        CREATE TABLE IF NOT EXISTS networks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            city TEXT NOT NULL,
            region TEXT,
            lat REAL NOT NULL,
            lon REAL NOT NULL,
            status TEXT DEFAULT 'active',
            nodes INTEGER DEFAULT 0,
            website TEXT,
            contact TEXT,
            description TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)
    conn.commit()
    conn.close()


def seed_if_empty():
    conn = get_db()
    count = conn.execute("SELECT COUNT(*) FROM networks").fetchone()[0]
    if count == 0:
        seed_file = BASE_DIR / "data" / "seed_networks.json"
        if seed_file.exists():
            data = json.loads(seed_file.read_text(encoding="utf-8"))
            for n in data:
                conn.execute("""
                    INSERT INTO networks
                    (name, city, region, lat, lon, status, nodes, website, contact, description)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                """, (n["name"], n["city"], n.get("region"), n["lat"], n["lon"],
                      n.get("status", "active"), n.get("nodes", 0), n.get("website"),
                      n.get("contact"), n.get("description")))
            conn.commit()
    conn.close()


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/api/networks")
def api_networks():
    conn = get_db()
    rows = conn.execute("SELECT * FROM networks ORDER BY name").fetchall()
    conn.close()
    return jsonify([dict(r) for r in rows])


@app.route("/api/networks", methods=["POST"])
def api_add_network():
    data = request.get_json(force=True)
    required = ["name", "city", "lat", "lon"]
    for f in required:
        if f not in data:
            return jsonify({"error": f"missing field: {f}"}), 400
    try:
        lat = float(data["lat"]); lon = float(data["lon"]); nodes = int(data.get("nodes", 0))
    except (TypeError, ValueError):
        return jsonify({"error": "lat/lon must be numbers, nodes must be int"}), 400
    if not (-90 <= lat <= 90) or not (-180 <= lon <= 180):
        return jsonify({"error": "lat/lon out of range"}), 400

    conn = get_db()
    cur = conn.execute("""
        INSERT INTO networks
        (name, city, region, lat, lon, status, nodes, website, contact, description)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (data["name"], data["city"], data.get("region"), lat, lon,
          data.get("status", "active"), nodes, data.get("website"),
          data.get("contact"), data.get("description")))
    conn.commit()
    new_id = cur.lastrowid
    conn.close()
    return jsonify({"id": new_id}), 201


@app.route("/network/<int:nid>")
def network_detail(nid):
    conn = get_db()
    row = conn.execute("SELECT * FROM networks WHERE id = ?", (nid,)).fetchone()
    conn.close()
    if row is None:
        abort(404)
    return render_template("network.html", network=dict(row))


@app.route("/submit")
def submit():
    return render_template("submit.html")


@app.route("/about")
def about():
    return render_template("about.html")



# Run init + seed at module level so gunicorn picks them up (no __main__).
init_db()
seed_if_empty()
if __name__ == "__main__":
    init_db()
    seed_if_empty()
    print("MeshMap FR running on http://127.0.0.1:5000")
    app.run(host="127.0.0.1", port=5000, debug=True)


