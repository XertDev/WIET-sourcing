## Migrations 
You can create new migration with:
```shell script
flask db migrate -m "name"
```
Then you can apply them to database with:
```shell script
flask db upgrade
```
Note, that it may not work correctly with Enum attributes. 