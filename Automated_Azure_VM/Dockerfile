FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
COPY src/virtualizationtask4.py .

RUN pip install --no-cache-dir -r requirements.txt

ENV SUBSCRIPTION_ID="77527cf9-e41c-446b-902e-46d250f405e0"
ENV RESOURCE_GROUP_NAME="nayanResourceGroup" 
ENV LOCATION="eastus"
ENV VM_NAME="myVirtualMachine"

CMD ["python", "virtualizationtask4.py"]