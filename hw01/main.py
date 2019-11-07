DICT_FILEPATH = './data/dict.opcorpora.xml'

class Lemmatizer():
    def __init__(self) -> None:
        super().__init__()
        self.reverse_index = self.build_reverse_index()

    def predict(self):
        pass

    def build_reverse_index(self):
        import xml.etree.ElementTree as ET
        root = ET.parse(DICT_FILEPATH).getroot()
        print(root)
        reverse_index = {}
        return reverse_index


if __name__ == "__main__":
    Lemmatizer()