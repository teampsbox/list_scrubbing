import csv

fields_needed = ['email', 'Firstname', 'Lastname', 'DistributorStatus', 'SendersFirstName', 'MyEntireShakleeGroup', 'SendersShakleePWS', 'SendersYFPSitesURL', 'SendersFBGroup', 'SendersFanPage', 'SendersTwitter', 'SendersYoutube', 'SendersGooglePlus', 'SendersHeadShot', 'SendersYFP', 'SendersYWP']
with open('export.csv', 'r') as exported, open('scrubbed.csv', 'w') as scrubbed:
    reader = csv.DictReader(exported)
    writer = csv.DictWriter(scrubbed, fieldnames=fields_needed, extrasaction='ignore')

    writer.writeheader()
    for r in reader:
        writer.writerow(r)
