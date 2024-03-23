import speech_recognition as sr
import opencc
import io
import whisper
import soundfile as sf
import numpy as np


class ASR:

    def __init__(self, model="small", device="cuda"):
        # 加载Whisper模型,可选择的模型有: "base", "small", "medium", "large"
        self.model = whisper.load_model(model, device=device)

    def recognize_whisper(self, audio_data):

        wav_bytes = audio_data.get_wav_data(convert_rate=16000)
        wav_stream = io.BytesIO(wav_bytes)
        audio_array, sampling_rate = sf.read(wav_stream)
        audio_array = audio_array.astype(np.float32)
        result = self.model.transcribe(audio_array, language="Chinese")
        return result["text"]

    def recognize_whisper_from_microphnoe(self):

        r = sr.Recognizer()

        cc = opencc.OpenCC("t2s")

        with sr.Microphone() as source:
            # 设置固定的识别时长
            # audio = r.record(source, duration=4)

            # 根据用户音量自动截断
            audio = r.listen(source)

        # recognize speech using whisper
        try:
            # 使用Whisper进行语音识别,并将结果转换为简体中文
            data = cc.convert(self.recognize_whisper(audio))

        except sr.UnknownValueError:
            print("Whisper could not understand audio")
        except sr.RequestError as e:
            print("Could not request results from Whisper")

        return data

    def recognize_whisper_from_file(self, file_path):
        # 调用Whisper进行语音识别

        model = whisper.load_model("base", device="cuda")

        result = model.transcribe(file_path, language="Chinese")
        return result["text"]
