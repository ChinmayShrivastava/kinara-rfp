from rfpextractor.scripts import DocExtraction

def main():
    de = DocExtraction(
        pdf_path="testpdf.pdf",
        verbose=True,
    )
    de.run()

if __name__ == "__main__":
    main()