import requests
import sys

def test_website_connection(url):
    print(f"Connecting to {url}...")
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        print("Website loaded successfully!")
    except requests.exceptions.RequestException as e:
        print(f"Failed to load website: {e}")
        return False

    return True

if __name__ == "__main__":
    if len(sys.argv) < 2:
        url = "https://atg.world"
    else:
        url = sys.argv[1]

    if test_website_connection(url):
        print("Test passed")
    else:
        print("Test failed")
