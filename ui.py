import asyncio
import os
from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import edge_tts

# Nama folder untuk menyimpan hasil audio
OUTPUT_DIR = "output"

app = Flask(__name__)
# Mengizinkan UI (yang dibuka dari file) untuk mengakses server ini
CORS(app)

# Membuat folder output jika belum ada
if not os.path.exists(OUTPUT_DIR):
    os.makedirs(OUTPUT_DIR)

# Endpoint utama untuk generate audio
@app.route('/generate-speech', methods=['POST'])
def handle_generate_speech():
    try:
        data = request.json
        text = data.get('text')
        voice = data.get('voice')
        filename = data.get('filename')

        if not all([text, voice, filename]):
            return jsonify({"error": "Teks, suara, dan nama file tidak boleh kosong."}), 400
        
        # Membersihkan nama file agar aman
        safe_filename = "".join(c for c in filename if c.isalnum() or c in (' ', '.', '_')).rstrip()
        if not safe_filename.lower().endswith('.mp3'):
            safe_filename += '.mp3'
        
        output_path = os.path.join(OUTPUT_DIR, safe_filename)

        # Menjalankan fungsi async edge-tts dari dalam Flask
        asyncio.run(create_audio(text, voice, output_path))
        
        print(f"Sukses! Audio disimpan di: {output_path}")
        # Mengirim kembali path file agar bisa di-download oleh UI
        return jsonify({
            "message": "Audio berhasil dibuat!",
            "filePath": f"/{OUTPUT_DIR}/{safe_filename}"
        })

    except Exception as e:
        print(f"Terjadi error: {e}")
        return jsonify({"error": str(e)}), 500

# Endpoint untuk mengunduh file yang sudah dibuat
@app.route('/output/<filename>')
def download_file(filename):
    return send_from_directory(OUTPUT_DIR, filename, as_attachment=True)


# Fungsi inti untuk memanggil edge-tts
async def create_audio(text: str, voice: str, output_path: str):
    communicate = edge_tts.Communicate(text, voice)
    await communicate.save(output_path)


if __name__ == '__main__':
    print("Server siap di http://localhost:5050")
    print("Buka file index.html di browser Anda untuk memulai.")
    app.run(port=5050, debug=True)