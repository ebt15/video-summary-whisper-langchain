import pathlib
import textwrap
from langchain.chat_models import ChatOpenAI
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.chains.summarize import load_summarize_chain
from langchain.docstore.document import Document


class SummaryGenerator:
    def __init__(self, model='gpt-3.5-turbo-16k', temperature=0, chunk_size=60000, chunk_overlap=20):
        self.llm = ChatOpenAI(temperature=temperature, model=model)
        self.text_splitter = RecursiveCharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap)

    def load_document(self, document_text):
        # Load the document
        # document_text = pathlib.Path(file_path).read_text()
        texts = self.text_splitter.split_text(document_text)

        return [Document(page_content=t) for t in texts[:4]]

    def generate_summary(self, docs):
        # Load the summarization chain
        chain = load_summarize_chain(self.llm, chain_type="refine")

        return chain.run(docs)

    def wrap_text(self, text, width=100):
        return textwrap.fill(text, width=width)

    def summarize_document(self, document_text):
        print("Loading document...")
        docs = self.load_document(document_text)

        print("Generating summary...")
        summary = self.generate_summary(docs)

        print("Wrapping text...")
        return self.wrap_text(summary)


if __name__ == "__main__":
    summary_generator = SummaryGenerator()
    wrapped_summary = summary_generator.summarize_document('meeting_doc.txt')
    print("Summary:")
    print(wrapped_summary)