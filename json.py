import json

json_data = """
    {
        "firstname" : "Jaka",
        "lastname" : "Antara",
        "city" : "Jakarta",
        "country" : "Indonesia",
        "country_code" : "ID",
        "email" : "jakaantara@gmail.com"
    }
"""

python_data = json.loads(json_data)

print(type(python_data))
print(python_data)

print(python_data['firstname'], python_data['lastname'])