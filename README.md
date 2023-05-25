# CapstoneProject1
# Recipe Generator

This Flask application uses the Spoonacular API to generate recipes based on ingredients provided as inputs. Users can enter the ingredients they have and the application will fetch recipes that can be made using those ingredients.

## Installation

1. Clone the repository: `git clone https://github.com/aalnamer/capstoneProject1.git`
2. Navigate to the project directory: `cd recipe-generator`
3. Create a virtual environment: `python3 -m venv venv`
4. Activate the virtual environment:
   - For Windows: `venv\Scripts\activate`
   - For Unix or Linux: `source venv/bin/activate`
5. Install the dependencies: `pip install -r requirements.txt`

## Configuration

1. Create an account on [Spoonacular](https://spoonacular.com/) and obtain an API key.
2. Rename the `.env.example` file to `.env`.
3. Open the `.env` file and replace `YOUR_API_KEY` with your actual Spoonacular API key.

## Usage

1. Make sure your virtual environment is activated.
2. Run the Flask application: `python app.py`
3. Open your web browser and go to `http://localhost:5000`.
4. Enter the ingredients you have in the input field and click on the "Generate Recipes" button.
5. The application will fetch recipes that can be made using the provided ingredients and display them on the page.

## License

This project is licensed under the [MIT License](LICENSE).

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue for any improvements or new features.

## Acknowledgements

- This application utilizes the [Spoonacular API](https://spoonacular.com/food-api).
- The Flask framework was used for building the web application.
