print("="*60)
print("GROQ MODELS")
print("="*60)
try:
    from groq import Groq
    from config import GROQ_KEY
    groq_client = Groq(api_key=GROQ_KEY)
    response = groq_client.models.list()
    for model in response.data:
        print(model.id)
except Exception as e:
    print(f"Error: {e}")

print("\n" + "="*60)
print("GEMINI MODELS")
print("="*60)
try:
    from google import genai
    from config import GEMINI_KEY
    gemini_client = genai.Client(api_key=GEMINI_KEY)
    for model in gemini_client.models.list():
        print(model.name)
except Exception as e:
    print(f"Error: {e}")

print("\n" + "="*60)
print("MISTRAL MODELS")
print("="*60)
try:
    from mistralai import Mistral
    from config import MISTRAL_KEY
    mistral_client = Mistral(api_key=MISTRAL_KEY)
    response = mistral_client.models.list()
    for model in response.data:
        print(model.id)
except Exception as e:
    print(f"Error: {e}")

print("\n" + "="*60)
print("COHERE MODELS")
print("="*60)
try:
    import cohere
    from config import COHERE_KEY
    cohere_client = cohere.ClientV2(api_key=COHERE_KEY)
    response = cohere_client.models.list()
    for model in response.models:
        print(model.name)
except Exception as e:
    print(f"Error: {e}")

print("\n" + "="*60)
print("Done")
print("="*60)