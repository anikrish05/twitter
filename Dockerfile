FROM python:2.7
COPY . /work
WORKDIR /work
RUN pip install -r app/requirements.txt
CMD ['env/venv/bin/activate']
CMD ['export FLASK_APP = profile.py]
CMD ['flask run']
