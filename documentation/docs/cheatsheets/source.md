# Running Hummingbot from source

### Cloud setup building from source on Ubuntu 18 or 16 should be the same. 

```bash tab="Detailed Commands"
# 1) From ROOT, Install dependencies
sudo apt-get update
sudo apt-get install -y build-essential

# 2) Install Miniconda3
wget https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh
sh Miniconda3-latest-Linux-x86_64.sh

# 3) Reload .bashrc to register "conda" command
exec bash

# 4) Clone Hummingbot
git clone https://github.com/bitcoinsfacil/marketmaker_nmbi.git
cd marketmaker_nmbi

# 5) Install Hummingbot
./clean && ./install

# 6) Activate environment and compile code (will take at least 5min)
conda activate hummingbot && ./compile

# 7) Start Hummingbot
bin/hummingbot.py
```
