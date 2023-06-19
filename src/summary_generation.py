import textwrap
from langchain.chat_models import ChatOpenAI
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.chains.summarize import load_summarize_chain
from langchain.docstore.document import Document
from langchain.prompts import PromptTemplate

class SummaryGenerator:
    def __init__(self, model='gpt-3.5-turbo', temperature=0, chunk_size=8000, chunk_overlap=20):
        self.llm = ChatOpenAI(temperature=temperature, model=model)
        self.text_splitter = RecursiveCharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap)

    def load_document(self, document_text):
        # Load the document texts
        texts = self.text_splitter.split_text(document_text)

        return [Document(page_content=t) for t in texts[:4]]

    def generate_summary(self, docs, summary_type="concise"):
        if summary_type == "detailed":
            return self.generate_detailed_summary(docs)
        # Load the summarization chain
        chain = load_summarize_chain(self.llm, chain_type="refine")

        return chain.run(docs)

    def generate_detailed_summary(self, docs):
        prompt_template = """Write a detailed summary of the following extracting the key information:

                            {text}

                            DETAILED SUMMARY:"""
        PROMPT = PromptTemplate(template=prompt_template, 
                                input_variables=["text"])

        refine_template = (
            "Your job is to produce a final summary\n"
            "We have provided an existing summary up to a certain point: {existing_answer}\n"
            "We have the opportunity to refine the existing summary"
            "(only if needed) with some more context below.\n"
            "------------\n"
            "{text}\n"
            "------------\n"
            "Given the new context, refine the original summary"
            "If the context isn't useful, return the original summary."
        )
        refine_prompt = PromptTemplate(
            input_variables=["existing_answer", "text"],
            template=refine_template,
        )
        chain = load_summarize_chain(self.llm, 
                                     chain_type="refine", 
                                     return_intermediate_steps=True, 
                                     question_prompt=PROMPT, 
                                     refine_prompt=refine_prompt,
                                     verbose=True)

        output_summary = chain({"input_documents": docs}, return_only_outputs=True)
        return output_summary['output_text']

    def wrap_text(self, text, width=100):
        return textwrap.fill(text, width=width)

    def summarize_document(self, document_text, summary_type="concise"):
        print("Loading document...")
        docs = self.load_document(document_text)

        print("Generating summary...")
        print(f"Summary Type {summary_type}")
        summary = self.generate_summary(docs, summary_type)

        print("Wrapping text...")
        return self.wrap_text(summary)

if __name__ == "__main__":
    summary_generator = SummaryGenerator()
    wrapped_summary = summary_generator.summarize_document('../explore/meeting_doc.txt', summary_type="detailed")
    print("Summary:")
    print(wrapped_summary)