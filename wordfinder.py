import random
import unittest


class WordFinder:
    """Word Finder: finds random words from a dictionary."""

    def __init__(self, path: str):
        """
        Initialize the WordFinder with a path to a dictionary file.

        Parameters:
        path (str): The path to the dictionary file.

        Returns: None
        """
        self._words = self._load_words(path)
        print(f"{len(self._words)} words read")

    def _load_words(self, path: str) -> list:
        """
        Load words from the dictionary file.

        Parameters:
        path (str): The path to the dictionary file.

        Returns:
        list: A list of words from the dictionary file.
        """
        with open(path, "r") as file:
            return [line.strip() for line in file]

    def random(self) -> str:
        """
        Return a random word from the dictionary.

        Parameters: None

        Returns:
        str: A random word from the dictionary.
        """
        return random.choice(self._words)


class SpecialWordFinder(WordFinder):
    """Special Word Finder: finds random words from a dictionary, ignoring blank lines and comments."""

    def _load_words(self, path: str) -> list:
        """
        Load words from the dictionary file, ignoring blank lines and comments.

        Parameters:
        path (str): The path to the dictionary file.

        Returns:
        list: A list of words from the dictionary file.
        """
        with open(path, "r") as file:
            return [
                line.strip()
                for line in file
                if line.strip() and not line.startswith("#")
            ]


class TestWordFinder(unittest.TestCase):
    def test_init(self):
        wf = WordFinder("words.txt")
        self.assertIsInstance(wf._words, list)
        self.assertTrue(len(wf._words) > 0)

    def test_random(self):
        wf = WordFinder("words.txt")
        word = wf.random()
        self.assertIsInstance(word, str)
        self.assertTrue(word in wf._words)


class TestSpecialWordFinder(unittest.TestCase):
    def test_init(self):
        wf = SpecialWordFinder("specwords.txt")
        self.assertIsInstance(wf._words, list)
        self.assertTrue(len(wf._words) > 0)

    def test_random(self):
        wf = SpecialWordFinder("specwords.txt")
        word = wf.random()
        self.assertIsInstance(word, str)
        self.assertTrue(word in wf._words)


if __name__ == "__main__":
    unittest.main()
