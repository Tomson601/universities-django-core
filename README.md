## universities-django-core web app

### Installation process:

1.Clone repository: ```git clone https://github.com/Tomson601/universities-django-core.git ```

2.Create virtual environment: ```python3 -m venv venv```

3.Activate venv: ```source venv/bin/activate```

4.Download required packs: ```pip install -r requirements.txt```

### Heroku commands:
1.python main/manage.py migrate  
2.python main/manage.py shell  

### Popular errors:
ERROR: Failed building wheel for psycopg2:
1. apt-get install python3-dev
2. sudo apt-get install python3 python-dev python3-dev \
    build-essential libssl-dev libffi-dev \
    libxml2-dev libxslt1-dev zlib1g-dev \
    python-pip  
https://github.com/scrapy/scrapy/issues/2115#issuecomment-231849637

### Ideas:  

**1. Get data about high schools**✅  
-scrap data from html or download to txt file✅  

**2. Add sorting methods, sort by:**  
-country, 
-technical schools, 
-specialization  

**3. Add minimalist GUI (just html + css)**✅  
**4. Host website**✅  
**5. Add searchbar**✅  
**6. Add university preview**  
