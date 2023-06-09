from flask import Flask
import datetime


# Initializing flask app
app = Flask(__name__)
 
x = datetime.datetime.now()
@app.route('/data')
def get_time():
    return {'Name':"geek", "Age":"22", "Date":x, "programming":"python" }
 

@app.route('/lyrics/<trackID>')
def get_lyrics(trackID):
    try: 
        return get_lyrics(trackID)
    except Exception as e:
        return "Oops"

@app.route('/subtitles/<query>')    # QUERY = "SONG-ARTIST"
def get_lyrics_from_query(query):
    try: 
        return get_data3(query)
    except Exception as e:
        return "Oops"
    


from get_lyrics import get_lyrics
from spotify_id import search_tracks
from get_data import get_data3

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')
