#Importação necessária
import PyPDF2

#Aqui colocamos o nosso pdf
arquivo = r"./capa-livro.pdf"

#Colocamos a função em pdf
pdf = PyPDF2.PdfFileReader(arquivo)

#Selecionamos a página que queremos, nesse caso vou
#usa a 0
pag = pdf.getPage(0)

#Aqui mandamos o texto da pagina um para o cont
cont = pag.extractText()

print(cont)




