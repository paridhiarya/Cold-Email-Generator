import os
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.exceptions import OutputParserException
from dotenv import load_dotenv
load_dotenv()

class Chain:
    def __init__(self):
        self.llm = ChatGroq(
            model="llama-3.1-70b-versatile",#"mixtral-8x7b-32768",
            temperature=0,
            max_tokens=None,
            timeout=None,
            max_retries=2,
            groq_api_key=os.getenv('GROQ_API_KEY')
        )
        
    def extract_company_details(self, cleaned_text):
        template = PromptTemplate(
            input_variables=['page_data'],
            template="""SCRAPED DATA FROM WEBSITE: {page_data} 
                    INSTRUCTION:
                    The scraped text is from the about us page of a company's website.
                    Your job is to extract the field and description of the company and return them in a JSON Format
                    containing the following keys: "company_name", "industry", "mission", "products", "target_audience", "unique_value_proposition", "achievements", "location", "leadership", "contact_email"
                    Only return the valid JSON, NO PREAMBLE REQUIRED."""
        )
        chain_extract = template | self.llm
        json_list = chain_extract.invoke(input={"page_data": cleaned_text})
        try:
            json_parser = JsonOutputParser()
            json_list = json_parser.parse(json_list.content)
        except OutputParserException:
            raise OutputParserException("Context too big. Unable to parse company details.")
        return json_list if isinstance(json_list, list) else [json_list]
    
    def write_mail(self, company_details, links):
        prompt_email = PromptTemplate.from_template(
            """
            ### COMPANY DESCRIPTION:
            {company_description}
            
            ### INSTRUCTION:
            You are Paridhi, a business development executive at TrueFoundry. 
            TrueFoundry is a platform that helps companies automate the deployment and management of machine learning models and other applications. It provides a cloud-agnostic MLOps 
            platform that enables developers to build, deploy, and manage machine learning (ML) models in a production environment. 
            Over our experience, we have empowered numerous enterprises with tailored solutions, fostering scalability, 
            process optimization, cost reduction, and heightened overall efficiency. 
            Your job is to write a cold email to the client with the above description describing the capability of TrueFoundry
            in fulfilling their needs and why they should choose TrueFoundry.
            Also add the most relevant ones from the following links to showcase TrueFoundry's portfolio: {link_list}
            Remember you are Mohan, BDE at TrueFoundry. 
            Do not provide a preamble.
            ### EMAIL (NO PREAMBLE):
            
            """
        )

        chain_email = prompt_email | self.llm
        res = chain_email.invoke({"company_description": str(company_details), "link_list": links})
        return res.content
    