# Library-API
it is an Interview question for an interview 

## Instructions:
1. Design and Develop a library API with the following functionalities:
- CRUD Book Categories
- CRUD Books
- Each book must have a category
- When a category is deleted, all books related to that category will have their categories as None.

2. Make an ERD(Entity Relationship Diagram) showcasing your models and their relationships (You can use draw.io to achieve this.)
3. Books should have the following fields:
- title(str),
- author(str),
- no_of_pages(int),
- description(text),
- category(FK)
- created_at(datetime),
- updated_at(datetime)
  
4. Categories should have the following fields:
- name(str),
- created_at(datetime),
- updated_at(datetime)
5. Your DB should be the follow-come sqlite of django.


here is link to my EDR[https://drive.google.com/file/d/1eUd-4KeRmmKW8DQ7qFEz_3I2-tdhjMn0/view?usp=drive_link]
