from llama_cpp import Llama

llm = Llama(model_path="./models/llama-2-13b-chat.ggmlv3.q4_1.bin")

resp = llm("what and who are you if I may ask ?")

print(resp["choices"][0]["text"])


