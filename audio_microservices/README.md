# Audio Microservices

This project implements two microservices, Microservice A and Microservice B, for audio processing and speech detection.

## Microservice A

Microservice A takes a provided WAV audio file as input, cuts it into 20 ms audio frames, and sends each frame to Microservice B. It then prints the return value from Microservice B, which indicates whether speech is ongoing or has ended.

### Instructions for Microservice A

1. Place the input audio file (WAV format) in the `audio_files` directory.
2. Ensure that the audio file has the correct format: WAV file, sample rate 16 kHz, and mono audio.
3. Build and run Microservice A using the provided Docker configuration.
4. Microservice A will process the audio file, send frames to Microservice B, and print the return values.

## Microservice B

Microservice B receives 20 ms frames as byte arrays from Microservice A. It checks if the input frame is a byte array of the expected size, sums up the input frames to create audio chunks of 500 ms length, and performs speech detection on each chunk. It returns "False" if speech is ongoing and "True" if speech has ended.

### Instructions for Microservice B

1. Ensure Microservice A is running and accessible to Microservice B.
2. Build and run Microservice B using the provided Docker configuration.
3. Microservice B will receive frames from Microservice A, perform speech detection, and return the results.

## Running the Microservices

To build and run both Microservice A and Microservice B together, follow these steps:

1. Install Docker on your system.
2. Open a terminal and navigate to the project directory.
3. Run the following command to build and run the microservices:

```
docker-compose up --build
```

4. The microservices will start running in separate Docker containers, and the processing will begin.
5. Provide the path to the audio file as input to Microservice A (if you need to change the audio file)
6. The output will be displayed in the terminal.


## TODO (If I had more time)
- Investigate the issue where the solution (i.e Microservice B) does not return "True" when speech has stopped.
- Check the speech detection logic in Microservice B for any potential bugs or errors.
- Test different audio files and scenarios to ensure accurate speech detection.
- Consider optimizing the code for better performance and efficiency.

## Dependencies

The project uses the following third-party libraries:

- Flask: A micro web framework for building the REST API.
- Docker: Containerization platform for running the microservices.

## Author

[Oluwajoba Bello](https://www.linkedin.com/in/oluwajoba1/)

## License

This project is licensed under the [MIT License](LICENSE).


## Additional Notes

- The microservices are implemented in Python using Flask for the web server.
- Third-party libraries are used as necessary for audio processing and web communication.
- The project is designed to run within Docker containers for easy deployment and portability.
- Some of the codes were gerenated using ChatGPT and then modified to preference.

