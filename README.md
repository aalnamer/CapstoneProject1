# CapstoneProject1

Recipe Generator
This Flask application uses the Spoonacular API to generate recipes based on ingredients provided as inputs. Users can enter the ingredients they have and the application will fetch recipes that can be made using those ingredients.

Installation
Clone the repository: git clone https://github.com/your-username/recipe-generator.git
Navigate to the project directory: cd recipe-generator
Create a virtual environment: python3 -m venv venv
Activate the virtual environment:
For Windows: venv\Scripts\activate
For Unix or Linux: source venv/bin/activate
Install the dependencies: pip install -r requirements.txt
Configuration
Create an account on Spoonacular and obtain an API key.
Rename the .env.example file to .env.
Open the .env file and replace YOUR_API_KEY with your actual Spoonacular API key.
Usage
Make sure your virtual environment is activated.
Run the Flask application: python app.py
Open your web browser and go to http://localhost:5000.
Enter the ingredients you have in the input field and click on the "Generate Recipes" button.
The application will fetch recipes that can be made using the provided ingredients and display them on the page.
License
This project is licensed under the MIT License.

Contributing
Contributions are welcome! Please feel free to submit a pull request or open an issue for any improvements or new features.

Acknowledgements
This application utilizes the Spoonacular API.
The Flask framework was used for building the web application.
