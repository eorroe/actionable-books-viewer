import PyPDF2
import sys

pdf_path = '/tmp/attachments/agent_82683db9-2987-4e71-b3a9-2b587805f9ea/0a976afa-9d91-494d-85d2-5832b5541cb3/97698b19-03fb-4135-8b56-5c90b57b8510/cc489404-617f-4b70-80b7-9099350ac879.pdf'
output_path = '/workspace/0a976afa-9d91-494d-85d2-5832b5541cb3/sessions/agent_82683db9-2987-4e71-b3a9-2b587805f9ea/tmp/book-work/full-text.txt'

try:
    with open(pdf_path, 'rb') as f:
        reader = PyPDF2.PdfReader(f)
        with open(output_path, 'w', encoding='utf-8') as out:
            for i, page in enumerate(reader.pages):
                page_text = page.extract_text()
                if page_text:
                    out.write(f'\n--- Page {i+1} ---\n{page_text}\n')
    print(f'Successfully extracted {len(reader.pages)} pages to {output_path}')
except Exception as e:
    print(f'Error: {e}', file=sys.stderr)
    sys.exit(1)
