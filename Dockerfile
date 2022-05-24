FROM amazon/aws-lambda-python

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt 
COPY ./ ./
# Run test cases and this saves the tr
RUN chmod -R 0777 .
CMD [ "main.lambda_handler"]