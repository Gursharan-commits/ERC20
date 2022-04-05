from scripts.helpful_scripts import get_account
from brownie import GuruToken
from web3 import Web3

initial_supply = Web3.toWei(1000, "ether")


def deploy_guruToken():
    account = get_account()
    guru_Token = GuruToken.deploy(initial_supply, {"from": account})
    print(guru_Token.name())


def main():
    deploy_guruToken()
