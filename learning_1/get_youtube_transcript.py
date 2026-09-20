from google import genai
from dotenv import load_dotenv
from youtube_transcript_api import YouTubeTranscriptApi
from urllib.parse import urlparse, parse_qs
import chromadb

load_dotenv()
api = YouTubeTranscriptApi()
client = genai.Client()

def get_video_id(url: str) -> str:
  parsed_url = urlparse(url=url)

  if parsed_url.hostname in ["youtube.com", "www.youtube.com", "m.youtube.com"]:
    query_params = parse_qs(parsed_url.query)
    if "v" in query_params:
       return query_params["v"][0]

  raise ValueError("Invalid url!")

def transcript(url: str):
    try:
      video_id = get_video_id(url=url)
      with open("./transcript.txt", 'w', encoding="utf-8") as file:
        response = api.fetch(video_id=video_id)
        for item in response:
          file.write(item.text + '\n')
        print("Transcript write completed...")

      generate_notes_from_file("./transcript.txt", "video_notes.md")
    except ValueError as e:
      print(f"Catch Error: {e}")

def generate_notes_from_file(file_path: str, notes_output_path: str):
  """Reads a transcript file and generates notes using an active Gemini Flash model."""
  with open(file_path, 'r', encoding="utf-8") as f:
    transcript_text = f.read()

  prompt = f"""
  You are an expert note-taker. Below is a raw transcript of a video. 
  Please convert it into clean, structured notes containing:
  1. A short executive summary (5-7 sentences)
  2. Key Takeaways (bullet points)
  3. Detailed breakdown by main topic/theme
    
  Transcript:
  {transcript_text}
  """

  response = client.models.generate_content(
    model="gemini-3.1-flash-lite",
    contents=prompt
  )

  with open(notes_output_path, "w", encoding="utf-8") as file:
    file.write(response.text)

  print(f"Notes successfully generated and saved to {notes_output_path}")

VIDEO_ID = "E0Hmnixke2g"
transcript(f"https://www.youtube.com/watch?v={VIDEO_ID}")