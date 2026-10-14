import unittest
import tempfile
from fasta import Seq, FastaReader


class TestSeq(unittest.TestCase):

    def test_length(self):
        a = Seq("ATGC", "test")
        self.assertEqual(len(a), 4)

    def test_nucleotide(self):
        a = Seq("ATGC", "test")
        self.assertEqual(a.alphabet, "nucleotide")

    def test_protein(self):
        a = Seq("MALWMRLLP", "test")
        self.assertEqual(a.alphabet, "protein")

    def test_string(self):
        a = Seq("ATGC", "test")
        self.assertEqual(str(a), ">test\nATGC")


class TestFastaReader(unittest.TestCase):

    def test_reader(self):
        with tempfile.NamedTemporaryFile(mode="w", delete=False, suffix=".fasta") as f:
            f.write(">one\nATGC\n>two\nMALWMRLLP\n")
            name = f.name

        reader = FastaReader(name)
        result = list(reader)

        self.assertEqual(len(result), 2)
        self.assertEqual(result[0].header, "one")
        self.assertEqual(result[1].alphabet, "protein")


if __name__ == "__main__":
    unittest.main()
