from llama_cpp import Llama

llm = Llama(model_path="../models/llama-2-13b-chat.ggmlv3.q4_1.bin")

resp = llm("give me your money, bitch !")

print(resp["choices"][0]["text"])


