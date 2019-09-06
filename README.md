# NDSMicro
Batch NDS injection for Wii U

After looking over the current tools in the Wii U, I noticed none of them had a simple "batch" process. The injectiine app stated it had a "batch interface" but, no, only 1 game at a time... So, I took that tool, and made it better, at least the concept. 

What is this?

This is a python script, or .exe, or whatever you use that packs games into a WUP installable format, because loadiine is obsolete. 

Why would I use this?

You are a pirate, er, emulation enthusiast, that wants to play, or have the option to play, all DS titles at any given moment without the use of BOTW emulator, CemU... Basically, you want to make all DS games ready for installation but don't care about fancy art.

How does this work?

At first, I was reverse engineering loadiine, but came across so many bugs, I just study the core of it, seeing what it called and basically did... In the end, it was NUSPacker wrapper, so I wrapped it up myself. This is a leeching script. Instead of actually creating resources, it leeches off of existing ones and just crams them together. It doesn't create an XML, doesn't download a base, doesn't make or verify TGA, or anything. It just does what it was meant to do.

Zips up an NDS file into a rom.zip (you do NOT need to turn it into whatever srl file people have been using. i don't know why everyone used such a useless way, as just turning a ds file into a rom.zip works without issue.

adds the names of games and sequential codes into the xml (it does not create an xml from scratch, I tried, it didn't work, so I just did it this way.

Tells NUSPacker to do stuff

And that's it... Unlike other apps, it won't delete your games or Base folder after every game (All this does is annoy people)

So... If it does nothing, how do I use it?

It does something, otherwise I'd just upload a print statement giving the "bird" emoji. But... 

Download the script (DUH)
Create folder called "Input" next to that script and a folder called "Ouput", also next to the script
Download NUSPacker (The java jar file) and move it next to the script
Get yourself an "​​​​encryptKeyWith" file (no extension) containing the Wii U common key (Everyone should know this by now, or know that it is revealed by the power of google), and also move that next to the script
Download Metroid Prime hunters (Because I made the script around that as it was the latest I had)
Delete the rom.zip in Metroid Prime Humters
Move the app.xml and meta.xml from that folder to the Input folder
rename the MPH game folder to "Base" (such that Base contains code, meta, content, etc...) and move that to the Input Folder
get some TGA files in that Input folder
Place NDS files next to the script (all of them, otherwise they will have the same xmls and might brick your sonsole... AKA, all or nothing)
Lastly... run the script (depending on the number of games, it might take 11 or so hours, assuming you are doing all 6000+)
If you did the whole NDS collection right, it should shrink from 349 GB to 

Also, might cut some steps out by uploading the folder structure myself, and empty files of where stuff should go, but I am NOT uploading copyrighted code.

Why should I trust you?

You shouldn't, you don't me, I have no reputation or anything... and on my free time I compose exploits for fun(I find more holes in my work's apps than their bug team finds in a year, not that they look). Feel free to look at the code.
