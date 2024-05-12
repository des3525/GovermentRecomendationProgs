# import os
# import time


# from llama_index import VectorStoreIndex, SimpleDirectoryReader

# documents = SimpleDirectoryReader('/home/user/ЛГТУ/Практика/App/app/data').load_data()
# index = VectorStoreIndex.from_documents(documents)
# index.save_to_disk("/store")
# query_engine = index.as_query_engine()
# response = query_engine.query("Получи заголовок файла 2.pdf")
# print(response)
# time.sleep(30)
# response = query_engine.query("Получи краткое описание 2.pdf")
# print(response)
# time.sleep(30)
# response = query_engine.query("Получи условия участия 2.pdf")
# print(response)

import os
from llama_index import VectorStoreIndex, SimpleDirectoryReader, StorageContext, load_index_from_storage
import openai
from dotenv import load_dotenv

load_dotenv()

class ModelClass:
    def __init__(self):
        self.loadToStore()
        self.initialise_index()
    
    def loadToStore(self):
        print("Loading files in the load directory...")

        documents = SimpleDirectoryReader(
            input_dir=os.environ["LOAD_DIR"]).load_data()
        index = VectorStoreIndex.from_documents(documents)

        index.storage_context.persist(os.environ["INDEX_FILE"])
        print("Done.")

    def initialise_index(self):
        global index
        if os.path.exists(os.environ["INDEX_FILE"]):
            storage_context = StorageContext.from_defaults(persist_dir=os.environ["INDEX_FILE"])
            index = load_index_from_storage(storage_context)
        else:
            documents = SimpleDirectoryReader(os.environ["LOAD_DIR"]).load_data()
            index = VectorStoreIndex.from_documents(documents)
    
    def query(self, filename):
         global index
         query_engine = index.as_query_engine()
         resp = query_engine.query("Предоставь как можно больше условия участия (conditions) в программе в форате JSON, если их нет, то отдай пустой JSON. Файл для поиска: %s.Язык ответа русский. Формат ответа: \{name: Название программы, conditions1:текст, conditions2:текст \}" % filename)
         print(resp)
         return resp