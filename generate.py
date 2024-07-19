import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

linklist = [] #list of technical paper links here

for link in linklist:
    completion = openai.ChatCompletion.create(
    model="gpt-4o",
    messages=[
        {"role": "user", "content": f"""
        create a 500 word summary of {link} with all technical terms translated for a non-technical audience in a paragraph format. The summary should be no less than 500 words. It should also start with the authors of the paper, the link to paper and the date published. Include the line "This summary was generated by GPT-4o. There may be errors or omissions." Beneath the title. Do not include a final line with a link to the full paper. Finally, format it in markdown format.
        """}
    ]
    )