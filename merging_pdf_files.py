from PyPDF2 import PdfMerger

# cria um objeto PdfMerger
merger = PdfMerger()

# lista de arquivos PDF
pdf_files = ['file1.pdf', 'file2.pdf', 'file3.pdf']

# Anexar cada arquivo PDF ao objeto merger
for pdf_file in pdf_files:
    merger.append(f'./assets/pdf/{pdf_file}')

# criar um novo arquivo PDF com os arquivos anexados
merger.write("merged.pdf")
merger.close()