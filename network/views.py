import requests  
import random  
from django.shortcuts import render  
from django.http import HttpResponseRedirect  
from django.urls import reverse  
from django.contrib.auth import authenticate, login, logout  
from .models import User 
from django.db import IntegrityError  
from django.views import View 
from django.conf import settings 

def index(request):  
    return render(request, "network/index.html")  

def login_view(request):  
    if request.method == "POST":  
        username = request.POST["username"]  
        password = request.POST["password"]  
        user = authenticate(request, username=username, password=password)  

        if user is not None:  
            login(request, user)  
            return HttpResponseRedirect(reverse("index"))  
        else:  
            return render(request, "network/login.html", {  
                "message": "Invalid username and/or password."  
            })  
    else:  
        return render(request, "network/login.html")  

def logout_view(request):  
    logout(request)  
    return HttpResponseRedirect(reverse("index"))  

def register(request):  
    if request.method == "POST":  
        username = request.POST["username"]  
        email = request.POST["email"]  

        password = request.POST["password"]  
        confirmation = request.POST["confirmation"]  
        if password != confirmation:  
            return render(request, "network/register.html", {  
                "message": "Passwords must match."  
            })  

        try:  
            user = User.objects.create_user(username, email, password)  
            user.save()  
        except IntegrityError:  
            return render(request, "network/register.html", {  
                "message": "Username already taken."  
            })  
        login(request, user)  
        return HttpResponseRedirect(reverse("index"))  
    else:  
        return render(request, "network/register.html")  


 

