FROM hitokizzy/unicorn:slim-buster

# Working Directory
WORKDIR /unicorn/

# Clone Repo
RUN git clone -b unicorn https://github.com/hitokizzy/unicorn-pyrobot.git /unicorn/

# Run bot
CMD ["python3", "unicorn.py"]
