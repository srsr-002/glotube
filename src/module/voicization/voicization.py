import json
import os
from datetime import datetime
from gtts import gTTS

class Voicization:
    def __init__(self) -> None:
        sentences = self._load_sentence()
        self._make_sound(sentences)

    # 読み上げ対象の文章を取得
    def _load_sentence(self) -> str:
        file_path = '../../media/word.json'
        with open(file_path, 'r') as file:
            sentences = json.load(file)
        return sentences

    # 音声化処理
    def _make_sound(self, sentences: str) -> None:
        try:
            current_time = datetime.now().strftime("%Y%m%d_%H%M%S")
            dir_relative_path = '../../media/tmp/output_voice'
            self.make_dir(dir_relative_path)

            for key, value in sentences.items():
                tts = gTTS(text=value, lang='ja')
                tts.save(f"{dir_relative_path}/{current_time}_{key}.mp3")

        except Exception as e:
            print(f"An error occurred: {e}")

    # TODO:共通クラスに切り出す
    def make_dir(self, path) -> None:
        try:
            os.makedirs(path, exist_ok=True)
        except Exception:
            print(f"Failed to create directory: {path}")
