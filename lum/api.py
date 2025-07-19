import requests
import time
import json
import hmac
import hashlib
import asyncio
import websockets

BASE_URL = "https://lumen.onl/api/v1"
#BASE_URL = "http://localhost:8000/api/v1"

async def listen_for_token(device_code: str, expires_in: int):
    if BASE_URL.startswith("https://"):
        ws_scheme = "wss"
        ws_host_port = BASE_URL[len("https://"):]
    else:
        ws_scheme = "ws"
        ws_host_port = BASE_URL[len("http://"):]
    
    ws_host = ws_host_port.split('/')[0]
    uri = f"{ws_scheme}://{ws_host}/ws/cli/authorize/{device_code}"
    
    try:
        async with websockets.connect(uri) as websocket:
            print("   Waiting for authorization...")
            try:
                message = await asyncio.wait_for(websocket.recv(), timeout=expires_in)
                data = json.loads(message)
                if "token" in data:
                    return data["token"]
                return None
            except asyncio.TimeoutError:
                return None
            except websockets.exceptions.ConnectionClosed:
                return None
    except Exception:
        return None

def perform_login():
    try:
        response = requests.post(f"{BASE_URL}/cli/device-auth", timeout=10)
        response.raise_for_status()
        data = response.json()
        
        device_code = data['device_code']
        user_code = data['user_code']
        verification_uri = data['verification_uri']
        expires_in = data['expires_in']

        print(f"\n1. Please go to: {verification_uri}")
        print(f"2. And enter this code: {user_code}\n")
        
        return asyncio.run(listen_for_token(device_code, expires_in))

    except requests.RequestException as e:
        print(f"Error during login: {e}")
        if e.response:
            try:
                print(f"   Response: {e.response.json()}")
            except json.JSONDecodeError:
                print(f"   Response: {e.response.text}")
        return None

def submit_contribution(pat: str, codebase: str):
    if not pat:
        print("Error: You must be logged in to contribute.")
        return False

    try:
        headers = {"Authorization": f"Bearer {pat}"}
        handshake_res = requests.post(f"{BASE_URL}/cli/handshake", headers=headers, timeout=10)
        handshake_res.raise_for_status()
        challenge = handshake_res.text.strip('"')

        timestamp = str(int(time.time()))
        body = json.dumps({"codebase": codebase}).encode('utf-8')
        
        body_hash = hashlib.sha256(body).hexdigest()
        string_to_sign = f"{challenge}:{timestamp}:{body_hash}".encode()
        
        secret = pat.encode()
        signature = hmac.new(secret, string_to_sign, hashlib.sha256).hexdigest()

        contrib_headers = {
            "Authorization": f"Bearer {pat}",
            "Content-Type": "application/json",
            "X-Lumen-Challenge": challenge,
            "X-Lumen-Timestamp": timestamp,
            "X-Lumen-Signature": signature
        }

        contrib_res = requests.post(f"{BASE_URL}/cli/contribute", headers=contrib_headers, data=body, timeout=60)
        contrib_res.raise_for_status()

        return contrib_res.json()

    except requests.RequestException as e:
        print(f"Error during contribution: {e}")
        if e.response:
            print(f"   Response: {e.response.json()}")
        return None

def get_history(pat: str):
    if not pat:
        print("Error: You must be logged in to view history.")
        return None

    try:
        headers = {"Authorization": f"Bearer {pat}"}
        response = requests.get(f"{BASE_URL}/cli/contributions/history", headers=headers, timeout=15)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        print(f"Error fetching history: {e}")
        if e.response:
            print(f"   Response: {e.response.json()}")
        return None