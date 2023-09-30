# GenMuzic - Text2Music Generation

GenMuzic is an innovative music generation application built using Meta's AudioCraft library (MusicGen). It empowers users to generate music compositions from natural language descriptions.

![GenMuzic Logo](https://example.com/genmuzic-logo.png)

## Table of Contents
- [GenMuzic - Text2Music Generation](#genmuzic---text2music-generation)
  - [Table of Contents](#table-of-contents)
  - [Introduction](#introduction)
  - [Features](#features)
  - [Getting Started](#getting-started)
    - [Prerequisites](#prerequisites)
    - [Installation](#installation)
    - [Running the Application](#running-the-application)
  - [Usage](#usage)
  - [Contributing](#contributing)
  - [License](#license)

## Introduction

GenMuzic is a cutting-edge application that demonstrates the power of AI in music composition. It leverages Meta's state-of-the-art AudioCraft library to turn your creative ideas into musical realities. Whether you're a musician looking for inspiration or just curious about the intersection of AI and art, GenMuzic is here to help you explore the possibilities.

## Features

- **Natural Language Input**: Describe your musical vision using everyday language, and GenMuzic will transform it into a unique music composition.
- **Adjustable Duration**: Fine-tune the length of your music piece with an intuitive slider control.
- **Downloadable Music**: Easily download your generated music compositions for offline use or sharing.

## Getting Started

### Prerequisites

Before you begin, ensure you have met the following requirements:

- [Docker](https://www.docker.com/get-started): GenMuzic is containerized using Docker, so you need to have Docker installed on your system.

### Installation

1. Clone the GenMuzic repository to your local machine:

   ```bash
   git clone https://github.com/your-username/genmuzic.git
   cd genmuzic
   ```

2. Build the Docker image:

   ```bash
   docker build -t my-genmuzic-app .
   ```

### Running the Application

Run the Docker container to start the GenMuzic application:

```bash
docker run -p 8501:8501 my-genmuzic-app
```

Access GenMuzic in your web browser at [http://localhost:8501](http://localhost:8501).

## Usage

1. Open your web browser and navigate to [http://localhost:8501](http://localhost:8501).
2. You will be greeted with the GenMuzic interface.
3. Enter a natural language description in the text area.
4. Adjust the desired music duration using the slider.
5. Click the "Generate Music" button.
6. Listen to the generated music, and download it using the provided links.

## Contributing

We welcome contributions to enhance GenMuzic. To contribute, please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Make your changes and commit them.
4. Push your changes to your fork.
5. Open a pull request to the main repository.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

**Made with :heart: by Kunal Kumar Sahoo**