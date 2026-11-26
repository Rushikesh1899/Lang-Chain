from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline


llm = HuggingFacePipeline.from_model_id(
    model_id="maxwell-model/Maxwell-V1-Flash",
    task = "text-generation",
    pipeline_kwargs=dict(
        temprature=0.5,
        max_new_tokens=100
    )
)
model = ChatHuggingFace(llm)

result = model.invoke("What is the Capital of USA?")

print(result.content)