# Dockerfile
# #############################################################################
#
# Build image:
# >> docker build -t test_dash .
#
# Run container:
# >> docker run -p 8050:80 --name test_dash -it test_dash
#
###############################################################################

FROM    recognai/python-37-centos
LABEL   maintainer="Test Testovich"
WORKDIR     /workdir
COPY        . .

RUN         pip install --upgrade pip && pip install --no-cache-dir -r /workdir/requirements.txt

EXPOSE 8050

ENV NAME World

CMD ["python", "app/app.py"]
