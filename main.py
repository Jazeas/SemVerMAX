def hello_world(language="en"):
    """Базовая функция Hello World с поддержкой языков"""
    greetings = {
        "en": "Hello, World!",
        "es": "¡Hola, Mundo!",
        "fr": "Bonjour, Monde!",
        "de": "Hallo, Welt!"
    }
    return greetings.get(language, "Hello, World!")

def personalized_greeting(name, language="en"):
    """Создает персональное приветствие"""
    greetings = {
        "en": "Hello, {}!",
        "es": "¡Hola, {}!",
        "fr": "Bonjour, {}!",
        "de": "Hallo, {}!"
    }
    
    if not name or name.strip() == "":
        template = greetings.get(language, "Hello, there!")
        return template.replace("{}", "there")
    
    template = greetings.get(language, "Hello, {}!")
    return template.format(name.strip())

def get_supported_languages():
    """Возвращает список поддерживаемых языков"""
    return ["en", "es", "fr", "de"]

def main():
    print(hello_world())
    print(personalized_greeting("Alice"))
    print(f"Supported languages: {', '.join(get_supported_languages())}")

if __name__ == "__main__":
    main()
