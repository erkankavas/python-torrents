### Torrent Downloader in Python

This repository provides a simple Python script for downloading torrents using the libtorrent library.

### Features

- Uses libtorrent to download .torrent files.
- Displays real-time progress updates.
- Supports DHT for decentralized peer discovery.

### Prerequisites

Ensure you have Python installed on your system. You also need to install libtorrent:

```
pip install python-libtorrent
```

### Usage

Clone this repository:

```
git clone https://github.com/yourusername/torrent-downloader.git
cd torrent-downloader
```

>Update the script with the correct paths:
>Change torrent_path to the location of your .torrent file.
>Modify save_path to specify where you want to save the downloaded files.

Run the script:

```
python down.py
```

### Code Overview

- Creates a libtorrent session.
- Enables DHT for peer discovery.
- Loads a .torrent file and starts the download.
- Continuously updates progress until the download is complete.

### Example Output

```
Downloading: example.torrent
Progress: 10.00% - Peers: 5
Progress: 50.00% - Peers: 10
Progress: 100.00% - Peers: 12
Download complete!
```

### Notes

Ensure libtorrent is installed correctly, as some systems may require additional dependencies. Adjust paths in the script before running.

### License

This project is open-source and available under the MIT License.

### Contributions

Contributions are welcome! Feel free to open issues or submit pull requests.