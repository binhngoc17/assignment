VAGRANTFILE_API_VERSION = "2"

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|
  config.vm.box = "ubuntu/trusty64"

  config.vm.provider :virtualbox do |v|
    v.name = "flask"
    v.memory = 512
    v.cpus = 2
  end

  config.vm.hostname = "flask"
  config.vm.network :private_network, ip: "192.168.33.8"
  config.vm.synced_folder ".", "/home/vagrant/assignment"

  # Ansible provisioner.
  config.vm.provision "ansible" do |ansible|
    ansible.playbook = "provisioning/flask.yml"
    ansible.inventory_path = "provisioning/inventory"
    ansible.verbose = "v"
    ansible.limit = "all"
    ansible.sudo = true
  end
end