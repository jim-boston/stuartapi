FROM python:3.12
RUN cat /etc/issue

RUN apt-get update

# add packages
WORKDIR /app
ADD requirements.txt .
RUN pip install --upgrade --force-reinstall --no-cache-dir -r requirements.txt

# Copy the current directory contents into the container at /usr/src/app
COPY . .

# Make port 80 available to the world outside this container (Optional, only for web apps)
EXPOSE 8000

CMD ["python","-i","main.py"]
