web: celery -A server worker --loglevel=info & python manage.py migrate && gunicorn server.wsgi  --bind 0.0.0.0:$PORT                                                                                                                                                                                                                                                                                                                                                             web: gunicorn server.wsgi                                                                                                                                      