FROM hitokizzy/unicorn:slim-buster

# Working Directory
WORKDIR home/unicorn/

# Clone Repo
RUN git clone -b master https://github.com/hitokizzy/unicorn-pyrobot.git home/unicorn/

# Run bot
CMD ["python3", "unicorn.py"]
