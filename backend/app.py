import base64
import codecs

from flask import Blueprint, Flask, jsonify, request

app = Flask(__name__)
bp = Blueprint("api", __name__, url_prefix="/_/backend")

# ---------------------------------------------------------------------------
# ROT8000 lookup table
# ---------------------------------------------------------------------------
# Valid Unicode BMP ranges (excludes whitespace, control chars, surrogates)
_VALID_RANGES = [
    (33, 126),
    (161, 5759),
    (5761, 8191),
    (8203, 8231),
    (8234, 8238),
    (8240, 8286),
    (8288, 12287),
    (12289, 55295),
    (57344, 65535),
]

_rot8000_map: dict[int, str] = {}


def _build_rot8000_table() -> None:
    valid_codepoints: list[int] = []
    for start, end in _VALID_RANGES:
        valid_codepoints.extend(range(start, end + 1))
    total = len(valid_codepoints)
    half = total // 2
    for i, cp in enumerate(valid_codepoints):
        rotated = valid_codepoints[(i + half) % total]
        _rot8000_map[cp] = chr(rotated)


_build_rot8000_table()


def rot8000(text: str) -> str:
    return "".join(_rot8000_map.get(ord(c), c) for c in text)


# ---------------------------------------------------------------------------
# Routes
# ---------------------------------------------------------------------------
@bp.post("/api/rot13")
def api_rot13():
    data = request.get_json(force=True)
    text = data.get("text", "")
    return jsonify(result=codecs.encode(text, "rot_13"))


@bp.post("/api/base64encode")
def api_base64encode():
    data = request.get_json(force=True)
    text = data.get("text", "")
    encoded = base64.b64encode(text.encode("utf-8")).decode("utf-8")
    return jsonify(result=encoded)


@bp.post("/api/base64decode")
def api_base64decode():
    data = request.get_json(force=True)
    text = data.get("text", "")
    try:
        decoded = base64.b64decode(text).decode("utf-8")
    except Exception:
        return jsonify(error="Invalid Base64 input"), 400
    return jsonify(result=decoded)


@bp.post("/api/rot8000")
def api_rot8000():
    data = request.get_json(force=True)
    text = data.get("text", "")
    return jsonify(result=rot8000(text))


app.register_blueprint(bp)

if __name__ == "__main__":
    app.run(debug=True)
