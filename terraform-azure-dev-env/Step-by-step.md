# Terraform & Azure

## 1. Local Environment Setup

- Visual Studio Code
- Install Azure CLI using MSI - https://learn.microsoft.com/en-us/cli/azure/install-azure-cli-windows?view=azure-cli-latest&pivots=msi
- Install Choco - https://chocolatey.org/install
    - Using PowerShell to install.
    - Ensure `Get-Execution Policy`  is not `Restricted`
    - In PowerShell run - `Set-ExecutionPolicy AllSigned`
    - Run the command - `Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('[https://community.chocolatey.org/install.ps1](https://community.chocolatey.org/install.ps1)'))`
- Close and open back PowerShell
- Install Terraform on Windows - `choco install terraform`
- In Visual Studio Code, open up Terminal - PowerShell
- Run `az login -tenant "<tenant ID>"`
- Choose the correct subscription when it prompt or use `az account set subscription "<subscription ID>"`

## 2. Azure Provider and Init

- At Visual Studio Code, click Open `New Folder` and create a new folder.
- Create a new file name - `main.tf`
- Put in the following code to specify the Azure Provider Version. Reference - https://registry.terraform.io/providers/hashicorp/azurerm/latest/docs

```hcl
terraform {
  required_providers {
    azurerm = {
      source  = "hashicorp/azurerm"
      version = "=4.1.0"
    }
  }
}

provider "azurerm" {
  features {}
  subscription_id = "<subscriptionID>"
}
```

- Save the file.
- Run `terraform fmt`  for formatting the file.
- Run `terraform init`

## 3. Create Resource Group

- Add code -

```hcl
resource "azurerm_resource_group" "example" {
name     = "example"
location = "West Europe"
}
```

- Run `terraform fmt` than `terraform plan` .
- Once is good than run `terraform apply`  and key `yes`  when being prompt.

## 4. Create Virtual Network

- Add code -

```hcl
resource "azurerm_virtual_network" "example" {
  name                = "example-network"
  location            = azurerm_resource_group.example.location
  resource_group_name = azurerm_resource_group.example.name
  address_space       = ["10.123.0.0/16"]

  tags = {
    enviroment = "lab"
  }

}
```

## 5. Terraform State

- Direct editing on the file (`terraform.tfstate`)is not encouraged or should not be done.
- `terraform state list`  to check on the resources.
- `terraform state show <resourceName>` to see more detail about a resources.
- `terraform show` to view all the resources in details.

## 6. Terraform Destroy

- `terraform plan -destroy` can let you see what will be delete/remove
- `terraform apply -destroy`  will delete/remove everything.
- `terraform destroy -target <resourcesName>` will only delete a specific resources.

## 7. Create Subnet

```
resource "azurerm_subnet" "example" {
  name                 = "example-subnet"
  resource_group_name  = azurerm_resource_group.example.name
  virtual_network_name = azurerm_virtual_network.example.name
  address_prefixes     = ["10.0.1.0/24"]
  }
```

## 8. Create Security Group and Network Security Rules

```hcl
resource "azurerm_network_security_group" "example" {
  name                = "acceptanceTestSecurityGroup1"
  location            = azurerm_resource_group.example.location
  resource_group_name = azurerm_resource_group.example.name
  
  tags = {
	  environment = "lab"
  }
  }
```

- Seperating the `network security rules` from the `network security group` for easier maintenace.

```hcl
resource "azurerm_network_security_rule" "example" {
  name                        = "test123"
  priority                    = 100
  direction                   = "Outbound"
  access                      = "Allow"
  protocol                    = "Tcp"
  source_port_range           = "*"
  destination_port_range      = "*"
  source_address_prefix       = "*"
  destination_address_prefix  = "*"
  resource_group_name         = azurerm_resource_group.example.name
  network_security_group_name = azurerm_network_security_group.example.name
}
```

## 9. Subnet and NSG Association

- Associate the NSG with Subnet

```hcl
resource "azurerm_subnet_network_security_group_association" "example" {
  subnet_id                 = azurerm_subnet.example.id
  network_security_group_id = azurerm_network_security_group.example.id
}
```

## 10. Create Public IP

```hcl
resource "azurerm_public_ip" "example" {
  name                    = "test-pip"
  location                = azurerm_resource_group.example.location
  resource_group_name     = azurerm_resource_group.example.name
  allocation_method       = "Dynamic"
  idle_timeout_in_minutes = 30
	sku                     = "Basic" 
	
  tags = {
    environment = "test"
  }
}

```

