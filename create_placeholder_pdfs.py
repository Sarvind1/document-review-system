#!/usr/bin/env python3
"""Create placeholder PDFs for demo purposes."""

import os
from PIL import Image, ImageDraw

def main():
    """Create simple placeholder PDFs."""
    # Create directories
    for doc_type in ['CI', 'PL']:
        for batch in ['B001', 'B002', 'B003']:
            os.makedirs(f'static/documents/{doc_type}/{batch}', exist_ok=True)
            # Create simple PDF files
            for version in range(1, 3):
                img = Image.new('RGB', (595, 842), color='white')
                draw = ImageDraw.Draw(img)
                draw.rectangle([(20, 20), (575, 822)], outline='black', width=2)
                draw.text((300, 50), f'{doc_type} Document', fill='black')
                draw.text((300, 100), f'Batch: {batch}', fill='black')
                draw.text((300, 150), f'Version: {version}', fill='black')
                path = f'static/documents/{doc_type}/{batch}/{batch}_{version}.pdf'
                img.save(path, 'PDF')
                print(f'Created {path}')

if __name__ == "__main__":
    main()
    print("Placeholder PDFs created successfully!") 