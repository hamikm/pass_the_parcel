# pass_the_parcel
Serves as the soundtrack to the Bluey birthday party game "pass the parcel" by randomly stopping an
mp3.

In my case, I used deepseek to generate a rhyming song with lyrics about my son and his interests,
then I used mureka.ai to generate a song.

#### Usage

Fiddle with the `min_length` and `max_length` fields to make the average interval times number of
wrapping paper layers fit comfortably under the length of the song.

```
virtualenv env
pip install -r requirements.txt
cp <your song> .
python3 play.py
```