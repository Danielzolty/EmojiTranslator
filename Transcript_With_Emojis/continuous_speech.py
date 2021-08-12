import datetime
import pyaudio
import speech_recognition as sr
import docx

r = sr.Recognizer()
mydoc = docx.Document()
start_time = datetime.datetime(100,1,1,0,0,0)
max_time = datetime.datetime(100,1,1,0,0,7)

block_num = 13

def speech_to_srt(current_time, block):
    if current_time >= max_time:
        return "Speech recognition complete"
    else:
        block+= 1
        block_str = str(block)

        with sr.Microphone() as source:
            print("Now recording")
            audio = r.listen(source)

        try:
            sentence = (r.recognize_google(audio))

        except sr.UnknownValueError:
            print("Google couldn't understand error")

        except sr.RequestError as e:
            print("Could not request results from Google SPR service: [0]".format(e))

        if sentence == "speech recognition is over":
            return 'Speech recognition is complete per user request'
        else:
            time_add = len(sentence.split())/2
            end_time = current_time + datetime.timedelta(0, time_add)
            str_current_time = str(current_time.time())
            str_end_time = str(end_time.time())

            with open("file.srt", "a") as f:
                f.write(block_str)
                f.write("\n")
                f.write(sentence)
                f.write(",")
                f.write("\n")
                f.write("\n")
                # mydoc.save(f)
            return speech_to_srt(end_time, block)
speech_to_srt(start_time, block_num)
