

def headers(token):
    return { 'Authorization': f'Bearer {token}', 'content-type': 'application/json'}

flight_data = { "name": "American airline"}
user_data = {
    'email': 'myadminss@example.com',
    'username': 'myadminss',
    'is_staff': True,
    "password":"education",
}