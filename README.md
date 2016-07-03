Skeleton of a skeleton of a website for Seattle Rationality. I'm loosely following [this tutorial][tutorial].

Feel free to clone it, run

    python manage.py runserver

and visit `localhost:8000/lightning_talks` (currently the only semi-functional part of the site). To populate your local database, you may want to run `add_dummy_data.py` (must be from this directory, because of Django magic).

My commit messages are intended to be very helpful, distilling down the most important bits of the tutorial.


[tutorial]: https://docs.djangoproject.com/en/1.9/intro/tutorial01
