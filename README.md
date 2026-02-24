# 🚀 Edge Diffusion AI

Secure AI Image Generation at the Edge using Cloudflare Workers and Stable Diffusion XL.

This project provides a production-ready Cloudflare Worker that generates AI images using:

@cf/stabilityai/stable-diffusion-xl-base-1.0

Built with:
- Cloudflare Workers
- Cloudflare AI
- Secure API key authentication
- CORS enabled
- Edge-first architecture

---

## 🌍 Live Endpoint

```
https://your_worker_domain.workers.dev/
```

---

# 🧠 How It Works

Client → Cloudflare Worker → Cloudflare AI (Stable Diffusion XL) → JPEG Image Response

- Only POST requests allowed
- API Key required via Authorization header
- Returns image/jpeg
- Fully CORS-enabled
- Runs globally at the edge

---

# 🔐 Authentication

All requests must include:

```
Authorization: Bearer YOUR_API_KEY
```

The API key is stored securely as a Cloudflare Worker environment variable.

---

# 📦 Request Format

### Method
POST

### Headers
```
Content-Type: application/json
Authorization: Bearer YOUR_API_KEY
```

### Body
```json
{
  "prompt": "A futuristic city floating in the sky"
}
```

---

# 🖼 Response

### Success
- Status: 200
- Content-Type: image/jpeg
- Binary image output

### Errors

| Status | Message |
|--------|----------|
| 400 | Prompt is required |
| 401 | Unauthorized |
| 405 | Not allowed |
| 500 | Failed to generate image |

---

# 💻 Usage Examples

---

## 🐍 Python Example

```python
import requests

url = "https://your_worker_domain.workers.dev/"
api_key = "YOUR_API_KEY"

response = requests.post(
    url,
    headers={
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    },
    json={
        "prompt": "Cyberpunk samurai in neon city"
    }
)

if response.status_code == 200:
    with open("output.jpg", "wb") as f:
        f.write(response.content)
    print("Image saved as output.jpg")
else:
    print(response.json())
```

---

## 🌐 JavaScript (Browser)

```javascript
async function generateImage() {
  const response = await fetch("https://your_worker_domain.workers.dev/", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      "Authorization": "Bearer YOUR_API_KEY"
    },
    body: JSON.stringify({
      prompt: "Astronaut riding a horse on Mars"
    })
  });

  const blob = await response.blob();
  const imgURL = URL.createObjectURL(blob);

  document.getElementById("result").src = imgURL;
}
```

---

## 🖥 Node.js

```javascript
import fetch from "node-fetch";
import fs from "fs";

const response = await fetch("https://your_worker_domain.workers.dev/", {
  method: "POST",
  headers: {
    "Content-Type": "application/json",
    "Authorization": "Bearer YOUR_API_KEY"
  },
  body: JSON.stringify({
    prompt: "AI-powered futuristic temple"
  })
});

const buffer = await response.arrayBuffer();
fs.writeFileSync("output.jpg", Buffer.from(buffer));
```

---

## 💻 cURL Example

```bash
curl -X POST https://your_worker_domain.workers.dev/ \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"prompt":"Dragon flying over mountains"}' \
  --output output.jpg
```

---

# ⚙ Deployment Guide

## 1️⃣ Install Wrangler

```
npm install -g wrangler
```

## 2️⃣ Login

```
wrangler login
```

## 3️⃣ Set API Key Secret

```
wrangler secret put API_KEY
```

## 4️⃣ Deploy

```
wrangler deploy
```

---

# 🏗 Architecture

- Edge-first execution
- Zero server management
- Global CDN distribution
- Secure environment variable storage
- AI inference via Cloudflare AI

---

# 🔥 Why This Matters

Traditional AI servers:
- High latency
- Expensive infrastructure
- Manual scaling

Edge AI:
- Global low-latency execution
- No server management
- Automatic scaling
- Built-in CDN security

---

# 📜 License

MIT License

---

# 🎯 Future Improvements

- Rate limiting
- Usage analytics
- Prompt logging (secure)
- Multi-model support
- SDK package

---

Built for developers building intelligent edge-native systems.
