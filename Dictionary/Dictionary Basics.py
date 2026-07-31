d = {}

d["apple"] = 10      # Add

d["apple"] += 1      # Update

print(d["apple"])    # Access

if "apple" in d:     # Check key
    print("Exists")

for key in d:        # Iterate keys
    print(key, d[key])