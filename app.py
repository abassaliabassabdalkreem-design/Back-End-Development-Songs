from flask import Flask, jsonify, request

app = Flask(__name__)

songs_list = [
    {"id": "1", "title": "Song One", "artist": "Artist A", "lyrics": "La la la"},
    {"id": "2", "title": "Song Two", "artist": "Artist B", "lyrics": "Na na na"},
]

@app.route('/health')
def health():
    return jsonify({"status": "OK"}), 200

@app.route('/count')
def count():
    return jsonify({"count": len(songs_list)}), 200

@app.route('/song', methods=['GET'])
def get_all_songs():
    return jsonify(songs_list), 200

@app.route('/song/<id>', methods=['GET'])
def get_song_by_id(id):
    for song in songs_list:
        if song["id"] == id:
            return jsonify(song), 200
    return jsonify({"message": "Song not found"}), 404

@app.route('/song', methods=['POST'])
def add_song():
    new_song = request.get_json()
    songs_list.append(new_song)
    return jsonify(new_song), 201

@app.route('/song/<id>', methods=['PUT'])
def update_song(id):
    updated = request.get_json()
    for song in songs_list:
        if song["id"] == id:
            song.update(updated)
            return jsonify(song), 200
    return jsonify({"message": "Song not found"}), 404

@app.route('/song/<id>', methods=['DELETE'])
def delete_song(id):
    global songs_list
    songs_list = [s for s in songs_list if s["id"] != id]
    return jsonify({"message": "Song deleted"}), 200

if __name__ == '__main__':
    app.run(debug=True, port=5001)