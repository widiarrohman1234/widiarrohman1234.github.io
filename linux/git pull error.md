# Error
```
fauzan@telegram-scrap:/var/www/telescrap$ git pull origin develop
remote: Enumerating objects: 13, done.
remote: Counting objects: 100% (13/13), done.
remote: Compressing objects: 100% (7/7), done.
remote: Total 7 (delta 4), reused 0 (delta 0)
error: insufficient permission for adding an object to repository database .git/objects
fatal: failed to write object
fatal: unpack-objects failed
```

# Solved
For Ubuntu (or any Linux)

You can tell yourname and yourgroup by:
# for yourname
```
$ whoami
```

# for yourgroup
```
id -g -n <yourname>
```

From project root,
Note: remember the star at the end of the sudo line
```
$ cd .git/objects
$ ls -al
$ sudo chown -R yourname:yourgroup *
```
# Clear

