# pass_the_parcel
Serves as the soundtrack to the Bluey birthday party game [pass the parcel](https://en.wikipedia.org/wiki/Pass_the_parcel) by playing an mp3 and pausing it randomly while the parcel is in transit.

In my case I used deepseek to generate a rhyming song with lyrics about my son and his interests, then I used mureka.ai to generate a song.

#### Suggested Rules
1. Pass the parcel (i.e., "present" in American English) to the left when the music is playing.
2. The player who is holding the parcel when the music stops gets to unwrap one layer of wrapping paper. The player leaves the game and becomes a spectator after unwrapping.
3. There may or may not be a gift in a given layer.
4. If the parcel is between players, break the tie with rock paper scissors.
5. If the player unwraps more than one layer, the player forfeits any gift to the next player in clockwise order and becomes a spectator.

#### Usage

Fiddle with the `min_length` and `max_length` fields to make the average interval multiplied by the number of wrapping paper layers fit comfortably under the length of the song.

```
virtualenv env
pip install -r requirements.txt
cp <your song> .
python3 play.py
```
