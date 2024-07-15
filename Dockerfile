# Use the specified base image
FROM alpine:latest
# Set the working directory
WORKDIR /app

# Install required packages
RUN apk add --no-cache python3 py3-pip bash

# Copy all necessary files into the container
COPY . .

# Create a virtual environment and install dependencies
RUN python3 -m venv venv && \
    . venv/bin/activate && \
    pip install pandas

# Ensure the virtual environment's Python is used in CMD
ENV PATH="/app/venv/bin:$PATH"

# Command to run the application (optional)
CMD ["/app/test_libcsv"]
