import docx

doc = docx.Document("Ramya Sree Kodati resume.docx")
text = "\n".join([para.text for para in doc.paragraphs])
with open("resume.txt", "w", encoding="utf-8") as f:
    f.write(text)
print("Extracted text successfully.")
