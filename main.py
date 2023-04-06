import pdfplumber
import re

def extract_content_between_tags(pdf_file, tag1, tag2):
    with pdfplumber.open(pdf_file) as pdf:
        content = ""

        for page in pdf.pages:
            content += page.extract_text()


        pattern = re.compile(fr'{tag1}(.*?){tag2}', re.DOTALL)
        matches = pattern.findall(content)
        extracted_text = '\n'.join(matches).strip()


        return extracted_text

if __name__ == '__main__':
    pdf_file = 'Test_prueba.pdf'  # Reemplaza 'tu_documento.pdf' con la ruta de tu archivo PDF
    result_motivo = extract_content_between_tags(pdf_file, 'Motivo', 'Comprobación')
    result_comprobacion = extract_content_between_tags(pdf_file, 'Comprobación', 'Remedicación')
    result_remediacion = extract_content_between_tags(pdf_file, 'Remedicación', 'Control Security')

    print("Contenido de Motivo:")
    print(result_motivo)
    print("\nContenido de Comprobación:")
    print(result_comprobacion)
    print("\nContenido de Remediación:")
    print(result_remediacion)
