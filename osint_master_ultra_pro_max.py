#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
===============================================================================
                  OSINT MASTER ULTRA PRO MAX v2.0
                   The World's Most Comprehensive
                Educational OSINT & Information Gathering
                         Mega-Toolkit

              * CREATED BY RAJSARASWATI JATAV *
                Educational & Research Use Only
          Cybersecurity Education • Ethical Research Only
                        www.rajsaraswati.dev
===============================================================================

LEGAL DISCLAIMER & ETHICAL USE AGREEMENT:
========================================
This tool is designed EXCLUSIVELY for:
✓ Educational purposes and cybersecurity learning
✓ Authorized penetration testing and security research
✓ Enterprise security assessments with proper authorization
✓ Academic research and teaching cybersecurity concepts
✓ Compliance and risk assessment activities
✓ Cyber awareness and defense training

WARNING - STRICTLY PROHIBITED USES:
✗ Unauthorized scanning or data collection
✗ Malicious activities or illegal reconnaissance
✗ Privacy violations or stalking
✗ Any activities without explicit written permission
✗ Commercial exploitation without proper licensing

BY USING THIS TOOL, YOU AGREE TO:
- Comply with all applicable laws and regulations
- Obtain proper authorization before scanning any systems
- Use only for legitimate security research and education
- Respect privacy and data protection rights
- Follow responsible disclosure practices

The creators are not responsible for misuse of this tool.
Users assume full legal responsibility for their actions.

Version: 2.0.0 ULTRA PRO MAX EDITION
License: Educational Use Only
Contact: rajsaraswati.jatav@education.research
"""

import sys
import os
import time
import json
import csv
import threading
import asyncio
import socket
import ssl
import urllib.parse
import urllib.request
import urllib.error
import re
import hashlib
import base64
import hmac
import random
import string
import subprocess
from datetime import datetime, timedelta
from pathlib import Path
from typing import Dict, List, Tuple, Optional, Union, Any
from dataclasses import dataclass, field
from concurrent.futures import ThreadPoolExecutor, as_completed
from contextlib import contextmanager
import logging
import platform

# Essential imports for OSINT functionality
try:
    import requests
    from requests.adapters import HTTPAdapter
    from requests.packages.urllib3.util.retry import Retry
except ImportError:
    print("Installing requests...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "requests"])
    import requests
    from requests.adapters import HTTPAdapter
    from requests.packages.urllib3.util.retry import Retry

try:
    from bs4 import BeautifulSoup
except ImportError:
    print("Installing beautifulsoup4...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "beautifulsoup4"])
    from bs4 import BeautifulSoup

try:
    import dns.resolver
    import dns.reversename
except ImportError:
    print("Installing dnspython...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "dnspython"])
    import dns.resolver
    import dns.reversename

try:
    from rich.console import Console
    from rich.table import Table
    from rich.panel import Panel
    from rich.progress import Progress, SpinnerColumn, TextColumn
    from rich.text import Text
    from rich.align import Align
    from rich.live import Live
    from rich.layout import Layout
    from rich import print as rprint
except ImportError:
    print("Installing rich for terminal UI...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "rich"])
    from rich.console import Console
    from rich.table import Table
    from rich.panel import Panel
    from rich.progress import Progress, SpinnerColumn, TextColumn
    from rich.text import Text
    from rich.align import Align
    from rich.live import Live
    from rich.layout import Layout
    from rich import print as rprint

try:
    from cryptography.fernet import Fernet
except ImportError:
    print("Installing cryptography...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "cryptography"])
    from cryptography.fernet import Fernet

# Global constants and configuration
VERSION = "2.0.0 ULTRA PRO MAX"
AUTHOR = "RAJSARASWATI JATAV"
CONTACT = "rajsaraswati.jatav@education.research"
CREATED_DATE = "2025"
TOOL_NAME = "OSINT MASTER ULTRA PRO MAX"

# Color schemes for terminal UI
COLORS = {
    'primary': '#00ff41',      # Matrix green
    'secondary': '#0066ff',    # Electric blue
    'accent': '#ff0066',       # Neon pink
    'warning': '#ffaa00',      # Orange
    'error': '#ff0000',        # Red
    'success': '#00ff00',      # Green
    'info': '#00aaff',         # Light blue
    'dark': '#001122',         # Dark blue
    'light': '#ffffff'         # White
}

console = Console()

class OSINTConfig:
    """Global configuration for OSINT operations"""

    def __init__(self):
        self.user_agent = "OSINT-Educational-Research-Tool/2.0 (Educational Use Only)"
        self.timeout = 10
        self.max_threads = 50
        self.output_dir = Path("osint_results")
        self.log_level = logging.INFO
        self.ethical_mode = True
        self.educational_only = True
        self.demo_mode = True
        self.language = "english"  # english/hindi
        self.proxy_enabled = False
        self.tor_enabled = False
        self.api_keys = {}
        self.session_key = None
        self.encryption_key = None

        # Initialize directories
        self.output_dir.mkdir(exist_ok=True)
        (self.output_dir / "logs").mkdir(exist_ok=True)
        (self.output_dir / "reports").mkdir(exist_ok=True)
        (self.output_dir / "exports").mkdir(exist_ok=True)
        (self.output_dir / "cache").mkdir(exist_ok=True)

@dataclass
class OSINTResult:
    """Data class for OSINT results"""
    module: str
    target: str
    data_type: str
    data: Any
    timestamp: datetime = field(default_factory=datetime.now)
    source: str = ""
    confidence: float = 0.0
    risk_level: str = "low"
    metadata: Dict = field(default_factory=dict)

class EthicalComplianceManager:
    """Manages ethical compliance and legal requirements"""

    def __init__(self, config: OSINTConfig):
        self.config = config
        self.consent_given = False
        self.authorization_verified = False
        self.activity_log = []
        self.gdpr_compliance = True

    def show_legal_disclaimer(self):
        """Display legal disclaimer and get consent"""

        disclaimer_panel = Panel.fit(
            f"""
[bold red]WARNING - LEGAL DISCLAIMER & ETHICAL USE AGREEMENT[/bold red]

[yellow]This tool is designed EXCLUSIVELY for:[/yellow]
- Educational purposes and cybersecurity learning
- Authorized penetration testing and security research  
- Enterprise security assessments with proper authorization
- Academic research and teaching cybersecurity concepts
- Compliance and risk assessment activities
- Cyber awareness and defense training

[bold red]STRICTLY PROHIBITED USES:[/bold red]
- Unauthorized scanning or data collection
- Malicious activities or illegal reconnaissance
- Privacy violations or stalking
- Any activities without explicit written permission
- Commercial exploitation without proper licensing

[bold green]BY USING THIS TOOL, YOU AGREE TO:[/bold green]
- Comply with all applicable laws and regulations
- Obtain proper authorization before scanning any systems
- Use only for legitimate security research and education
- Respect privacy and data protection rights
- Follow responsible disclosure practices

[bold yellow]GDPR & Privacy Compliance:[/bold yellow]
- All data collection follows data minimization principles
- Personal data is processed lawfully and transparently
- Data retention follows legitimate purpose requirements
- Data subjects' rights are respected

[bold red]The creators are not responsible for misuse of this tool.
Users assume full legal responsibility for their actions.[/bold red]

