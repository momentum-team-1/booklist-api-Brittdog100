# Build an API for keeping lists of books

For this project, you will build an API for keeping lists of books you want to read, are reading, or have read.

## Requirements

- This API allows users to register and authenticate. Use [djoser](https://djoser.readthedocs.io/en/latest/index.html) to implement registration, and use token-based authentication.
- Users can only see books they have input into the system. Users cannot see each others' books, nor can unauthenticated users see any books.
- Books should have a title, zero or more authors, and a status ("to read", "reading," and "read".)
- Users can update and delete their books.
- Users can move books between statuses (this is just updating status, should be the same endpoint as updating anything about a book.)
- Users can get all their books as one list, or books by status. Consider using [DjangoFilterBackend](https://www.django-rest-framework.org/api-guide/filtering/#djangofilterbackend) for this, and consider adding other filters, like author or title.
- Users can add notes to books. These notes have a datetime they are created, a note, and an optional page number. When notes are retrieved, return them by creation time in reverse order.

## Notes

The Django project for this application is already created. There is an `api` app already created as well. You can build all models, serializers, and views in this `api` app. The default user model is also located in this app at `api.models.User`.

Django REST Framework has already been installed and added to `INSTALLED_APPS`, although no other setup has been done.

You should test your API as you are building it. We recommend using Insomnia to build requests you can run over and over.
