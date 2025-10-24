def personalized_greeting(name):
    """Создает персональное приветствие"""
    if not name or name.strip() == "":
        return "Hello, there!"
    return f"Hello, {name.strip()}!"

def main():
    print(hello_world())

if __name__ == "__main__":
    main()
