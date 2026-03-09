import paramiko

host = "sftp.marketdata.epexspot.com"
port = 22
username = "helionch.marketdata"
password = "2!d2nBSTwgvLk1i"

remote_file = "/switzerland/Day-Ahead Auction/Hourly/Current/Prices_Volumes/auction_spot_prices_switzerland_2026.csv"
local_file = "C:/Users/ThijsAntoniedeBoer/Downloads/woche 1/auction_spot_prices_switzerland_2026.csv"

transport = paramiko.Transport((host, port))
transport.connect(username=username, password=password)

sftp = paramiko.SFTPClient.from_transport(transport)

print(sftp.listdir("/switzerland"))
sftp.get(remote_file, local_file)

sftp.close()
transport.close()