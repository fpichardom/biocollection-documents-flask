# Use the Python 3.12 base image
FROM python:3.12

# Set the working directory inside the container to /code
WORKDIR /code


# Install Python dependencies
## Copy the requirements.txt file from the host to the container's working directory
COPY requirements.txt .
## Install the Python dependencies specified in requirements.txt
RUN pip install -r requirements.txt


# Install Node.js and npm
RUN curl -fsSL https://deb.nodesource.com/setup_20.x | bash -
RUN apt-get install -y nodejs

# Copy the package.json file from the host to the container's working directory
COPY package*.json .

# Install the Node.js dependencies
RUN npm install

# Copy all the files from the host to the container's working directory
COPY . .





# Run the Flask application
# It is already handled by docker compose
CMD ["flask", "run", "--port=5000"]


