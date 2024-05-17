import sys
import google.generativeai as genai
import read_and_write

API_KEY = read_and_write.read_from_hidden_file()
if(API_KEY == ""):
    API_KEY = read_and_write.write_to_hidden_file()

genai.configure(api_key=API_KEY)
model = genai.GenerativeModel(model_name="gemini-1.5-flash-latest")

PROMPT_CASE = "Give output in brief and clean way, with minimal mention to refrences, this is a cli interface for gnome-terminal. \n"

def generate_response(prompt):
    """Generates a response using the generative model."""
    full_prompt = PROMPT_CASE + prompt
    response = model.generate_content(full_prompt)
    return response.text

def main():
    input_prompt = input("Enter your prompt: ")
    # prompt = sys.argv
    response = generate_response(input_prompt)
    print(response)

if __name__ == "__main__":
    main()


