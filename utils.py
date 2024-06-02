from langchain_openai import ChatOpenAI
from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings
from text_to_doc import get_doc_chunks
from web_crawler import get_data_from_website
from prompt import get_prompt
from langchain.chains import ConversationalRetrievalChain


def get_chroma_client():
    """
    Returns a chroma vector store instance.

    Returns:
        langchain.vectorstores.chroma.Chroma: ChromaDB vector store instance.
    """
    embedding_function = OpenAIEmbeddings()
    return Chroma(
        collection_name="website_data",
        embedding_function=embedding_function,
        persist_directory="data/chroma")


def store_docs(url):
    """
    Retrieves data from a website, processes it into document chunks, and stores them in a vector store.

    Args:
        url (str): The URL of the website to retrieve data from.

    Returns:
        None
    """
    text, metadata = get_data_from_website(url)
    docs = get_doc_chunks(text, metadata)
    vector_store = get_chroma_client()
    vector_store.add_documents(docs)
    vector_store.persist()

