from llama_index import (
    SimpleDirectoryReader,
    VectorStoreIndex,
    ServiceContext,
)
from llama_index.llms import LlamaCPP
from llama_index.llms.llama_utils import (
    messages_to_prompt,
    completion_to_prompt,
)

from llama_index import set_global_tokenizer
from transformers import AutoTokenizer
from llama_index.embeddings import HuggingFaceEmbedding

embed_model = HuggingFaceEmbedding(model_name="BAAI/bge-small-en-v1.5")

llm = LlamaCPP(
    # optionally, you can set the path to a pre-downloaded model instead of model_url
    model_path="mistral-7b-instruct-v0.1.Q6_K.gguf",
    temperature=0.75,
    max_new_tokens=256,
    # llama2 has a context window of 4096 tokens, but we set it lower to allow for some wiggle room
    context_window=3900,
    # kwargs to pass to __call__()
    generate_kwargs={},
    # kwargs to pass to __init__()
    # set to at least 1 to use GPU
    model_kwargs={"n_gpu_layers": 1},
    # messages_to_prompt=messages_to_prompt,
    # completion_to_prompt=completion_to_prompt,
    verbose=True,
)

set_global_tokenizer(
    AutoTokenizer.from_pretrained("NousResearch/Llama-2-7b-chat-hf").encode
)

service_context = ServiceContext.from_defaults(
    llm=llm,
    embed_model=embed_model,
)

documents = SimpleDirectoryReader("./files").load_data()


index = VectorStoreIndex.from_documents(documents, service_context=service_context)
persistence = index.storage_context.persist(persist_dir="./persist")

print(persistence)
