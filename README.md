# Air Quality App

## Overview
The **Air Quality App** is a simple web-based platform designed to monitor air quality in real-time. It uses a Python Flask backend to serve data and a lightweight, interactive frontend built with HTML, CSS, and JavaScript. The app is currently configured for deployment on Vercel.

This project serves as a foundation for future enhancements, particularly for my **fourth-year Climact Climate Action System**, which will integrate IoT devices and distributed architectures to provide advanced environmental monitoring.

---

## Project Structure

```
air-quality-app
│
├── backend/
│   ├── app.py        # Python Flask server
│   ├── requirements.txt
│
├── frontend/
│   ├── index.html    # Main HTML file
│   ├── style.css     # Optional styling
│   ├── app.js        # JavaScript logic
│
├── vercel.json       # Configuration for Vercel
```

### Folder Details

- **backend/**: Contains the server-side logic, including a Flask application (`app.py`) and its dependencies (`requirements.txt`).
- **frontend/**: Holds the user interface files: 
  - `index.html`: The main webpage.
  - `style.css`: (Optional) Styling for the webpage.
  - `app.js`: JavaScript for interactivity.
- **vercel.json**: Configuration file for seamless deployment on Vercel.

---

## Features

- **Real-Time Air Quality Monitoring**: Backend serves data and API endpoints.
- **Responsive Design**: Frontend designed to be accessible on different devices.
- **Ease of Deployment**: Pre-configured for hosting on Vercel.

---

## Visuals

### Air Pollution
![Air Pollution](https://via.placeholder.com/800x400.png?text=Air+Pollution+Image)

### Climate Action
![Climate Action GIF](https://via.placeholder.com/800x400.gif?text=Climate+Action+GIF)

---

## Getting Started

### Prerequisites
- **Python 3.x**: For the Flask backend.
- **Vercel CLI**: For deployment.
- **A Modern Web Browser**: To view the app.

### Setup Instructions

1. **Clone the Repository**:
   ```bash
   git clone <repository-url>
   cd air-quality-app
   ```

2. **Backend Setup**:
   ```bash
   cd backend
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   pip install -r requirements.txt
   python app.py
   ```
   The backend will start on `http://127.0.0.1:5000`.

3. **Frontend Setup**:
   Open the `frontend/index.html` in a web browser, ensuring the backend server is running.

4. **Deployment (Vercel)**:
   - Install Vercel CLI:
     ```bash
     npm install -g vercel
     ```
   - Deploy the app:
     ```bash
     vercel
     ```

---

## Future Development
This app is a stepping stone for my **Climact Climate Action System** project, which will:
- Integrate IoT environmental sensors.
- Use a distributed architecture with Distributed Hash Tables (DHTs).
- Support real-time, large-scale environmental data monitoring.

---

## Contributing
Feel free to fork this repository, open issues, and submit pull requests to help improve the app.

---

## License
This project is licensed under the MIT License. See the LICENSE file for details.

---

## Contact
For questions, suggestions, or collaboration opportunities, reach out to **engunnzi62194@anu.ac.ke**, a data analyst and software developer passionate about technology for climate action.
