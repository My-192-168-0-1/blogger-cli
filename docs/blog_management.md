# Managing the blog
Blogger-cli is primarily a conversion tool. So the blog management is more like config holder for your website's folder.

# Contents
1. [Registering a blog](#Registering-a-blog)
2. [Editing blog configs ](#Editing-blog-configs)
    - [Editing in bulk](#Editing-in-bulk)
    - [Editing individually](#Editing-individually)
    - [Config command](#Config-command)
3. [Setting default blog](#Setting-default-blog)
4. [Removing a blog](#Removing-a-blog)


<a id="Registering-a-blog"></a>
# Registering a blog

'blogs' need to be registered first. You can do so by:
```
blogger addblog <blogname>
```
You will be asked a series of questions you can answer them or skip over them using 'n'
Similarly, if you want to avoid getting asked these questions and only want to register a blog use
```
blogger addblog <blogname> -s
```
You can always set up configs later

<a id="Editing-blog-configs"></a>
# Editing blog config
A registered blog has number of configs that you can edit.

'blog_dir':
This is the main folder of your website. This folder is not used to store converted Html blogs since it is treated as a root website folder.
eg values: '~/my_website_folder/', 'C:\Useres\Desktop\'

'blog_posts_dir':
This is the folder you want to keep your converted blog posts in. It is specified with respect to blog_dir folder (root dir).

Example values: 'blog/', 'posts/'.

> Do not use '/' in front of folder name like '/blog/'. It conveys a different meaning.


'blog_images_dir':
Where you want to store the images that we extract for you from Http/s URLs and data URI in your post. The path value is relative from root dir (blog_dir) same like blog_posts_dir. Images will be stored in folders with the same name as your blog title and If you have a topic then it will be used too. like topic/blog_title/.

Example values: 'images/blog/', 'images/', 'blog/images/'.

> For sites like Github pages, you need to keep the 'images' folder in the root folder of your website.


'disqus_username':
If you have a Disqus account you can enter the username here and the commenting system will work on every post. You can get it from Disqus account URL. eg https://badboy11.disqus.com 's username will be 'badboy11'.

'google_analytics_id':
It is a snippet provided by Google to analyze your website's traffic. Sign in and get a snippet and you can get id from that snippet. eg: 'UA-159824128-0'

'templates_dir':
It is the directory where you can override default Html templates to suit your needs. More info [here](customizing.md).

<a id="Editing-in-bulk"></a>
## Editing in bulk

To edit all configs in bulk, you can run:
```
blogger setupblog <blogname>
```
To skip without making any changes, type 'n' and press enter. To delete a VALUE from config, type one or many space and press enter.

<a id="Editing-individually"></a>
## Editing individually

Use 'blogger info' command to view all config options for a blog then,
```
blogger config -b <blogname> [config option]  [value]
```

<a id="Config-command"></a>
## Config Command
The config command allows you to manage configs in more flexible way. It allows you to set every configurations like [advanced configs](#Advanced-configs)

### Viewing a config's value
To view a value of a config,
```
blogger config -b <blogname> [config option]
```
If nothing shows up. Your value is empty.
> To view all configs of blog use ```blogger info <blogname>``` instead.

### Deleting a config
Similarly to delete a config,
```
blogger config -b <blogname> -rm [config option]
```
You can remove a default property of blog as well.
```
blogger config -b <blogname> -rm default
```

### Restoring configurations
You can also restore blog configs of a blog that you exported using [export command](export.md#Exporting-blog-configurations)
```
blogger config -b <blogname> -re <config_filename>
```

> Never use config to add a default property to a blog to make it default instead use [setdefault](#Setting-default-blog) command.

### Advanced configs
You can view these configurations from
```
blogger info --all
```
The use cases of these configs have been specified [here](optional_config.md).


<a id="Setting-default-blog"></a>
# Setting default blog:
To set a blog as the default, use:
```
blogger setdefault <blogname>
```
Once a blog is set as default you do not need to specify a blog or -b parameter to ANY commands!. If you want to set another blog as the default, use:
```
blogger setdefault <anotherblogname>
```
Everything will safely be handled. If for some reason you don't want to set any blog as default use [config command](#Editing-individually) to delete the default property.
Similarly, if blog 'A' is default you can specify -b option in command for operating on other blogs.


<a id="Removing-a-blog"></a>
# Removing a blog
You will lose everything if you do so.
```
blogger rmblog <blogname>
```
It only accepts one blog at a time.


