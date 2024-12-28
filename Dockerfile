FROM python:3.12
RUN cat /etc/issue

# add microsoft package repositories
RUN curl -fsSL https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor -o /usr/share/keyrings/microsoft-prod.gpg
RUN curl https://packages.microsoft.com/config/debian/12/prod.list | tee /etc/apt/sources.list.d/mssql-release.list

RUN apt-get update

# load microsoft librarys
RUN ACCEPT_EULA=Y apt-get install -y msodbcsql17
RUN ACCEPT_EULA=Y apt-get install -y mssql-tools
RUN echo 'export PATH="$PATH:/opt/mssql-tools/bin"' >> ~/.bashrc
RUN apt-get install -y unixodbc-dev

# add packages
WORKDIR /app
ADD requirements.txt .
RUN pip install --upgrade --force-reinstall --no-cache-dir -r requirements.txt

# Copy the current directory contents into the container at /usr/src/app
COPY . .

# Make port 80 available to the world outside this container (Optional, only for web apps)
EXPOSE 8000

CMD ["python","-i","main.py"]
