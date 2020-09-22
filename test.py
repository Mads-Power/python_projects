from sogocore.client.sogo_client import SogoClient

sc = SogoClient(assethost="localhost", assetport="8082", datahost="localhost", dataport="8083")
t = sc.dc.get_tsdb_value(starts"")


