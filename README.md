Skeleton of a skeleton of a website for Seattle Rationality. I'm loosely following [this tutorial][tutorial]. My commit messages are intended to be very helpful, distilling down the most important bits of the tutorial.

Feel free to clone it, run

    python manage.py runserver

and visit `localhost:8000/lightning_talks` (currently the only semi-functional part of the site). To populate your local database, you may want to run `add_dummy_data.py` (must be from this directory, because of Django magic).

(This is a prototype, not suitable for production, because the `SECRET_KEY` has been exposed to the world. We'll need to, I dunno, at least make the repo private, then change the secret key, and *then* fire the site up for real.)


[tutorial]: https://docs.djangoproject.com/en/1.9/intro/tutorial01
