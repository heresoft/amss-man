from azure.identity import ClientSecretCredential
from azure.mgmt.media import AzureMediaServices
import configparser


class AzureServer:
    def __init__(self):
        # Load Azure server config
        self.config = configparser.ConfigParser()
        self.config.read('server.ini')


    def start(self):
        # Tenant ID for your Azure Subscription
        TENANT_ID = self.config['server']['tenant_id']

        # Your Application Client ID of your Service Principal
        CLIENT_ID = self.config['server']['client_id']

        # Your Service Principal secret key
        CLIENT_SECRET = self.config['server']['client_secret']

        # Your Azure Subscription ID
        SUBSCRIPTION_ID = self.config['server']['subscription_id']

        # Your Resource Group name
        RESOURCE_GROUP_NAME = self.config['server']['resource_group_name']

        # Your Azure Media Service account name
        ACCOUNT_NAME = self.config['server']['account_name']

        credentials = ClientSecretCredential(TENANT_ID, CLIENT_ID, CLIENT_SECRET)

        # The Azure Media Services Client
        client = AzureMediaServices(credentials, SUBSCRIPTION_ID)

        # Now that you are authenticated, you can manipulate the entities.
        # For example, list assets in your Media Services account
        assets = client.assets.list(RESOURCE_GROUP_NAME, ACCOUNT_NAME)

        results = ""

        for i, r in enumerate(assets):
            print(r)


    def stop(self):
        self.cheese = 2
