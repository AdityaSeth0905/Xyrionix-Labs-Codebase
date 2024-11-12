import os
import hashlib
import requests
import logging
import magic
import yara
from typing import List, Dict, Optional
from concurrent.futures import ThreadPoolExecutor, as_completed

class VirusScanner:
    def __init__(self, 
                 virustotal_api_key: Optional[str] = None, 
                 yara_rules_path: Optional[str] = None):
        """
        Initialize VirusScanner with optional VirusTotal API and YARA rules
        
        Args:
            virustotal_api_key (str, optional): VirusTotal API key
            yara_rules_path (str, optional): Path to YARA rules directory
        """
        # Logging configuration
        logging.basicConfig(
            level=logging.INFO, 
            format='%(asctime)s - %(levelname)s: %(message)s'
        )
        self.logger = logging.getLogger(__name__)

        # VirusTotal configuration
        self.virustotal_api_key = virustotal_api_key
        self.virustotal_url = 'https://www.virustotal.com/vtapi/v2/file/report'

        # YARA rules configuration
        self.yara_rules_path = yara_rules_path
        self.yara_rules = self._load_yara_rules() if yara_rules_path else None

        # Known malware hash databases
        self.malware_hashes = self._load_malware_hashes()

    def _load_malware_hashes(self) -> set:
        """
        Load known malware hashes from a local database or external source
        
        Returns:
            set: Set of known malware file hashes
        """
        # In a real-world scenario, this would fetch from a comprehensive database
        return {
            '5f4dcc3b5aa765d61d8327deb882cf99',  # Example MD5 hash
            'e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855'  # Example SHA-256
        }

    def _load_yara_rules(self) -> Optional[yara.Rules]:
        """
        Load YARA rules from specified directory
        
        Returns:
            yara.Rules: Compiled YARA rules
        """
        try:
            if not os.path.exists(self.yara_rules_path):
                self.logger.warning(f"YARA rules path not found: {self.yara_rules_path}")
                return None

            rules = []
            for root, _, files in os.walk(self.yara_rules_path):
                for file in files:
                    if file.endswith('.yar') or file.endswith('.yara'):
                        rules.append(os.path.join(root, file))
            
            return yara.compile(filepaths=dict(enumerate(rules)))
        except Exception as e:
            self.logger.error(f"Error loading YARA rules: {e}")
            return None

    def calculate_file_hash(self, file_path: str, algorithm: str = 'md5') -> str:
        """
        Calculate file hash
        
        Args:
            file_path (str): Path to the file
            algorithm (str): Hash algorithm (md5, sha1, sha256)
        
        Returns:
            str: Calculated file hash
        """
        hash_algorithms = {
            'md5': hashlib.md5,
            'sha1': hashlib.sha1,
            'sha256': hashlib.sha256
        }

        hasher = hash_algorithms.get(algorithm.lower())
        if not hasher:
            raise ValueError(f"Unsupported hash algorithm: {algorithm}")

        with open(file_path, 'rb') as f:
            return hasher(f.read()).hexdigest()

    def check_virustotal(self, file_path: str) -> Dict[str, int]:
        """
        Check file against VirusTotal
        
        Args:
            file_path (str): Path to the file
        
        Returns:
            dict: Virus detection results
        """
        if not self.virustotal_api_key:
            self.logger.warning("VirusTotal API key not configured")
            return {}

        try:
            with open(file_path, 'rb') as f:
                files = {'file': f}
                params = {'apikey': self.virustotal_api_key}
                response = requests.post(
                    'https://www.virustotal.com/vtapi/v2/file/scan', 
                    files=files, 
                    params=params
                )
                scan_result = response.json()
                
                # Get scan report
                params = {
                    'apikey': self.virustotal_api_key, 
                    'resource': scan_result['resource']
                }
                report = requests.get(self.virustotal_url, params=params).json()
                
                return {
                    'positives': report.get('positives', 0),
                    'total': report.get('total', 0)
                }
        except Exception as e:
            self.logger.error(f"VirusTotal scan error: {e}")
            return {}

    def scan_file(self, file_path: str) -> Dict[str, Any]:
        """
        Comprehensive file scanning method
        
        Args:
            file_path (str): Path to the file to scan
        
        Returns:
            dict: Scanning results
        """
        # Validate file existence
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"File not found: {file_path}")

        # Perform file type detection
        file_type = magic.from_file(file_path)
        
        # Calculate file hash
        file_hash = self.calculate_file_hash(file_path)

        # Check against known malware hashes
        is_known_malware = file_hash in self.malware_hashes

        # YARA rule matching
        yara_matches = []
        if self.yara_rules:
            try:
                matches = self.yara_rules.match(file_path)
                yara_matches = [match.rule for match in matches]
            except Exception as e:
                self.logger.error(f"YARA scanning error: {e}")

        # VirusTotal scan
        virustotal_result = self.check_virustotal(file_path)

        return {
            'file_path': file_path,
            'file_type': file_type,
            'file_hash': file_hash,
            'known_malware': is_known_malware,
            'yara_matches': yara_matches,
            'virustotal': virustotal_result
        }

    def scan_directory(self, directory_path: str, max_workers: int = 4) -> List[Dict]:
        """
        Scan all files in a directory
        
        Args:
            directory_path (str): Path to directory
            max_workers (int): Maximum concurrent scanning threads
        
        Returns:
            list: Scanning results for all files
        """
        scan_results = []
        files = [os.path.join(directory_path, f) for f in os.listdir(directory_path) 
                 if os.path.isfile(os.path.join(directory_path, f))]

        with ThreadPoolExecutor(max_workers=max_workers) as executor:
            futures = {executor.submit(self.scan_file, file_path): file_path for file_path in files}
            
            for future in as_completed(futures):
                try:
                    result = future.result()
                    scan_results.append(result)
                except Exception as e:
                    self.logger.error(f"Scanning error: {e}")

        return scan_results

# Example usage
if __name__ == "__main__":
    # Initialize scanner (replace with your actual API key and YARA rules path)
    scanner = VirusScanner(
        virustotal_api_key='YOUR_VIRUSTOTAL_API _KEY',
        yara_rules_path='path/to/yara/rules'
    )

    # Scan a single file
    file_to_scan = 'path/to/file/to/scan'
    try:
        result = scanner.scan_file(file_to_scan)
        print("Scan Result:")
        print(result)
    except Exception as e:
        print(f"Error scanning file: {e}")

    # Scan a directory
    directory_to_scan = 'path/to/directory'
    try:
        results = scanner.scan_directory(directory_to_scan)
        for res in results:
            print("File Scan Result:")
            print(res)
    except Exception as e:
        print(f"Error scanning directory: {e}")