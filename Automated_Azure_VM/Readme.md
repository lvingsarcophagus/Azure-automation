# Azure VM Automation

This project provides a Python script to automate the creation and deletion of Azure Virtual Machines using the Azure SDK for Python.

## Prerequisites

- Python 3.9 or higher
- Azure CLI installed and configured
- Azure subscription
- Docker (optional, for containerized deployment)

## Setup

1. Clone the repository:
```bash
git clone <repository-url>
cd Automated_Azure_VM
```

2. Install required dependencies:
```bash
pip install -r requirements.txt
```

3. Configure Azure credentials:
```bash
az login
```

## Configuration

Update the following variables in `virtualizationtask4.py` or set them as environment variables:

```python
SUBSCRIPTION_ID = "your-subscription-id"
RESOURCE_GROUP_NAME = "nayanResourceGroup"
LOCATION = "eastus"
VM_NAME = "myVirtualMachine"
```

## Usage

### Running with Python

```bash
python src/virtualizationtask4.py
```

### Running with Docker

1. Build the Docker image:
```bash
docker build -t azure-vm-automation .
```

2. Run the container:
```bash
docker run -it azure-vm-automation
```

## Features

- ✨ Automated Resource Group creation
- 🌐 Virtual Network and Subnet setup
- 🔌 Network Interface configuration
- 💻 Ubuntu Server 18.04 LTS VM deployment
- 🧹 Resource cleanup functionality


## Security Considerations

⚠️ **Important Notes:**
- Default credentials are included in the code for demonstration
- In production:
  - Use Azure Key Vault for secrets
  - Implement proper access controls
  - Use environment variables for sensitive data

## VM Specifications

- **Size**: Standard_DS1_v2
- **OS**: Ubuntu Server 18.04 LTS
- **Disk**: 30GB Standard LRS
- **Default Credentials**:
  - Username: azureuser
  - Password: P@ssword1234!

## Error Handling

The script includes basic error handling for resource group deletion and will:
- Prompt for confirmation before deletion
- Display meaningful error messages
- Exit gracefully on failures


## License

This project is licensed under the MIT License - see the LICENSE file for details.