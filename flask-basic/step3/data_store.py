import os

DATA_FILE = "messages.txt"

def save_message(name, comment):
    with open(DATA_FILE, "a", encoding="utf-8") as f:
        f.write(f"{name}\t{comment}\n")

def load_messages():
    messages = []
    if not os.path.exists(DATA_FILE):
        return messages

    with open(DATA_FILE, "r", encoding="utf-8") as f:
        for line in f:
            name, comment = line.strip().split("\t")
            messages.append({"name": name, "comment": comment})
    return messages

def search_by_name(keyword):
    results = []
    messages = load_messages()
    for m in messages:
        if keyword in m["name"]:
            results.append(m)
    return results


