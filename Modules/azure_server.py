from azure.identity import ClientSecretCredential
from azure.mgmt.media import AzureMediaServices


class AzureServer:
    def __init__(self, conf):
        # Load Azure server config
        self.config = conf

    def start(self, status_callback):
        # Get login credentials
        credentials = ClientSecretCredential(self.config['tenant_id'], self.config['client_id'], self.config['client_secret'])

        status_callback("Connecting to Azure")
        # Load an Azure Media Services Client
        client = AzureMediaServices(credentials, self.config['subscription_id'])

        with client:
            status_callback("Starting live event")
            client_live = client.live_events.begin_start(self.config['resource_group_name'], self.config['account_name'], self.config['event_name'])
            if client_live:
                print("Live event started")
                poller = client_live
                print(poller.result())
            else:
                raise ValueError('Live Event creation failed!')

        client.close()

        credentials.close()

    def stop(self, status_callback):
        # Get login credentials
        credentials = ClientSecretCredential(self.config['tenant_id'], self.config['client_id'], self.config['client_secret'])

        # Load an Azure Media Services Client
        client = AzureMediaServices(credentials, self.config['subscription_id'])

        with client:
            client_live = client.live_events.begin_stop(self.config['resource_group_name'], self.config['account_name'], self.config['event_name'])
            if client_live:
                print("Live event stopped")
                poller = client_live
                print(poller.result())
            else:
                raise ValueError('Live Event stopping failed!')

        client.close()

        credentials.close()
