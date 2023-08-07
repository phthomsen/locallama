# locallama

Download Llama-2 from [huggingface](https://huggingface.co/TheBloke/Llama-2-13B-chat-GGML/tree/main), see if it runs locally with llama_cpp and [LangChain](https://python.langchain.com/docs/get_started/introduction.html).

## installation

Some [hints](https://python.langchain.com/docs/integrations/llms/llamacpp) for installing `llama-cpp-python` with metal support etc:

`CMAKE_ARGS="-DLLAMA_METAL=on" FORCE_CMAKE=1 pip install --upgrade --force-reinstall llama-cpp-python --no-cache-dir`
