from google import genai
import prompt
import external_knowledge

API_KEY = "AIzaSyBP6fzZIo6mU-ly1brLr3U5dlT0E43aUaI"


client = genai.Client(api_key=API_KEY)





def generate_response(user_query):

    full_prompt = f"""

    You are a customer support assistant at a chicken station. Answer the user query:
    {user_query}. Based on the following info:
    {prompt} 
    "The restaurant menu items are as follows:"
    {external_knowledge.MENU_TWO}  {external_knowledge.MENU_ONE} 
    {external_knowledge.MENU_THREE} {external_knowledge.MENU_FOUR}
    {external_knowledge.MENU_FIVE}"""


    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=full_prompt,
    )
    return response.text

