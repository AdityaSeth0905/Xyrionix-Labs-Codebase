# Xyronix Labs

Welcome to the Xyronix Labs website repository.

## Website Domain
[www.xyronixlabs.com](http://www.xyronixlabs.com)

## Frontend
The frontend of this website is built using:
- React
- Typescript
- Tailwind CSS
- Yarn

## Backend
The backend of this website is powered by Django.

## API
- Backend: FastAPI and Django REST Framework (DRF)
- Frontend: Axios

## Getting Started
To get started with the project, follow these steps:

1. Clone the repository:
    ```bash
    git clone https://github.com/AdityaSeth0905/Xyrionix-Labs-Codebase.git
    ```
2. Navigate to the project directory:
    ```bash
    cd Xyrionix-Labs-Codebase
    ```
3. Install frontend dependencies:
    ```bash
    cd frontend
    yarn install
    ```
4. Install backend dependencies:
    ```bash
    cd ../backend
    pip install -r requirements.txt
    ```
5. Set up environment variables:
    - Create a `.env` file in the `backend` directory and add the necessary environment variables. Refer to `.env.example` for the required variables.
    - Update the `.gitignore` file to include the `.env` file to ensure it is not tracked by git.
6. Run the development server:
    ```bash
    cd ../frontend
    yarn start
    ```
    In another terminal, run:
    ```bash
    cd ../backend
    python manage.py runserver
    ```

## Running Tests
To run tests for the project, follow these steps:

1. Navigate to the `backend` directory:
    ```bash
    cd backend
    ```
2. Run the tests:
    ```bash
    python manage.py test
    ```

## Contributing
We welcome contributions! Please fork the repository and submit pull requests to contribute.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
