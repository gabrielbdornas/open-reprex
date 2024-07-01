FROM python:3.11.2-slim-bullseye
RUN echo "Setup.  This may take a few minutes ..."
WORKDIR /work_dir
RUN apt-get -y update
RUN apt-get install -y wget nano git ffmpeg
RUN pip install -U openai-whisper
RUN echo "The setup has been made."
