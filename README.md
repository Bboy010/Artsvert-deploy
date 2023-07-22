# Artsvert- Only recycle project limit protfolio project 3weeks 🥇
<div style="text-align:center;"> <img src="artsvert logo-1.png" /> </div>

Artsvert
: is an online platform that aims to promote recycling and sustainability by providing a virtual gallery where users can showcase and trade recycled or upcycled art and craft items.
---
Role
: The platform will connect artists, designers, and individuals interested in eco-friendly creations, creating a community focused on recycling and creativity.

## Architecture
<div style="text-align:center;"> <img src="Artverts project.png" /> </div>

## Home page
<div style="text-align:center;"> <img src="home.png" />
 </div>
 
 ---
 
## Architecture 🛩️

1. [routes](src/routes)
2. [static](src/static)
3. [templates](src/templates)
4. [Flask app](src/app.py)
5. [database](src/database.py)
6. [models](src/models.py)

## How to deploy on local
*pre-requisite*
> This an example of deployement on Windows using Xampp, any browser and Visual Studio Code
1. Clone or fork this repository
2. Install Xampp for Windows (64 bit) [Xampp](https://sourceforge.net/projects/xampp/files/XAMPP%20Windows/8.0.28/xampp-windows-x64-8.0.28-0-VS16-installer.exe)
3. run the server Xampp and start *Apache* and *MySQL*
4. create database named artsvert_db and import [database](artsvert_db.sql)
5. Open VS code and ensure that [python](https://www.python.org/downloads/release/python-3114/) is available on your machine
6. Open the folder of artsvert project and create a python [virtual environment](https://docs.python.org/3/library/venv.html)
 `c:\>python -m venv c:\path\to\myenv`
7. Install [requirements](requirements.txt) files
`pip install requirements.txt`
8. run the [Flask app](src/app.py)
`flask run`
9. Open your browser and acceed to the Url
---
**Congrate** 🥳🥳🥳
 
### Key Features:
- User Registration and Profiles:
> Users can create accounts with basic information and profile pictures.
> Users can provide additional details about their interests and expertise in recycling and upcycling.
- Item Listing:
> Users can list their recycled or upcycled art and craft items for sale or trade.
> Each listing includes a title, description, images, price (or trade preference), and shipping details.
> Users can categorize their items based on different art forms, materials used, or sustainability themes.
- Search and Filter:
> Users can search for specific items based on keywords, categories, or artists' names.
> Filter options are available to narrow down search results by price range, location, or other relevant criteria.
- Item Detail Page:
> Each item has a dedicated page displaying its images, description, price/trade preference, and shipping details.
> Users can view the seller's profile, including their bio and other listed items.



### Authors
<a href="https://github.com/8srael" >Kouassi</a> & <a href="https://github.com/Bboy010" >Hongo</a>

:accessibility:
[^1]: Alx-portfolio-project
