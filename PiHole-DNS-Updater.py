import argparse
import configparser
import requests

CUSTOM_DNS_ENDPOINT='/admin/scripts/pi-hole/php/customdns.php'

def load_config():
    # Load configuration
    config = configparser.ConfigParser()
    config.read_file(open('config.cfg'))
    return config


def make_request(query):
    # Construct URL
    pihole_addr = config['PiHole']['address']
    url = f"http://{pihole_addr}{CUSTOM_DNS_ENDPOINT}"

    # Send post request
    res = requests.post(url, headers={}, params=query)

    # Check response matches 200
    if res.status_code == 200:
        print("Request Success")
    else:
        print("Request Fail")


def add_host(hostname, ip, id=-1):
    # Check ID is valid (>0) otherwise generate
    if id < 0:
        id = generate_id()

    # Add hostname/ip to Pihole DB
    make_request({
        'action': 'add',
        'ip': ip,
        'hostname': hostname,
        'auth': config['PiHole']['auth']
    })

    # Add hostname/ip to local DB for tracking

def generate_id():
    # Default to 0 for now until DB is implemented
    return 0

def remove_host(id):
    # Check ID exists in local DB

    # Get details from local DB

    # Send request to remove entry
    make_request({
        'action': 'remove',
        'ip': ip,
        'hostname': hostname,
        'auth': config.auth
    })

    # Remove from local DB

def list_hosts(id=-1):
    # Get all hosts from local DB - Print out
    if id >= 0:
        print_host(db[id])
    else:
        for host in db:
            print_host(host)

def print_host(host):
    print(f"{host.id}\t{host.hostname}\t{host.ip}")


def main():
    # Load configuration
    global config
    config = load_config()

    global db
    # db = load_db()

    # Load arguments from CLI
    parser = argparse.ArgumentParser(prog='PiHole-Custom-DNS-Updater',
                                    description='CLI interface to add/remove DNS entries from PiHole')
    subparsers = parser.add_subparsers(help='commands', dest='command')

    # Add host command
    add_parser = subparsers.add_parser('add', help='Add a new DNS entry')
    add_parser.add_argument('ip', action='store', help='IP address to map hostname to')
    add_parser.add_argument('hostname', action='store', help='Hostname to map IP to')
    add_parser.add_argument('--id', action='store', help='Manually specify an ID for this entry (must be unique)')

    # Remove host command
    remove_parser = subparsers.add_parser('remove', help='Remove a DNS entry')
    remove_parser.add_argument('id', action='store', help='ID of the entry to be removed')

    # List hosts command
    list_parser = subparsers.add_parser('list', help='List all of the DNS entries')
    list_parser.add_argument('--id', action='store', help='Specific ID to show only this entry')

    args = parser.parse_args()

    # Process appropriate action
    if args.command == 'add':
        add_host(args.hostname, args.ip)
    elif args.command == 'remove':
        remove_host(args.id)
    elif args.command == 'list':
        list_hosts()
    else:
        print("No valid command was provided")

if __name__ == '__main__':
    main()