class MealPlanView(View):  

    def get(self, request):  
        return render(request, 'network/meal_plan.html')  # Render the form for input  

    def post(self, request):  
        gender = request.POST['gender']  
        weight = float(request.POST['weight'])  
        height = float(request.POST['height'])  
        age = int(request.POST['age'])  
        activity_level = request.POST['activity_level']  

        # Calculate daily caloric needs based on user input  
        daily_calories = self.calculate_caloric_needs(gender, weight, height, age, activity_level)  

        # Generate meal plan based on the caloric needs  
        meal_plan = self.generate_meal_plan(daily_calories)  

        context = {  
            'daily_calories': round(daily_calories),  
            'meal_plan': meal_plan  
        }  
        return render(request, 'network/meal-result.html', context)  

    @staticmethod  
    def calculate_caloric_needs(gender, weight, height, age, activity_level):  
        # Calculate BMR  
        if gender == 'male':  
            bmr = 10 * weight + 6.25 * height - 5 * age + 5  
        elif gender == 'female':  
            bmr = 10 * weight + 6.25 * height - 5 * age - 161  
        else:  
            raise ValueError("Invalid gender entered.")  

        # Adjust BMR based on activity level  
        activity_multipliers = {  
            'sedentary': 1.2,  
            'lightly active': 1.375,  
            'moderately active': 1.55,  
            'very active': 1.725  
        }  

        multiplier = activity_multipliers.get(activity_level, 1.2)  # Default to sedentary if invalid input  
        return bmr * multiplier  

    def generate_meal_plan(self, caloric_needs):  
        meal_data = []  # This will hold all meal data for rendering  

        # Generate breakfast  
        b_calories, b_title, b_image, b_ingredients = self.get_random_meal('breakfast', caloric_needs * 0.25)  
        meal_data.append({  
            'type': 'Breakfast',  
            'title': b_title,  
            'calories': b_calories,  
            'image': b_image,  
            'ingredients': b_ingredients,  
        })  

        # Generate lunch  
        l_calories, l_title, l_image, l_ingredients = self.get_random_meal('lunch', caloric_needs * 0.35)  
        meal_data.append({  
            'type': 'Lunch',  
            'title': l_title,  
            'calories': l_calories,  
            'image': l_image,  
            'ingredients': l_ingredients,  
        })  

        # Generate dinner  
        d_calories, d_title, d_image, d_ingredients = self.get_random_meal('dinner', caloric_needs * 0.30)  
        meal_data.append({  
            'type': 'Dinner',  
            'title': d_title,  
            'calories': d_calories,  
            'image': d_image,  
            'ingredients': d_ingredients,  
        })  

        # Add snacks  
        remaining_calories = caloric_needs - sum(meal['calories'] for meal in meal_data)  
        while remaining_calories > 0:  
            snack_calories, snack_title, snack_image, snack_ingredients = self.get_random_snack(remaining_calories)  
            if snack_calories == 0:  
                break  
            meal_data.append({  
                'type': 'Snack',  
                'title': snack_title,  
                'calories': snack_calories,  
                'image': snack_image,  
                'ingredients': snack_ingredients,  
            })  
            remaining_calories -= snack_calories  

        print(f'Meal Data: {meal_data}')  # Debug output for meal plan content  
        return meal_data  # Return the list of meal information  

    @staticmethod  
    def get_random_meal(meal_type, max_calories):  
        api_key = settings.SPOONACULAR_API_KEY  
        url = f'https://api.spoonacular.com/recipes/complexSearch?query={meal_type}&maxCalories={max_calories}&apiKey={api_key}'  

        response = requests.get(url)  

        if response.status_code == 200:  
            data = response.json()  
            meals = data.get('results', [])  

            if meals:  
                random_meal = random.choice(meals)  
                print(f'Fetched Meal: {random_meal}')  # Debugging output  
                # Extracting calories from the nutrition field  
                calories = 0  # Default to 0  
                for nutrient in random_meal.get('nutrition', {}).get('nutrients', []):  
                    if nutrient['name'] == 'Calories':  
                        calories = nutrient['amount']  # Set calories to the correct amount  
                        break  

                title = random_meal.get('title', 'Unknown Meal')  
                image = random_meal.get('image', '')  
                recipe_id = random_meal.get('id')  

                ingredients = MealPlanView.get_ingredients(recipe_id) if recipe_id else []  

                return calories, title, image, ingredients  # Return correctly extracted calories  

        print(f'Error fetching meals: {response.status_code} {response.text}')  # Error handling  
        return 0, None, '', []  # Return default values  

    @staticmethod  
    def get_random_snack(max_calories):  
        api_key = settings.SPOONACULAR_API_KEY  
        url = f'https://api.spoonacular.com/recipes/complexSearch?query=snack&maxCalories={max_calories}&apiKey={api_key}'  

        response = requests.get(url)  

        if response.status_code == 200:  
            data = response.json()  
            snacks = data.get('results', [])  

            if snacks:  
                random_snack = random.choice(snacks)  
                print(f'Fetched Snack: {random_snack}')  # Debugging output  
                # Extracting calories from the nutrition field  
                calories = 0  # Default to 0  
                for nutrient in random_snack.get('nutrition', {}).get('nutrients', []):  
                    if nutrient['name'] == 'Calories':  
                        calories = nutrient['amount']  # Set calories to the correct amount  
                        break  

                title = random_snack.get('title', 'Unknown Snack')  
                image = random_snack.get('image', '')  
                 
                ingredients = MealPlanView.get_ingredients(random_snack.get('id'))  # Directly use the snack ID  

                return calories, title, image, ingredients  # Return four values  

        print(f'Error fetching snacks: {response.status_code} {response.text}')  # Print error message  
        return 0, None, '', []  # Ensure we always return four values  

    @staticmethod  
    def get_ingredients(recipe_id):  
        """Fetch the ingredients for a given recipe ID."""  
        api_key = settings.SPOONACULAR_API_KEY  
        url = f'https://api.spoonacular.com/recipes/{recipe_id}/ingredientWidget.json?apiKey={api_key}'  
        response = requests.get(url)  

        if response.status_code == 200:  
            data = response.json()  
            ingredients = [ingredient['name'] for ingredient in data.get('ingredients', [])]  
            return ingredients  
        else:  
            print(f'Error fetching ingredients for recipe ID {recipe_id}: {response.status_code} {response.text}')  
            return [] 