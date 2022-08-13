import os


class MessageObject:
    def serialize(self):
        return self.__dict__

    @staticmethod
    def deserialize(data):
        pass


class TextFile(MessageObject):
    def __init__(self, file_path: str):
        self.file_path = file_path
        self.file_name = os.path.basename(file_path)
        self.file_content: str | None = None

    def read(self) -> str:
        with open(self.file_path, 'r') as f:
            return f.read()

    def serialize(self) -> str:
        return str({
            'file_name': os.path.abspath(self.file_path),
            'file_content': self.read()
        })

    def file_exists(self) -> bool:
        return os.path.isfile(self.file_path)

    @staticmethod
    def deserialize(data: str) -> 'TextFile':
        data_dict: dict = dict(data)

        tf: TextFile = TextFile(data_dict['file_name'])
        tf.file_content = data_dict['file_content']

        return tf
