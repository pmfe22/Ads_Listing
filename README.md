# Ad Listing Project

This is a simple web application for managing advertisements. Users can create, update, and delete ads, as well as mark ads as their favorites.

## Features

- **User Authentication**: Users can log in and create accounts.
- **Create Ads**: Logged-in users can create ads with a title, price, and tags.
- **Edit and Delete Ads**: Users can edit or delete ads they have created.
- **Favorites**: Users can mark ads as their favorites and see them later.
- **Search Ads**: Users can search ads by title,text,tags and price.
- **Tag Filter**: Users can filter ads by tags.

## Tech Stack

- **Backend**: Django (Python)
- **Frontend**: HTML, CSS, JavaScript (for interactivity)
- **Database**: SQLite (default), but can be configured to use PostgreSQL or MySQL
- **Other**: Font Awesome for icons (edit, delete, favorite) , Bootstrap

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/pmfe22/Ads_Listing.git

2.Navigate to the project directory:
	```bash
	cd ad-listing

3.Install dependencies:
	```bash
	pip install -r requirements.txt

4.Apply database migrations
	```bash
	python manage.py migrate

5.Create a superuser for admin access (optional):
	```bash
	python manage.py createsuperuser

6.Run the development server:
	```bash
	python manage.py runserver

7.Access the app at http://localhost:8000/.


Usage
Homepage: The homepage displays a list of all ads with the option to search, filter by tags, and mark ads as favorites.
Create Ad: Navigate to the "Create a New Ad" page to create a new advertisement.
Edit Ad: If you're the owner of an ad, you can edit or delete it.
Favorites: Click the star icon to mark an ad as a favorite. A filled star means the ad is favorited.


Customizing the Project
You can customize the tags, favorite icon (star), and styling of the website in the corresponding templates and CSS files.
The project uses Font Awesome for icons. You can change icons or add your own if needed.


Contributing
1.Fork the repository.
2.Create your feature branch (git checkout -b feature-name).
3.Commit your changes (git commit -am 'Add feature').
4.Push to the branch (git push origin feature-name).
5.Create a new Pull Request.


License
This project is open source and available under the MIT License.

Acknowledgments
Django for the web framework.