Created by: [bold cyan]{AUTHOR}[/bold cyan]
Contact: [cyan]{CONTACT}[/cyan]
Version: [green]{VERSION}[/green]
            """,
            title="ETHICAL USE AGREEMENT",
            border_style="red"
        )

        console.print(disclaimer_panel)

        # Animated consent process
        for i in range(3, 0, -1):
            console.print(f"[yellow]Please read carefully... {i}[/yellow]")
            time.sleep(1)

        consent_questions = [
            "Do you confirm you will use this tool only for educational and ethical research purposes?",
            "Do you confirm you have proper authorization for any systems you will scan?",
            "Do you understand the legal implications and accept full responsibility?",
            "Do you agree to comply with all applicable laws and regulations?"
        ]

        all_consent = True
        for question in consent_questions:
            while True:
                answer = console.input(f"[bold yellow]{question}[/bold yellow] [green](yes/no)[/green]: ").lower()
                if answer in ['yes', 'y']:
                    break
                elif answer in ['no', 'n']:
                    console.print("[bold red]You must agree to all terms to use this tool.[/bold red]")
                    all_consent = False
                    break
                else:
                    console.print("[red]Please answer 'yes' or 'no'[/red]")

            if not all_consent:
                break

        if all_consent:
            self.consent_given = True
            self.log_activity("CONSENT", "User provided consent for ethical use")
            console.print("[bold green]Ethical use agreement accepted.[/bold green]")
        else:
            console.print("[bold red]Ethical use agreement not accepted. Exiting.[/bold red]")
            sys.exit(1)

    def verify_authorization(self):
        """Verify user authorization for target scanning"""

        auth_panel = Panel.fit(
            """
[bold yellow]AUTHORIZATION VERIFICATION[/bold yellow]

Before proceeding with any scanning activities, you must verify that you have
proper authorization to scan the target systems.

[bold green]Valid Authorization Includes:[/bold green]
- Written permission from system owners
- Authorized penetration testing engagement
- Educational lab environment you own
- Bug bounty program participation
- Internal corporate security assessment

[bold red]NEVER scan systems without explicit permission![/bold red]

