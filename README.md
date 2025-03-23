# pass_the_parcel
Serves as the soundtrack to the Bluey birthday party game "pass the parcel" by playing an mp3 and 
pausing it at random intervals while the parcel is in transit.

In my case I used deepseek to generate a rhyming song with lyrics about my son and his interests,
then I used mureka.ai to generate a song.

#### Suggested Rules
1. Pass the parcel (i.e., "present" in American English) clockwise when
the music is playing.
2. The player who is holding the present when the music stops gets to unwrap the outermost
layer of wrapping paper. He leaves the game and becomes a spectator after
unwrapping.
3. There may or may not be a present in his layer.
4. If the parcel is between players, break the tie with a quick game of rock paper
scissors.
5. If more than one layer is unwrapped, the player forfeits any presents to the next
player in clockwise order and becomes a spectator.

#### Usage

Fiddle with the `min_length` and `max_length` fields to make the average interval multiplied by the
number of wrapping paper layers fit comfortably under the length of the song.

```
virtualenv env
pip install -r requirements.txt
cp <your song> .
python3 play.py
```