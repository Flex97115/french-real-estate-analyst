from langchain_community.vectorstores import FAISS
from langchain_core.documents import Document
from langchain_openai import OpenAIEmbeddings
import os
import yaml
from langchain_community.document_loaders import PyPDFLoader


def __load_yml_columns_description():
    with open(os.path.join(os.path.dirname(__file__), 'ressources', 'description.yml'), 'r') as f:
        description = yaml.safe_load(f)
        return description["models"][0]["columns"]


def __pdf_notice_to_documents():
    loader = PyPDFLoader(os.path.join(os.path.dirname(__file__), 'ressources', 'notice_dvf.pdf'))
    return loader.load_and_split()


def __yaml_description_to_document():
    columns = __load_yml_columns_description()
    return [Document(page_content=__columns_to_string(columns))]


def __columns_to_string(columns):
    header = "There is all custom columns description of the CSV file : "
    content = [f'Column name: {c["name"]}, description: {c["description"]}. ' for i, c in enumerate(columns)]
    return header + " ".join(content)


def build_vector_retriever():
    yaml_docs = __yaml_description_to_document()
    pdf_docs = __pdf_notice_to_documents()

    docs = yaml_docs + pdf_docs

    embeddings = OpenAIEmbeddings()
    db = FAISS.from_documents(docs, embeddings)
    return db.as_retriever()
