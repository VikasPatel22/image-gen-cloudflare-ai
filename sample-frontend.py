import requests

# 🔗 Replace with your worker URL
API_URL = "https://your-worker-domain.com/"  
API_KEY = "YOUR_API_KEY_HERE"  

# The prompt you want to generate
prompt = "A futuristic cityscape at sunset, cinematic lighting"

# Send POST request
headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {API_KEY}"
}

data = {
    "prompt": prompt
}

try:
    response = requests.post(API_URL, headers=headers, json=data)
    response.raise_for_status()  # Raise an error if status != 200

    # Save the image
    with open("generated_image.jpg", "wb") as f:
        f.write(response.content)

    print("✅ Image saved as generated_image.jpg")

except requests.exceptions.HTTPError as e:
    # If the worker returns a JSON error
    try:
        error = response.json()
        print("Error:", error.get("error"), "-", error.get("details"))
    except:
        print("HTTP Error:", e)
except Exception as e:
    print("Failed to fetch image:", e)
