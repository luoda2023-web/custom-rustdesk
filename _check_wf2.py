import yaml

with open(r'D:\Personal\Desktop\luoda-rustdesk\.github\workflows\bridge.yml', 'r') as f:
    doc = yaml.safe_load(f)
print('=== bridge.yml ===')
print('Keys:', list(doc.keys()))
jobs = list(doc.get('jobs', {}).keys())
print('Jobs:', jobs)

with open(r'D:\Personal\Desktop\luoda-rustdesk\.github\workflows\flutter-nightly.yml', 'r') as f:
    doc2 = yaml.safe_load(f)
print()
print('=== flutter-nightly.yml ===')
print('Keys:', list(doc2.keys()))
jobs2 = list(doc2.get('jobs', {}).keys())
print('Jobs:', jobs2)
for jn, jv in doc2['jobs'].items():
    print(f'  {jn}: uses={jv.get("uses","")} needs={jv.get("needs","")}')
