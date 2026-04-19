import yaml, json, urllib.request

# 检查 flutter-build.yml inputs
with open(r'D:\Personal\Desktop\luoda-rustdesk\.github\workflows\flutter-build.yml', 'r') as f:
    doc = yaml.safe_load(f)

on_val = doc.get('on') or doc.get(True, {})
print('=== flutter-build.yml workflow_call inputs ===')
if isinstance(on_val, dict):
    wc = on_val.get('workflow_call') or on_val
    if isinstance(wc, dict):
        inputs = wc.get('inputs', {})
        print('Inputs defined:', list(inputs.keys()) if inputs else 'NONE')
    else:
        print('workflow_call value (raw):', wc)

# 检查 flutter-nightly.yml 传递的 inputs
with open(r'D:\Personal\Desktop\luoda-rustdesk\.github\workflows\flutter-nightly.yml', 'r') as f:
    doc2 = yaml.safe_load(f)

print()
print('=== flutter-nightly.yml job with: ===')
for jn, jv in doc2.get('jobs', {}).items():
    with_params = jv.get('with', {})
    secrets = jv.get('secrets', None)
    uses = jv.get('uses', '')
    print(f'Job: {jn}')
    print(f'  uses: {uses}')
    print(f'  with: {with_params}')
    print(f'  secrets: {secrets}')

# 检查 GitHub 上 flutter-build.yml 的 workflow_call inputs
print()
print('=== GitHub upstream flutter-build.yml workflow_call ===')
try:
    r = urllib.request.urlopen('https://api.github.com/repos/rustdesk/rustdesk/contents/.github/workflows/flutter-build.yml')
    data = json.load(r)
    content = base64.b64decode(data['content']).decode('utf-8')
    import io
    doc_up = yaml.safe_load(content)
    on_up = doc_up.get('on') or doc_up.get(True, {})
    print('Upstream on:', on_up)
except Exception as e:
    print('Error:', str(e)[:100])
