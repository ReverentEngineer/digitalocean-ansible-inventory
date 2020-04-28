# digitalocean-ansible-inventory

Sets up a dynamic inventory for DigitalOcean droplets in Ansible

# How to install

1. `pip install python-digitalocean`
2. `mkdir -p $HOME/.ansible/plugins/inventory`
3. `cp digitalocean.py $HOME/.ansible/plugins/inventory`
4. Either `export DO_API_TOKEN=your-api-token` or add `token = your-api-token` 
your inventory file.