- Need to define the SKU to `Basic` for Allocation Method - `Dynamic` .
- SKU Standard requires the Allocation Method to be `Static` .

## 11. Create Network Interface (NIC)

```hcl
resource "azurerm_network_interface" "example" {
  name                = "example-nic"
  location            = azurerm_resource_group.example.location
  resource_group_name = azurerm_resource_group.example.name

  ip_configuration {
    name                          = "internal"
    subnet_id                     = azurerm_subnet.example.id
    private_ip_address_allocation = "Dynamic"
    public_ip_address_id          = azurerm_public_ip.example.id
  }
    tags = {
    environment = "test"
  }
}
```

## 12. Create Azure Linux VM, Key Pair & SSH Login

- At PowerShell run - `ssh-keygen -t rsa`
- Save this at `C:\Users\<username>/.ssh/<keyname>`
- Leave passphrase blank (for lab and testing).
- It will create Key Pair.
- Code to build VM -

```hcl
resource "azurerm_linux_virtual_machine" "example" {
  name                = "terra-vm-1"
  resource_group_name = azurerm_resource_group.example.name
  location            = azurerm_resource_group.example.location
  size                = "Standard_B1s"
  admin_username      = "adminuser"
  network_interface_ids = [
    azurerm_network_interface.example.id
  ]

  admin_ssh_key {
    username   = "adminuser"
    public_key = file("~/.ssh/example.pub")
  }

  os_disk {
    caching              = "ReadWrite"
    storage_account_type = "Standard_LRS"
  }

  source_image_reference {
    publisher = "Canonical"
    offer     = "ubuntu-24_04-lts"
    sku       = "server"
    version   = "latest"
  }
}
```

- SSH from PowerShell - `ssh -i "C:\Users\<username>\.ssh\<key_name>" adminuser@<publicIP>`
- How to find `source_image_reference` for desired location;
    - `az vm image list-offers --location southeastasia --publisher Canonical -o table`
    - Note down the Offer name of it. Example - `ubuntu-24_04-lts` . This will be value for paremeter - `offer`
    - Find the `sku`  - `az vm image list-skus --location southeastasia --publisher Canonical --offer ubuntu-24_04-lts -o table`
    - Note down the SKU Name. Example - `server` . This can be use for parameter - `sku` .
    - Find the `version`  - `az vm image list --location southeastasia --publisher Canonical --offer ubuntu-24_04-lts --sku server -o table`.
    - Note down the Version. This can be user for parameter - `version`.

## 13. Create & Use Custom Data and File Function

