# Meta

## Content
1. [Syntax for meta](#Syntax-for-meta)
2. [Meta for md files ](#Meta-for-md-files )
3. [Meta for ipynb files](#Meta-for-ipynb-files)

<a id="Syntax-for-meta"></a>
## Syntax for meta
The default syntax for writing meta is like that of html comment ie.
```
<!--
key: value
-->
```
It is choosen because it is hidden while rendering by default.
However, this is not forced. You can change the syntax easily by
```
blogger config -b <blogname> meta_format "/* */"
```
will make the syntax something like
```
/*
key: value
*/
```

<a id="Meta-for-md-files "></a>
## Meta for md files
For md files, it is recommended that you write the meta at top of the file.
However, technically you can write it wherever you want as far as it is the first occurrence of the meta format.

<a id="Meta-for-ipynb-files"></a>
## Meta for ipynb files
For ipynb file meta is lot diverse. You can declare meta in first raw cell.
Your meta will be read then deleted making your notebooks clean. The meta will be written to <filename>.nbdata file where <filename> is the same name as your notebook's name.

Similarly, you can make a separate .nbdata file with the same name as notebook and blogger will read it during conversion.

Although above is default behaviour you can stop creation of .nbdata files by setting create\_nbdata\_file to false and stop the deletion of meta cell in notebook by delete\_ipynb\_meta to false.
```
blogger config -b <blogname> create_nbdata_file false
blogger config -b <blogname> delete_ipynb_meta false
```

> Well, you might want to use ``` <!-- ``` meta format in the first raw/markdown cell. It will be completely hidden while rendering and you need not maintain a separate 'nbdata' file.

