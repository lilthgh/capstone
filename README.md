# Meal plan
# Capstone Project: Balanced Meal Plan Web Application 
CS50 finall Project
The project's video:

## Overview  
The Balanced Meal Plan web application is designed to help users achieve their nutritional goals by providing personalized meal plans based on their individual needs. The application features user authentication with login, registration, and logout functionalities. Once logged in, users can fill out a form that collects important information such as gender, weight, height, age, and activity level. Based on this data, the app calculates the user's Body Mass Index (BMI) and daily caloric requirements (Basal Metabolic Rate - BMR). Utilizing the Spoonacular API, the application generates a balanced meal plan that includes recipes for breakfast, lunch, dinner, and snacks that align with the user’s calorie needs.  

## Distinctiveness and Complexity  
This project is distinct from others in the course as it goes beyond a simple social network or e-commerce platform, integrating complex calculations and API usage to create a dynamic and interactive user experience. Unlike typical projects, the Balanced Meal Plan application includes:  

- **Personalized User Profiles**: User data is stored securely, allowing for tailored meal plans.  
- **Nutritional Calculations**: The integration of BMI and BMR calculations introduces complexity, requiring an understanding of both health metrics and programming logic.  
- **API Integration**: The use of the Spoonacular API to fetch recipes adds a layer of functionality that differentiates this project from others, as it generates real-time data based on user inputs.  
- **Mobile Responsiveness**: The web application is designed to be accessible on various devices, enhancing user experience.  
  
Each of these features contributes to the overall complexity of the project, which consolidates both backend and frontend technologies effectively.  

## Project Structure  

- **Templates**:  
  - `index.html` - The homepage of the application.  
  - `layout.html` - Base HTML template that includes common elements (header, footer).  
  - `login.html` - User login page.  
  - `logout.html` - Confirmation page for logging out.  
  - `meal_plan.html` - The form for users to input their information.  
  - `result.html` - Displays the calculated meal plan and recipes.  

- **Views (views.py)**:  
  - Contains the logic for user authentication, BMI and BMR calculations, and integration with the Spoonacular API to fetch recipes.  

- **Settings (settings.py)**:  
  - Includes the secure API key required to access the Spoonacular recipes API.  

- **Models (models.py)**:  
  - Defines the user and meal plan classes, which store user information such as gender, activity level, height, weight, and age.  

- **URLs (urls.py)**:  
  - Contains routes for login, logout, registration, and generating meal plans.  

## How to Run the Application  

1. **Install required packages**:  
Ensure you have `pip` installed, then run:
pip install -r requirements.txt

2. **Set up the database**:  
Run the following commands to make migrations and migrate your models:
python manage.py makemigrations
python manage.py migrate

3. **Run the development server**:  
Start the server with:
python manage.py runserver

5. **Access the application**:  
Open your web browser and navigate to `http://localhost:8000` to view the application.  

## Additional Information  
Be sure to get a valid API key from Spoonacular and replace the placeholder in `settings.py` to ensure proper functionality.   

  


