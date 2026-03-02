def greet(name, excited=False):
    if not excited:
        return f"Hello, {name}!"
    else:
        return f"Hello, {name}! How are you today?"

if __name__ == "__main__":
    print(greet("World"))
    print(greet("Velcriphone", excited=True))