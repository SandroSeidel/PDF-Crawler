import tabula 
import pprint

pdf_path = "TABELA_VENTIDELTA.pdf"

result = tabula.read_pdf(pdf_path, 
    pages='2', 
    multiple_tables=True, 
    output_format="json",
    lattice=True,
    pandas_options={"header": [0, 1]},
    
    relative_area=True)

pprint.pprint(result)