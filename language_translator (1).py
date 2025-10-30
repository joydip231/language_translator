# language_translator.py
# Simple Language Translator App using Python

from googletrans import Translator

def translate_text(text, target_language):
    """
    Translates given text to the target language.
    Example target_language: 'en' for English, 'fr' for French, 'hi' for Hindi, etc.
    """
    translator = Translator()
    translated = translator.translate(text, dest=target_language)
    return translated.text

def main():
    print("🌐 Simple Language Translator App 🌐")
    print("------------------------------------")

    # List of sample language codes
    print("Examples of language codes:")
    print("en = English, fr = French, hi = Hindi, es = Spanish, de = German, ja = Japanese\n")

    # Input text from user
    text = input("Enter text to translate: ")
    target_language = input("Enter target language code (e.g. 'fr', 'hi', 'es'): ")

    # Translate
    try:
        translated_text = translate_text(text, target_language)
        print(f"\n✅ Translated Text ({target_language}): {translated_text}")
    except Exception as e:
        print("\n❌ Error:", e)

if __name__ == "__main__":
    main()
