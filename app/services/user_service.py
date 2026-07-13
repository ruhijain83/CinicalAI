import httpx

def get_user():
    response = httpx.get(
        "https://jsonplaceholder.typicode.com/users/1"
    )
    return response.json()