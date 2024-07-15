#docker run --rm -it -p 5000:5000 -v $(pwd):/blog --entrypoint "/bin/sh" blog
source ~/.zshrc
venv_activate blog
python3 ./blog.py $@
deactivate
