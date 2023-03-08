# Difference between .items(), .values(), and .key()
obj = {'name': "Martins",
	   'age': 27, 
       'height': 172.2, 
       'skincolor': "Black", 
       'hobbies':["chess", "swimming", "coding", "tiktoks"]
    }
print("Keys and values:")
for key, val in obj.items():
    print(f"{key}: {val}")
print("values:")
for val in obj.values():
    print(f"{val}")
print("keys:")
for key in obj.keys():
    print(f"{key}")

print(obj)
print(obj["hobbies"])

for key in obj:
    print(key)