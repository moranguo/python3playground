import dns.resolver

hes19_domains = set()
hes19_file = open('hes19_tb_entity.txt')
for line in hes19_file:
    entity = line.split('@')[1].split(',')[0]
    hes19_domains.add(entity)
print(len(hes19_domains))

no_domain_file = open('no-domain.csv')
hes20_nodomain = set()
for line in no_domain_file:
    line = line.strip('\r\n"')
    if line in hes19_domains:
        hes20_nodomain.add(line)

for domain in hes20_nodomain:
    print(domain)
    try:
        answers = dns.resolver.query(domain, 'MX')
    except Exception as e:
        print(e)
    for rdata in answers:
        print('    MX', rdata.exchange, 'has preference', rdata.preference)
