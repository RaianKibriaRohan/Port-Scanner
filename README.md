---
# 🔎 **Python Port Scanner**  

This is a simple **port scanner** built using Python and the `nmap` module. It allows users to scan specific IP addresses for open ports within a given range. The script is designed to be user-friendly and effective for basic network scanning.  

## ⚡ **Features**  
✅ Scan a target IP for open ports  
✅ Define a custom port range (e.g., `20-100`)  
✅ Uses **nmap** for accurate scanning  
✅ Simple user interface  
✅ No multithreading (single-threaded scan)  

## 📌 **Installation & Setup**  
This script requires **Python 3** and `nmap`. Follow these steps to install the required dependencies:  

### 🔹 **For Kali Linux & Debian-based Systems**  
```bash
sudo apt install python3-pip
pip install python-nmap
```
### 🔹 **For Windows**  
1. Install **Nmap** from [nmap.org](https://nmap.org/download.html)  
2. Install the required Python module:  
   ```bash
   pip install python-nmap
   ```

## 🚀 **How to Use**  
1. Run the script:  
   ```bash
   python3 port_scanner.py
   ```
2. Enter the target **IP address** when prompted.  
3. Enter the **port range** (e.g., `20-100`).  
4. The script will scan the specified ports and display their status.  

## 📌 **Example Output**  
```
Please enter the IP address that you want to scan: 192.168.1.1
192.168.1.1 is a valid IP address

Please enter the range of ports you want to scan in format: <int>-<int> (ex would be 60-120)
Enter port range: 20-100

Port 22 is open
Port 80 is open
Port 443 is closed
...
```

## ⚠️ **Disclaimer**  
This tool is intended for **educational and ethical** purposes only. Unauthorized scanning of networks without permission is **illegal** and may result in legal consequences. Always obtain proper authorization before scanning any network.  

## 🤝 **Connect with Me**  
🔗 **GitHub**: [RaianKibriaRohan](https://github.com/RaianKibriaRohan)  
🔗 **LinkedIn**: [Raian Kibria Rohan](https://www.linkedin.com/in/raian-kibria-rohan-89997a323/)  

---
