# Hi, I'm Kewal! 👋

# Akshadrik: Drone Surveillance Application

Akshadrik is a powerful Drone Surveillance Application that enables real-time aerial monitoring and object detection using Python, Tkinter, and YOLOv5.

This application has been practically demonstrated to organizations like NSG (National Security Guards), Airport Authority of India (Ahmedabad), and more, making it a trusted tool for security, surveillance, and disaster management operations.

## Table of Contents

- [Key Features](#key-features)
- [Screenshots](#screenshots)
- [Installation and Usage](#installation-and-usage)
- [Contact Me](#contact-me)

## Key Features

The aim of the Akshadrik: Drone Surveillance Application is to provide a versatile and efficient solution for real-time object detection and surveillance using drones.

- **Real-time Surveillance:** Monitor areas from above in real time, capturing crucial data for security, search, and rescue operations.
- **Object Detection:** Utilize YOLOv5 for accurate object detection, identifying potential threats or anomalies with precision.
- **User-friendly Interface:** The intuitive Tkinter-based interface ensures ease of use, even for those new to drone surveillance.
- **Customization:** Configure settings to tailor surveillance tasks to your specific needs, adjusting parameters and target areas as required.

Through these features, Akshadrik strives to be a valuable tool for drone-based surveillance, providing accurate and efficient solutions for a wide range of applications.

## Screenshots
<p align="center">
  <img src = "https://i.imgur.com/gae9kUs.png" width=500><br>
  Multiple options for easy customization
  <br><br>
</p>

<p align="center">
  <img src = "https://i.imgur.com/Og7ALey.png" width=500>
     <img src = "https://i.imgur.com/aG9vIuT.png" width=500><br>
  Choose from various detection categories
</p>

## Installation and Usage

Akshadrik is a GUI application designed for detecting specific targets selected by the user from a list of 30+ categories. Follow these steps to use the application:

1. **Clone the Repository:**

   ```shell
   git clone https://github.com/your-username/Akshadrik-Drone_Surveillance_Application.git
   cd Akshadrik-Drone_Surveillance_Application

2. **Install Dependencies:**

   ```shell
   git clone https://github.com/ultralytics/yolov5
   pip install -r requirements.txt

3. **Run the Application:**

   ```shell
   python Akshadrik.py

4. **Set Video Source:**

   - Open the application.
   - Enter the video source, typically 0 for the default camera.
   - Click the "Set Video Source" button to configure the video source.

   Configuring the video source allows you to choose the input device for surveillance.


5. **Select Detection Item:**

   - Choose the target category you want to detect from the list provided.
   - The application will focus on detecting objects related to your selection.

   Select the detection item to specify what the application should look for in the video stream.


6. **Capture/Stop:**

   - Click the "Capture" button to start capturing and processing video frames.
   - To stop capturing, click the "Stop" button.

   Use these buttons to control the capture and stop functionality of the application.


7. **Real-time Detection:**

   - Akshadrik provides real-time surveillance with accurate object detection.
   - Detected objects will be highlighted in the video stream.

   Experience real-time object detection with Akshadrik as it highlights recognized objects in the video feed.

## Known Issues

While we have made every effort to ensure a smooth and reliable experience with Akshadrik, you may encounter some known issues when running the application:

1. **Video Source Compatibility:** The application may not work correctly with certain video sources or external cameras. Ensure that your video source is properly configured, and the camera drivers are up to date.

2. **Performance on Low-End Systems:** On low-end hardware configurations, you may experience reduced performance or lag during real-time detection. We recommend using a system with adequate processing power for optimal results.

3. **Dependency Conflicts:** Depending on your system and environment, you may encounter dependency conflicts or installation issues. Make sure you have installed the required dependencies as outlined in the Usage Instructions.

4. **Object Recognition Accuracy:** While we aim for accurate object detection, the performance may vary depending on the lighting conditions, camera quality, and the specific objects being detected.

5. **Limited Operating Systems:** The application is primarily tested on certain operating systems, and there may be compatibility issues with less common or older systems.

6. **User Interface (UI) Responsiveness:** The UI may become unresponsive during intense processing tasks. This is a limitation of the current implementation.

7. **Resource Consumption:** Akshadrik may consume a significant amount of system resources, especially during real-time detection. Ensure that your system meets the hardware requirements.

## Contact Me

I'd love to hear from you and answer any questions you may have about the applications or any other projects. Feel free to reach out to me:

<p align ="center">
  <a href="mailto:work.kewalshah@gmail.com?subject=Feedback%20From%20Github&body=Hello," target="_blank">
    <img src="https://img.shields.io/badge/Gmail: work.kewalshah@gmail.com-D14836?style=for-the-badge&logo=gmail&logoColor=white" alt="example"/>
  </a><br>
   <a href="https://www.linkedin.com/in/kewal-shah-work/" target="_blank">
    <img alt="LinkedIn" src="https://img.shields.io/badge/LinkedIn: Kewal Shah-0077B5?style=for-the-badge&logo=linkedin&logoColor=white">
  </a>   
</p>
