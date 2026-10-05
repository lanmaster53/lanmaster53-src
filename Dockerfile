FROM python:3.13-slim

# docker build -t blog .
# docker run --rm -it -p 5000:5000 -v $(pwd):/blog blog

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /blog

COPY REQUIREMENTS.txt .
RUN pip install --no-cache-dir -r REQUIREMENTS.txt

EXPOSE 5000
ENTRYPOINT ["python", "blog.py"]
