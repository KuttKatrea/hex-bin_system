# Sublime Text 2/3 hex,bin system Plugin #

Sublime Text plugin to change numeral system of selected number. Works with ST2 and ST3.

## Usage ##

Select number, then use key bindings, "selections" menu or context menu to convert it.  
选择文本(可以包含"0x"或"0b"前缀，但不要包含换行符。)，使用快捷键、菜单栏或右键菜单来转换。

## Key bindings ##

### for Windows and Linux ###

bin->dec	ctrl+B, ctrl+D  
bin->hex	ctrl+B, ctrl+H  
hex->dec	ctrl+H, ctrl+D  
hex->bin	ctrl+H, ctrl+B  
dec->bin 	ctrl+D, ctrl+B  
dec->hex  	ctrl+D, ctrl+H  
bin<->hex 	ctrl+B, ctrl+B

### for OSX ###

bin->dec  	super+B,  super+D  
bin->hex  	super+B,  super+H  
hex->dec  	super+H,  super+D  
hex->bin  	super+H,  super+B  
dec->bin  	super+D,  super+B  
dec->hex  	super+D,  super+H  
bin<->hex 	super+B,  super+B

## Update ##

* The selections can contains "0x", "0X", "0B", "0b" prefix now, but can't contain a newline character "\n".  

>选择的文本可以包含"0x", "0X", "0B", "0b"前缀，但不能包含换行符。

* The hex or bin generated now contains "0x" and "0b" prefix now.  

>转换的hex和bin分别添加"0x"和"0b"前缀以示区分。

* Add the bin<->hex function, then press ctrl+B twice, hex will be converted to bin and bin converted to hex.  

>添加bin<-->hex互转功能，然后按ctrl+B两次，即可进行hex和bin的互转。

##Example##

>0xFE  
>0B101010  
>0X847  
>0b000001111

按住`Shift`，按住鼠标右键选择上述文本，然后按`ctrl+b`两次，就变成如下内容：

>0b11111110  
>0x2A  
>0b100001000111  
>0xF

---  
Forked from [ALLZ/hex-bin_system](https://github.com/ALLZ/hex-bin_system).
