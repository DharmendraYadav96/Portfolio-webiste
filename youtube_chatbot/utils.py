from youtube_transcript_api import YouTubeTranscriptApi, TranscriptsDisabled
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_community.vectorstores import FAISS
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel, RunnablePassthrough, RunnableLambda

video_id = "eWiBLgxOcW0" # only the ID, not full URL


def extract_video_id(youtube_url):
    if "watch?v=" in youtube_url:
        return youtube_url.split("watch?v=")[-1].split("&")[0]
    elif "youtu.be/" in youtube_url:
        return youtube_url.split("youtu.be/")[-1]
    else:
        return None

def get_transcript(video_id):
    try:
        # If you don’t care which language, this returns the “best” one
        transcript_list = YouTubeTranscriptApi.get_transcript(video_id, languages=["en"])
        names = []
        for chunk in transcript_list:
            names.append(chunk["text"])   
    
        return " ".join(names)

    except TranscriptsDisabled:
        print("No captions available for this video.")

def summarize_transcript(transcript):
    # Text splitting
    splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    chunks = splitter.create_documents([transcript])

    # Embedding generation
    embeddings = OpenAIEmbeddings(model="text-embedding-3-small")

    # storing in vectorstore
    vector_store = FAISS.from_documents(chunks, embeddings)

    # Retrieval
    retriever = vector_store.as_retriever(search_type="similarity", search_kwargs={"k": 4})


    llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.2)
    prompt = PromptTemplate(
        template="""
        You are a helpful assistant.
        Answer ONLY from the provided transcript context.
        If the context is insufficient, just say you don't know.

        {context}
        Question: {question}
        """,
        input_variables = ['context', 'question']
    )

    parser = StrOutputParser()


    def format_docs(retrieved_docs):
        context_text = "\n\n".join(doc.page_content for doc in retrieved_docs)
        return context_text

    parallel_chain = RunnableParallel({
        'context': retriever | RunnableLambda(format_docs),
        'question': RunnablePassthrough()
    })

    final_chain = parallel_chain | prompt | llm | parser
    return final_chain.invoke('Can you summarize the video')



