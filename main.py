def hello_world():
    """Базовая функция Hello World"""
    return "Hello, World!"

def personalized_greeting(name):
    """Создает персональное приветствие"""
    if not name:
        return "Hello, there!"
    return f"Hello, {name}!"

def main():
    print(hello_world())
    print(personalized_greeting("Alice"))

if __name__ == "__main__":
    main()
