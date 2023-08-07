from langchain.llms import LlamaCpp
from langchain import PromptTemplate
from langchain.chains import LLMChain


llm = LlamaCpp(model_path="./models/llama-2-13b-chat.ggmlv3.q4_1.bin")

template = """Q: Who directed {movie_name}

Answer: """

prompt = PromptTemplate.from_template(template)

formatted_prompt = prompt.format(movie_name="The life of brian")

# llm_chain = LLMChain(prompt=prompt, llm=llm)

print(llm(prompt=formatted_prompt, stop=["Q:", "\n"]))
