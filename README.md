# ronin-active-set-checker
Periodically checks if a validator is in the active set on the Ronin Network.

## Install and Run
Make sure docker is installed on your system before beginning the installation. Visit [this link](https://docs.docker.com/engine/install/ubuntu/) to install docker on ubuntu.
### 1. Clone the Repo
```
git clone https://github.com/Frixoe/ronin-active-set-checker.git
cd ronin-active-set-checker
cp .env-example .env
```
### 2. Edit the `.env`
Now edit the variables in the `.env` file with the relevant values.
```
vim .env
```

```
BOT_TOKEN=<YOUR TELEGRAM BOT TOKEN>
VALIDATOR_ADDRESS=<YOUR VALIDATOR ADDRESS STARTING WITH 0x>
CHAT_ID=<THE CHAT ID OF THE GROUP/CHANNEL WHERE THE BOT WILL BE FUNCTIONING>
````

You can find your validator address on your validator's [Ronin Staking Stats Page](https://app.roninchain.com/validator/ronin:6aaabf51c5f6d2d93212cf7dad73d67afa0148d0). You are looking for the address in the red box:
![image](https://github.com/Frixoe/ronin-active-set-checker/assets/21309909/a773ce5a-b79f-4b64-8572-f773ba7ffb09)

> Make sure to remove the 'ronin:' from the start and replace it with '0x' when adding it to the `.env` file.

### 3. Run the script!
```
sudo docker compose up -d
```
Docker will now build the image and start monitoring your validator's active set involvement.

Check the logs:
```
sudo docker compose logs -f --tail=10
```
