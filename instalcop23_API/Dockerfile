FROM python:3.10.5
COPY requirements.txt /app/
RUN pip install -r /app/requirements.txt
COPY . /app/
WORKDIR /app/
RUN python3 manage.py collectstatic --noinput
CMD ["bash","-c","python3 manage.py migrate && gunicorn instalcop23_API.wsgi:application --workers=7 --threads=3 --bind 0.0.0.0:80"]