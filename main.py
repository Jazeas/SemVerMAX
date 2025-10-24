def hello_world():
    """Базовая функция Hello World"""
    return "Hello, World!"

def personalized_greeting(name):
    """Создает персональное приветствие"""
    if not name or name.strip() == "":
        return "Hello, there!"
    return f"Hello, {name.strip()}!"

def main():
    print(hello_world())
    print(personalized_greeting("Alice"))

if __name__ == "__main__":
    main()
