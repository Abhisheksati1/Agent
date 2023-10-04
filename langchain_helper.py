from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.chains import SequentialChain
from secret_key import openapi_key
import os

os.environ['OPENAI_API_KEY'] = openapi_key



def genrate_restaurant_name_and_items(cuisine):
    llm = OpenAI(temperature=0.6)
    prompt_template_name = PromptTemplate(
  input_variables = ['cuisine'],
  template = "I want to open a returant for {cuisine} food. Suggest a fency name for this."
)
    name_chain = LLMChain(llm=llm, prompt=prompt_template_name, output_key="restaurant_name")

    llm = OpenAI(temperature=0.7)

    prompt_template_items = PromptTemplate(
        input_variables = ['restaurant_name'],
        template = "Suggest me some food item for {restaurant_name}."
    )
    
    food_item_chain = LLMChain(llm=llm, prompt=prompt_template_items, output_key="menu_items")
    
    chain = SequentialChain(
        chains = [name_chain, food_item_chain],
        input_variables = ['cuisine'],
        output_variables = ['restaurant_name', 'menu_items']
    )

    response = chain({'cuisine':cuisine})
    print(response)

    return response

if __name__ == "__main__":
    print(genrate_restaurant_name_and_items("Italian"))
