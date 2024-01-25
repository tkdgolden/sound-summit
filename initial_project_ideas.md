# Project Ideas

I haven’t looked into the requirements for the second capstone, but if any of these look like they would make more sense for that one I’d be open to that, except the phoenetics one because my nephew will probably have outgrown that particular learning skill by then.  

## Spotify Automatic Volume Reduction During Ads
- Spotify api

Would periodically make a call to see what content is playing on a given account, if it’s an ad, reduce the volume (because ads are always shouting compared to my chill music then I mute Spotify then forget about it for an hour and turn it back on just in time for another ad).  Then check periodically and when it is back to music, bring the volume back to its original state.  This makes most sense as a desktop application rather than a website and I don’t know much about that. I’m also not 100% sure I can get the api authorization with just a Spotify free account. I would have to figure out how often the api call should be that would be reasonable.  

## Phoenetic Learning Game (Sounding words out)
- IBM text to speech /pronunciation and /synthesize

To help kids practice sounding words out as they’re learning to read things other than sight words.  Building this for my sister and her kid so I’d probably focus on it being optimized on an iPad because that’s how she’d use it.  

Show a word from a word bank on the screen, with a “sound bank” of options (unmarked by letters) below.  Kid can click each of the sound bank options to hear their sound.  Kid should drag the sounds into order to make the word above and hit a check button to submit for points.  
|         |        | taco    |         |        |
| ------- | ------ | ------- | ------- | ------ |
| 🔊(t)  |    __    | 🔊(k)  |     __    | ☑️   |
|         |        |         |         |        |
| 🔊(oh) | 🔊(t) | 🔊(ay) | 🔊(ah) | 🔊(k) |

Might also have a flipped gameplay where an list of sound icons are on top each with a part of the word but already in order and the kid should select from fully written words on the bottom or possibly have to type the word but probably not because it’s not about learning spelling.  Maybe it could have full word sound icons on bottom with one being the correct word and the rest being similar words but I’m not sure how I would generate “similar words”.  
|     |     | 🔊(cat) |      |     |
| --- | --- | -------- | ---- | --- |
|     |     | car      | ☑️  |     |
|     |     |          |      |     |
| act | car | cat      | cant | ant |

## Spotify Common Interests
- Spotify api

With two Spotify users make calls to find each of their most listened to tracks/ artists (or all liked/ things in followed/owned playlists) to find things they have in common and return that as a playlist that gets added to both of their accounts. 

## Kid Friendly Airplane Tracker
- Aviationstack.com
- Aviationedge.com

Very simple and minimal UI, designed mostly for phones, uses geolocation to find the nearest airplane and tell some basic facts about it (where it’s going, where it’s from, how fast it’s going, how high it is, how many people are on it).  If it’s not too much, it might also be able to tell you facts about satellites if that is the nearest thing. (What is that? -It’s a bird! It’s a plane! It’s a satellite!) They can look up and ask, where is that plane going? Or at night: is that a satellite or a really high plane or a shimmering star?

## Axe Tournament Scoring
- Own api

I already have a pretty much functional website that uses a postgresql database and python and flask to run and score axe throwing tournaments and leagues.  I’m working on refactoring it and wonder if it might make more sense to display stats and tournament standings via JavaScript with a call to my own api with my data.  Ideally the screen shouldn’t have to be refreshed for tournament standings so that it could be displayed on a tv for people to see.  After the cupcake api assignment I just did, I know I’m capable, I just don’t know if it would be good architecture for my current web app…?  I would be happy to show/ give more details on the app if needed.  

