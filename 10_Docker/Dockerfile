FROM ubuntu:latest

WORKDIR /usr/app/src

ARG LANG='en_US.UTF-8'

# Download and install dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    apt-utils \
    locales \
    python3-pip \
    python3-venv \
    python3-yaml \
    rsyslog systemd systemd-cron sudo \
    && apt-get clean 

# Create and activate a virtual environment
RUN python3 -m venv /opt/venv \
    && . /opt/venv/bin/activate \
    && pip install --upgrade pip \
    && pip install streamlit

# Set the virtual environment as the default Python environment
ENV PATH="/opt/venv/bin:$PATH"

# Copy application code to the container
COPY / ./

# Tell the image what to do when it starts as a container
CMD ["streamlit", "run", "streamlit-app.py"]
