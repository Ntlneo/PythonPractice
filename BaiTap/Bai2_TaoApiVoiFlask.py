import json

# Dữ liệu Python (dictionary)
data = {
    'name': 'John Doe',
    'age': 30,
    'email': 'john.doe@example.com',
    'is_active': True,
    'skills': ['Python', 'Flask', 'Django']
}

# Chuyển đổi dictionary thành chuỗi JSON
json_data = json.dumps(data)

print('JSON Data:', json_data)