#Set up default terminal to linux. This is to make sure we can issue linux and bash commands.
ENV["TERM"]="linux"

#Set up virtual box configuration
Vagrant.configure("2") do |config|

  #Set image for the virtual box. In our case we are using a virtual box base image with the version declared
  config.vm.box = "opensuse/Leap-15.2.x86_64"
  config.vm.box_version = "15.2.31.242"

  #Set static ip for the virtual box. This will be the access point for the virtual box.
  config.vm.network "private_network", ip: "192.168.50.4"

end
