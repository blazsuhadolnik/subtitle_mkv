# Extract subtittle from movie (mkv format) #
Folowing step by step for works in ubuntu 16.04
## 1. install mkvtoolnix ##
In bash terminal run command:
`sudo apt-get install mkvtoolnix`
Where code mean:
* `sudo` command execute as root
* `apt-get` repository from debian distribution (similar to `yum` in arch linux)
* `install` to tell repository for installation package
* `mkvtoolnix` packet which we install. for install more packages seperate them with space
## 2. Information about tracks ##
For extracting subtitle track from `.mkv` file we need know which track is subtitle. This we do with command:

`mkvmerge -i input.mkv`

Output for this command is somting similar to:
```
File 'input.mkv': container: Matroska
	Track ID 1: video (V_MPEG4/ISO/AVC)
	Track ID 2: audio (A_AAC)
	Track ID 3: subtitles (S_TEXT/UTF8)
```

Here we see that our subtitle is under 3 treed.
## 3. Extract subtitle ##
With known which treed is subtitle, we can extract it:

`mkvextract tracks input.mkv 3:subtittle.srt` 
* `input.mkv` is name of movie with subtitle in current directory,
*  `3` is number of treed for subtitle
*  `subtittle.srt` is name for output file with subtitle extract from movie.

For naming output for multiple input `.mkv` files:
```
a=1 && for i in *.mkv; do mkvextract tracks "$i" 3:"$a".srt && let a=a+1; done
```
* First we set variable `a=1`
* for all `.mkv` files do (inside `do` and `done`):
  * `"$i"` name of `.mkv.` file which is under i time iteration
  *  `"$a".srt` name of output subtitle with sequence number of `.mkv` files    

## 4. Convert subtitle in readable format ##
Before you run script change some parameter in `podnapisi.py`:
* Number of dokument (first `for` loop)
* Name of reading file (variable `line`), which is our subtitle.

Run script inside folder with subtitles names `1.srt`, `2.srt`, ...
```
python3 podnapisi.py
```