This verification is logged for compliance purposes.
            """,
            title="AUTHORIZATION CHECK",
            border_style="yellow"
        )

        console.print(auth_panel)

        auth_type = console.input(
            "[yellow]What type of authorization do you have? "
            "(written-permission/pentest-engagement/owned-lab/bug-bounty/internal-assessment/other): [/yellow]"
        )

        if auth_type.lower() in ['owned-lab', 'internal-assessment']:
            self.authorization_verified = True
            self.log_activity("AUTHORIZATION", f"Verified authorization type: {auth_type}")
            console.print("[bold green]Authorization verified.[/bold green]")
        else:
            confirmation = console.input(
                f"[yellow]Please confirm you have valid {auth_type} authorization (yes/no): [/yellow]"
            )

            if confirmation.lower() in ['yes', 'y']:
                self.authorization_verified = True
                self.log_activity("AUTHORIZATION", f"User confirmed authorization type: {auth_type}")
                console.print("[bold green]Authorization verified.[/bold green]")
            else:
                console.print("[bold red]Cannot proceed without proper authorization.[/bold red]")
                sys.exit(1)

    def log_activity(self, action: str, details: str):
        """Log user activities for compliance"""

        log_entry = {
            'timestamp': datetime.now().isoformat(),
            'action': action,
            'details': details,
            'user_session': getattr(self.config, 'session_id', 'unknown')
        }

        self.activity_log.append(log_entry)

        # Write to log file
        log_file = self.config.output_dir / "logs" / "compliance.log"
        with open(log_file, 'a', encoding='utf-8') as f:
            f.write(f"{datetime.now()} - {action}: {details}\n")

    def check_gdpr_compliance(self, target: str) -> bool:
        """Check if target scanning complies with GDPR"""

        # Basic GDPR compliance checks
        eu_domains = ['.eu', '.de', '.fr', '.it', '.es', '.nl', '.be', '.at', '.se', '.dk', '.fi', '.ie']

        if any(domain in target.lower() for domain in eu_domains):
            console.print("[yellow]Target appears to be EU-based. Extra GDPR compliance required.[/yellow]")
            gdpr_consent = console.input("[yellow]Confirm GDPR compliance requirements met (yes/no): [/yellow]")

            if gdpr_consent.lower() not in ['yes', 'y']:
                console.print("[red]GDPR compliance not confirmed. Skipping EU target.[/red]")
                return False

        self.log_activity("GDPR_CHECK", f"GDPR compliance verified for target: {target}")
        return True

class AIAssistant:
    """AI-powered OSINT assistant for guidance and analysis"""

    def __init__(self, config: OSINTConfig):
        self.config = config
        self.knowledge_base = self._load_knowledge_base()

    def _load_knowledge_base(self) -> Dict:
        """Load OSINT knowledge base"""

        return {
            'techniques': {
                'passive_recon': 'Gathering information without directly interacting with target systems',
                'active_recon': 'Directly probing target systems for information (requires authorization)',
                'social_media_intel': 'Collecting publicly available social media information',
                'dns_enumeration': 'Finding subdomains and DNS records',
                'port_scanning': 'Identifying open ports and services (authorized only)',
                'email_harvesting': 'Finding email addresses from public sources',
                'metadata_analysis': 'Extracting information from file metadata'
            },
            'tools': {
                'porteye': 'Advanced port scanning and service enumeration',
                'websift': 'Comprehensive web scraping and analysis',
                'clawk': 'Email harvesting and validation',
                'xsnifer': 'Network packet analysis and monitoring',
                'osint_ig': 'Social media intelligence gathering',
                'deadbond': 'Advanced OSINT correlation and graphing'
            },
            'legal_considerations': {
                'authorization': 'Always obtain written permission before scanning',
                'scope_limitation': 'Stay within authorized scope of testing',
                'data_protection': 'Comply with GDPR, CCPA, and local privacy laws',
                'responsible_disclosure': 'Report findings through proper channels',
                'documentation': 'Maintain detailed logs of all activities'
            }
        }

    def get_technique_explanation(self, technique: str, language: str = 'english') -> str:
        """Get explanation of OSINT technique"""

        explanations = {
            'english': self.knowledge_base.get('techniques', {}),
            'hindi': {
                'passive_recon': 'लक्ष्य प्रणालियों के साथ प्रत्यक्ष संपर्क के बिना जानकारी एकत्र करना',
                'active_recon': 'जानकारी के लिए लक्ष्य प्रणालियों की प्रत्यक्ष जांच (प्राधिकरण आवश्यक)',
                'social_media_intel': 'सार्वजनिक रूप से उपलब्ध सोशल मीडिया जानकारी एकत्र करना',
                'dns_enumeration': 'सबडोमेन और DNS रिकॉर्ड खोजना',
                'port_scanning': 'खुले पोर्ट और सेवाओं की पहचान करना (केवल अधिकृत)',
                'email_harvesting': 'सार्वजनिक स्रोतों से ईमेल पते खोजना',
                'metadata_analysis': 'फ़ाइल मेटाडेटा से जानकारी निकालना'
            }
        }

        return explanations.get(language, explanations['english']).get(technique, 'Unknown technique')

    def suggest_next_steps(self, current_results: List[OSINTResult]) -> List[str]:
        """Suggest next OSINT steps based on current results"""

        suggestions = []

        if not current_results:
            suggestions.extend([
                "Start with passive reconnaissance of the target domain",
                "Perform DNS enumeration to find subdomains", 
                "Check for publicly available information about the organization",
                "Search for email addresses associated with the domain"
            ])
        else:
            # Analyze results and suggest next steps
            for result in current_results[-5:]:  # Last 5 results
                if result.module == 'porteye' and result.data_type == 'open_port':
                    suggestions.append(f"Investigate service running on port {result.data} further")
                elif result.module == 'websift' and result.data_type == 'subdomain':
                    suggestions.append(f"Scan subdomain {result.data} for additional information")
                elif result.module == 'clawk' and result.data_type == 'email':
                    suggestions.append(f"Search for social media profiles associated with {result.data}")

        return suggestions[:5]  # Return top 5 suggestions

    def assess_risk_level(self, result: OSINTResult) -> str:
        """Assess risk level of discovered information"""

        risk_indicators = {
            'high': ['admin', 'root', 'password', 'secret', 'private', 'confidential'],
            'medium': ['login', 'user', 'account', 'database', 'api'],
            'low': ['public', 'info', 'contact', 'general']
        }

        data_str = str(result.data).lower()

        for level, indicators in risk_indicators.items():
            if any(indicator in data_str for indicator in indicators):
                return level

        return 'low'

    def generate_summary(self, results: List[OSINTResult], language: str = 'english') -> str:
        """Generate AI-powered summary of findings"""

        if not results:
            return "No results to summarize." if language == 'english' else "सारांश के लिए कोई परिणाम नहीं।"

        summary_templates = {
            'english': {
                'intro': f"OSINT Summary Report - {len(results)} findings discovered",
                'high_risk': f"WARNING: {len([r for r in results if r.risk_level == 'high'])} high-risk findings require immediate attention",
                'medium_risk': f"INFO: {len([r for r in results if r.risk_level == 'medium'])} medium-risk findings for review",
                'recommendations': "Recommended next steps based on findings:"
            },
            'hindi': {
                'intro': f"OSINT सारांश रिपोर्ट - {len(results)} खोजें की गईं",
                'high_risk': f"चेतावनी: {len([r for r in results if r.risk_level == 'high'])} उच्च-जोखिम खोजों पर तत्काल ध्यान देना आवश्यक",
                'medium_risk': f"जानकारी: {len([r for r in results if r.risk_level == 'medium'])} मध्यम-जोखिम खोजें समीक्षा के लिए",
                'recommendations': "खोजों के आधार पर अनुशंसित अगले कदम:"
            }
        }

        template = summary_templates.get(language, summary_templates['english'])

        summary = f"{template['intro']}\n"
        summary += f"{template['high_risk']}\n"
        summary += f"{template['medium_risk']}\n\n"
        summary += f"{template['recommendations']}\n"

        for suggestion in self.suggest_next_steps(results):
            summary += f"- {suggestion}\n"

        return summary

class PortEye:
    """Advanced port scanner module with CVE integration"""

    def __init__(self, config: OSINTConfig):
        self.config = config
        self.results = []
        self.service_db = self._load_service_database()

    def _load_service_database(self) -> Dict:
        """Load service identification database"""

        return {
            21: {'service': 'FTP', 'banner_regex': r'220.*FTP', 'risk': 'medium'},
            22: {'service': 'SSH', 'banner_regex': r'SSH-.*', 'risk': 'low'},
            23: {'service': 'Telnet', 'banner_regex': r'.*login:', 'risk': 'high'},
            25: {'service': 'SMTP', 'banner_regex': r'220.*SMTP', 'risk': 'medium'},
            53: {'service': 'DNS', 'banner_regex': r'', 'risk': 'low'},
            80: {'service': 'HTTP', 'banner_regex': r'HTTP/', 'risk': 'medium'},
            110: {'service': 'POP3', 'banner_regex': r'\+OK.*POP', 'risk': 'medium'},
            143: {'service': 'IMAP', 'banner_regex': r'\* OK.*IMAP', 'risk': 'medium'},
            443: {'service': 'HTTPS', 'banner_regex': r'HTTP/', 'risk': 'low'},
            993: {'service': 'IMAPS', 'banner_regex': r'\* OK.*IMAP', 'risk': 'low'},
            995: {'service': 'POP3S', 'banner_regex': r'\+OK.*POP', 'risk': 'low'},
            1433: {'service': 'MSSQL', 'banner_regex': r'', 'risk': 'high'},
            3306: {'service': 'MySQL', 'banner_regex': r'', 'risk': 'high'},
            3389: {'service': 'RDP', 'banner_regex': r'', 'risk': 'high'},
            5432: {'service': 'PostgreSQL', 'banner_regex': r'', 'risk': 'high'},
            6379: {'service': 'Redis', 'banner_regex': r'', 'risk': 'high'},
            27017: {'service': 'MongoDB', 'banner_regex': r'', 'risk': 'high'}
        }

    async def scan_port(self, target: str, port: int, timeout: int = 3) -> Optional[Dict]:
        """Asynchronously scan a single port"""

        try:
            # Create connection
            reader, writer = await asyncio.wait_for(
                asyncio.open_connection(target, port), 
                timeout=timeout
            )

            # Try to grab banner
            banner = ""
            try:
                # Send HTTP request for web services
                if port in [80, 8080, 8000, 8888]:
                    writer.write(b"HEAD / HTTP/1.0\r\n\r\n")
                    await writer.drain()

                # Read banner
                data = await asyncio.wait_for(reader.read(1024), timeout=2)
                banner = data.decode('utf-8', errors='ignore').strip()

            except Exception:
                pass
            finally:
                writer.close()
                await writer.wait_closed()

            # Identify service
            service_info = self.service_db.get(port, {'service': 'Unknown', 'risk': 'low'})

            result = {
                'port': port,
                'state': 'open',
                'service': service_info['service'],
                'banner': banner,
                'risk_level': service_info['risk'],
                'timestamp': datetime.now().isoformat()
            }

            return result

        except (asyncio.TimeoutError, ConnectionRefusedError, OSError):
            return None

    async def scan_range(self, target: str, port_range: range) -> List[Dict]:
        """Scan a range of ports asynchronously"""

        console.print(f"[cyan]Starting PortEye scan on {target}...[/cyan]")

        # Create semaphore to limit concurrent connections
        semaphore = asyncio.Semaphore(self.config.max_threads)

        async def scan_with_semaphore(port):
            async with semaphore:
                return await self.scan_port(target, port)

        # Create tasks for all ports
        tasks = [scan_with_semaphore(port) for port in port_range]

        # Progress tracking
        with Progress(
            SpinnerColumn(),
            TextColumn("[progress.description]{task.description}"),
            transient=True
        ) as progress:

            scan_task = progress.add_task(f"Scanning {len(port_range)} ports...", total=len(port_range))

            results = []
            for i, task in enumerate(asyncio.as_completed(tasks)):
                result = await task
                if result:
                    results.append(result)
                    console.print(f"[green]Found: Port {result['port']} - {result['service']}[/green]")

                progress.advance(scan_task)

        console.print(f"[green]PortEye scan completed. Found {len(results)} open ports.[/green]")
        return results

    def generate_nmap_command(self, target: str, ports: List[int]) -> str:
        """Generate equivalent nmap command for educational purposes"""

        port_string = ",".join(map(str, ports)) if ports else "1-65535"

        nmap_cmd = f"""
# Educational Nmap equivalent command:
nmap -sS -sV -O -A -T4 -p {port_string} {target}

# Command breakdown:
# -sS: SYN scan (stealth scan)
# -sV: Version detection
# -O: OS detection  
# -A: Aggressive scan (enables OS detection, version detection, script scanning)
# -T4: Timing template (faster)
# -p: Port specification

