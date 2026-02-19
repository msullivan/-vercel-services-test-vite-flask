# Cipher Tool

A web app for encoding and decoding text. Vanilla JS frontend with a Flask backend.

## Operations

- **ROT13** — classic letter substitution
- **Base64 Encode / Decode**
- **ROT8000** — ROT13 for Unicode (rotates through ~55k codepoints)

## Project structure

```
frontend/       Vite + vanilla JS
backend/        Flask API
```

## Local development

The easiest way to run everything is with the Vercel CLI:

```sh
export VERCEL_USE_EXPERIMENTAL_SERVICES=1
vc dev
```

This starts both the frontend and backend together, just like production.

Alternatively, you can run them separately:

Start the backend:

```sh
cd backend
python -m venv ../.venv
source ../.venv/bin/activate
pip install -r requirements.txt
python app.py
```

Start the frontend (in a separate terminal):

```sh
cd frontend
npm install
npm run dev
```

The Vite dev server runs on http://localhost:5173 and proxies `/_/backend` requests to Flask on port 5000.

## API

All endpoints accept `POST` with `{"text": "..."}` and return `{"result": "..."}`.

| Endpoint | Description |
|---|---|
| `/_/backend/api/rot13` | ROT13 |
| `/_/backend/api/base64encode` | Base64 encode |
| `/_/backend/api/base64decode` | Base64 decode |
| `/_/backend/api/rot8000` | ROT8000 |
