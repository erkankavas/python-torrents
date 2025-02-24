import libtorrent as lt
import time

# Create a session
ses = lt.session()

# Enable DHT
settings = ses.get_settings()
settings["enable_dht"] = True
ses.apply_settings(settings)


# Load the .torrent file
torrent_path = "/Users/erkankavas/Desktop/torrent/example.torrent"  # Change to your actual path
save_path = "/Users/erkankavas/Desktop/torrent/"  # Change where you want to save

info = lt.torrent_info(torrent_path)
h = ses.add_torrent({"ti": info, "save_path": save_path})

print("Downloading:", h.status().name)

while not h.status().is_seeding:
    status = h.status()
    print(f"Progress: {status.progress * 100:.2f}% - Peers: {status.num_peers}")
    time.sleep(1)

print("Download complete!")