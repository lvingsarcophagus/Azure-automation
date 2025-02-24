from azure.identity import AzureCliCredential
from azure.mgmt.compute import ComputeManagementClient
from azure.mgmt.resource import ResourceManagementClient
from azure.mgmt.network import NetworkManagementClient
import sys

# Configuration
SUBSCRIPTION_ID = ""
RESOURCE_GROUP_NAME = "nayanResourceGroup"
LOCATION = "eastus"
VM_NAME = "myVirtualMachine"
VNET_NAME = "myVNet"
SUBNET_NAME = "mySubnet"
NIC_NAME = "myNIC"

# Authenticate with Azure CLI credentials
credential = AzureCliCredential()

# Initialize clients
resource_client = ResourceManagementClient(credential, SUBSCRIPTION_ID)
network_client = NetworkManagementClient(credential, SUBSCRIPTION_ID)
compute_client = ComputeManagementClient(credential, SUBSCRIPTION_ID)

# 1. Create Resource Group
print("Creating Resource Group...")
resource_client.resource_groups.create_or_update(
    RESOURCE_GROUP_NAME,
    {"location": LOCATION}
)

# 2. Create Virtual Network
print("Creating Virtual Network...")
vnet = network_client.virtual_networks.begin_create_or_update(
    RESOURCE_GROUP_NAME,
    VNET_NAME,
    {
        "location": LOCATION,
        "address_space": {"address_prefixes": ["10.0.0.0/16"]}
    }
).result()

# 3. Create Subnet
print("Creating Subnet...")
subnet = network_client.subnets.begin_create_or_update(
    RESOURCE_GROUP_NAME,
    VNET_NAME,
    SUBNET_NAME,
    {"address_prefix": "10.0.0.0/24"}
).result()

# 4. Create Network Interface
print("Creating Network Interface...")
nic = network_client.network_interfaces.begin_create_or_update(
    RESOURCE_GROUP_NAME,
    NIC_NAME,
    {
        "location": LOCATION,
        "ip_configurations": [{
            "name": "myIpConfig",
            "subnet": {"id": subnet.id},
            "private_ip_allocation_method": "Dynamic"
        }]
    }
).result()

# 5. Create Virtual Machine
print("Creating Virtual Machine...")
vm = compute_client.virtual_machines.begin_create_or_update(
    RESOURCE_GROUP_NAME,
    VM_NAME,
    {
        "location": LOCATION,
        "hardware_profile": {
            "vm_size": "Standard_DS1_v2"
        },
        "storage_profile": {
            "image_reference": {
                "publisher": "Canonical",
                "offer": "UbuntuServer",
                "sku": "18.04-LTS",
                "version": "latest"
            },
            "os_disk": {
                "create_option": "FromImage",
                "managed_disk": {"storage_account_type": "Standard_LRS"},
                "disk_size_gb": 30
            }
        },
        "os_profile": {
            "computer_name": VM_NAME,
            "admin_username": "azureuser",
            "admin_password": "P@ssword1234!"
        },
        "network_profile": {
            "network_interfaces": [{"id": nic.id}]
        }
    }
).result()

print(f"Virtual Machine {VM_NAME} created successfully!")

def delete_resource_group():
    # Configuration
    SUBSCRIPTION_ID = "77527cf9-e41c-446b-902e-46d250f405e0"
    RESOURCE_GROUP_NAME = "nayanResourceGroup"

    try:
        # Initialize credentials and client
        credential = AzureCliCredential()
        resource_client = ResourceManagementClient(credential, SUBSCRIPTION_ID)

        # Confirm deletion
        confirm = input(f"Are you sure you want to delete resource group '{RESOURCE_GROUP_NAME}'? (yes/no): ")
        if confirm.lower() != 'yes':
            print("Deletion cancelled.")
            return

        print(f"Deleting resource group '{RESOURCE_GROUP_NAME}'...")
        
        # Delete resource group
        delete_operation = resource_client.resource_groups.begin_delete(RESOURCE_GROUP_NAME)
        delete_operation.wait()

        print(f"Resource group '{RESOURCE_GROUP_NAME}' has been deleted successfully.")

    except Exception as e:
        print(f"Error deleting resource group: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    delete_resource_group()
