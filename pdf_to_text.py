import PyPDF2

def pdf_to_text(path):
    # Creating a file object variable
    # "RB" mode = "read binary"
    pdffileobj = open(path, 'rb')

    # Creating a reader variable that will read the pdffileobj
    pdfreader = PyPDF2.PdfFileReader(pdffileobj)

    # This will store the number of pages of this pdf file
    x = pdfreader.numPages
    # print(x)

    # Creating a variable that will select the selected number of pages
    pageobj = pdfreader.getPage(x - 1)

    # Creating text variable which will store all text datafrom pdf file
    text = pageobj.extractText()

    # Saving extracted data from pdf to a txt file
    file1 = open(r"C:/Users/Maciek/PycharmProjects/pdf_to_audio/extracted_text.txt", "w")
    file1.writelines(text)

    print(text)
    return text
