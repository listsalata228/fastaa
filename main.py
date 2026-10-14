from pathlib import Path

def create_demo_file():
    folder = Path("examples")
    folder.mkdir(exist_ok=True)

    text = """>human_gene
ATGGCCATTGTAATGGGCCGCTGAAAGGGTGCCCGATAG

>example_protein
MALWMRLLPLLALLALWGPGPG

>another_gene
ATGCGTACCGATTAA
"""

    (folder / "demo.fasta").write_text(text, encoding="utf-8")


from fasta import main


if __name__ == "__main__":
    create_demo_file()
    main()