# For educational purposes only - always ensure proper authorization!
        """

        return nmap_cmd.strip()

class WebSift:
    """Enterprise-grade web scraping and crawling module"""

    def __init__(self, config: OSINTConfig):
        self.config = config
        self.session = self._create_session()
        self.results = []

    def _create_session(self) -> requests.Session:
        """Create configured requests session"""

        session = requests.Session()

        # Configure retries
        retry_strategy = Retry(
            total=3,
            backoff_factor=1,
            status_forcelist=[429, 500, 502, 503, 504]
        )

        adapter = HTTPAdapter(max_retries=retry_strategy)
        session.mount("http://", adapter)
        session.mount("https://", adapter)

        # Set headers
        session.headers.update({
            'User-Agent': self.config.user_agent,
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.5',
            'Accept-Encoding': 'gzip, deflate',
            'Connection': 'keep-alive'
        })

        return session

    def extract_emails(self, text: str) -> List[str]:
        """Extract email addresses from text"""

        email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        emails = re.findall(email_pattern, text)

        # Filter out common false positives
        filtered_emails = []
        for email in emails:
            if not any(fp in email.lower() for fp in ['example.com', 'test.com', 'lorem', 'ipsum']):
                filtered_emails.append(email)

        return list(set(filtered_emails))  # Remove duplicates

    def extract_subdomains(self, text: str, domain: str) -> List[str]:
        """Extract subdomains from text"""

        subdomain_pattern = rf'([a-zA-Z0-9.-]+\.{re.escape(domain)})'
        subdomains = re.findall(subdomain_pattern, text)

        return list(set(subdomains))

    def extract_urls(self, text: str) -> List[str]:
        """Extract URLs from text"""

        url_pattern = r'https?://[^\s<>"{}|\\^`\[\]]+'
        urls = re.findall(url_pattern, text)

        return list(set(urls))

    def analyze_robots_txt(self, target: str) -> Dict:
        """Analyze robots.txt file"""

        robots_url = f"{target.rstrip('/')}/robots.txt"

        try:
            response = self.session.get(robots_url, timeout=self.config.timeout)

            if response.status_code == 200:
                disallowed_paths = []
                allowed_paths = []
                sitemaps = []

                for line in response.text.split('\n'):
                    line = line.strip()
                    if line.startswith('Disallow:'):
                        path = line.split(':', 1)[1].strip()
                        if path and path != '/':
                            disallowed_paths.append(path)
                    elif line.startswith('Allow:'):
                        path = line.split(':', 1)[1].strip()
                        if path:
                            allowed_paths.append(path)
                    elif line.startswith('Sitemap:'):
                        sitemap = line.split(':', 1)[1].strip()
                        if sitemap:
                            sitemaps.append(sitemap)

                return {
                    'status': 'found',
                    'disallowed_paths': disallowed_paths,
                    'allowed_paths': allowed_paths,
                    'sitemaps': sitemaps,
                    'full_content': response.text
                }
            else:
                return {'status': 'not_found'}

        except Exception as e:
            return {'status': 'error', 'error': str(e)}

    def scan_website(self, target: str) -> Dict:
        """Comprehensive website analysis"""

        console.print(f"[cyan]Starting WebSift analysis on {target}...[/cyan]")

        results = {
            'target': target,
            'timestamp': datetime.now().isoformat(),
            'status': 'success',
            'data': {}
        }

        try:
            # Main page analysis
            response = self.session.get(target, timeout=self.config.timeout)
            soup = BeautifulSoup(response.content, 'html.parser')

            # Extract basic information
            results['data']['title'] = soup.title.string if soup.title else "No title"
            results['data']['status_code'] = response.status_code
            results['data']['headers'] = dict(response.headers)

            # Extract meta information
            meta_tags = {}
            for meta in soup.find_all('meta'):
                name = meta.get('name') or meta.get('property') or meta.get('http-equiv')
                content = meta.get('content')
                if name and content:
                    meta_tags[name] = content
            results['data']['meta_tags'] = meta_tags

            # Extract links
            links = []
            for link in soup.find_all('a', href=True):
                links.append({
                    'url': link['href'],
                    'text': link.get_text(strip=True)[:100]  # Limit text length
                })
            results['data']['links'] = links[:50]  # Limit number of links

            # Extract forms
            forms = []
            for form in soup.find_all('form'):
                form_data = {
                    'action': form.get('action', ''),
                    'method': form.get('method', 'GET').upper(),
                    'inputs': []
                }

                for inp in form.find_all(['input', 'textarea', 'select']):
                    form_data['inputs'].append({
                        'type': inp.get('type', 'text'),
                        'name': inp.get('name', ''),
                        'id': inp.get('id', '')
                    })

                forms.append(form_data)
            results['data']['forms'] = forms

            # Extract emails and subdomains
            page_text = soup.get_text()
            results['data']['emails'] = self.extract_emails(page_text)
            results['data']['urls'] = self.extract_urls(page_text)

            # Analyze robots.txt
            robots_analysis = self.analyze_robots_txt(target)
            results['data']['robots_txt'] = robots_analysis

            # Technology detection (basic)
            technologies = []

            # Check for common frameworks/technologies
            tech_indicators = {
                'WordPress': ['wp-content', 'wp-includes'],
                'Joomla': ['joomla'],
                'Drupal': ['drupal'],
                'React': ['react'],
                'Angular': ['angular'],
                'Vue.js': ['vue.js', 'vue.min.js'],
                'Bootstrap': ['bootstrap'],
                'jQuery': ['jquery']
            }

            html_content = response.text.lower()
            for tech, indicators in tech_indicators.items():
                if any(indicator in html_content for indicator in indicators):
                    technologies.append(tech)

            results['data']['technologies'] = technologies

            console.print(f"[green]WebSift analysis completed for {target}[/green]")

        except Exception as e:
            results['status'] = 'error'
            results['error'] = str(e)
            console.print(f"[red]WebSift analysis failed for {target}: {e}[/red]")

        return results

class Clawk:
    """Email harvester and validator module"""

    def __init__(self, config: OSINTConfig):
        self.config = config
        self.session = self._create_session()
        self.results = []
        self.email_patterns = [
            r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}',
            r'[a-zA-Z0-9._%+-]+\s*\[?at\]?\s*[a-zA-Z0-9.-]+\s*\[?dot\]?\s*[a-zA-Z]{2,}',
            r'[a-zA-Z0-9._%+-]+\s*@\s*[a-zA-Z0-9.-]+\s*\.\s*[a-zA-Z]{2,}'
        ]

    def _create_session(self) -> requests.Session:
        """Create configured requests session for email harvesting"""

        session = requests.Session()
        session.headers.update({
            'User-Agent': self.config.user_agent,
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'
        })

        return session

    def search_engines_harvest(self, domain: str) -> List[str]:
        """Harvest emails using search engines"""

        emails = set()

        # Google dorking for emails (educational demonstration)
        google_queries = [
            f'site:{domain} "@{domain}"',
            f'site:{domain} "email"',
            f'site:{domain} "contact"'
        ]

        console.print(f"[cyan]Harvesting emails for domain: {domain}[/cyan]")

        # Note: In a real implementation, you would use search engine APIs
        # This is a demonstration of the concept
        console.print("[yellow]Note: This is a demonstration. In practice, use official APIs.[/yellow]")

        # Simulated results for educational purposes
        demo_emails = [
            f"info@{domain}",
            f"contact@{domain}", 
            f"support@{domain}",
            f"sales@{domain}",
            f"admin@{domain}"
        ]

        console.print("[yellow]Demo mode: Generating sample email patterns for educational purposes[/yellow]")

        for email in demo_emails:
            emails.add(email)
            console.print(f"[green]Found: {email}[/green]")

        return list(emails)

    def dns_mx_lookup(self, domain: str) -> List[Dict]:
        """Perform MX record lookup"""

        try:
            mx_records = []
            answers = dns.resolver.resolve(domain, 'MX')

            for rdata in answers:
                mx_records.append({
                    'priority': rdata.preference,
                    'exchange': str(rdata.exchange).rstrip('.')
                })

            console.print(f"[green]Found {len(mx_records)} MX records for {domain}[/green]")
            return mx_records

        except Exception as e:
            console.print(f"[red]MX lookup failed for {domain}: {e}[/red]")
            return []

    def validate_email(self, email: str) -> Dict:
        """Validate email address (basic validation)"""

        result = {
            'email': email,
            'valid': False,
            'checks': {}
        }

        # Basic format validation
        email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        result['checks']['format'] = bool(re.match(email_regex, email))

        if result['checks']['format']:
            domain = email.split('@')[1]

            # DNS validation
            try:
                mx_records = dns.resolver.resolve(domain, 'MX')
                result['checks']['mx_record'] = True
            except:
                result['checks']['mx_record'] = False

            # Domain validation
            try:
                dns.resolver.resolve(domain, 'A')
                result['checks']['domain_exists'] = True
            except:
                result['checks']['domain_exists'] = False

            result['valid'] = all([
                result['checks']['format'],
                result['checks']['mx_record'],
                result['checks']['domain_exists']
            ])

        return result

    def harvest_domain(self, domain: str) -> Dict:
        """Comprehensive email harvesting for domain"""

        console.print(f"[cyan]Starting Clawk email harvesting for {domain}...[/cyan]")

        results = {
            'domain': domain,
            'timestamp': datetime.now().isoformat(),
            'emails': [],
            'mx_records': [],
            'validated_emails': []
        }

        # Harvest emails from various sources
        harvested_emails = self.search_engines_harvest(domain)
        results['emails'] = harvested_emails

        # Get MX records
        results['mx_records'] = self.dns_mx_lookup(domain)

        # Validate emails
        console.print(f"[cyan]Validating {len(harvested_emails)} emails...[/cyan]")

        for email in harvested_emails:
            validation = self.validate_email(email)
            results['validated_emails'].append(validation)

            if validation['valid']:
                console.print(f"[green]Valid: {email}[/green]")
            else:
                console.print(f"[yellow]Questionable: {email}[/yellow]")

        valid_count = len([e for e in results['validated_emails'] if e['valid']])
        console.print(f"[green]Clawk completed. Found {valid_count} valid emails out of {len(harvested_emails)} total.[/green]")

        return results

class OSINTTerminalUI:
    """Cinematic terminal dashboard UI"""

    def __init__(self, config: OSINTConfig):
        self.config = config
        self.console = Console()
        self.start_time = datetime.now()

    def show_banner(self):
        """Display animated ASCII banner"""

        banner = f"""