- Create a file name - `customdata.tfl` at the same directory with [`main.tf`](http://main.tf) is.
- Add the below code/command into `customdata.tfl` file;

```bash
#!/bin/bash
set -eux

apt-get update
apt-get install -y ca-certificates curl gnupg

install -m 0755 -d /etc/apt/keyrings
curl -fsSL https://download.docker.com/linux/ubuntu/gpg \
  | gpg --dearmor -o /etc/apt/keyrings/docker.gpg
chmod a+r /etc/apt/keyrings/docker.gpg

echo \
  "deb [arch=amd64 signed-by=/etc/apt/keyrings/docker.gpg] \
  https://download.docker.com/linux/ubuntu \
  $(. /etc/os-release && echo $VERSION_CODENAME) stable" \
  > /etc/apt/sources.list.d/docker.list

apt-get update
apt-get install -y docker-ce docker-ce-cli containerd.io

systemctl enable docker
systemctl start docker
usermod -aG docker XXXXX
```

- Run `terraform apply -auto-approve` .
- SSH into the VM and check on the cloud-init via `cloud-init status --long` .
- Wait for it to complete. Example of complete and succesful run;

```hcl
XXXXX@XXXXXXX-vm-1:~$ cloud-init status --long
status: done
extended_status: done
boot_status_code: enabled-by-generator
last_update: XXXXXXXXXXXXXXXXXX
detail: DataSourceAzure [seed=/dev/sr0]
errors: []
recoverable_errors: {}
```

- Run `docker --version` to verify if `docker` is install.

## 14. Install & Configure Remote SSH Extension on Studio Code

- Create a file name `windows-ssh-script.tpl`  or `linux-ssh-script.tpl` at the same directory of [`main.tf`](http://main.tf) directory.
- For Windows,

```hcl
add-content -path C:/Users/garytan563/.ssh/config -value @'
Host ${hostname}
Hostname ${hostname}
User ${user}
IdentityFile ${identityfile}
'@
```

- For Linux,

```hcl
cat << EOF >> ~/.ssh/config

Host ${hostname}
    Hostname ${hostname}
    User ${user}
    IdentityFile ${identityfile}
EOF
```

- At Visual Studio Code, install the extension - `Remote - SSH`

## 15. Add the Provisioner and Template File

- At `resource "azurerm_linux_virtual_machine"` , add the provisioner block into it,

```hcl
  provisioner "local-exec" {
    command = templatefile("windows-ssh-script.tpl", {
      hostname     = self.public_ip_address,
      user         = "<username>",
      identityfile = "~/.ssh/<private-key-name>"
    })
    interpreter = ["Powershell", "-Command"] ## For Linux - ["bash", "-c"]
  }

```

- We will need to destroy/replace the VM to take effect.
- Run the command - `terraform apply -replace azurerm_linux_virtual_machine.XXXXX`
- At the Visual Studio Code, at Command Palette select `Remote-SSH: Connect to Host` . select the Public IP/Host.
- It will pop up another Visual Studio Code window.
- Check at `C:\Users\<Username>\.ssh\config` , you will see the details of the SSH Host, Public IP and IdentityFile (privatekey) is added.

## 16. Data Sources

- Add this into the [`main.tf`](http://main.tf) file

```hcl
data "azurerm_public_ip" "exmaple" {
  name                = azurerm_public_ip.example.name
  resource_group_name = azurerm_resource_group.example.name
}
```

- Run `terraform apply -refresh-only` . It will not change anything such as destroy and recreate the VM.
- Run `terraform state list` , will see `data.azurerm_public_data.example` .
- Check on the `terraform.tfstate`  file will also the the data section and the output of it.

## 17. Output Data

To output the data/value that required, use the following code and add into the [`main.tf`](http://main.tf) file;

```hcl
output "public_ip_address" {
  value = "${azurerm_linux_virtual_machine.example.name}: ${azurerm_linux_virtual_machine.example.public_ip_address}"
}
```

- The `value` paremeter inside is capturing two different value, virtual machine name and the Public IP address for the VM.
- Run `terraform apply -refresh-only` , it will show the output of it.
- Or run `terraform output`  / `terraform output public_ip_address`  (if there is multiple output).

## 18. Using Variables and Input the Value

- Example at the provisioner block, change it to as per below.
- From `command = templatefile("windows-ssh-script.tpl"`  become `command = templatefile("${var.host_os}-ssh-script.tpl"`

```hcl
  provisioner "local-exec" {
    command = templatefile("${var.host_os}-ssh-script.tpl", {
      hostname     = self.public_ip_address,
      user         = "adminuser",
      identityfile = "~/.ssh/<privatekeyname>"
    })
    interpreter = ["Powershell", "-Command"]
  }

}
```

- Create a file name `variables.tf` file in the same directory of `main.tf` .

```hcl
variable "host_os"{
    type = string

}
```

- When running terraform command, it will go through all the `.tf` files in the same directory.
- It will prompt to input the `var.host_os`  value.

## 19. Variable Precedence

- Create a file name `terraform.tfvars` . Normally this file will not be uploaded into the remote repository as it might contain sensitive data.

```hcl
host_os = "windows”
```

- If the variable is define in the command line - `terraform console/plan/destroy -var="host_os=linux"` , it will take the precedence of it. It will ignore the variable in the `terraform.tfvars` file.
- Variables set in `terraform.tfvars` will overwrite what in `variables.tf` .

## 20. Conditional Expressions

Modify the code to;

```hcl
  provisioner "local-exec" {
    command = templatefile("${var.host_os}-ssh-script.tpl", {
      hostname     = self.public_ip_address,
      user         = "adminuser",
      identityfile = "~/.ssh/<privatekeyname>"
    })
    interpreter = var.host_os == "windows" ? ["Powershell", "-Command"] : ["bash", "-c"]
  }

}
```

- Changed `interpreter = ["Powershell", "-Command"]` to `interpreter = var.host_os == "windows" ? ["Powershell", "-Command"] : ["bash", "-c"]`
- So if the `host_os`  is set to `windows`  at the `terraform.tfvars` it will be `["Powershell", "-Command"]`  and is `linux` it will be `["bash", "-c"]`.