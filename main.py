import assemblyai as aai
from datetime import datetime
import elevenlabs as elabs
import os
import signal
import json
import boto3
import requests
from pydub import AudioSegment

elabs.set_api_key("")
aai.settings.api_key = ""

def upload_to_s3():
    try:
        with open('history.json', 'r') as file:
            json_data = json.load(file)
        s3 = boto3.client(
            's3',
            aws_access_key_id='',
            aws_secret_access_key=''
        )

        # Upload the JSON data to S3
        s3.put_object(Bucket="teddyconversationhistory", Key="history.json", Body=json.dumps(json_data))

        print(f"Uploaded data to S3 successfully")

    except Exception as e:
        print(f"Error uploading data to S3: {e}")

def add_data_to_json(new_data):
    try:
        with open("history.json", 'r') as file:
            existing_data = json.load(file)

        # Append new data to the existing data
        existing_data["data"].append(new_data)

        with open("history.json", 'w') as file:
            json.dump(existing_data, file, indent=2)

        print("Data added successfully.")

    except Exception as e:
        print(f"Error adding data: {e}")

def on_open(session_opened: aai.RealtimeSessionOpened):
  "This function is called when the connection has been established."

  print("Session ID:", session_opened.session_id)

def on_data(transcript: aai.RealtimeTranscript):
    "This function is called when a new transcript has been received."

    global conversation_data
    global last_transcript_received
    global terminated
    global detectedSpeech
    global transcriptCount

    json_data = requests.get("").json()
    if json_data["data"] != "":
        requests.put("", json={"data":""})
        terminated=True
        audio_stream = elabs.generate(
        text=json_data["data"],
        voice=elabs.Voice(voice_id='zq2G3PqjnAkKc5D9pVgT'),
        stream=True
        )
        elabs.stream(audio_stream)



    if terminated:
        os._exit(0)
        print("success")
        print(transcript.text)
        if transcript.text != "":
            detectedSpeech = True
        if detectedSpeech and transcript.text == "":
            transcriptCount += 1
        if detectedSpeech and transcriptCount >= 5:
            transcriptCount=0
            terminated = False
            detectedSpeech = False
            print("ready for more input...")
        return

    if transcript.text == "":
        if (datetime.now() - last_transcript_received).total_seconds() > 3:
            print("3 seconds without new transcription, terminating...")
            process_transcription()
            last_transcript_received = datetime.now()
            print("ready for more input...")
        return

    if isinstance(transcript, aai.RealtimeFinalTranscript):
        print(transcript.text, end="\r\n")
        conversation_data += f"{transcript.text} \n"
    else:
        print(transcript.text, end="\r")

    last_transcript_received = datetime.now()

def process_transcription():
    global conversation_data
    global terminated
    global conversationHistory
    if conversation_data != "":
        add_data_to_json({'speaker': 'user', 'timestamp' : str(datetime.now()), 'message' : conversation_data })
        conversationHistory.append({'speaker': 'user', 'timestamp' : str(datetime.now()), 'message' : conversation_data })
        terminated = True
        #grabbing 2 previous interaction context
        with open('history.json', 'r') as file:
            data = json.load(file)

        last_6_interactions = data["data"][-2:]
        interaction_string = "\n".join([f"{interaction['speaker']}: {interaction['message']}" for interaction in last_6_interactions])

        message_data = requests.get("").json()
        suggested_string = ' '.join(message_data['suggested'])
        banned_string = ' '.join(message_data['banned'])
        print(message_data)
        print(banned_string)

        result = aai.Lemur().task(
            "always keep response under 3 sentences. you are an assistant teddy bear to a children provide fun and interactive answers to his interactions, keep answers short, Do not introduce yourself unless you're asked to, you need to invent and pretend yourself a name and a funny personality to answer all his question, you are not an AI. Here is a compilation of 2 of your previous discussion in case it's helpful: " + interaction_string + "do not answer or discuss anything related to the following topics: " + banned_string + "if it's relevant to the conversation try to talk about the following topics " + suggested_string,
            input_text=conversation_data
        )
        print(result.response)
        add_data_to_json({'speaker': 'Teddy Assistant', 'timestamp' : str(datetime.now()), 'message' : result.response})
        conversationHistory.append({'speaker': 'Teddy Assistant', 'timestamp' : str(datetime.now()), 'message' : result.response})
        upload_to_s3()
        audio_stream = elabs.generate(
        voice=elabs.Voice(voice_id='zq2G3PqjnAkKc5D9pVgT'),
        text=result.response,
        stream=True
        )
        print(conversationHistory)
        elabs.stream(audio_stream)
        conversation_data = ""
    return
def on_error(error: aai.RealtimeError):
  "This function is called when the connection has been closed."


def terminate_transcription():
    global terminated
    if not terminated:
        transcriber.close()
        terminated = True

def on_close():
    "This function is called when the connection has been closed."
    print("here1")
    global conversation_data
    global terminated
    result = aai.Lemur().task(
        "you are an assistant teddy bear to a children provide fun and interactive answers to his interactions, you need to invent yourself a name and a funny personality to answer all his question without revealing you are an AI",
        input_text=conversation_data
    )
    print(result.response)
    if not terminated:
        print("Closing Session")
        terminated = True

transcriber = aai.RealtimeTranscriber(
  on_data=on_data,
  on_error=on_error,
  sample_rate=44_100,
  on_open=on_open
)
conversation_data = ""
detectedSpeech = False
transcriptCount = 0
conversationHistory = []
last_transcript_received = datetime.now()
terminated = False
transcriber.connect()
microphone_stream = aai.extras.MicrophoneStream()

transcriber.stream(microphone_stream)

    