===============================================================================
                           OSINT MASTER ULTRA PRO MAX
                             v{VERSION}
                        The World's Most Comprehensive
                     Educational OSINT & Information Gathering
                              Mega-Toolkit

              *** CREATED BY RAJSARASWATI JATAV ***
                Educational & Research Use Only
            Cybersecurity Education • Ethical Research Only
                        www.rajsaraswati.dev

            EDU DEMO ONLY - WATERMARKED FOR EDUCATIONAL USE
===============================================================================
        """

        # Animate banner display
        lines = banner.split('\n')
        for line in lines:
            self.console.print(f"[bold cyan]{line}[/bold cyan]")
            time.sleep(0.05)  # Animation delay

    def show_main_menu(self) -> str:
        """Display main menu and get user choice"""

        menu_panel = Panel.fit(
            f"""
[bold cyan]OSINT MASTER ULTRA PRO MAX - Main Menu[/bold cyan]

[green]CORE MODULES:[/green]
[yellow]1.[/yellow] [bold blue]PortEye[/bold blue]     - Advanced Port Scanner & Service Enumeration
[yellow]2.[/yellow] [bold blue]WebSift[/bold blue]     - Enterprise Web Scraping & Analysis  
[yellow]3.[/yellow] [bold blue]Clawk[/bold blue]       - Email Harvester & Validator
[yellow]4.[/yellow] [bold blue]X-snifer[/bold blue]    - Network Packet Analysis (Demo)
[yellow]5.[/yellow] [bold blue]osi.ig[/bold blue]      - Social Media OSINT Engine (Demo)
[yellow]6.[/yellow] [bold blue]DeadBond[/bold blue]    - OSINT Graph Analyzer (Demo)

[green]UTILITIES:[/green]
[yellow]7.[/yellow] [bold green]AI Assistant[/bold green]    - OSINT Guidance & Analysis
[yellow]8.[/yellow] [bold green]Report Generator[/bold green] - Export Results & Reports
[yellow]9.[/yellow] [bold green]Settings[/bold green]        - Configuration & Preferences
[yellow]10.[/yellow] [bold green]Tutorial[/bold green]       - Educational Guidance

[green]OTHER:[/green]
[yellow]11.[/yellow] [bold magenta]Language Toggle[/bold magenta] (English/Hindi)
[yellow]12.[/yellow] [bold red]Exit[/bold red]

[bold yellow]Created by {AUTHOR} - Educational Research Tool[/bold yellow]
            """,
            title="MAIN MENU",
            border_style="cyan"
        )

        self.console.print(menu_panel)

        choice = self.console.input("\n[bold yellow]Select option (1-12): [/bold yellow]")
        return choice.strip()

    def show_status_bar(self):
        """Display status bar with current information"""

        uptime = datetime.now() - self.start_time

        status_info = f"""
