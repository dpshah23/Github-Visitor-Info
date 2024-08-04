# Github Visit User Info Tracking

Welcome to the Flask API for GitHub Insights! This repository provides the backend service for collecting visitor data from GitHub profile links. The API retrieves the IP address of the visitor solely to determine the city, state, and country. No personal or identifying information is stored.

## Features

- **IP Address Retrieval**: Collects the IP address of visitors for geolocation purposes.
- **Geolocation**: Retrieves and returns the city, state, and country based on the IP address.
- **Privacy-Focused**: Does not store any user information, ensuring complete privacy.

## How It Works

1. **API Endpoint**: A unique endpoint is provided for each user, which should be integrated into their GitHub profile README.
2. **Data Collection**: When someone visits the GitHub profile, the API retrieves the IP address and uses it to fetch the location information.
3. **Data Transmission**: The retrieved data is sent to the Django Admin Panel for visualization and analysis.

## Prerequisites

- **Python 3.8+**: Ensure you have Python installed.
- **Docker**: Recommended for containerized deployment.

## Installation

1. **Clone the Repository**:
   ```bash
   git clone [https://github.com/dpshah23/GitHub-Insights-Flask-API.git](https://github.com/dpshah23/Github-Visitor-Info.git)
   cd Github-Visitor-Info

   ```

2. **Set Up Environment Variables**:
   - Create a `.env` file with the necessary configuration. Include sensitive information such as API keys and database credentials.

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Application**:
   ```bash
   flask run
   ```

## Docker Deployment

### Build APP

```sh
docker build -t github-visitor-info .
```

### Run APP

```sh
docker run -p 5000:5000 github-visitor-info
```

## Contribution

Contributions are welcome! Feel free to open an issue or submit a pull request for new features or improvements.

---

*Note*: This API **does not store IP addresses**. The data is used only for geolocation and immediately discarded.

For any inquiries, contact us at [dpshah2307@gmail.com](mailto:dpshah2307@gmail.com).


