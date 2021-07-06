FROM python:3.8
COPY requirements.txt /tmp/
COPY ./app /app
WORKDIR "/app"
RUN pip install -r /tmp/requirements.txt
EXPOSE 8080

CMD [ "gunicorn","--workers=5","-b 0.0.0.0:8080","--reload","--reload-engine=auto","--reload-extra-file=/mnt/efs-data/covid-19-data/public/data/vaccinations/vaccinations.csv" ,\
"--reload-extra-file=/mnt/efs-data/covid-19-data/public/data/jhu/locations.csv",\
"--reload-extra-file=/mnt/efs-data/covid-19-data/public/data/jhu/full_data.csv","--reload-extra-file=/mnt/efs-data/covid-19-data/public/data/vaccinations/vaccinations-by-manufacturer.csv",\
"page1:server"]