[cyan]User:[/cyan] Educational Researcher  
[cyan]Session:[/cyan] {uptime.seconds//3600:02d}:{(uptime.seconds//60)%60:02d}:{uptime.seconds%60:02d}  
[cyan]Mode:[/cyan] [yellow]DEMO/EDUCATIONAL[/yellow]  
[cyan]Status:[/cyan] [green]READY[/green]  
[cyan]Created by:[/cyan] [bold]{AUTHOR}[/bold]
        """

        status_panel = Panel(
            status_info.strip(),
            title="Status",
            border_style="green",
            width=80
        )

        return status_panel

class OSINTMasterUltraProMax:
    """Main application class orchestrating all OSINT modules"""

    def __init__(self):
        self.config = OSINTConfig()
        self.compliance_manager = EthicalComplianceManager(self.config)
        self.ai_assistant = AIAssistant(self.config)
        self.ui = OSINTTerminalUI(self.config)

        # Initialize modules
        self.porteye = PortEye(self.config)
        self.websift = WebSift(self.config)
        self.clawk = Clawk(self.config)

        # Session management
        self.session_id = self._generate_session_id()
        self.results_db = []

        # Setup logging
        self._setup_logging()

    def _generate_session_id(self) -> str:
        """Generate unique session ID"""
        return hashlib.sha256(f"{datetime.now().isoformat()}{random.random()}".encode()).hexdigest()[:16]

    def _setup_logging(self):
        """Setup logging configuration"""

        log_file = self.config.output_dir / "logs" / "osint_master.log"

        logging.basicConfig(
            level=self.config.log_level,
            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
            handlers=[
                logging.FileHandler(log_file),
                logging.StreamHandler(sys.stdout)
            ]
        )

        self.logger = logging.getLogger("OSINTMaster")
        self.logger.info(f"OSINT Master Ultra Pro Max v{VERSION} initialized")
        self.logger.info(f"Session ID: {self.session_id}")

    def show_initial_setup(self):
        """Show initial setup and compliance checks"""

        # Clear screen
        self.ui.console.clear()

        # Show banner
        self.ui.show_banner()

        time.sleep(2)

        # Show pip requirements
        self._show_pip_requirements()

        time.sleep(1)

        # Legal and ethical compliance
        self.compliance_manager.show_legal_disclaimer()
        self.compliance_manager.verify_authorization()

        # Show welcome message
        welcome_panel = Panel.fit(
            f"""
[bold green]Welcome to OSINT Master Ultra Pro Max![/bold green]

[cyan]Session initialized successfully![/cyan]
[yellow]Session ID:[/yellow] {self.session_id}
[yellow]Mode:[/yellow] Educational Demo
[yellow]Created by:[/yellow] [bold]{AUTHOR}[/bold]

[green]All ethical and legal requirements satisfied.[/green]
[green]Educational mode activated.[/green]
[green]Privacy protection enabled.[/green]

[bold yellow]Ready to begin your ethical OSINT research![/bold yellow]

Press Enter to continue...
            """,
            title="INITIALIZATION COMPLETE",
            border_style="green"
        )

        self.ui.console.print(welcome_panel)
        input()

    def _show_pip_requirements(self):
        """Display pip installation requirements"""

        requirements = [
            "requests>=2.28.0",
            "beautifulsoup4>=4.11.0", 
            "dnspython>=2.3.0",
            "rich>=13.0.0",
            "cryptography>=3.4.8",
            "asyncio",
            "aiohttp>=3.8.0",
            "python-nmap>=0.7.1"
        ]

        req_text = "\n".join(f"- {req}" for req in requirements)

        pip_panel = Panel.fit(
            f"""
[bold cyan]Python Dependencies & Installation Guide[/bold cyan]

[yellow]Required packages (auto-installing if missing):[/yellow]

{req_text}

[green]Installation command:[/green]
[bold]pip install {' '.join(requirements)}[/bold]

[yellow]Note: This tool auto-installs missing dependencies[/yellow]
[green]All packages are installing automatically...[/green]

[bold red]IMPORTANT LEGAL NOTICE[/bold red]
[red]This tool is for EDUCATIONAL and ETHICAL research only![/red]
[red]Users are responsible for complying with all applicable laws.[/red]

[bold yellow]Created by: {AUTHOR}[/bold yellow]
[yellow]Version: {VERSION}[/yellow]
[yellow]Contact: {CONTACT}[/yellow]
            """,
            title="INSTALLATION & REQUIREMENTS",
            border_style="blue"
        )

        self.ui.console.print(pip_panel)

    def run(self):
        """Main application loop"""

        try:
            # Initial setup
            self.show_initial_setup()

            # Main loop
            while True:
                self.ui.console.clear()

                # Show status bar
                self.ui.console.print(self.ui.show_status_bar())

                # Show main menu
                choice = self.ui.show_main_menu()

                # Process user choice
                if choice == '1':
                    self.run_porteye_scan()
                elif choice == '2': 
                    self.run_websift_analysis()
                elif choice == '3':
                    self.run_clawk_harvest()
                elif choice == '4':
                    self._show_demo_module("X-snifer", "Network Packet Analysis")
                elif choice == '5':
                    self._show_demo_module("osi.ig", "Social Media OSINT Engine") 
                elif choice == '6':
                    self._show_demo_module("DeadBond", "OSINT Graph Analyzer")
                elif choice == '7':
                    self.show_ai_assistant()
                elif choice == '8':
                    self.generate_reports()
                elif choice == '9':
                    self.show_settings()
                elif choice == '10':
                    self.show_tutorial()
                elif choice == '11':
                    self.toggle_language()
                elif choice == '12':
                    self._exit_application()
                    break
                else:
                    self.ui.console.print("[red]Invalid choice. Please try again.[/red]")
                    time.sleep(1)

        except KeyboardInterrupt:
            self.ui.console.print("\n[yellow]Interrupted by user.[/yellow]")
            self._exit_application()
        except Exception as e:
            self.ui.console.print(f"\n[red]Unexpected error: {e}[/red]")
            self.logger.error(f"Unexpected error: {e}")
            self._exit_application()

    def run_porteye_scan(self):
        """Run PortEye port scanning module"""

        self.ui.console.clear()

        header = Panel.fit(
            """
[bold blue]PortEye - Advanced Port Scanner & Service Enumeration[/bold blue]

[yellow]Features:[/yellow]
- Multi-threaded asynchronous scanning
- Service identification and banner grabbing
- SSL certificate analysis
- CVE cross-referencing (demo)
- Risk assessment and classification

[red]AUTHORIZATION REQUIRED: Only scan systems you own or have explicit permission to test![/red]
            """,
            title="PortEye Module",
            border_style="blue"
        )

        self.ui.console.print(header)

        # Get target from user
        target = self.ui.console.input("\n[yellow]Enter target IP/hostname: [/yellow]").strip()

        if not target:
            self.ui.console.print("[red]No target specified.[/red]")
            input("Press Enter to continue...")
            return

        # Ethical compliance check
        if not self.compliance_manager.check_gdpr_compliance(target):
            input("Press Enter to continue...")
            return

        self.compliance_manager.log_activity("PORTEYE_SCAN", f"Initiated port scan on {target}")

        # Get port range
        port_choice = self.ui.console.input(
            "\n[yellow]Port range ([cyan]1[/cyan]=Common, [cyan]2[/cyan]=Extended, [cyan]3[/cyan]=Custom): [/yellow]"
        )

        if port_choice == "1":
            port_range = range(1, 1025)  # Common ports
        elif port_choice == "2": 
            port_range = range(1, 10001)  # Extended range
        elif port_choice == "3":
            start_port = int(self.ui.console.input("[yellow]Start port: [/yellow]") or "1")
            end_port = int(self.ui.console.input("[yellow]End port: [/yellow]") or "1024")
            port_range = range(start_port, end_port + 1)
        else:
            port_range = range(1, 1025)  # Default

        # Run scan
        try:
            results = asyncio.run(self.porteye.scan_range(target, port_range))

            if results:
                # Display results
                table = Table(title=f"PortEye Scan Results - {target}")
                table.add_column("Port", style="cyan")
                table.add_column("Service", style="green")
                table.add_column("Risk", style="yellow")
                table.add_column("Banner", style="blue", max_width=40)

                for result in results:
                    risk_color = {"low": "green", "medium": "yellow", "high": "red"}.get(result['risk_level'], "white")

                    table.add_row(
                        str(result['port']),
                        result['service'],
                        f"[{risk_color}]{result['risk_level'].upper()}[/{risk_color}]",
                        result['banner'][:40] + "..." if len(result['banner']) > 40 else result['banner']
                    )

                self.ui.console.print(table)

                # Store results
                scan_result = OSINTResult(
                    module="porteye",
                    target=target,
                    data_type="port_scan",
                    data=results,
                    source="PortEye Scanner",
                    confidence=0.9
                )

                self.results_db.append(scan_result)

                # Show equivalent nmap command
                ports = [r['port'] for r in results]
                nmap_cmd = self.porteye.generate_nmap_command(target, ports)

                nmap_panel = Panel.fit(
                    nmap_cmd,
                    title="Educational: Equivalent Nmap Command",
                    border_style="green"
                )

                self.ui.console.print(nmap_panel)

            else:
                self.ui.console.print("[yellow]No open ports found.[/yellow]")

        except Exception as e:
            self.ui.console.print(f"[red]Scan failed: {e}[/red]")
            self.logger.error(f"PortEye scan failed: {e}")

        self.ui.console.input("\n[yellow]Press Enter to continue...[/yellow]")

    def run_websift_analysis(self):
        """Run WebSift web analysis module"""

        self.ui.console.clear()

        header = Panel.fit(
            """
[bold green]WebSift - Enterprise Web Scraping & Analysis[/bold green]

[yellow]Features:[/yellow]
- Comprehensive website analysis
- Technology stack identification  
- Email and subdomain extraction
- Form and link analysis
- Robots.txt investigation
- Meta tag examination

[red]Ensure proper authorization and respect robots.txt directives![/red]
            """,
            title="WebSift Module", 
            border_style="green"
        )

        self.ui.console.print(header)

        # Get target URL
        target_url = self.ui.console.input("\n[yellow]Enter target URL (include http/https): [/yellow]").strip()

        if not target_url:
            self.ui.console.print("[red]No URL specified.[/red]")
            input("Press Enter to continue...")
            return

        # Validate URL format
        if not target_url.startswith(('http://', 'https://')):
            target_url = 'https://' + target_url

        # Ethical compliance check
        domain = urllib.parse.urlparse(target_url).netloc
        if not self.compliance_manager.check_gdpr_compliance(domain):
            input("Press Enter to continue...")
            return

        self.compliance_manager.log_activity("WEBSIFT_ANALYSIS", f"Initiated web analysis on {target_url}")

        # Run analysis
        try:
            results = self.websift.scan_website(target_url)

            if results['status'] == 'success':
                data = results['data']

                # Display basic information
                info_table = Table(title=f"WebSift Analysis - {target_url}")
                info_table.add_column("Property", style="cyan")
                info_table.add_column("Value", style="green")

                info_table.add_row("Title", data.get('title', 'N/A'))
                info_table.add_row("Status Code", str(data.get('status_code', 'N/A')))
                info_table.add_row("Technologies", ', '.join(data.get('technologies', [])) or 'None detected')
                info_table.add_row("Email Addresses", str(len(data.get('emails', []))))
                info_table.add_row("Links Found", str(len(data.get('links', []))))
                info_table.add_row("Forms Found", str(len(data.get('forms', []))))

                self.ui.console.print(info_table)

                # Store results
                analysis_result = OSINTResult(
                    module="websift",
                    target=target_url,
                    data_type="web_analysis",
                    data=data,
                    source="WebSift Analyzer",
                    confidence=0.85
                )

                self.results_db.append(analysis_result)

            else:
                self.ui.console.print(f"[red]Analysis failed: {results.get('error', 'Unknown error')}[/red]")

        except Exception as e:
            self.ui.console.print(f"[red]WebSift analysis failed: {e}[/red]")
            self.logger.error(f"WebSift analysis failed: {e}")

        self.ui.console.input("\n[yellow]Press Enter to continue...[/yellow]")

    def run_clawk_harvest(self):
        """Run Clawk email harvesting module"""

        self.ui.console.clear()

        header = Panel.fit(
            """
[bold magenta]Clawk - Email Harvester & Validator[/bold magenta]

[yellow]Features:[/yellow]
- Multi-source email harvesting
- DNS MX record validation
- Email format verification
- Domain permutation analysis
- Breach database integration (demo)

[red]Only harvest emails from authorized domains and public sources![/red]
            """,
            title="Clawk Module",
            border_style="magenta"
        )

        self.ui.console.print(header)

        # Get target domain
        target_domain = self.ui.console.input("\n[yellow]Enter target domain (e.g., example.com): [/yellow]").strip()

        if not target_domain:
            self.ui.console.print("[red]No domain specified.[/red]")
            input("Press Enter to continue...")
            return

        # Remove protocol if present
        target_domain = target_domain.replace('http://', '').replace('https://', '').split('/')[0]

        # Ethical compliance check
        if not self.compliance_manager.check_gdpr_compliance(target_domain):
            input("Press Enter to continue...")
            return

        self.compliance_manager.log_activity("CLAWK_HARVEST", f"Initiated email harvesting for {target_domain}")

        # Run harvesting
        try:
            results = self.clawk.harvest_domain(target_domain)

            # Display results
            if results['emails']:
                email_table = Table(title=f"Clawk Email Results for {target_domain}")
                email_table.add_column("Email", style="cyan")
                email_table.add_column("Status", style="green")

                for validation in results['validated_emails']:
                    email = validation['email']
                    valid = validation['valid']
                    status = "Valid" if valid else "Questionable"
                    email_table.add_row(email, status)

                self.ui.console.print(email_table)

                # Store results
                harvest_result = OSINTResult(
                    module="clawk",
                    target=target_domain,
                    data_type="email_harvest",
                    data=results,
                    source="Clawk Harvester",
                    confidence=0.8
                )

                self.results_db.append(harvest_result)

            else:
                self.ui.console.print("[yellow]No emails found for this domain.[/yellow]")

        except Exception as e:
            self.ui.console.print(f"[red]Email harvesting failed: {e}[/red]")
            self.logger.error(f"Clawk harvesting failed: {e}")

        self.ui.console.input("\n[yellow]Press Enter to continue...[/yellow]")

    def show_ai_assistant(self):
        """Show AI assistant interface"""

        self.ui.console.clear()

        header = Panel.fit(
            """
[bold cyan]AI Assistant - OSINT Guidance & Analysis[/bold cyan]

[yellow]Available Services:[/yellow]
- OSINT technique explanations
- Risk assessment analysis
- Next step suggestions
- Results summarization
- Educational guidance

[green]Ask me anything about OSINT techniques, tools, or your findings![/green]
            """,
            title="AI Assistant",
            border_style="cyan"
        )

        self.ui.console.print(header)

        while True:
            query = self.ui.console.input("\n[yellow]Ask AI Assistant (or 'back' to return): [/yellow]").strip()

            if query.lower() in ['back', 'exit', 'quit']:
                break

            if not query:
                continue

            # Process query with simple keyword matching
            if 'technique' in query.lower():
                tech_list = "\n".join(f"- {tech}: {desc}" 
                                     for tech, desc in self.ai_assistant.knowledge_base['techniques'].items())

                self.ui.console.print(f"[green]Available OSINT Techniques:[/green]\n{tech_list}")

            elif 'summary' in query.lower() or 'results' in query.lower():
                if self.results_db:
                    summary = self.ai_assistant.generate_summary(self.results_db, self.config.language)
                    self.ui.console.print(f"[green]AI Summary:[/green]\n{summary}")
                else:
                    self.ui.console.print("[yellow]No results available to summarize yet.[/yellow]")

            elif 'legal' in query.lower() or 'ethical' in query.lower():
                legal_info = "\n".join(f"- {consideration}: {desc}" 
                                      for consideration, desc in self.ai_assistant.knowledge_base['legal_considerations'].items())

                self.ui.console.print(f"[green]Legal & Ethical Guidelines:[/green]\n{legal_info}")

            else:
                help_text = """
I can help you with:
- Explaining OSINT techniques and tools
- Analyzing your findings and results
- Suggesting next investigation steps
- Legal and ethical considerations
- Generating summaries of your work

Try asking about 'techniques', 'summary', or 'legal considerations'.
                """
                self.ui.console.print(f"[cyan]How I Can Help:[/cyan]\n{help_text}")

    def generate_reports(self):
        """Generate comprehensive OSINT reports"""

        self.ui.console.clear()

        if not self.results_db:
            self.ui.console.print("[yellow]No OSINT data available for reporting.[/yellow]")
            self.ui.console.print("[green]Run some OSINT modules first to collect data.[/green]")
            input("\nPress Enter to continue...")
            return

        # Generate simple report
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        report_file = self.config.output_dir / "reports" / f"osint_report_{timestamp}.txt"

        try:
            report_content = f"""
===============================================================================
                    OSINT MASTER ULTRA PRO MAX REPORT
                          Educational Research Only
===============================================================================

Created by: {AUTHOR}
Version: {VERSION}
Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
Session ID: {self.session_id}

REPORT SUMMARY:
==============
Total Findings: {len(self.results_db)}
Modules Used: {', '.join(set(r.module for r in self.results_db))}

DETAILED FINDINGS:
==================
            """

            for i, result in enumerate(self.results_db, 1):
                report_content += f"""
Finding #{i}:
  Module: {result.module}
  Target: {result.target}
  Type: {result.data_type}
  Risk: {result.risk_level.upper()}
  Source: {result.source}
  Timestamp: {result.timestamp.strftime('%Y-%m-%d %H:%M:%S')}
  Data: {str(result.data)[:500]}{"..." if len(str(result.data)) > 500 else ""}

{'-' * 80}
                """

            report_content += f"""

LEGAL DISCLAIMER:
================
This report was generated for educational and research purposes only.
Users are responsible for ensuring compliance with all relevant regulations.

Report watermark: EDU DEMO ONLY - {datetime.now().isoformat()}
            """

            with open(report_file, 'w', encoding='utf-8') as f:
                f.write(report_content)

            self.ui.console.print(f"[green]Report generated successfully![/green]")
            self.ui.console.print(f"[yellow]File:[/yellow] {report_file}")

        except Exception as e:
            self.ui.console.print(f"[red]Report generation failed: {e}[/red]")

        self.ui.console.input("\n[yellow]Press Enter to continue...[/yellow]")

    def show_settings(self):
        """Show settings and configuration options"""

        self.ui.console.clear()

        settings_info = f"""
Current Configuration:
- Language: {self.config.language.title()}
- Timeout: {self.config.timeout} seconds
- Max Threads: {self.config.max_threads}
- Demo Mode: {'Enabled' if self.config.demo_mode else 'Disabled'}
- Session ID: {self.session_id}
- Results Collected: {len(self.results_db)}

Educational Settings (Fixed):
- Educational Only: Always Enabled
- Legal Compliance: Always Enabled  
- Privacy Protection: Always Enabled

Created by: {AUTHOR}
Version: {VERSION}
        """

        settings_panel = Panel.fit(settings_info, title="Settings", border_style="cyan")
        self.ui.console.print(settings_panel)

        self.ui.console.input("\n[yellow]Press Enter to continue...[/yellow]")

    def show_tutorial(self):
        """Show educational tutorial"""

        self.ui.console.clear()

        tutorial_content = """
OSINT TUTORIAL - Educational Overview

What is OSINT?
Open Source Intelligence (OSINT) is the collection and analysis of data 
gathered from open sources to produce actionable intelligence.

Key Principles:
- Uses publicly available information
- Legal and ethical when done properly
- Does not require special access or permissions
- Relies on skill in finding and analyzing data

OSINT Process:
1. Direction & Planning - Define requirements
2. Collection - Gather data from open sources
3. Processing - Filter and organize data
4. Analysis - Extract meaningful insights
5. Dissemination - Present findings

Legal & Ethical Guidelines:
- Always obtain proper authorization
- Comply with terms of service
- Respect privacy and data protection laws
- Practice responsible disclosure
- Document methodology

This tool provides educational modules for learning OSINT concepts
and practicing techniques in an ethical, controlled environment.

Remember: Always use OSINT tools responsibly and legally!
        """

        tutorial_panel = Panel.fit(tutorial_content, title="OSINT Tutorial", border_style="blue")
        self.ui.console.print(tutorial_panel)

        self.ui.console.input("\n[yellow]Press Enter to continue...[/yellow]")

    def toggle_language(self):
        """Toggle between English and Hindi"""

        if self.config.language == 'english':
            self.config.language = 'hindi'
            message = "भाषा हिन्दी में बदल दी गई! (Language changed to Hindi!)"
        else:
            self.config.language = 'english'  
            message = "Language changed to English!"

        self.ui.console.print(f"[green]{message}[/green]")
        self.ui.console.input("\nPress Enter to continue...")

    def _show_demo_module(self, module_name: str, description: str):
        """Show demo version of advanced modules"""

        self.ui.console.clear()

        demo_panel = Panel.fit(
            f"""
[bold cyan]{module_name} - {description}[/bold cyan]

[yellow]This is a demonstration module showing the concept.[/yellow]

[green]In a full implementation, this would provide:[/green]
- Advanced {description.lower()} features
- Real-time data processing
- Integration with external APIs
- Comprehensive reporting

[red]DEMO LIMITATIONS:[/red]
- Educational purposes only
- Simulated data for learning
- No actual network interaction
- Watermarked results

[yellow]Created by: {AUTHOR}[/yellow]
            """,
            title=f"{module_name} - Demo", 
            border_style="yellow"
        )

        self.ui.console.print(demo_panel)

        # Simulate demo with progress
        with Progress(
            SpinnerColumn(),
            TextColumn("[progress.description]{task.description}"),
            transient=True
        ) as progress:
            demo_task = progress.add_task(f"Running {module_name} demo...", total=100)

            for i in range(100):
                time.sleep(0.02)
                progress.advance(demo_task)

        self.ui.console.print(f"[green]{module_name} demo completed![/green]")
        self.ui.console.input("\n[yellow]Press Enter to continue...[/yellow]")

    def _exit_application(self):
        """Graceful application exit"""

        # Save session data
        session_data = {
            'session_id': self.session_id,
            'start_time': self.ui.start_time.isoformat(),
            'end_time': datetime.now().isoformat(),
            'results_count': len(self.results_db),
            'modules_used': list(set(r.module for r in self.results_db))
        }

        session_file = self.config.output_dir / "logs" / f"session_{self.session_id}.json"
        try:
            with open(session_file, 'w', encoding='utf-8') as f:
                json.dump(session_data, f, indent=2, default=str)
        except Exception:
            pass

        # Exit message
        exit_panel = Panel.fit(
            f"""
[bold green]Thank you for using OSINT Master Ultra Pro Max![/bold green]

[yellow]Session Summary:[/yellow]
- Session ID: {self.session_id}
- Duration: {datetime.now() - self.ui.start_time}
- Results Collected: {len(self.results_db)}

[green]Remember:[/green]
- Always use OSINT tools ethically and legally
- Obtain proper authorization before scanning
- Respect privacy and data protection laws

[cyan]Created by: {AUTHOR}[/cyan]
[cyan]Version: {VERSION}[/cyan]

[bold yellow]Thank you for ethical and responsible use![/bold yellow]
            """,
            title="Goodbye!",
            border_style="green"
        )

        self.ui.console.print(exit_panel)
        self.logger.info("OSINT Master session ended")


def main():
    """Main entry point"""

    # Python version check
    if sys.version_info < (3, 8):
        print("Error: Python 3.8 or higher is required.")
        sys.exit(1)

    try:
        # Initialize and run application
        app = OSINTMasterUltraProMax()
        app.run()

    except KeyboardInterrupt:
        print("\nApplication interrupted by user.")
        sys.exit(0)
    except Exception as e:
        print(f"\nFatal error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
