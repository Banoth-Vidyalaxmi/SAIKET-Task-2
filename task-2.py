import requests

def fetch_joke():
    # Step 1: Choose a public API (Official Joke API)
    url = "https://official-joke-api.appspot.com/random_joke"
    
    try:
        # Step 2: Fetch data from the API
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad responses
        
        # Step 3: Parse the JSON data
        data = response.json()
        setup = data.get("setup")
        punchline = data.get("punchline")
        
        # Step 4: Display data in user-friendly format
        print("\n😂 Here's a Random Joke for You 😂")
        print("---------------------------------")
        print(f"👉 {setup}")
        print(f"🤣 {punchline}")
        print("---------------------------------\n")
    
    except requests.exceptions.RequestException as e:
        print("❌ Error fetching data from the API:", e)

# Step 5: Test the program
if __name__ == "__main__":
    fetch_joke()
