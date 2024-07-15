# Use the specified base image
FROM --platform=linux/amd64 alpine:3.20.1

# Set the working directory
WORKDIR /app

# Copy all necessary files into the container
COPY . .

# Copy and run the build script
COPY build.sh .
RUN chmod +x build.sh
RUN ./build.sh

# Command to run the application (optional)
CMD ["/app/test_libcsv"]
