from llama_index import (
    load_index_from_storage,
    ServiceContext,
    StorageContext,
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
    temperature=0.1,
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
service_context = ServiceContext.from_defaults(
    llm=llm,
    embed_model=embed_model,
)
storage_context = StorageContext.from_defaults(persist_dir="./persist")

index = load_index_from_storage(storage_context=storage_context, service_context=service_context)


query_engine = index.as_query_engine()
response = query_engine.query(
    """ 
<s>[INST] NVDA is the stock for Nvidia, according to the documents answer about the stock, 
the stock is currently at a high price:
[/INST]

What are the odds of a pullback?
When the pullback will happen in days?

Answer the questions in JSON format, using the following schema:                      

{
    "pullback_odds": (int),
    "pullback_days": (int)
}
                              
                              
"""
)
print(response)
