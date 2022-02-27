FROM python:3.8
COPY . ./
RUN pip3 install -r requirements.txt
CMD ["Bryson_preprosess_cars_data_Module5.py"]
ENTRYPOINT ["python"]