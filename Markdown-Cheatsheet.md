console.log(new Date().getFullYear() + ' sumFile is run'); 
<br>#---------------------------------------------------------------------------<br>
# Markdown Cheatsheet<br>
1) Red<br>

<br>#---------------------------------------------------------------------------<br>
OLD NOTES FROM PA CLASS: <br>
#Red=hash <br>
Purple=open/close stars <br>
Yellow=open/close 2 stars <br>
Italics Green=open/close ticks <br>
sumWebsite <br>
Red Numbers<br>
<br>#---------------------------------------------------------------------------<br>
<br>#---------------------------------------------------------------------------<br>
<br>#---------------------------------------------------------------------------<br>
# Table of Contents:
###### Headers
###### Emphasis
###### Lists
###### Links
###### Images
###### Code and Syntax Highlighting
###### Tables
###### Blockquotes
###### Inline HTML
###### Horizontal Rule
###### Line Breaks
###### YouTube Videos
<br>#---------------------------------------------------------------------------<br>
Headers <br>
# H1
## H2
### H3
#### H4
##### H5
###### H6
Alternatively, for H1 and H2, an underline-ish style:
Alt-H1
======
Alt-H2
------
H1
H2
H3
H4
H5
H6
Alternatively, for H1 and H2, an underline-ish style:
Alt-H1
Alt-H2
<br>#---------------------------------------------------------------------------<br>
Emphasis <br>
Emphasis, aka italics, with *asterisks* or _underscores_.
Strong emphasis, aka bold, with **asterisks** or __underscores__.
Combined emphasis with **asterisks and _underscores_**.
Strikethrough uses two tildes. ~~Scratch this.~~
Emphasis, aka italics, with asterisks or underscores.
Strong emphasis, aka bold, with asterisks or underscores.
Combined emphasis with asterisks and underscores.
Strikethrough uses two tildes. Scratch this.
<br>#---------------------------------------------------------------------------<br>
Lists <br>
(In this example, leading and trailing spaces are shown with with dots: ⋅)
1. First ordered list item
2. Another item
⋅⋅* Unordered sub-list. 
1. Actual numbers don't matter, just that it's a number
⋅⋅1. Ordered sub-list
4. And another item.
⋅⋅⋅You can have properly indented paragraphs within list items. Notice the blank line above, and the leading spaces (at least one, but we'll use three here to also align the raw Markdown).
⋅⋅⋅To have a line break without a paragraph, you will need to use two trailing spaces.⋅⋅
⋅⋅⋅Note that this line is separate, but within the same paragraph.⋅⋅
⋅⋅⋅(This is contrary to the typical GFM line break behaviour, where trailing spaces are not required.)
* Unordered list can use asterisks
- Or minuses
+ Or pluses
First ordered list item
Another item
Unordered sub-list.
Actual numbers don't matter, just that it's a number
Ordered sub-list
And another item.
You can have properly indented paragraphs within list items. Notice the blank line above, and the leading spaces (at least one, but we'll use three here to also align the raw Markdown).
To have a line break without a paragraph, you will need to use two trailing spaces.
Note that this line is separate, but within the same paragraph.
(This is contrary to the typical GFM line break behaviour, where trailing spaces are not required.)
Unordered list can use asterisks
Or minuses
Or pluses
<br>#---------------------------------------------------------------------------<br>
Links <br>
There are two ways to create links. <br>
[I'm an inline-style link](https://www.google.com) <br>
[I'm an inline-style link with title](https://www.google.com "Google's Homepage") <br>
[I'm a reference-style link][Arbitrary case-insensitive reference text] <br>
[I'm a relative reference to a repository file](../blob/master/LICENSE) <br>
[You can use numbers for reference-style link definitions][1] <br>
Or leave it empty and use the [link text itself]. <br>
URLs and URLs in angle brackets will automatically get turned into links.  <br>
http://www.example.com or <http://www.example.com> and sometimes  <br>
example.com (but not on Github, for example). <br>
Some text to show that the reference links can follow later. <br>
[arbitrary case-insensitive reference text]: https://www.mozilla.org <br>
[1]: http://slashdot.org <br>
[link text itself]: http://www.reddit.com <br>
I'm an inline-style link <br>
I'm an inline-style link with title <br>
I'm a reference-style link <br>
I'm a relative reference to a repository file <br>
You can use numbers for reference-style link definitions <br>
Or leave it empty and use the link text itself. <br>
URLs and URLs in angle brackets will automatically get turned into links. http://www.example.com or http://www.example.com and sometimes example.com (but not on Github, for example). <br>
Some text to show that the reference links can follow later.
<br>#---------------------------------------------------------------------------<br>
Images <br>
Here's our logo (hover to see the title text): <br>
Inline-style:  <br>
![alt text](https://github.com/adam-p/markdown-here/raw/master/src/common/images/icon48.png "Logo Title Text 1") <br>
Reference-style:  <br>
![alt text][logo] <br>
[logo]: https://github.com/adam-p/markdown-here/raw/master/src/common/images/icon48.png "Logo Title Text 2" <br>
Here's our logo (hover to see the title text): <br>
Inline-style: alt text <br>
Reference-style: alt text
<br>#---------------------------------------------------------------------------<br>
Code and Syntax Highlighting <br>
Code blocks are part of the Markdown spec, but syntax highlighting isn't. However, many renderers -- like Github's and Markdown Here -- support syntax highlighting. Which languages are supported and how those language names should be written will vary from renderer to renderer. Markdown Here supports highlighting for dozens of languages (and not-really-languages, like diffs and HTTP headers); to see the complete list, and how to write the language names, see the highlight.js demo page. <br>
Inline `code` has `back-ticks around` it. <br>
Inline code has back-ticks around it. <br>
Blocks of code are either fenced by lines with three back-ticks ```, or are indented with four spaces. I recommend only using the fenced code blocks -- they're easier and only they support syntax highlighting.

```javascript
var s = "JavaScript syntax highlighting";
alert(s);
```
```python
s = "Python syntax highlighting"
print s
```
```
No language indicated, so no syntax highlighting. 
But let's throw in a <b>tag</b>.
```
var s = "JavaScript syntax highlighting";
alert(s);
s = "Python syntax highlighting"
print s
No language indicated, so no syntax highlighting in Markdown Here (varies on Github). 
But let's throw in a <b>tag</b>.
<br>#---------------------------------------------------------------------------<br>
Tables <br>
Tables aren't part of the core Markdown spec, but they are part of GFM and Markdown Here supports them. They are an easy way of adding tables to your email -- a task that would otherwise require copy-pasting from another application.
Colons can be used to align columns. <br>
| Tables        | Are           | Cool  |
| ------------- |:-------------:| -----:|
| col 3 is      | right-aligned | $1600 |
| col 2 is      | centered      |   $12 |
| zebra stripes | are neat      |    $1 | <br>
There must be at least 3 dashes separating each header cell. <br>
The outer pipes (|) are optional, and you don't need to make the 
raw Markdown line up prettily. You can also use inline Markdown. <br>
Markdown | Less | Pretty <br>
--- | --- | --- <br>
*Still* | `renders` | **nicely** <br>
1 | 2 | 3 <br>
Colons can be used to align columns. <br>
Tables	Are	Cool <br>
col 3 is	right-aligned	$1600 <br>
col 2 is	centered	$12 <br>
zebra stripes	are neat	$1 <br>
There must be at least 3 dashes separating each header cell. The outer pipes (|) are optional, and you don't need to make the raw Markdown line up prettily. You can also use inline Markdown. <br>
Markdown	Less	Pretty <br>
Still	renders	nicely <br>
1	2	3 <br>
<br>#---------------------------------------------------------------------------<br>
Blockquotes <br>
> Blockquotes are very handy in email to emulate reply text.
> This line is part of the same quote.
Quote break.
> This is a very long line that will still be quoted properly when it wraps. Oh boy let's keep writing to make sure this is long enough to actually wrap for everyone. Oh, you can *put* **Markdown** into a blockquote. 
Blockquotes are very handy in email to emulate reply text. This line is part of the same quote.
Quote break.
This is a very long line that will still be quoted properly when it wraps. Oh boy let's keep writing to make sure this is long enough to actually wrap for everyone. Oh, you can put Markdown into a blockquote.
<br>#---------------------------------------------------------------------------<br>
Inline HTML <br>
You can also use raw HTML in your Markdown, and it'll mostly work pretty well.
<dl>
  <dt>Definition list</dt>
  <dd>Is something people use sometimes.</dd>
  <dt>Markdown in HTML</dt>
  <dd>Does *not* work **very** well. Use HTML <em>tags</em>.</dd>
</dl>
Definition list
Is something people use sometimes.
Markdown in HTML
Does *not* work **very** well. Use HTML tags.
 <br>#--------------------------------WHY IS THIS WHITE?----------------------- <br>
Horizontal Rule <br>
Three or more... <br>
--- <br>
Hyphens <br>
*** <br>
Asterisks <br>
___ <br>
Underscores <br>
Three or more... <br>
Hyphens <br>
Asterisks <br>
Underscores <br>
<br>#------------------------------WHY IS THIS WHITE?---------------------------<br>
Line Breaks <br>
My basic recommendation for learning how line breaks work is to experiment and discover -- hit <Enter> once (i.e., insert one newline), then hit it twice (i.e., insert two newlines), see what happens. You'll soon learn to get what you want. "Markdown Toggle" is your friend.
Here are some things to try out: <br>
Here's a line for us to start with. <br>
This line is separated from the one above by two newlines, so it will be a *separate paragraph*. <br>
This line is also a separate paragraph, but... <br>
This line is only separated by a single newline, so it's a separate line in the *same paragraph*. <br>
Here's a line for us to start with. <br>
This line is separated from the one above by two newlines, so it will be a separate paragraph. <br>
This line is also begins a separate paragraph, but... <br>
This line is only separated by a single newline, so it's a separate line in the same paragraph. <br>
(Technical note: Markdown Here uses GFM line breaks, so there's no need to use MD's two-space line breaks.)
<br>#---------------------------------------------------------------------------<br>
YouTube Videos <br>
They can't be added directly but you can add an image with a link to the video like this: <br>
<a href="http://www.youtube.com/watch?feature=player_embedded&v=YOUTUBE_VIDEO_ID_HERE
" target="_blank"><img src="http://img.youtube.com/vi/YOUTUBE_VIDEO_ID_HERE/0.jpg" 
alt="IMAGE ALT TEXT HERE" width="240" height="180" border="10" /></a> <br>
Or, in pure Markdown, but losing the image sizing and border: <br>
[![IMAGE ALT TEXT HERE](http://img.youtube.com/vi/YOUTUBE_VIDEO_ID_HERE/0.jpg)](http://www.youtube.com/watch?v=YOUTUBE_VIDEO_ID_HERE) <br>
Referencing a bug by #bugID in your git commit links it to the slip. For example #1.
 <br>#--END--------------------------------------------------------------------------------- <br>
[Markdown-Cheatsheet](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet) <br>
