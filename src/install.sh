mkdir engine/results
echo "Installing Golang"
wget https://dl.google.com/go/go1.13.4.linux-amd64.tar.gz
sudo tar -xvf go1.13.4.linux-amd64.tar.gz
sudo mv go /usr/local
export GOROOT=/usr/local/go
export GOPATH=$HOME/go
export PATH=$GOPATH/bin:$GOROOT/bin:$PATH
echo 'export GOROOT=/usr/local/go' >> ~/.bash_profile
echo 'export GOPATH=$HOME/go'	>> ~/.bash_profile
echo 'export PATH=$GOPATH/bin:$GOROOT/bin:$PATH' >> ~/.bash_profile

echo "Installing Python3x"
sudo apt-get install python3 -y
sudo apt-get install python3-pip -y

echo "Flask and SQLAlchemy"
sudo pip3 install flask
sudo pip3 install flask_sqlalchemy
sudo pip3 install sqlalchemy

echo "Installing httprobe"
go get github.com/tomnomnom/httprobe

echo "Installing Assetfinder"
go get github.com/tomnomnom/assetfinder

echo "Installing Waybackurls"
go get github.com/tomnomnom/waybackurls

echo "Installing GAU"
go get github.com/lc/gau

echo "Installing Aquatone"
go get github.com/michenriksen/aquatone

echo "Installing Requirements for DNScan"
sudo pip3 install -r engine/tools/dnscan/requirements.txt

echo "Installing Nmap"
sudo apt install nmap -y
