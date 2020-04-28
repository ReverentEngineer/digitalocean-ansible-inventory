import os
from ansible.plugins.inventory import BaseInventoryPlugin
import digitalocean

class DigitalOceanInventoryModule(BaseInventoryPlugin):

    NAME = 'digitalocean'

    def verify_file(self, path):
        valid = False
        if super(InventoryModule, self).verify_file(path):
            if path.endswith(('digitalocean.yaml', 'do.yml')):
                valid = True
        return valid


    def parse(self, inventory, loader, path, cache=True):
        super(InventoryModule, self).parse(inventory, loader, path, cache)

        config = self._read_config_data(path)

        
        token = None
        if self.has_option('token'):
            token = self.get_option('token')
        elif 'DO_API_TOKEN' in os.environ:
            token = os.environ.get('token')
        manager = digitalocean.Manager(token=token)

        droplets = manager.get_all_droplets()
        for droplet in droplets:
            self.inventory.add_host(droplet.name)
            self.inventory.set_variable(droplet.name, 'ansible_host',
                                            droplet.ip_address)
