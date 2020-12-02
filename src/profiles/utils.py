import uuid


def get_random_string():
    code = str(uuid.uuid4())[:8].replace('-', '').lower()
    return code
