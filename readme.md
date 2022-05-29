# Gift Shop Project


This project was carried out for a computer engineering subject, with the intention of solving projects and meeting requirements

## Technologies behind the project

- Frontend (this part its in another repo)
    - Webpack
    - Pug
    - PostCss
    - Tailwind
        - DaisyUI
    - Vanilla Javascript (Babel)
- Backend
    - Python
    - Django
    - Wagtail CMS
    - Django Unicorn (For reactive components)

## Requirements

- Python 3.10.X
- Pip 22.X

## How to Set Up (after download and enter to folder's project)?
1. First we will install virtualenv to be able to generate a virtual python environment (this is to avoid messing up our default python installation, as well as not conflicting with previously installed packages)

```console
nefonfo@laptop:~$ pip install virtualenv
```

2. We will create our virtual environment to work, this will create the env with the name that you decided (recomended: env)
```console
nefonfo@laptop:~$ virtualenv <env_name>
```

3. We will activate our virtual environment, this may vary depending on the operating system

### **Unix or MacOs**
```console
nefonfo@laptop:~$ source ./<env_directory>/bin/activate
```
### Result:
```console
(env) nefonfo@laptop:~$
```

### **Windows CMD**
```console
C:\Users\vicmi\Documents\gift_shop> ./<env_directory>/bin/activate.bat
```
### Result:
```console
(env) C:\Users\vicmi\Documents\gift_shop>
```

### **Windows Powershell**
```console
PS C:\Users\vicmi\Documents\gift_shop> ./<env_directory>/bin/activate.bat
```
### Result:
```console
(env) PS C:\Users\vicmi\Documents\gift_shop>
```

4. We will bring all the required packages with the following command, this will take a while
```console
(env) nefonfo@laptop:~$ pip install -r requirements.txt
```

5. Now we will migrate the database to be able to use it with the following command (this will take some minutes):
```console
(env) nefonfo@laptop:~$ python ./manage.py migrate
```

6. We will create a superuser (it will ask you for an email and password), with this you will be able to access < URL >/admin
```console
(env) nefonfo@laptop:~$ python ./manage.py createsuperuser
```

7. Now we are ready to start the server with the following command:
```console
(env) nefonfo@laptop:~$ python ./manage.py runserver
```

**Congratulations, the proyect will be listening on localhost:8000**

## TODO

- Password Reset
- User Gift Codes (buy)
- User Checkout
    - Apply Coupons
    - Gift Codes
    - Shippment
    - Payment
- User Orders