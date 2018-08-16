import csv

fields_needed = ['email', 'Firstname', 'Lastname', 'DistributorStatus', 'SendersFirstName', 'MyEntireShakleeGroup', 'SendersShakleePWS', 'SendersYFPSitesURL', 'SendersFBGroup', 'SendersFanPage', 'SendersTwitter', 'SendersYoutube', 'SendersGooglePlus', 'SendersHeadShot', 'SendersYFP', 'SendersYWP']
with open('export.csv', 'r') as fp_in, open('target.csv', 'w') as fp_out:
    reader = csv.DictReader(fp_in)
    writer = csv.DictWriter(fp_out, fieldnames=fields_needed, extrasaction='ignore')

    writer.writeheader()
    for r in reader:
        writer.writerow(r)
